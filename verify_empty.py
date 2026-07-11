"""
완전히 빈 응답(499-506 bytes)인 13개 대학의 코드가 맞는지 확인.
각 코드로 adiga.kr univDetail 페이지를 열어 실제 대학명 추출.
"""
import asyncio, re
from playwright.async_api import async_playwright

EMPTY_ONES = [
    ("국민대학교",        "0000077"),
    ("명지대학교",        "0000110"),
    ("홍익대학교",        "0000210"),
    ("덕성여자대학교",    "0000090"),
    ("한국항공대학교",    "0000193"),
    ("단국대학교(죽전)",  "0000087"),
    ("전북대학교",        "0000174"),
    ("전주교육대학교",    "0000258"),
    ("조선대학교",        "0000166"),
    ("경북대학교",        "0000057"),
    ("영남대학교",        "0000157"),
    ("대구대학교",        "0000083"),
    ("울산대학교",        "0000162"),
]

async def get_name_for_code(page, code):
    """univDetail 페이지에서 대학명 추출"""
    await page.goto(
        f"https://www.adiga.kr/ucp/uvt/uni/univDetail.do"
        f"?menuId=PCUVTINF2000&searchSyr=2026&unvCd={code}",
        wait_until="networkidle", timeout=30000
    )
    await asyncio.sleep(2)
    # og:title 또는 title 태그에서 대학명 추출
    title = await page.title()
    og_title = await page.get_attribute('meta[property="og:title"]', "content") or ""
    # 페이지 내 h1, h2 태그
    h_texts = await page.evaluate("""() => {
        const els = document.querySelectorAll('h1, h2, .univName, .univ-name, [class*="univNm"], [class*="unvNm"]');
        return Array.from(els).map(e => e.textContent.trim()).filter(t => t.length > 1);
    }""")
    # 학교명 포함될만한 클래스명
    inner = await page.evaluate("""() => document.body.innerText""")
    # 교명 패턴 (대학교로 끝나는 것)
    univs = re.findall(r'[가-힣]{2,10}(?:대학교|교육대학교|과학기술대학교)', inner)
    top = list(dict.fromkeys(univs))[:5]  # 순서 유지 dedup, 상위 5개
    return {
        "title": title[:80],
        "og_title": og_title[:80],
        "h_tags": h_texts[:3],
        "top_univs": top
    }

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context(user_agent="Mozilla/5.0 Chrome/120.0.0.0")
        page = await context.new_page()

        lines = []
        for our_name, code in EMPTY_ONES:
            info = await get_name_for_code(page, code)
            lines.append(f"\n[{our_name}] 코드={code}")
            lines.append(f"  title: {info['title']}")
            lines.append(f"  og:title: {info['og_title']}")
            lines.append(f"  h태그: {info['h_tags']}")
            lines.append(f"  페이지 내 대학명: {info['top_univs']}")
            # 우리가 찾는 대학명이 있는지 확인
            base = re.sub(r'[(\[（【].*?[)\]）】]', '', our_name).strip()
            found = any(base in u or u.startswith(base[:3]) for u in info['top_univs'])
            lines.append(f"  -> 코드 일치: {'OK' if found else 'NG - 다른 대학 또는 미공개'}")
            print(lines[-4])
            print(lines[-1])

        with open("verify_empty_result.txt", "w", encoding="utf-8") as f:
            f.write("\n".join(lines))
        print("\n결과 저장: verify_empty_result.txt")
        await browser.close()

asyncio.run(main())
