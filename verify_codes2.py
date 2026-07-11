"""
각 코드로 adiga.kr univDetail API를 호출해서 실제 대학교명을 가져와 우리 목록과 비교.
페이지 로드 없이 API 직접 호출.
"""
import asyncio, re, json
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

async def get_univ_name(page, code):
    """univAjax에서 코드로 역검색 — 코드가 HTML에 있으면 그 대학명 반환"""
    resp = await page.evaluate(f"""async () => {{
        const fd = new FormData();
        fd.append('searchSyr', '2026');
        fd.append('searchUnvNm', '');
        fd.append('searchStdClsfRgnCn', '');
        const res = await fetch('/ucp/uvt/uni/univAjax.do', {{
            method: 'POST', body: fd, credentials: 'include'
        }});
        return await res.text();
    }}""")
    # code="{code}"> 바로 뒤 대학명 추출
    pattern = rf'code="{code}">([^<]+)</a>'
    m = re.search(pattern, resp)
    if m:
        return m.group(1).strip(), resp
    return None, resp

async def search_by_name(page, keyword):
    """이름으로 검색해서 (code, name) 목록 반환"""
    kw_json = json.dumps(keyword)
    resp = await page.evaluate(f"""async () => {{
        const fd = new FormData();
        fd.append('searchSyr', '2026');
        fd.append('searchUnvNm', {kw_json});
        fd.append('searchStdClsfRgnCn', '');
        const res = await fetch('/ucp/uvt/uni/univAjax.do', {{
            method: 'POST', body: fd, credentials: 'include'
        }});
        return await res.text();
    }}""")
    pattern = r'code="(\d{7})">([^<]+)</a>'
    return [(code, name.strip()) for code, name in re.findall(pattern, resp)]

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

        # Phase 1: 전체 목록 한번에 가져오기 (이름 없이 검색)
        print("Phase 1: 전체 대학 목록 수집 중...")
        _, full_html = await get_univ_name(page, "DUMMY_IMPOSSIBLE")
        all_univs = dict(re.findall(r'code="(\d{7})">([^<]+)</a>', full_html))
        # code -> name 역방향
        code_to_name = {code: name.strip() for code, name in re.findall(r'code="(\d{7})">([^<]+)</a>', full_html)}
        print(f"  전체 목록에서 {len(code_to_name)}개 코드 발견")

        ok, wrong, notfound_in_list = [], [], []

        for our_name, our_code in OUR_LIST:
            adiga_name = code_to_name.get(our_code)
            base = re.sub(r'[(\[（【].*?[)\]）】]', '', our_name).strip()

            if adiga_name is None:
                # Phase 2: 이름으로 검색
                results = await search_by_name(page, base)
                await asyncio.sleep(0.2)
                if not results:
                    notfound_in_list.append((our_name, our_code, None))
                else:
                    # 가장 잘 맞는 것 찾기
                    best = next(((c,n) for c,n in results if base in n), results[0])
                    if best[0] == our_code:
                        ok.append((our_name, our_code, adiga_name or best[1]))
                    else:
                        notfound_in_list.append((our_name, our_code, f"{best[0]} ({best[1]})"))
            else:
                if base in adiga_name or adiga_name.startswith(base):
                    ok.append((our_name, our_code, adiga_name))
                else:
                    wrong.append((our_name, our_code, adiga_name))

        lines = []
        lines.append("=" * 70)
        lines.append(f"[OK] 코드 일치: {len(ok)}개")
        lines.append(f"[NG] 코드가 다른 대학 매핑됨: {len(wrong)}개")
        lines.append(f"[??] 전체목록에 없음 (개별검색 결과): {len(notfound_in_list)}개")
        lines.append("=" * 70)

        if wrong:
            lines.append("")
            lines.append("[NG] 현재 코드가 다른 대학을 가리킴 -- 코드 찾기 필요")
            for name, ours, aname in wrong:
                lines.append(f"  {name}: 코드 {ours} -> adiga에서는 [{aname}]")

        if notfound_in_list:
            lines.append("")
            lines.append("[??] 전체목록 미포함 -- 개별검색 결과")
            for name, ours, suggestion in notfound_in_list:
                lines.append(f"  {name}: {ours} | 검색결과: {suggestion}")

        if ok:
            lines.append("")
            lines.append("[OK] 확인된 정상 코드")
            for name, code, aname in ok:
                lines.append(f"  {name}: {code} ({aname})")

        result_text = "\n".join(lines)
        with open("verify_result2.txt", "w", encoding="utf-8") as f:
            f.write(result_text)
        print("결과 저장: verify_result2.txt")
        await browser.close()

asyncio.run(main())
