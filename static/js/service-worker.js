const CACHE_NAME = "cyberwatch-v1";

const urlsToCache = [
  "/",
  "/index.html",
  "/offline.html",
  "/static/css/style.css",
  "/static/js/script.js",
  "/static/icons/icon-192.png"
];

self.addEventListener("install", event => {
  event.waitUntil(
    caches.open(CACHE_NAME)
      .then(cache => cache.addAll(urlsToCache))
  );
});

self.addEventListener("fetch", event => {
  event.respondWith(
    caches.match(event.request)
      .then(response => {
        return response || fetch(event.request).catch(() => {
          return caches.match("/offline.html");
        });
      })
  );
});