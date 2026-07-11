"""
adiga.kr 팝업 페이지의 비교대학 드롭다운에서 전체 코드 추출 후 우리 목록 대조
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

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context(user_agent="Mozilla/5.0 Chrome/120.0.0.0")
        page = await context.new_page()

        # 팝업 페이지 로드 (아무 대학 코드나)
        await page.goto(
            "https://www.adiga.kr/uct/acd/ade/criteriaAndResultPopup.do"
            "?unvCd=0000019&searchSyr=2026&tsrdCmphSlcnArtclUpCd=10",
            wait_until="networkidle", timeout=30000
        )
        await asyncio.sleep(2)

        # 모든 select 옵션에서 대학 코드/이름 추출
        options = await page.evaluate("""() => {
            const results = [];
            document.querySelectorAll('select option').forEach(opt => {
                if (opt.value && /^\\d{7}$/.test(opt.value)) {
                    results.push({code: opt.value, name: opt.textContent.trim()});
                }
            });
            return results;
        }""")

        # 비교대학 추가 드롭다운 AJAX 응답 캡처
        ajax_options = []
        async def on_resp(response):
            if "Ajax" in response.url or "ajax" in response.url:
                try:
                    body = await response.body()
                    text = body.decode("utf-8", "ignore")
                    found = re.findall(r'code="(\d{7})">([^<]+)</a>', text)
                    if found:
                        ajax_options.extend(found)
                except Exception:
                    pass
        page.on("response", on_resp)

        # 비교대학 섹션에서 대학 선택 드롭다운 트리거
        try:
            # 비교대학 추가 버튼 클릭
            btn = await page.query_selector("button.addCompUniv, button[onclick*='comp'], .compareUniv button")
            if btn:
                await btn.click()
                await asyncio.sleep(2)
        except Exception:
            pass

        print(f"select 옵션: {len(options)}개")
        print(f"AJAX 옵션: {len(ajax_options)}개")

        # 전체 페이지 HTML에서 대학 코드 패턴 추출
        content = await page.content()
        html_codes = re.findall(r'(?:value|code)="(\d{7})"[^>]*>([가-힣\w\[\]()（）\s]+)', content)

        # 코드→이름 맵 구축
        code_map = {}
        for code, name in options:
            n = name.strip()
            if n and '선택' not in n:
                code_map[code] = n
        for code, name in ajax_options:
            n = name.strip()
            if n:
                code_map[code] = n
        for code, name in html_codes:
            n = name.strip()
            if n and len(n) > 2 and '선택' not in n:
                code_map[code] = n

        print(f"수집된 고유 코드: {len(code_map)}개")

        # 수집된 코드 샘플 출력
        sample = list(code_map.items())[:20]
        for c, n in sample:
            print(f"  {c}: {n}")

        # 개별 검색으로 나머지 채우기
        print("\n개별 검색 시작...")
        await page.goto(
            "https://www.adiga.kr/ucp/uvt/uni/univDetailSelection.do?menuId=PCUVTINF2000&searchSyr=2026",
            wait_until="networkidle", timeout=30000
        )
        await asyncio.sleep(2)

        name_to_code = {v: k for k, v in code_map.items()}
        results = {"ok": [], "wrong": [], "unknown": []}

        for our_name, our_code in OUR_LIST:
            base = re.sub(r'[(\[（【].*?[)\]）】]', '', our_name).strip()

            if our_code in code_map:
                adiga_name = code_map[our_code]
                if base in adiga_name:
                    results["ok"].append((our_name, our_code, adiga_name))
                else:
                    results["wrong"].append((our_name, our_code, adiga_name))
            else:
                # 이름으로 코드 역검색
                best_code = None
                for acode, aname in code_map.items():
                    if base in aname:
                        best_code = (acode, aname)
                        break

                # 없으면 AJAX 검색
                if not best_code:
                    kw_json = json.dumps(base)
                    resp_text = await page.evaluate(f"""async () => {{
                        const fd = new FormData();
                        fd.append('searchSyr', '2026');
                        fd.append('searchUnvNm', {kw_json});
                        fd.append('searchStdClsfRgnCn', '');
                        const res = await fetch('/ucp/uvt/uni/univAjax.do', {{
                            method: 'POST', body: fd, credentials: 'include'
                        }});
                        return await res.text();
                    }}""")
                    found = re.findall(r'code="(\d{7})">([^<]+)</a>', resp_text)
                    found_filtered = [(c, n.strip()) for c, n in found if base in n.strip() or n.strip().startswith(base[:2])]
                    if found_filtered:
                        best_code = found_filtered[0]
                    await asyncio.sleep(0.3)

                if best_code:
                    if best_code[0] == our_code:
                        results["ok"].append((our_name, our_code, best_code[1]))
                    else:
                        results["unknown"].append((our_name, our_code, f"-> {best_code[0]} ({best_code[1]})"))
                else:
                    results["unknown"].append((our_name, our_code, "검색 안됨"))

        lines = []
        lines.append("=" * 70)
        lines.append(f"[OK] 정상: {len(results['ok'])}개")
        lines.append(f"[NG] 코드가 다른 대학 매핑: {len(results['wrong'])}개")
        lines.append(f"[??] 불명확: {len(results['unknown'])}개")
        lines.append("=" * 70)

        if results["wrong"]:
            lines.append("\n[NG] 우리 코드가 다른 대학을 가리킴:")
            for name, ours, aname in results["wrong"]:
                lines.append(f"  {name}: {ours} -> 실제 [{aname}]")

        if results["unknown"]:
            lines.append("\n[??] 코드 재확인 필요:")
            for name, ours, info in results["unknown"]:
                lines.append(f"  {name}: {ours} | {info}")

        if results["ok"]:
            lines.append("\n[OK] 확인 완료:")
            for name, code, aname in results["ok"]:
                lines.append(f"  {name}: {code} ({aname})")

        text = "\n".join(lines)
        with open("verify_result3.txt", "w", encoding="utf-8") as f:
            f.write(text)
        print("\n결과 저장: verify_result3.txt")
        await browser.close()

asyncio.run(main())
