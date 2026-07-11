# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Architecture

두 모듈이 역할을 분리한다:
- `js/storage.js` — `BucketStorage` 객체 리터럴: LocalStorage CRUD + 통계/필터링. UI 로직 없음.
- `js/app.js` — `BucketListApp` 클래스: DOM 조작, 이벤트 바인딩, 렌더링. 데이터 직접 접근 없음.

이 분리를 유지할 것. 새 기능 추가 시 데이터 조작은 `BucketStorage`에, UI 처리는 `BucketListApp`에 추가한다.

## Key Conventions

- **인덴트**: 4칸 스페이스
- **언어**: UI 텍스트와 코드 주석은 한국어로 유지
- **Tailwind CSS**: CDN으로 로드됨 (`index.html` `<head>`). npm/node 빌드 도구를 추가하지 말 것.
- **XSS 방지**: 사용자 입력을 HTML 템플릿에 삽입하기 전 반드시 `this.escapeHtml()`을 사용할 것
- **신규 항목 순서**: `BucketStorage.addItem()`은 `unshift()`로 최신 항목을 목록 상단에 추가함

## Data Model

LocalStorage 키: `bucketList` (JSON 배열)

```js
{ id: Date.now().toString(), title, completed: false, createdAt: ISO string, completedAt: null | ISO string }
```

## Running the App

VS Code Live Server 확장으로 `index.html`을 열거나, 터미널에서 `python -m http.server 8000` 실행 후 `http://localhost:8000` 접속. 빌드 단계 없음.
