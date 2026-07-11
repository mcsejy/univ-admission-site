"""
각 대학 코드로 adiga.kr 팝업에 실제 데이터가 오는지 확인.
빈 결과면 이름 검색으로 올바른 코드 탐색.
"""
import asyncio, re, json
from playwright.async_api import async_playwright

OUR_LIST = [
    ("가톨릭대학교",      "0000007"), ("건국대학교",        "0000011"),
    ("경희대학교",        "0000065"), ("고려대학교",        "0000069"),
    ("광운대학교",        "0000073"), ("국민대학교",        "0000077"),
    ("동국대학교",        "0000100"), ("명지대학교",        "0000110"),
    ("서강대학교",        "0000120"), ("서울과학기술대학교","0000125"),
    ("서울대학교",        "0000019"), ("서울시립대학교",    "0000040"),
    ("성균관대학교",      "0000133"), ("성신여자대학교",    "0000143"),
    ("세종대학교",        "0000145"), ("숙명여자대학교",    "0000147"),
    ("숭실대학교",        "0000148"), ("연세대학교",        "0000149"),
    ("이화여자대학교",    "0000163"), ("중앙대학교",        "0000175"),
    ("한국외국어대학교",  "0000192"), ("한성대학교",        "0000200"),
    ("한양대학교",        "0000203"), ("홍익대학교",        "0000210"),
    ("덕성여자대학교",    "0000090"), ("동덕여자대학교",    "0000103"),
    ("삼육대학교",        "0000116"), ("상명대학교",        "0000119"),
    ("서울여자대학교",    "0000128"), ("성공회대학교",      "0000136"),
    ("한국항공대학교",    "0000193"), ("가천대학교",        "0000063"),
    ("경기대학교",        "0000056"), ("단국대학교(죽전)",  "0000087"),
    ("아주대학교",        "0000156"), ("인하대학교",        "0000169"),
    ("인천대학교",        "0000170"), ("연세대학교(미래)",  "0000150"),
    ("고려대학교(세종)",  "0000070"), ("강원대학교",        "0000009"),
    ("한림대학교",        "0000196"), ("가톨릭관동대학교",  "0000008"),
    ("충남대학교",        "0000029"), ("충북대학교",        "0000181"),
    ("공주대학교",        "0000072"), ("순천향대학교",      "0000146"),
    ("단국대학교(천안)",  "0000088"), ("한국교원대학교",    "0000187"),
    ("한국기술교육대학교","0000189"), ("건양대학교",        "0000012"),
    ("호서대학교",        "0000207"), ("한밭대학교",        "0000198"),
    ("전남대학교",        "0000173"), ("전북대학교",        "0000174"),
    ("전주교육대학교",    "0000258"), ("진주교육대학교",    "0000260"),
    ("조선대학교",        "0000166"), ("목포대학교",        "0000113"),
    ("군산대학교",        "0000079"), ("순천대학교",        "0000144"),
    ("우석대학교",        "0000161"), ("경북대학교",        "0000057"),
    ("영남대학교",        "0000157"), ("계명대학교",        "0000060"),
    ("대구가톨릭대학교",  "0000082"), ("대구대학교",        "0000083"),
    ("안동대학교",        "0000153"), ("동국대학교(경주)",  "0000101"),
    ("부산대학교",        "0000025"), ("경상국립대학교",    "0000064"),
    ("동아대학교",        "0000104"), ("부경대학교",        "0000024"),
    ("경성대학교",        "0000062"), ("동의대학교",        "0000106"),
    ("울산대학교",        "0000162"), ("인제대학교",        "0000168"),
    ("신라대학교",        "0000141"), ("경남대학교",        "0000054"),
    ("제주대학교",        "0000178"),
]

ADIGA = "https://www.adiga.kr"
AJAX_PATH = "/uct/acd/ade/criteriaAndResultItemAjax.do"

async def has_data(page, csrf, form_data, code):
    """해당 코드로 팝업에 데이터가 있는지 확인 (수시 탭 10)"""
    fd = dict(form_data)
    fd["unvCd"] = code
    fd["tsrdCmphSlcnArtclUpCd"] = "10"
    params_json = json.dumps(fd, ensure_ascii=False)
    csrf_safe = csrf.replace("'", "\\'")
    resp = await page.evaluate(f"""async () => {{
        const fd = new FormData();
        const p = {params_json};
        for (const [k,v] of Object.entries(p)) fd.append(k,v);
        const res = await fetch('{ADIGA}{AJAX_PATH}', {{
            method:'POST',
            headers:{{'X-CSRF-TOKEN':'{csrf_safe}','X-Requested-With':'XMLHttpRequest'}},
            body:fd, credentials:'include'
        }});
        return await res.text();
    }}""")
    if not resp:
        return False, 0
    sz = len(resp)
    # 실제 테이블 데이터가 있으면 "모집단위" 포함
    return sz > 600 and ("없습니다" not in resp), sz

async def find_code_by_name(page, name):
    """이름으로 univAjax 검색하여 코드 반환"""
    kw = json.dumps(name)
    resp = await page.evaluate(f"""async () => {{
        const fd = new FormData();
        fd.append('searchSyr', '2026');
        fd.append('searchUnvNm', {kw});
        fd.append('searchStdClsfRgnCn', '');
        const res = await fetch('/ucp/uvt/uni/univAjax.do', {{
            method:'POST', body:fd, credentials:'include'
        }});
        return await res.text();
    }}""")
    found = re.findall(r'code="(\d{7})">([^<]+)</a>', resp)
    return [(c, n.strip()) for c, n in found]

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context(user_agent="Mozilla/5.0 Chrome/120.0.0.0")
        page = await context.new_page()

        # 팝업 기준 페이지 로드 (CSRF + form_data 획득)
        await page.goto(
            f"{ADIGA}/uct/acd/ade/criteriaAndResultPopup.do"
            "?unvCd=0000063&searchSyr=2026&tsrdCmphSlcnArtclUpCd=10",
            wait_until="load", timeout=30000
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
        form_data["tsrdCmphSlcnArtclCd"] = "22"
        print(f"CSRF: {csrf[:20]}... form keys: {list(form_data.keys())}")

        # 이름 검색용 페이지 준비
        search_page = await context.new_page()
        await search_page.goto(
            f"{ADIGA}/ucp/uvt/uni/univDetailSelection.do?menuId=PCUVTINF2000&searchSyr=2026",
            wait_until="networkidle", timeout=30000
        )
        await asyncio.sleep(2)

        has_data_list, no_data_list = [], []

        total = len(OUR_LIST)
        for i, (name, code) in enumerate(OUR_LIST):
            ok, sz = await has_data(page, csrf, form_data, code)
            print(f"[{i+1}/{total}] {name} ({code}): {'OK' if ok else 'NO'} ({sz}b)")
            if ok:
                has_data_list.append((name, code))
            else:
                # 이름으로 올바른 코드 찾기 시도
                base = re.sub(r'[(\[（【].*?[)\]）】]', '', name).strip()
                found = await find_code_by_name(search_page, base)
                await asyncio.sleep(0.3)
                # 실제로 데이터가 있는 코드만 필터
                correct = None
                for fc, fn in found:
                    if fc == code:
                        continue
                    fok, fsz = await has_data(page, csrf, form_data, fc)
                    if fok:
                        correct = (fc, fn)
                        break
                no_data_list.append((name, code, correct))

        lines = []
        lines.append("=" * 70)
        lines.append(f"데이터 있는 대학: {len(has_data_list)}개")
        lines.append(f"데이터 없는 대학: {len(no_data_list)}개")
        lines.append("=" * 70)

        lines.append("\n[데이터 있음 -- 코드 정상]")
        for name, code in has_data_list:
            lines.append(f"  {name}: {code}")

        lines.append("\n[데이터 없음 -- 코드 확인 필요]")
        for name, code, correct in no_data_list:
            if correct:
                lines.append(f"  {name}: {code} -> 올바른코드: {correct[0]} ({correct[1]})")
            else:
                lines.append(f"  {name}: {code} -> adiga 미공개 (Gemini fallback)")

        text = "\n".join(lines)
        with open("verify_result4.txt", "w", encoding="utf-8") as f:
            f.write(text)
        print("\n결과 저장: verify_result4.txt")
        await browser.close()

asyncio.run(main())
