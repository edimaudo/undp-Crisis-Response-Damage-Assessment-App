self.addEventListener("fetch",e=>{
 if(e.request.url.includes("tile.openstreetmap")){
  e.respondWith(
    caches.open("tiles").then(cache=>{
      return cache.match(e.request).then(resp=>{
        return resp||fetch(e.request).then(net=>{
          cache.put(e.request,net.clone());
          return net;
        });
      });
    })
  );
 }
});
