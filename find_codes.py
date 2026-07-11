# -*- coding: utf-8 -*-
"""
adiga.kr 대학 선택 페이지에서 전체 대학 코드 목록을 추출하고,
잘못된 12개 대학의 올바른 코드를 찾는다.
"""
import asyncio, json, re
from playwright.async_api import async_playwright

ADIGA = "https://www.adiga.kr"

# 코드를 찾아야 하는 대학들
TARGET_NAMES = [
    "국민대학교", "명지대학교", "홍익대학교", "덕성여자대학교",
    "한국항공대학교", "단국대학교", "전북대학교", "조선대학교",
    "경북대학교", "영남대학교", "대구대학교", "울산대학교",
]

async def extract_all_univ_codes(page):
    """univDetailSelection 페이지에서 전체 대학명+코드 추출"""
    await page.goto(
        f"{ADIGA}/ucp/uvt/uni/univDetailSelection.do?menuId=PCUVTINF2000&searchSyr=2026",
        wait_until="networkidle", timeout=30000,
    )
    await asyncio.sleep(3)

    # 방법 1: code= 속성이 있는 a 태그
    code_map = await page.evaluate("""() => {
        const result = {};
        // code 속성이 있는 a 태그
        document.querySelectorAll('a[code]').forEach(el => {
            const code = el.getAttribute('code');
            const name = el.textContent.trim();
            if (code && name) result[name] = code;
        });
        // data-unv-cd, data-cd 등 data 속성
        document.querySelectorAll('[data-unv-cd],[data-cd],[data-code]').forEach(el => {
            const code = el.getAttribute('data-unv-cd') || el.getAttribute('data-cd') || el.getAttribute('data-code');
            const name = el.textContent.trim();
            if (code && /\\d{7}/.test(code) && name) result[name] = code;
        });
        return result;
    }""")

    # 방법 2: 페이지 HTML에서 패턴 매칭
    html = await page.content()
    # <a ... code="0000007" ...>가톨릭대학교</a> 패턴
    pattern_matches = re.findall(r'code=["\'](\d{7})["\'][^>]*>([^<]{2,20}대학교[^<]*)</a>', html)
    for code, name in pattern_matches:
        name = name.strip()
        if name and name not in code_map:
            code_map[name] = code

    # 방법 3: univAjax로 목표 대학들 검색
    for target in TARGET_NAMES:
        resp = await page.evaluate(f"""async () => {{
            const fd = new FormData();
            fd.append('searchSyr', '2026');
            fd.append('searchUnvNm', {json.dumps(target)});
            fd.append('searchStdClsfRgnCn', '');
            const r = await fetch('/ucp/uvt/uni/univAjax.do', {{
                method: 'POST', body: fd, credentials: 'include'
            }});
            return await r.text();
        }}""")
        matches = re.findall(r'code=["\'](\d{7})["\'][^>]*>([^<]+)</a>', resp)
        for code, name in matches:
            name = name.strip()
            if name and name not in code_map:
                code_map[name] = code
        if matches:
            print(f"  univAjax [{target}]: {matches[:3]}")

    return code_map, html

async def verify_code_has_data(page, csrf, form_data, code):
    """해당 코드에 실제 데이터(합격등급)가 있는지 확인"""
    fd = dict(form_data)
    fd["unvCd"] = code
    fd["tsrdCmphSlcnArtclUpCd"] = "10"
    fd["tsrdCmphSlcnArtclCd"] = "22"
    params_json = json.dumps(fd, ensure_ascii=False)
    csrf_safe = csrf.replace("'", "\\'")
    resp = await page.evaluate(f"""async () => {{
        const fd = new FormData();
        const p = {params_json};
        for (const [k,v] of Object.entries(p)) fd.append(k,v);
        const r = await fetch('{ADIGA}/uct/acd/ade/criteriaAndResultItemAjax.do', {{
            method:'POST',
            headers:{{'X-CSRF-TOKEN':'{csrf_safe}','X-Requested-With':'XMLHttpRequest'}},
            body:fd, credentials:'include'
        }});
        return await r.text();
    }}""")
    sz = len(resp) if resp else 0
    # 499-506바이트 = 완전 빈 응답
    return sz, sz > 550

async def get_univ_name_for_code(page, code):
    """univDetail 페이지에서 대학명 확인"""
    await page.goto(
        f"{ADIGA}/ucp/uvt/uni/univDetail.do?menuId=PCUVTINF2000&searchSyr=2026&unvCd={code}",
        wait_until="networkidle", timeout=20000,
    )
    await asyncio.sleep(2)
    inner = await page.evaluate("() => document.body.innerText")
    univs = re.findall(r'[가-힣]{2,10}(?:대학교|교육대학교|과학기술대학교)', inner)
    return list(dict.fromkeys(univs))[:3]

async def scan_code_range(page, csrf, form_data, start, end, univ_page):
    """코드 범위를 스캔하여 데이터 있는 코드와 대학명 반환"""
    results = {}
    for num in range(start, end + 1):
        code = f"{num:07d}"
        sz, has_data = await verify_code_has_data(page, csrf, form_data, code)
        if has_data:
            names = await get_univ_name_for_code(univ_page, code)
            results[code] = {"sz": sz, "names": names}
            print(f"    코드 {code}: 데이터있음 ({sz}b) -> {names}")
        else:
            print(f"    코드 {code}: 빈응답 ({sz}b)")
    return results

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context(
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/120.0.0.0 Safari/537.36"
        )
        page = await context.new_page()
        univ_page = await context.new_page()

        # ── CSRF 획득 ──
        await page.goto(
            f"{ADIGA}/uct/acd/ade/criteriaAndResultPopup.do"
            "?unvCd=0000063&searchSyr=2026&tsrdCmphSlcnArtclUpCd=10",
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
        print(f"CSRF: {csrf[:20]}...")

        # ── 전체 대학 코드 추출 시도 ──
        print("\n=== 대학 선택 페이지에서 전체 코드 추출 ===")
        code_map, raw_html = await extract_all_univ_codes(page)
        print(f"추출된 대학 수: {len(code_map)}")

        # 목표 대학이 있는지 확인
        found = {}
        for target in TARGET_NAMES:
            # 완전 일치
            if target in code_map:
                found[target] = code_map[target]
                print(f"  ✓ {target}: {code_map[target]}")
            else:
                # 부분 일치
                for name, code in code_map.items():
                    if target[:3] in name:
                        print(f"  ~ {target} ≈ {name}: {code}")

        # HTML에서 추가 패턴 검색
        if len(found) < len(TARGET_NAMES):
            print("\n=== HTML 패턴 검색 ===")
            # 코드 + 대학명 패턴
            patterns = [
                r'unvCd=(\d{7})[^>]*>([^<]{2,20}대학교)',
                r"'(\d{7})'[^,}]{0,30}([가-힣]{2,10}대학교)",
                r'"(\d{7})"[^,}]{0,30}([가-힣]{2,10}대학교)',
            ]
            for pat in patterns:
                extra = re.findall(pat, raw_html)
                for code, name in extra:
                    name = name.strip()
                    if name and name not in code_map:
                        code_map[name] = code
                        if any(t[:3] in name for t in TARGET_NAMES):
                            print(f"  패턴발견: {name} = {code}")

        # ── 범위 스캔 (목표 대학 못 찾은 경우) ──
        missing = [t for t in TARGET_NAMES if t not in found]
        if missing:
            print(f"\n=== 코드 범위 스캔 ({len(missing)}개 대학) ===")
            print("범위: 0000050-0000099 (경~단 범위)")
            range_results = await scan_code_range(page, csrf, form_data, 50, 99, univ_page)

            print("범위: 0000100-0000125 (동~서 범위)")
            range_results2 = await scan_code_range(page, csrf, form_data, 100, 125, univ_page)

            print("범위: 0000150-0000175 (안~중 범위)")
            range_results3 = await scan_code_range(page, csrf, form_data, 150, 175, univ_page)

            print("범위: 0000190-0000215 (한~홍 범위)")
            range_results4 = await scan_code_range(page, csrf, form_data, 190, 215, univ_page)

        # ── 결과 저장 ──
        output = {
            "code_map": code_map,
            "found": found,
            "missing": missing,
        }
        with open("find_codes_result.json", "w", encoding="utf-8") as f:
            json.dump(output, f, ensure_ascii=False, indent=2)
        print("\n결과 저장: find_codes_result.json")

        await browser.close()

asyncio.run(main())
