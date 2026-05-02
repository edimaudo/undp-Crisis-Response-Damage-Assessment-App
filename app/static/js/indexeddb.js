const dbName="crisis-db";

function initDB(){
 return new Promise(res=>{
  let r=indexedDB.open(dbName,1);
  r.onupgradeneeded=e=>{
    e.target.result.createObjectStore("queue",{keyPath:"id",autoIncrement:true});
  };
  r.onsuccess=()=>res(r.result);
 });
}
