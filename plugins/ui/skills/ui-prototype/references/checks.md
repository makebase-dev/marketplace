# Checks after every change

## Contrast over tokens

A Node script reads `tokens.json` and asserts every foreground/background pair the components use, per theme (4.5 text, 3 large text and non-text). Add a pair before a component uses it. Run it with the token build on every colour change.

## DOM check (paste into the browser via javascript_tool)

Run per theme × language after waiting for transitions:

```js
function lum(c){const m=c.match(/[\d.]+/g).map(Number);const [r,g,b]=m.slice(0,3).map(v=>{v/=255;return v<=.04045?v/12.92:((v+.055)/1.055)**2.4});return .2126*r+.7152*g+.0722*b}
function bgOf(el){while(el){const s=getComputedStyle(el);const a=(s.backgroundColor.match(/[\d.]+/g)||[]).map(Number);if(a.length&&(a.length<4||a[3]>.9))return s.backgroundColor;el=el.parentElement}return getComputedStyle(document.body).backgroundColor}
const out={broken:[],leak:[],lowContrast:[],small:[],noName:[],hscroll:[]};
document.querySelectorAll('body *').forEach(el=>{
  for(const a of el.attributes) if(/[<>]/.test(a.value)) out.broken.push(a.name);            // HTML leaked into attributes
  const tn=[...el.childNodes].filter(n=>n.nodeType===3).map(n=>n.textContent).join('').trim();
  if(/\$\{|undefined|NaN/.test(tn)) out.leak.push(tn.slice(0,30));                           // template leaks
  if(tn&&!el.closest('[inert],[disabled]')){const s=getComputedStyle(el),bg=bgOf(el),r=(Math.max(lum(s.color),lum(bg))+.05)/(Math.min(lum(s.color),lum(bg))+.05),sz=parseFloat(s.fontSize);if(r<((sz>=24||(sz>=18.66&&+s.fontWeight>=700))?3:4.5))out.lowContrast.push(tn.slice(0,20)+' '+r.toFixed(2))}
  if(el.matches('button,a,input:not(.sr)')&&!el.closest('[inert]')){const b=el.getBoundingClientRect();if(b.width&&(b.width<24||b.height<24))out.small.push((el.getAttribute('aria-label')||el.textContent).trim().slice(0,20));if(!(el.getAttribute('aria-label')||el.textContent||el.labels?.length).toString().trim())out.noName.push(el.outerHTML.slice(0,60))}
  if(el.scrollWidth>el.clientWidth+1&&['auto','scroll'].includes(getComputedStyle(el).overflowX))out.hscroll.push(el.className);
});
JSON.stringify({...out,h1:document.querySelectorAll('h1').length,bdi:document.querySelectorAll('bdi').length,docOverflow:document.documentElement.scrollWidth>innerWidth})
```

## Manual sweep

- Widths 375, 820, 1280 (and 1920 for side-by-side reading); dark and light; every language.
- Keyboard: Tab order, radios with arrows, sheets trap and close on Esc, focus returns.
- Reduced motion on: nothing moves, fades remain, the timer still updates.
- First visit with storage cleared; a full task flow; a timed flow to the end.
- Console: no errors.
