htmx.defineExtension("preload",{onEvent:function(name,event){if(name!=="htmx:afterProcessNode"){return;}
var attr=function(node,property){if(node==undefined){return undefined;}
return node.getAttribute(property)||node.getAttribute("data-"+property)||attr(node.parentElement,property)}
var load=function(node){var done=function(html){if(!node.preloadAlways){node.preloadState="DONE"}
if(attr(node,"preload-images")=="true"){document.createElement("div").innerHTML=html}}
return function(){if(node.preloadState!=="READY"){return;}
var hxGet=node.getAttribute("hx-get")||node.getAttribute("data-hx-get")
if(hxGet){htmx.ajax("GET",hxGet,{source:node,handler:function(elt,info){done(info.xhr.responseText);}});return;}
if(node.getAttribute("href")){var r=new XMLHttpRequest();r.open("GET",node.getAttribute("href"));r.onload=function(){done(r.responseText);};r.send();return;}}}
var init=function(node){if(node.getAttribute("href")+node.getAttribute("hx-get")+node.getAttribute("data-hx-get")==""){return;}
if(node.preloadState!==undefined){return;}
var on=attr(node,"preload")||"mousedown"
const always=on.indexOf("always")!==-1
if(always){on=on.replace('always','').trim()}
node.addEventListener(on,function(evt){if(node.preloadState==="PAUSE"){node.preloadState="READY";if(on==="mouseover"){window.setTimeout(load(node),100);}else{load(node)()}}})
switch(on){case"mouseover":node.addEventListener("touchstart",load(node));node.addEventListener("mouseout",function(evt){if((evt.target===node)&&(node.preloadState==="READY")){node.preloadState="PAUSE";}})
break;case"mousedown":node.addEventListener("touchstart",load(node));break;}
node.preloadState="PAUSE";node.preloadAlways=always;htmx.trigger(node,"preload:init")}
event.target.querySelectorAll("[preload]").forEach(function(node){init(node)
node.querySelectorAll("a,[hx-get],[data-hx-get]").forEach(init)})}});