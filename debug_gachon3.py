"""가천대학교 adiga.kr 코드 확인 및 반도체 데이터 탐색"""
import asyncio, json, re
from playwright.async_api import async_playwright

async def test():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context(user_agent="Mozilla/5.0 Chrome/120.0.0.0")
        page = await context.new_page()

        ajax_hits = []
        async def on_response(response):
            url = response.url
            try:
                body = await response.body()
                text = body.decode("utf-8", "ignore")
                if len(body) > 200 and "ajax" in url.lower():
                    ajax_hits.append({"url": url, "size": len(body), "text": text[:500]})
            except Exception:
                pass
        page.on("response", on_response)

        # adiga.kr 대학 검색 API로 가천대 코드 찾기
        search_url = "https://www.adiga.kr/ucp/uvt/uni/univDetailSelection.do?menuId=PCUVTINF2000&searchSyr=2026&searchUnivNm=%EA%B0%80%EC%B2%9C%EB%8C%80%ED%95%99%EA%B5%90"
        await page.goto(search_url, wait_until="networkidle", timeout=30000)
        await asyncio.sleep(2)

        content = await page.content()

        # unvCd 패턴 추출
        codes = re.findall(r"unvCd[='\"\s:]+([0-9]{7})", content)
        names = re.findall(r"가천[^\s<\"']{0,15}", content)
        print("발견된 unvCd:", list(set(codes))[:10])
        print("가천 관련 텍스트:", list(set(names))[:10])

        # href에서 가천대 관련 링크 추출
        links = re.findall(r'href="([^"]*(?:gachon|0000006|0000005)[^"]*)"', content, re.IGNORECASE)
        print("가천 관련 링크:", links[:10])

        print(f"\nAJAX 응답 {len(ajax_hits)}건:")
        for h in ajax_hits[:5]:
            print(f"  {h['url']} ({h['size']}b)")

        await browser.close()

asyncio.run(test())
