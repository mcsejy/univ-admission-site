# -*- coding: utf-8 -*-
"""
스캔 결과에서 데이터가 있는 코드들의 대학명을 univDetail.do로 확인.
스캔 단계와 이름 확인 단계를 분리해서 안정적으로 실행.
"""
import asyncio, re, json
from playwright.async_api import async_playwright

ADIGA = "https://www.adiga.kr"
POPUP_PATH = "/uct/acd/ade/criteriaAndResultPopup.do"
AJAX_PATH  = "/uct/acd/ade/criteriaAndResultItemAjax.do"

# 잘못된 코드를 가진 대학들
WRONG_UNIVS = {
    "경북대학교":      "0000057",
    "국민대학교":      "0000077",
    "대구대학교":      "0000083",
    "단국대학교(죽전)":"0000087",
    "덕성여자대학교":  "0000090",
    "명지대학교":      "0000110",
    "조선대학교":      "0000166",
    "영남대학교":      "0000157",
    "전북대학교":      "0000174",
    "울산대학교":      "0000162",
    "한국항공대학교":  "0000193",
    "홍익대학교":      "0000210",
}

# 스캔 범위 (잘못된 코드 주변 ±20)
SCAN_RANGES = [
    (50, 99),    # 경~단 (경북, 국민, 대구, 단국, 덕성 범위)
    (100, 125),  # 동~서 (명지 범위)
    (148, 175),  # 안~중 (영남, 울산, 조선, 전북 범위)
    (188, 215),  # 한~홍 (한국항공, 홍익 범위)
]

async def get_csrf_and_form(page):
    await page.goto(
        f"{ADIGA}{POPUP_PATH}?unvCd=0000063&searchSyr=2026&tsrdCmphSlcnArtclUpCd=10",
        wait_until="load", timeout=30000,
    )
    await asyncio.sleep(2)
    csrf = await page.get_attribute('meta[name="_csrf"]', "content") or ""
    form_data = await page.evaluate("""() => {
        const frm = document.getElementById('frm');
        if (!frm) return {};
        const d = {};
        for (const el of frm.elements) { if (el.name) d[el.name] = el.value; }
        return d;
    }""")
    return csrf, form_data

async def check_size(page, csrf, form_data, code):
    fd = dict(form_data)
    fd["unvCd"] = code
    fd["tsrdCmphSlcnArtclUpCd"] = "10"
    fd["tsrdCmphSlcnArtclCd"] = "22"
    params_json = json.dumps(fd, ensure_ascii=False)
    csrf_safe = csrf.replace("'", "\\'")
    try:
        resp = await page.evaluate(f"""async () => {{
            const fd = new FormData();
            const p = {params_json};
            for (const [k,v] of Object.entries(p)) fd.append(k,v);
            const r = await fetch('{ADIGA}{AJAX_PATH}', {{
                method:'POST',
                headers:{{'X-CSRF-TOKEN':'{csrf_safe}','X-Requested-With':'XMLHttpRequest'}},
                body:fd, credentials:'include'
            }});
            return await r.text();
        }}""")
        return len(resp) if resp else 0
    except Exception:
        return -1

async def get_univ_name(page, code):
    """univDetail.do 에서 대학명 추출"""
    try:
        await page.goto(
            f"{ADIGA}/ucp/uvt/uni/univDetail.do?menuId=PCUVTINF2000&searchSyr=2026&unvCd={code}",
            wait_until="networkidle", timeout=20000,
        )
        await asyncio.sleep(2)
        inner = await page.evaluate("() => document.body.innerText")
        univs = re.findall(r'[가-힣]{2,10}(?:대학교|교육대학교|과학기술대학교)', inner)
        return list(dict.fromkeys(univs))[:3]
    except Exception:
        return []

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        ctx = await browser.new_context(
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/120.0.0.0"
        )

        # ── 1단계: 코드 스캔 (AJAX 크기 확인) ──
        print("=== 1단계: 코드별 데이터 크기 스캔 ===")
        scan_page = await ctx.new_page()
        csrf, form_data = await get_csrf_and_form(scan_page)
        print(f"CSRF: {csrf[:20]}...")

        size_map = {}  # code -> size
        for start, end in SCAN_RANGES:
            print(f"\n[범위 {start:07d} ~ {end:07d}]")
            for num in range(start, end + 1):
                code = f"{num:07d}"
                sz = await check_size(scan_page, csrf, form_data, code)
                size_map[code] = sz
                if sz > 550:
                    print(f"  {code}: {sz:,}b (데이터있음)")
                elif sz < 0:
                    print(f"  {code}: ERROR - CSRF 만료, 재취득 시도")
                    csrf, form_data = await get_csrf_and_form(scan_page)

        # ── 2단계: 데이터 있는 코드의 대학명 확인 ──
        print("\n=== 2단계: 데이터 있는 코드의 대학명 확인 ===")
        name_page = await ctx.new_page()

        data_codes = {c: s for c, s in size_map.items() if s > 550}
        results = {}
        for code in sorted(data_codes.keys()):
            names = await get_univ_name(name_page, code)
            sz = data_codes[code]
            results[code] = {"sz": sz, "names": names}
            print(f"  {code} ({sz:,}b): {names}")

        # ── 3단계: 목표 대학 매핑 ──
        print("\n=== 3단계: 목표 대학 코드 매핑 ===")
        corrections = {}
        for target_name in WRONG_UNIVS:
            base = re.sub(r'[(\[（【].*?[)\]）】]', '', target_name).strip()
            for code, info in results.items():
                for univ_name in info["names"]:
                    if base in univ_name or univ_name in base:
                        corrections[target_name] = {"code": code, "sz": info["sz"], "matched": univ_name}
                        print(f"  ✓ {target_name} → {code} ({univ_name}, {info['sz']:,}b)")
                        break

        missing = [n for n in WRONG_UNIVS if n not in corrections]
        if missing:
            print(f"\n아직 못 찾은 대학: {missing}")

        # ── 저장 ──
        output = {
            "size_map": size_map,
            "name_results": {c: {"sz": v["sz"], "names": v["names"]} for c, v in results.items()},
            "corrections": corrections,
        }
        with open("verify_names_result.json", "w", encoding="utf-8") as f:
            json.dump(output, f, ensure_ascii=False, indent=2)
        print("\n결과 저장: verify_names_result.json")

        await browser.close()

asyncio.run(main())
