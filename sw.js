self.addEventListener('install',(e)=>{e.waitUntil(caches.open('ray-v01').then((c)=>c.addAll(['./','./index.html','./manifest.json','./sw.js','./version.json']).catch(()=>{})))});
self.addEventListener('fetch',(e)=>{if(new URL(e.request.url).origin===location.origin){e.respondWith(caches.match(e.request).then((r)=>r||fetch(e.request)));}});
