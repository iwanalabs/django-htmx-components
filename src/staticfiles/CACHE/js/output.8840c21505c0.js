{const data=document.currentScript.dataset;const isDebug=data.debug==="True";if(isDebug){document.addEventListener("htmx:beforeOnLoad",function(event){const xhr=event.detail.xhr;if(xhr.status==500||xhr.status==404){event.stopPropagation();document.children[0].innerHTML=xhr.response;(1,eval)(document.scripts[0].innerText);window.onload();}});}};