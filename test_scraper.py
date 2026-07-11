# -*- coding: utf-8 -*-
import sys, asyncio, json
# Windows 콘솔 UTF-8 강제
sys.stdout.reconfigure(encoding="utf-8", errors="replace")

from playwright.async_api import async_playwright

API_HITS = []

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context(
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/120.0.0.0 Safari/537.36"
        )
        page = await context.new_page()

        # 모든 XHR/Fetch 응답 캡처
        async def on_response(resp):
            if resp.request.resource_type in ("xhr", "fetch") and "adiga.kr" in resp.url:
                try:
                    body = await resp.text()
                    API_HITS.append({"url": resp.url, "status": resp.status, "body": body[:600]})
                except Exception:
                    pass
        page.on("response", on_response)

        print("메인 접속...")
        await page.goto("https://www.adiga.kr", wait_until="load", timeout=20000)
        await asyncio.sleep(1)

        print("팝업 접속...")
        await page.goto(
            "https://www.adiga.kr/uct/acd/ade/criteriaAndResultPopup.do"
            "?unvCd=0000169&searchSyr=2026&tsrdCmphSlcnArtclUpCd=20",
            wait_until="load", timeout=30000
        )
        await asyncio.sleep(8)  # 동적 로딩 충분히 대기

        print(f"\n=== AJAX 응답 {len(API_HITS)}건 ===")
        for h in API_HITS:
            print(f"\n  URL: {h['url']}")
            print(f"  STATUS: {h['status']}")
            print(f"  BODY: {h['body'][:400]}")

        # 페이지 HTML 저장
        html = await page.content()
        with open("popup_output.html", "w", encoding="utf-8") as f:
            f.write(html)
        print(f"\n팝업 HTML 저장됨: popup_output.html ({len(html):,} bytes)")

        # 등급 관련 텍스트 추출
        text = await page.inner_text("body")
        with open("popup_text.txt", "w", encoding="utf-8") as f:
            f.write(text)

        relevant = [l.strip() for l in text.split("\n") if l.strip() and any(
            k in l for k in ["등급", "학과", "전형", "일본", "합격", "수시", "정시", "내신", "교과", "종합"]
        )]
        print(f"\n=== 관련 텍스트 ({len(relevant)}줄) ===")
        for l in relevant[:40]:
            print(f"  {l}")

        await browser.close()

asyncio.run(main())
