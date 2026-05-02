function setFont(size){
 document.documentElement.dataset.font = size;
 localStorage.setItem("font", size);
}

function toggleTheme(){
 let t = document.documentElement.dataset.theme==="dark"?"light":"dark";
 document.documentElement.dataset.theme=t;
 localStorage.setItem("theme",t);
}

window.onload=()=>{
 document.documentElement.dataset.font=localStorage.getItem("font")||"medium";
 document.documentElement.dataset.theme=localStorage.getItem("theme")||"light";
}
