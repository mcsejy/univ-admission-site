#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
로컬 Flask 서버의 CORS 문제를 해결하기 위한 간단한 프록시
외부에서 접속 가능하도록 0.0.0.0에 바인딩
"""

from flask import Flask, request, jsonify
import requests
from flask_cors import CORS
import sys
import io

# Windows 콘솔 UTF-8 설정
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

app = Flask(__name__)
CORS(app)

LOCAL_API = "http://localhost:5000"

@app.route('/api/<path:path>', methods=['GET', 'POST'])
def proxy_api(path):
    """로컬 grade_server.py로 요청을 프록시"""
    try:
        url = f"{LOCAL_API}/api/{path}"

        # 쿼리 파라미터 전달
        if request.query_string:
            url += f"?{request.query_string.decode()}"

        # 요청 전달
        if request.method == 'GET':
            response = requests.get(url)
        else:
            response = requests.post(url, json=request.get_json())

        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    print("[시작] 프록시 서버 시작...")
    print("[정보] 로컬 서버: http://localhost:5000")
    print("[정보] 프록시 서버: http://0.0.0.0:3000")
    print("[주소] http://localhost:3000에서 접속 가능")
    print("[주소] 외부 IP: http://<당신의-IP>:3000")
    print()

    app.run(host='0.0.0.0', port=3000, debug=False)
