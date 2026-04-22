self.addEventListener('fetch', event => {
    event.respondWith(
        caches.open('my-pwa-cache')
            .then(cache => {
                return cache.match(event.request)
                    .then(response => {
                        return response || fetch(event.request);
                    });
            })
    );
});