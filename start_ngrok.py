#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ngrok을 사용하여 로컬 Python 서버를 공개 URL로 노출
grade_server.py가 localhost:5000에서 실행 중이어야 합니다.
"""

from pyngrok import ngrok
import time
import sys
import io

# Windows 콘솔 UTF-8 설정
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

print("=" * 60)
print("[시작] ngrok 시작 중...")
print("=" * 60)

try:
    # ngrok 구성 (포트 5000 포워딩)
    public_url = ngrok.connect(5000, "http")
    print("\n[성공] ngrok 터널 생성 완료!")
    print(f"\n[URL] 공개 주소: {public_url}")
    print(f"\n[지시] 다음 URL을 합격등급비교.html의 334줄에 입력하세요:")
    print(f"   const API = '{public_url}';")
    print("\n" + "=" * 60)
    print("[상태] 실행 중... (Ctrl+C 눌러서 종료)")
    print("=" * 60 + "\n")

    # 계속 실행 유지
    ngrok_process = ngrok.get_ngrok_process()
    ngrok_process.proc.wait()

except KeyboardInterrupt:
    print("\n\n[종료] ngrok 종료됨")
    ngrok.kill()
    sys.exit(0)
except Exception as e:
    print(f"\n[오류] {e}")
    sys.exit(1)
