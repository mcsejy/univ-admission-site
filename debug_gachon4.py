"""adiga.kr univAjax에서 가천대학교 코드 및 반도체 데이터 탐색"""
import asyncio, json, re
from playwright.async_api import async_playwright

async def test():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context(user_agent="Mozilla/5.0 Chrome/120.0.0.0")
        page = await context.new_page()

        univ_data = {}
        async def on_response(response):
            url = response.url
            if "univAjax" in url or "univGroupAjax" in url:
                try:
                    body = await response.body()
                    text = body.decode("utf-8", "ignore")
                    if "가천" in text:
                        univ_data[url] = text
                except Exception:
                    pass
        page.on("response", on_response)

        search_url = "https://www.adiga.kr/ucp/uvt/uni/univDetailSelection.do?menuId=PCUVTINF2000&searchSyr=2026"
        await page.goto(search_url, wait_until="networkidle", timeout=30000)
        await asyncio.sleep(3)

        for url, text in univ_data.items():
            print(f"URL: {url}")
            # 가천 주변 텍스트 50자
            idx = text.find("가천")
            if idx >= 0:
                print(f"가천 컨텍스트: {text[max(0,idx-50):idx+100]}")
            print()

        # 직접 API 호출
        print("=== univAjax 직접 호출 ===")
        resp = await page.evaluate("""async () => {
            const fd = new FormData();
            fd.append('searchSyr', '2026');
            fd.append('searchUnvNm', '가천대학교');
            fd.append('searchStdClsfRgnCn', '');
            const res = await fetch('/ucp/uvt/uni/univAjax.do', {
                method: 'POST',
                body: fd,
                credentials: 'include'
            });
            return await res.text();
        }""")
        if resp:
            print(f"univAjax 응답 ({len(resp)}b):")
            # 가천 찾기
            idx = resp.find("가천")
            if idx >= 0:
                print(resp[max(0,idx-100):idx+300])
            else:
                print(resp[:500])

        await browser.close()

asyncio.run(test())
