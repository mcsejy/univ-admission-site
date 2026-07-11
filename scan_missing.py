# -*- coding: utf-8 -*-
"""
미스캔 범위(126-147, 176-187, 216-260)에서 데이터 있는 코드 찾기.
결과를 UTF-8 JSON 파일로 저장.
"""
import asyncio, json, re
from playwright.async_api import async_playwright

ADIGA = "https://www.adiga.kr"
POPUP_PATH = "/uct/acd/ade/criteriaAndResultPopup.do"
AJAX_PATH  = "/uct/acd/ade/criteriaAndResultItemAjax.do"

SCAN_RANGES = [
    (126, 147),
    (176, 190),
    (216, 262),
]

# 현재까지 확인된 대학 (건너뛸 코드들)
KNOWN = {
    "0000007","0000008","0000009","0000011","0000012","0000019",
    "0000024","0000025","0000029","0000040","0000054","0000056",
    "0000060","0000062","0000063","0000064","0000065","0000069",
    "0000070","0000072","0000073","0000078","0000079","0000082",
    "0000084","0000088","0000099","0000100","0000101","0000103",
    "0000104","0000106","0000111","0000113","0000116","0000119",
    "0000120","0000125","0000128","0000133","0000136","0000141",
    "0000143","0000144","0000145","0000146","0000147","0000148",
    "0000149","0000150","0000151","0000153","0000156","0000158",
    "0000161","0000163","0000168","0000169","0000170","0000172",
    "0000173","0000175","0000178","0000181","0000187","0000189",
    "0000192","0000194","0000196","0000198","0000200","0000203",
    "0000207","0000212","0000258","0000260",
}

TARGET_NAMES = {"경북대학교","전북대학교","단국대학교"}

async def get_csrf_and_form(page):
    await page.goto(
        f"{ADIGA}{POPUP_PATH}?unvCd=0000063&searchSyr=2026&tsrdCmphSlcnArtclUpCd=10",
        wait_until="load", timeout=30000,
    )
    await asyncio.sleep(2)
    csrf = await page.get_attribute('meta[name="_csrf"]', "content") or ""
    form_data = await page.evaluate("""() => {
        const frm = document.getElementById('frm');
        if (!frm) return {};
        const d = {};
        for (const el of frm.elements) { if (el.name) d[el.name] = el.value; }
        return d;
    }""")
    return csrf, form_data

async def check_size(page, csrf, form_data, code):
    fd = dict(form_data)
    fd["unvCd"] = code
    fd["tsrdCmphSlcnArtclUpCd"] = "10"
    fd["tsrdCmphSlcnArtclCd"] = "22"
    params_json = json.dumps(fd, ensure_ascii=False)
    csrf_safe = csrf.replace("'", "\\'")
    try:
        resp = await page.evaluate(f"""async () => {{
            const fd = new FormData();
            const p = {params_json};
            for (const [k,v] of Object.entries(p)) fd.append(k,v);
            const r = await fetch('{ADIGA}{AJAX_PATH}', {{
                method:'POST',
                headers:{{'X-CSRF-TOKEN':'{csrf_safe}','X-Requested-With':'XMLHttpRequest'}},
                body:fd, credentials:'include'
            }});
            return await r.text();
        }}""")
        return len(resp) if resp else 0
    except Exception:
        return -1

async def get_univ_name(page, code):
    try:
        await page.goto(
            f"{ADIGA}/ucp/uvt/uni/univDetail.do?menuId=PCUVTINF2000&searchSyr=2026&unvCd={code}",
            wait_until="networkidle", timeout=20000,
        )
        await asyncio.sleep(2)
        inner = await page.evaluate("() => document.body.innerText")
        univs = re.findall(r'[가-힣]{2,10}(?:대학교|교육대학교|과학기술대학교)', inner)
        return list(dict.fromkeys(univs))[:2]
    except Exception:
        return []

async def main():
    results = {}

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        ctx = await browser.new_context(
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/120.0.0.0"
        )

        scan_page = await ctx.new_page()
        csrf, form_data = await get_csrf_and_form(scan_page)

        name_page = await ctx.new_page()

        for start, end in SCAN_RANGES:
            for num in range(start, end + 1):
                code = f"{num:07d}"
                if code in KNOWN:
                    continue

                sz = await check_size(scan_page, csrf, form_data, code)
                if sz < 0:
                    # CSRF 만료 → 재취득
                    csrf, form_data = await get_csrf_and_form(scan_page)
                    sz = await check_size(scan_page, csrf, form_data, code)

                if sz > 550:
                    names = await get_univ_name(name_page, code)
                    results[code] = {"sz": sz, "names": names}
                    # 대상 대학 발견 시 출력
                    if any(t in n for t in TARGET_NAMES for n in names):
                        print(f"[TARGET] {code}: {names} ({sz:,}b)")
                    else:
                        print(f"  {code}: {names} ({sz:,}b)")
                else:
                    results[code] = {"sz": sz, "names": []}

        with open("scan_missing_result.json", "w", encoding="utf-8") as f:
            json.dump(results, f, ensure_ascii=False, indent=2)

        # 목표 대학 매핑 요약
        print("\n=== 목표 대학 결과 ===")
        for code, info in results.items():
            for name in info.get("names", []):
                if any(t in name for t in TARGET_NAMES):
                    print(f"  {name} -> {code}")

        await browser.close()

asyncio.run(main())
