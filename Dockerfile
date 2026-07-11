# Playwright(헤드리스 Chromium)가 이미 설치된 공식 이미지 사용
# requirements.txt의 playwright==1.40.0 과 버전을 맞춤
FROM mcr.microsoft.com/playwright/python:v1.40.0-jammy

WORKDIR /app

# 의존성 먼저 설치 (캐시 활용)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 서버 코드와 API 응답에 필요한 HTML 복사
COPY grade_server.py .
COPY 합격등급비교.html .

# Render가 PORT 환경변수를 주입함 (grade_server.py가 이미 os.environ["PORT"] 지원)
EXPOSE 5000

CMD ["python", "grade_server.py"]
