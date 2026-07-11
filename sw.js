const CACHE_NAME = 'bucket-list-v1';
const urlsToCache = [
    '/',
    '/index.html',
    '/css/styles.css',
    '/js/storage.js',
    '/js/app.js',
    '/manifest.json',
    'https://cdn.tailwindcss.com',
    'https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@400;500;700;900&display=swap',
];

// 설치 이벤트
self.addEventListener('install', event => {
    event.waitUntil(
        caches.open(CACHE_NAME).then(cache => {
            return cache.addAll(urlsToCache).catch(() => {
                // 일부 외부 리소스 로드 실패해도 계속 진행
                return Promise.resolve();
            });
        }).then(() => self.skipWaiting())
    );
});

// 활성화 이벤트
self.addEventListener('activate', event => {
    event.waitUntil(
        caches.keys().then(cacheNames => {
            return Promise.all(
                cacheNames.map(cacheName => {
                    if (cacheName !== CACHE_NAME) {
                        return caches.delete(cacheName);
                    }
                })
            );
        }).then(() => self.clients.claim())
    );
});

// Fetch 이벤트
self.addEventListener('fetch', event => {
    const url = new URL(event.request.url);

    // 로컬호스트/127.0.0.1 요청은 캐싱하지 않음 (개발 서버 제외)
    if (url.hostname === 'localhost' || url.hostname === '127.0.0.1' || url.hostname.startsWith('192.168.')) {
        // 개발 서버로의 요청은 그냥 네트워크 요청만 함
        if (event.request.method === 'GET') {
            event.respondWith(fetch(event.request));
        }
        return;
    }

    // GET 요청만 캐싱
    if (event.request.method !== 'GET') {
        return;
    }

    event.respondWith(
        caches.match(event.request).then(response => {
            // 캐시에 있으면 반환
            if (response) {
                return response;
            }

            // 네트워크에서 가져오기
            return fetch(event.request).then(response => {
                // 200 상태 코드가 아니면 캐싱하지 않음
                if (!response || response.status !== 200 || response.type === 'error') {
                    return response;
                }

                // 응답 복제
                const responseToCache = response.clone();

                caches.open(CACHE_NAME).then(cache => {
                    cache.put(event.request, responseToCache);
                });

                return response;
            }).catch(() => {
                // 네트워크 실패 시 캐시된 응답 반환
                return caches.match(event.request).then(response => {
                    if (response) {
                        return response;
                    }
                    // 모든 실패 시 오프라인 페이지 반환 가능
                    return new Response('오프라인 상태입니다. 인터넷 연결을 확인하세요.', {
                        status: 503,
                        statusText: 'Service Unavailable',
                        headers: new Headers({
                            'Content-Type': 'text/plain; charset=utf-8'
                        })
                    });
                });
            });
        })
    );
});

// 백그라운드 동기화 (선택사항)
self.addEventListener('sync', event => {
    if (event.tag === 'sync-bucket-list') {
        event.waitUntil(
            // 여기에 동기화 로직 추가 가능
            Promise.resolve()
        );
    }
});
