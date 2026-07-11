# -*- coding: utf-8 -*-
"""AJAX 응답 구조 확인 - 인하대 교과전형 2025 결과"""
import sys, asyncio, json
sys.stdout.reconfigure(encoding="utf-8", errors="replace")

from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context(
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
        )
        page = await context.new_page()

        # 교과전형 탭으로 팝업 로드
        url = ("https://www.adiga.kr/uct/acd/ade/criteriaAndResultPopup.do"
               "?unvCd=0000169&searchSyr=2026&tsrdCmphSlcnArtclUpCd=30")
        print(f"팝업 로드: {url}")
        await page.goto(url, wait_until="load", timeout=30000)
        await asyncio.sleep(2)

        csrf = await page.get_attribute('meta[name="_csrf"]', "content") or ""
        print(f"CSRF: {csrf[:20]}...")

        # 폼 데이터
        form_data = await page.evaluate("""() => {
            const frm = document.getElementById('frm');
            const data = {};
            for (const el of frm.elements) {
                if (el.name) data[el.name] = el.value;
            }
            return data;
        }""")
        print(f"폼 데이터: {json.dumps(form_data, ensure_ascii=False)}")

        # AJAX POST: 2025학년도 전형 결과 (artCd=22)
        resp = await page.evaluate(f"""async () => {{
            const fd = new FormData();
            const params = {json.dumps({**form_data, "tsrdCmphSlcnArtclCd": "22"})};
            for (const [k, v] of Object.entries(params)) fd.append(k, v);
            const res = await fetch('https://www.adiga.kr/uct/acd/ade/criteriaAndResultItemAjax.do', {{
                method: 'POST',
                headers: {{
                    'X-CSRF-TOKEN': '{csrf}',
                    'X-Requested-With': 'XMLHttpRequest'
                }},
                body: fd,
                credentials: 'include'
            }});
            return await res.text();
        }}""")

        print(f"\n응답 길이: {len(resp)} bytes")
        print(f"\n응답 미리보기:\n{resp[:2000]}")

        # 파일로 저장
        with open("ajax_response.html", "w", encoding="utf-8") as f:
            f.write(resp)
        print("\najax_response.html 저장 완료")

        await browser.close()

asyncio.run(main())
