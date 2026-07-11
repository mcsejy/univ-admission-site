"""가천대학교 adiga.kr 학과검색 경로 탐색"""
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
                # 반도체 또는 가천 데이터가 있으면 캡처
                if len(body) > 1000 and ("반도체" in text or "가천" in text or "grade" in text.lower()):
                    ajax_hits.append({"url": url, "size": len(body), "sample": text[:400]})
            except Exception:
                pass
        page.on("response", on_response)

        # adiga.kr 학과 검색 → 가천대학교 반도체
        search_url = "https://www.adiga.kr/ucp/cls/uni/classUnivAdmssView.do?menuId=PCUVTINF3000&searchSyr=2026"
        await page.goto(search_url, wait_until="networkidle", timeout=30000)
        await asyncio.sleep(2)

        # 대학교 선택
        try:
            # 가천대 검색
            inputs = await page.query_selector_all("input")
            for inp in inputs:
                ph = await inp.get_attribute("placeholder") or ""
                if "대학" in ph:
                    await inp.fill("가천대학교")
                    await asyncio.sleep(1)
                    print(f"입력 완료: {ph}")
                    break
        except Exception as e:
            print("input error:", e)

        # 학과 검색
        try:
            inputs2 = await page.query_selector_all("input")
            for inp in inputs2:
                ph = await inp.get_attribute("placeholder") or ""
                if "학과" in ph or "전공" in ph:
                    await inp.fill("반도체")
                    await asyncio.sleep(1)
                    print(f"학과 입력: {ph}")
                    break
        except Exception as e:
            print("dept input error:", e)

        # 검색 버튼 클릭
        try:
            btns = await page.query_selector_all("button")
            for btn in btns:
                txt = (await btn.inner_text()).strip()
                if "검색" in txt:
                    await btn.click()
                    await asyncio.sleep(3)
                    print(f"검색 클릭: {txt}")
                    break
        except Exception as e:
            print("btn error:", e)

        print(f"\n캡처된 AJAX 응답: {len(ajax_hits)}건")
        for h in ajax_hits:
            print(f"  URL: {h['url']}")
            print(f"  Size: {h['size']}")
            print(f"  Sample: {h['sample'][:200]}")
            print()

        await browser.close()

asyncio.run(test())
