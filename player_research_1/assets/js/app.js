const nav=document.querySelector("#nav"),menu=document.querySelector("#menuBtn");
menu?.addEventListener("click",()=>nav.classList.toggle("open"));
nav?.querySelectorAll("a").forEach(a=>a.addEventListener("click",()=>nav.classList.remove("open")));
const overlay=document.querySelector("#overlay");
document.querySelector("#searchBtn")?.addEventListener("click",()=>{overlay.classList.add("open");overlay.querySelector("input").focus()});
document.querySelector("#close")?.addEventListener("click",()=>overlay.classList.remove("open"));
document.addEventListener("keydown",e=>{if(e.key==="Escape")overlay.classList.remove("open")});
function findPlayer(){
 const q=document.querySelector("#playerSearch").value.trim(), p=document.querySelector("#position").value;
 const params=new URLSearchParams(); if(q)params.set("q",q); if(p)params.set("position",p);
 location.href="players.php"+(params.toString()?"?"+params:"");
}
