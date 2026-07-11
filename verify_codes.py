"""adiga.kr univAjax에서 전체 대학 목록을 가져와 grade_server.py 코드와 비교"""
import asyncio, re
from playwright.async_api import async_playwright

OUR_LIST = [
    ("가톨릭대학교",      "0000007"),
    ("건국대학교",        "0000011"),
    ("경희대학교",        "0000065"),
    ("고려대학교",        "0000069"),
    ("광운대학교",        "0000073"),
    ("국민대학교",        "0000077"),
    ("동국대학교",        "0000100"),
    ("명지대학교",        "0000110"),
    ("서강대학교",        "0000120"),
    ("서울과학기술대학교","0000125"),
    ("서울대학교",        "0000019"),
    ("서울시립대학교",    "0000040"),
    ("성균관대학교",      "0000133"),
    ("성신여자대학교",    "0000143"),
    ("세종대학교",        "0000145"),
    ("숙명여자대학교",    "0000147"),
    ("숭실대학교",        "0000148"),
    ("연세대학교",        "0000149"),
    ("이화여자대학교",    "0000163"),
    ("중앙대학교",        "0000175"),
    ("한국외국어대학교",  "0000192"),
    ("한성대학교",        "0000200"),
    ("한양대학교",        "0000203"),
    ("홍익대학교",        "0000210"),
    ("덕성여자대학교",    "0000090"),
    ("동덕여자대학교",    "0000103"),
    ("삼육대학교",        "0000116"),
    ("상명대학교",        "0000119"),
    ("서울여자대학교",    "0000128"),
    ("성공회대학교",      "0000136"),
    ("한국항공대학교",    "0000193"),
    ("가천대학교",        "0000063"),
    ("경기대학교",        "0000056"),
    ("단국대학교(죽전)",  "0000087"),
    ("아주대학교",        "0000156"),
    ("인하대학교",        "0000169"),
    ("인천대학교",        "0000170"),
    ("연세대학교(미래)",  "0000150"),
    ("고려대학교(세종)",  "0000070"),
    ("강원대학교",        "0000009"),
    ("한림대학교",        "0000196"),
    ("가톨릭관동대학교",  "0000008"),
    ("충남대학교",        "0000029"),
    ("충북대학교",        "0000181"),
    ("공주대학교",        "0000072"),
    ("순천향대학교",      "0000146"),
    ("단국대학교(천안)",  "0000088"),
    ("한국교원대학교",    "0000187"),
    ("한국기술교육대학교","0000189"),
    ("건양대학교",        "0000012"),
    ("호서대학교",        "0000207"),
    ("한밭대학교",        "0000198"),
    ("전남대학교",        "0000173"),
    ("전북대학교",        "0000174"),
    ("전주교육대학교",    "0000258"),
    ("진주교육대학교",    "0000260"),
    ("조선대학교",        "0000166"),
    ("목포대학교",        "0000113"),
    ("군산대학교",        "0000079"),
    ("순천대학교",        "0000144"),
    ("우석대학교",        "0000161"),
    ("경북대학교",        "0000057"),
    ("영남대학교",        "0000157"),
    ("계명대학교",        "0000060"),
    ("대구가톨릭대학교",  "0000082"),
    ("대구대학교",        "0000083"),
    ("안동대학교",        "0000153"),
    ("동국대학교(경주)",  "0000101"),
    ("부산대학교",        "0000025"),
    ("경상국립대학교",    "0000064"),
    ("동아대학교",        "0000104"),
    ("부경대학교",        "0000024"),
    ("경성대학교",        "0000062"),
    ("동의대학교",        "0000106"),
    ("울산대학교",        "0000162"),
    ("인제대학교",        "0000168"),
    ("신라대학교",        "0000141"),
    ("경남대학교",        "0000054"),
    ("제주대학교",        "0000178"),
]

async def search_univ(page, name):
    """adiga.kr univAjax에서 대학명으로 코드 검색, (code, adiga_name) 반환"""
    import json as _json
    keyword = re.sub(r'[(\[].*?[)\]]', '', name).strip()
    keyword_json = _json.dumps(keyword)
    resp = await page.evaluate(f"""async () => {{
        const fd = new FormData();
        fd.append('searchSyr', '2026');
        fd.append('searchUnvNm', {keyword_json});
        fd.append('searchStdClsfRgnCn', '');
        const res = await fetch('/ucp/uvt/uni/univAjax.do', {{
            method: 'POST', body: fd, credentials: 'include'
        }});
        return await res.text();
    }}""")
    pattern = r'code="(\d{7})">([^<]+)</a>'
    matches = re.findall(pattern, resp)
    return [(code, mname.strip()) for code, mname in matches]

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context(user_agent="Mozilla/5.0 Chrome/120.0.0.0")
        page = await context.new_page()

        await page.goto(
            "https://www.adiga.kr/ucp/uvt/uni/univDetailSelection.do?menuId=PCUVTINF2000&searchSyr=2026",
            wait_until="networkidle", timeout=30000
        )
        await asyncio.sleep(2)

        ok, wrong, notfound = [], [], []

        for name, our_code in OUR_LIST:
            results = await search_univ(page, name)
            await asyncio.sleep(0.3)

            if not results:
                notfound.append((name, our_code))
                continue

            # 가장 잘 맞는 결과 선택 (분교 포함 이름이면 정확 매칭 우선)
            base = re.sub(r'[(\[].*?[)\]]', '', name).strip()
            best = None
            for code, aname in results:
                if name in aname or aname.startswith(base):
                    best = (code, aname)
                    break
            if best is None:
                best = results[0]

            matched_code, matched_name = best
            if matched_code == our_code:
                ok.append((name, our_code))
            else:
                wrong.append((name, our_code, matched_code, matched_name))

        lines = []
        lines.append("=" * 60)
        lines.append(f"[OK] 코드 일치: {len(ok)}개")
        lines.append(f"[NG] 코드 불일치: {len(wrong)}개")
        lines.append(f"[??] adiga.kr 미발견: {len(notfound)}개")
        lines.append("=" * 60)

        if wrong:
            lines.append("")
            lines.append("[코드 불일치 -- 수정 필요]")
            for name, ours, theirs, aname in wrong:
                lines.append(f"  {name}: 현재={ours} -> 올바름={theirs}  (adiga명: {aname})")

        if notfound:
            lines.append("")
            lines.append("[adiga.kr 검색 안됨]")
            for name, code in notfound:
                lines.append(f"  {name}: {code}")

        if ok:
            lines.append("")
            lines.append("[코드 일치 -- 정상]")
            for name, code in ok:
                lines.append(f"  {name}: {code}")

        result_text = "\n".join(lines)
        with open("verify_result.txt", "w", encoding="utf-8") as f:
            f.write(result_text)
        print("결과 저장: verify_result.txt")

        await browser.close()

asyncio.run(main())
