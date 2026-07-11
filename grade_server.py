# -*- coding: utf-8 -*-
"""
합격등급 비교 백엔드 서버
- adiga.kr 의 criteriaAndResultItemAjax.do 를 Playwright 로 호출
- 결과 HTML 을 파싱해 학과별 합격등급 JSON 으로 반환

실행: python grade_server.py
접속: http://localhost:5000
"""
import asyncio, json, re, sys
from flask import Flask, jsonify, request, send_from_directory
from flask_cors import CORS
from bs4 import BeautifulSoup
from playwright.async_api import async_playwright
import os

app = Flask(__name__)
CORS(app)

ADIGA_BASE = "https://www.adiga.kr"
POPUP_PATH = "/uct/acd/ade/criteriaAndResultPopup.do"
AJAX_PATH  = "/uct/acd/ade/criteriaAndResultItemAjax.do"

TAB_CODES = {
    "종합": "20",
    "교과": "30",
    "수능": "40",
    "공통": "10",
}

# ──────────────────────────────────────────────
# adiga.kr Playwright 비동기 조회
# ──────────────────────────────────────────────
async def fetch_grade_data(unv_cd: str, year: str, tab: str = "교과", dept_filter: str = ""):
    tab_code = TAB_CODES.get(tab, "30")
    # 원하는 탭 코드로 팝업 직접 로드 → 서버가 form 필드를 올바르게 초기화
    popup_url = (
        f"{ADIGA_BASE}{POPUP_PATH}"
        f"?unvCd={unv_cd}&searchSyr={year}&tsrdCmphSlcnArtclUpCd={tab_code}"
    )

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context(
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/120.0.0.0 Safari/537.36"
        )
        page = await context.new_page()

        await page.goto(popup_url, wait_until="load", timeout=30000)
        await asyncio.sleep(1)

        csrf = await page.get_attribute('meta[name="_csrf"]', "content") or ""

        form_data = await page.evaluate("""() => {
            const frm = document.getElementById('frm');
            if (!frm) return {};
            const data = {};
            for (const el of frm.elements) {
                if (el.name) data[el.name] = el.value;
            }
            return data;
        }""")

        # 원하는 탭 코드로 오버라이드
        form_data["tsrdCmphSlcnArtclUpCd"] = tab_code

        results = {}
        # art_cd 22 = 전년도 전형 결과 (실제 합격등급)
        # art_cd 21 = 당해 전형 주요사항 (모집요강)
        for art_cd, label in [
            ("22", f"{int(year)-1}학년도 전형 결과"),
            ("21", f"{year}학년도 전형 주요사항"),
        ]:
            params = {**form_data, "tsrdCmphSlcnArtclCd": art_cd}
            params_json = json.dumps(params, ensure_ascii=False)
            csrf_safe = csrf.replace("'", "\\'")

            resp = await page.evaluate(f"""async () => {{
                const fd = new FormData();
                const params = {params_json};
                for (const [k, v] of Object.entries(params)) fd.append(k, v);
                const res = await fetch('{ADIGA_BASE}{AJAX_PATH}', {{
                    method: 'POST',
                    headers: {{ 'X-CSRF-TOKEN': '{csrf_safe}', 'X-Requested-With': 'XMLHttpRequest' }},
                    body: fd,
                    credentials: 'include'
                }});
                return await res.text();
            }}""")

            if resp and len(resp) > 100:
                rows = parse_grade_html(resp, dept_filter)
                # 탭에 맞는 전형명만 남김 (adiga.kr가 탭 전환 후 이전 탭 데이터를 그대로 렌더링하는 경우 방어)
                TAB_JEONHYEONG = {"교과": "교과", "종합": "종합", "수능": "수능"}
                kw = TAB_JEONHYEONG.get(tab)
                if kw:
                    rows = [r for r in rows if kw in r.get("jeonhyeong", "")]
                results[label] = rows

        await browser.close()
        return {"year": year, "unvCd": unv_cd, "tab": tab, "data": results}


def parse_grade_html(html_text: str, dept_filter: str = "") -> list:
    """adiga.kr 결과 HTML 에서 학과별 합격등급 파싱."""
    soup = BeautifulSoup(html_text, "html.parser")
    all_rows = []

    # 전형명 인정 키워드 (이 단어가 포함된 전형만 결과로 처리)
    JEONHYEONG_KEYWORDS = ("학생부", "인하미래인재", "교과", "종합", "수능", "지역", "사회배려", "기회균형",
                           "고른기회", "농어촌", "특성화", "사범", "고교", "예체능")

    for table in soup.find_all("table"):
        rows = table.find_all("tr")
        if len(rows) < 4:
            continue

        # 행0: 첫 셀이 "모집단위"이고 둘째 셀이 전형명인 테이블만 처리
        first_tds = rows[0].find_all("td")
        if not first_tds or len(first_tds) < 2:
            continue
        first_cell = first_tds[0].get_text(strip=True)
        if first_cell != "모집단위":
            continue
        jeonhyeong = first_tds[1].get_text(strip=True)
        # 유효한 전형명인지 확인
        if not any(kw in jeonhyeong for kw in JEONHYEONG_KEYWORDS):
            continue

        # 행3 이후: 실제 학과 데이터
        for tr in rows[3:]:
            tds = tr.find_all("td")
            if len(tds) < 5:
                continue
            dept = tds[0].get_text(strip=True)
            if not dept or dept in ("모집단위", "전형명", "학과명"):
                continue

            grade_50 = tds[4].get_text(strip=True) if len(tds) > 4 else ""
            grade_70 = tds[5].get_text(strip=True) if len(tds) > 5 else ""
            note     = tds[6].get_text(strip=True)[:80] if len(tds) > 6 else ""

            # 비공개 처리 (3명 이하)
            if "선발인원" in grade_50 or "이하" in grade_50:
                grade_50 = "비공개"
                grade_70 = "비공개"

            all_rows.append({
                "jeonhyeong": jeonhyeong,
                "dept": dept,
                "capacity": tds[1].get_text(strip=True) if len(tds) > 1 else "",
                "competition": tds[2].get_text(strip=True) if len(tds) > 2 else "",
                "grade_50": grade_50,
                "grade_70": grade_70,
                "note": note,
            })

    if not dept_filter:
        return all_rows

    # 1차: 입력 그대로 포함 매칭
    filtered = [r for r in all_rows if dept_filter in r["dept"]]
    if filtered:
        return filtered

    # 2차: 접미사 제거한 핵심 키워드로 유사 학과 매칭
    # 신설 학과(반도체 등)는 대학마다 학과명이 달라 정확 매칭 실패 가능
    core = re.sub(r'(학과|전공|학부|과|부)$', '', dept_filter).strip()
    if core and core != dept_filter:
        similar = [r for r in all_rows if core in r["dept"]]
        if similar:
            return similar

    # 3차: 교육대학교처럼 모집단위 컬럼에 전형명이 들어오는 경우 전체 반환
    return all_rows


# ──────────────────────────────────────────────
# 동기 래퍼
# ──────────────────────────────────────────────
def run_async(coro):
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    try:
        return loop.run_until_complete(coro)
    finally:
        loop.close()


# ──────────────────────────────────────────────
# Flask 라우트
# ──────────────────────────────────────────────
@app.route("/")
def index():
    return send_from_directory(".", "합격등급비교.html")


@app.route("/api/grades")
def api_grades():
    """단일 대학 합격등급 조회."""
    unv_cd = request.args.get("unvCd", "").strip()
    year   = request.args.get("year", "2026").strip()
    tab    = request.args.get("tab", "교과").strip()
    dept   = request.args.get("dept", "").strip()

    if not unv_cd:
        return jsonify({"error": "unvCd 파라미터가 필요합니다."}), 400
    if not re.match(r"^\d{7}$", unv_cd):
        return jsonify({"error": "unvCd 는 7 자리 숫자여야 합니다. 예: 0000169"}), 400

    try:
        result = run_async(fetch_grade_data(unv_cd, year, tab, dept))
        return jsonify(result)
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/api/grades/compare")
def api_compare():
    """2025 vs 2026 비교 (tab 별)."""
    unv_cd = request.args.get("unvCd", "").strip()
    tab    = request.args.get("tab", "교과").strip()
    dept   = request.args.get("dept", "").strip()

    if not unv_cd:
        return jsonify({"error": "unvCd 파라미터가 필요합니다."}), 400
    if not re.match(r"^\d{7}$", unv_cd):
        return jsonify({"error": "unvCd 는 7 자리 숫자여야 합니다."}), 400

    try:
        r2025 = run_async(fetch_grade_data(unv_cd, "2025", tab, dept))
        r2026 = run_async(fetch_grade_data(unv_cd, "2026", tab, dept))
        return jsonify({"y2025": r2025, "y2026": r2026})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/api/univs")
def api_univs():
    """대학 목록 및 코드 반환."""
    q = request.args.get("q", "").strip()
    data = [u for u in UNIV_LIST if not q or q in u["name"]]
    return jsonify(data)


# ──────────────────────────────────────────────
# 대학 코드 목록 (adiga.kr unvCd)
# ──────────────────────────────────────────────
UNIV_LIST = [
    # 서울 — 기존
    {"name": "가톨릭대학교",        "region": "서울", "code": "0000007"},
    {"name": "건국대학교",           "region": "서울", "code": "0000011"},
    {"name": "경희대학교",           "region": "서울", "code": "0000065"},
    {"name": "고려대학교",           "region": "서울", "code": "0000069"},
    {"name": "광운대학교",           "region": "서울", "code": "0000073"},
    {"name": "국민대학교",           "region": "서울", "code": "0000078"},
    {"name": "동국대학교",           "region": "서울", "code": "0000100"},
    {"name": "명지대학교",           "region": "서울", "code": "0000111"},
    {"name": "서강대학교",           "region": "서울", "code": "0000120"},
    {"name": "서울과학기술대학교",   "region": "서울", "code": "0000036"},
    {"name": "서울대학교",           "region": "서울", "code": "0000019"},
    {"name": "서울시립대학교",       "region": "서울", "code": "0000040"},
    {"name": "서경대학교",           "region": "서울", "code": "0000121"},
    {"name": "성균관대학교",         "region": "서울", "code": "0000133"},
    {"name": "성신여자대학교",       "region": "서울", "code": "0000143"},
    {"name": "세종대학교",           "region": "서울", "code": "0000145"},
    {"name": "숙명여자대학교",       "region": "서울", "code": "0000147"},
    {"name": "숭실대학교",           "region": "서울", "code": "0000148"},
    {"name": "연세대학교",           "region": "서울", "code": "0000149"},
    {"name": "이화여자대학교",       "region": "서울", "code": "0000163"},
    {"name": "중앙대학교",           "region": "서울", "code": "0000175"},
    {"name": "한국외국어대학교",     "region": "서울", "code": "0000192"},
    {"name": "한성대학교",           "region": "서울", "code": "0000200"},
    {"name": "한양대학교",           "region": "서울", "code": "0000203"},
    {"name": "홍익대학교",           "region": "서울", "code": "0000212"},
    # 서울 — 추가
    {"name": "덕성여자대학교",       "region": "서울", "code": "0000099"},
    {"name": "동덕여자대학교",       "region": "서울", "code": "0000103"},
    {"name": "삼육대학교",           "region": "서울", "code": "0000116"},
    {"name": "상명대학교",           "region": "서울", "code": "0000119"},
    {"name": "서울여자대학교",       "region": "서울", "code": "0000128"},
    {"name": "성공회대학교",         "region": "서울", "code": "0000136"},
    {"name": "한국항공대학교",       "region": "경기", "code": "0000194"},
    # 경기/인천
    {"name": "가천대학교",           "region": "경기", "code": "0000063"},
    {"name": "경기대학교",           "region": "경기", "code": "0000056"},
    {"name": "단국대학교(죽전)",     "region": "경기", "code": "0000087"},
    {"name": "아주대학교",           "region": "경기", "code": "0000156"},
    {"name": "인하대학교",           "region": "인천", "code": "0000169"},
    {"name": "인천대학교",           "region": "인천", "code": "0000170"},
    {"name": "연세대학교(미래)",     "region": "강원", "code": "0000150"},
    {"name": "고려대학교(세종)",     "region": "충남", "code": "0000070"},
    # 강원
    {"name": "강원대학교",           "region": "강원", "code": "0000009"},
    {"name": "한림대학교",           "region": "강원", "code": "0000196"},
    {"name": "가톨릭관동대학교",     "region": "강원", "code": "0000008"},
    # 충청
    {"name": "충남대학교",           "region": "대전", "code": "0000029"},
    {"name": "충북대학교",           "region": "충북", "code": "0000181"},
    {"name": "공주대학교",           "region": "충남", "code": "0000072"},
    {"name": "순천향대학교",         "region": "충남", "code": "0000146"},
    {"name": "단국대학교(천안)",     "region": "충남", "code": "0000088"},
    {"name": "한국교원대학교",       "region": "충북", "code": "0000187"},
    {"name": "한국기술교육대학교",   "region": "충남", "code": "0000189"},
    {"name": "건양대학교",           "region": "충남", "code": "0000012"},
    {"name": "호서대학교",           "region": "충남", "code": "0000207"},
    {"name": "한밭대학교",           "region": "대전", "code": "0000198"},
    # 호남
    {"name": "전남대학교",           "region": "광주", "code": "0000173"},
    {"name": "전북대학교",           "region": "전북", "code": "0000174"},
    {"name": "전주교육대학교",       "region": "전북", "code": "0000258"},
    {"name": "진주교육대학교",       "region": "경남", "code": "0000260"},
    {"name": "조선대학교",           "region": "광주", "code": "0000172"},
    {"name": "목포대학교",           "region": "전남", "code": "0000113"},
    {"name": "군산대학교",           "region": "전북", "code": "0000079"},
    {"name": "순천대학교",           "region": "전남", "code": "0000144"},
    {"name": "우석대학교",           "region": "전북", "code": "0000161"},
    # 대구/경북
    {"name": "경북대학교",           "region": "대구", "code": "0000057"},
    {"name": "영남대학교",           "region": "경북", "code": "0000151"},
    {"name": "계명대학교",           "region": "대구", "code": "0000060"},
    {"name": "대구가톨릭대학교",     "region": "대구", "code": "0000082"},
    {"name": "대구대학교",           "region": "경북", "code": "0000084"},
    {"name": "안동대학교",           "region": "경북", "code": "0000153"},
    {"name": "동국대학교(경주)",     "region": "경북", "code": "0000101"},
    # 경남/부산/울산
    {"name": "부산대학교",           "region": "부산", "code": "0000025"},
    {"name": "경상국립대학교",       "region": "경남", "code": "0000064"},
    {"name": "동아대학교",           "region": "부산", "code": "0000104"},
    {"name": "부경대학교",           "region": "부산", "code": "0000024"},
    {"name": "경성대학교",           "region": "부산", "code": "0000062"},
    {"name": "동의대학교",           "region": "부산", "code": "0000106"},
    {"name": "울산대학교",           "region": "울산", "code": "0000158"},
    {"name": "인제대학교",           "region": "경남", "code": "0000168"},
    {"name": "신라대학교",           "region": "부산", "code": "0000141"},
    {"name": "경남대학교",           "region": "경남", "code": "0000054"},
    # 제주
    {"name": "제주대학교",           "region": "제주", "code": "0000178"},
    # 전문대학 — 서울
    {"name": "동양미래대학교",       "region": "서울", "code": "0000463"},
    {"name": "명지전문대학",         "region": "서울", "code": "0000473"},
    {"name": "배화여자대학교",       "region": "서울", "code": "0000476"},
    {"name": "삼육보건대학교",       "region": "서울", "code": "0000483"},
    {"name": "서울여자간호대학교",   "region": "서울", "code": "0002973"},
    {"name": "서일대학교",           "region": "서울", "code": "0000490"},
    {"name": "숭의여자대학교",       "region": "서울", "code": "0000500"},
    {"name": "인덕대학교",           "region": "서울", "code": "0000525"},
    {"name": "한양여자대학교",       "region": "서울", "code": "0000554"},
    # 전문대학 — 경기
    {"name": "경기과학기술대학교",   "region": "경기", "code": "0000560"},
    {"name": "경민대학교",           "region": "경기", "code": "0000416"},
    {"name": "경복대학교",           "region": "경기", "code": "0002641"},
    {"name": "계원예술대학교",       "region": "경기", "code": "0000426"},
    {"name": "국제대학교",           "region": "경기", "code": "0000549"},
    {"name": "김포대학교",           "region": "경기", "code": "0000440"},
    {"name": "농협대학교",           "region": "경기", "code": "0000441"},
    {"name": "동남보건대학교",       "region": "경기", "code": "0000457"},
    {"name": "동서울대학교",         "region": "경기", "code": "0000450"},
    {"name": "동아방송예술대학교",   "region": "경기", "code": "0000461"},
    {"name": "동원대학교",           "region": "경기", "code": "0000465"},
    {"name": "두원공과대학교",       "region": "경기", "code": "0000469"},
    {"name": "서울예술대학교",       "region": "경기", "code": "0000489"},
    {"name": "서정대학교",           "region": "경기", "code": "0000566"},
    {"name": "부천대학교",           "region": "경기", "code": "0000482"},
    {"name": "수원과학대학교",       "region": "경기", "code": "0000497"},
    {"name": "수원여자대학교",       "region": "경기", "code": "0000496"},
    {"name": "신구대학교",           "region": "경기", "code": "0000501"},
    {"name": "신안산대학교",         "region": "경기", "code": "0000506"},
    {"name": "안산대학교",           "region": "경기", "code": "0000507"},
    {"name": "여주대학교",           "region": "경기", "code": "0000510"},
    {"name": "연성대학교",           "region": "경기", "code": "0002651"},
    {"name": "오산대학교",           "region": "경기", "code": "0002653"},
    {"name": "용인예술과학대학교",   "region": "경기", "code": "0000520"},
    {"name": "웅지세무대학교",       "region": "경기", "code": "0000568"},
    {"name": "유한대학교",           "region": "경기", "code": "0000524"},
    {"name": "장안대학교",           "region": "경기", "code": "0000527"},
    {"name": "청강문화산업대학교",   "region": "경기", "code": "0000544"},
    {"name": "한국관광대학교",       "region": "경기", "code": "0000565"},
    {"name": "한국복지대학교",       "region": "경기", "code": "0002659"},
]


if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    print("=" * 50)
    print("합격등급 비교 서버 시작")
    print(f"http://localhost:{port}")
    print("=" * 50)
    app.run(host="0.0.0.0", port=port, debug=False, threaded=False)
