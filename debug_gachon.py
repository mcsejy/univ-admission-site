import asyncio, json
from playwright.async_api import async_playwright

captured_responses = []

async def test():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context(user_agent="Mozilla/5.0 Chrome/120.0.0.0")
        page = await context.new_page()

        async def on_response(response):
            url = response.url
            if any(k in url for k in ["Ajax", "ajax", "tsrd", "grade", "admss", "Rslt", "result"]):
                try:
                    body = await response.body()
                    if len(body) > 600:
                        captured_responses.append({
                            "url": url,
                            "size": len(body),
                            "sample": body[:300].decode("utf-8", "ignore")
                        })
                except Exception:
                    pass

        page.on("response", on_response)

        # 가천대 팝업 (tsrdCmphSlcnArtclUpCd=10 = 수시 전체)
        popup_url = "https://www.adiga.kr/uct/acd/ade/criteriaAndResultPopup.do?unvCd=0000006&searchSyr=2026&tsrdCmphSlcnArtclUpCd=10"
        await page.goto(popup_url, wait_until="networkidle", timeout=30000)
        await asyncio.sleep(3)

        # 탭 버튼들 클릭해보기
        tabs = await page.query_selector_all("button, a[class*=tab], li[class*=tab]")
        print(f"탭 요소 수: {len(tabs)}")
        for t in tabs[:10]:
            txt = (await t.inner_text()).strip()
            if txt:
                print(f"  탭: {txt}")

        print("\n캡처된 응답:")
        for r in captured_responses:
            print(f"  URL: {r['url']}")
            print(f"  Size: {r['size']}  Sample: {r['sample'][:120]}")
            print()

        # 페이지 가시 텍스트
        visible = await page.evaluate("() => document.body.innerText")
        lines = [l.strip() for l in visible.splitlines() if l.strip() and len(l.strip()) > 3]
        print("페이지 텍스트 (상위 30줄):")
        for l in lines[:30]:
            print(f"  {l}")

        await browser.close()

asyncio.run(test())
