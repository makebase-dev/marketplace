# Scripted page check

Run this on every rendered state, in every theme and text direction, whether or not an automated checker exists. It reads the page only. With no checker in the project, it is the automated pass; report it as "scripted page check", never as axe or Lighthouse.

Wait until transitions and animations have finished (poll for the screen's main element, or wait about 1 s after navigation) before running it.

```js
function lum(c){const m=c.match(/[\d.]+/g).map(Number);const [r,g,b]=m.slice(0,3).map(v=>{v/=255;return v<=.04045?v/12.92:((v+.055)/1.055)**2.4});return .2126*r+.7152*g+.0722*b}
function bgOf(el){while(el){const s=getComputedStyle(el);const a=(s.backgroundColor.match(/[\d.]+/g)||[]).map(Number);if(a.length&&(a.length<4||a[3]>.9))return s.backgroundColor;el=el.parentElement}return getComputedStyle(document.body).backgroundColor}
const out={brokenAttr:[],leakedText:[],lowContrast:[],smallTarget:[],noName:[],hScroll:[]};
document.querySelectorAll('body *').forEach(el=>{
  for(const a of el.attributes) if(/[<>]/.test(a.value)) out.brokenAttr.push(a.name+'='+a.value.slice(0,30));
  const tn=[...el.childNodes].filter(n=>n.nodeType===3).map(n=>n.textContent).join('').trim();
  if(/\$\{|undefined|NaN|\[object/.test(tn)) out.leakedText.push(tn.slice(0,30));
  if(tn&&!el.closest('[inert],[disabled],[aria-hidden="true"]')){const s=getComputedStyle(el);if(s.visibility!=='hidden'&&+s.opacity>0.9){const bg=bgOf(el),r=(Math.max(lum(s.color),lum(bg))+.05)/(Math.min(lum(s.color),lum(bg))+.05),sz=parseFloat(s.fontSize);if(r<((sz>=24||(sz>=18.66&&+s.fontWeight>=700))?3:4.5))out.lowContrast.push(tn.slice(0,20)+' '+r.toFixed(2))}}
  if(el.matches('button,a[href],input:not([type=hidden]),select,textarea,[role=button]')&&!el.closest('[inert]')){const b=el.getBoundingClientRect();if(b.width&&(b.width<24||b.height<24))out.smallTarget.push((el.getAttribute('aria-label')||el.textContent||el.name||'').trim().slice(0,20)+' '+Math.round(b.width)+'x'+Math.round(b.height));const name=(el.getAttribute('aria-label')||el.getAttribute('aria-labelledby')||el.textContent||(el.labels&&el.labels.length?'label':'')||el.title||'').toString().trim();if(!name)out.noName.push(el.outerHTML.slice(0,60))}
  if(el.scrollWidth>el.clientWidth+1&&['auto','scroll'].includes(getComputedStyle(el).overflowX))out.hScroll.push(el.className||el.tagName);
});
for(const k in out) out[k]=[...new Set(out[k])].slice(0,10);
JSON.stringify({...out,h1:document.querySelectorAll('h1').length,lang:document.documentElement.lang,dir:document.documentElement.dir,bdi:document.querySelectorAll('bdi').length,docOverflow:document.documentElement.scrollWidth>innerWidth})
```

## Reading the result

| Field | Failure | Criterion |
|---|---|---|
| `brokenAttr` | HTML or markup inside an attribute (often a regex run over finished HTML) | 4.1.2 |
| `leakedText` | Template text shown to users | 3.3.2 / content |
| `lowContrast` | Text below 4.5:1 (3:1 large) against its effective background | 1.4.3 |
| `smallTarget` | Below 24 × 24 CSS px; check the spacing exception before reporting | 2.5.8 |
| `noName` | Control with no accessible name | 4.1.2 |
| `hScroll` | A scroll container that overflows; check it is intended | 1.4.10 |
| `h1` | Not exactly 1 per screen | 1.3.1, 2.4.6 |
| `docOverflow` | Page scrolls sideways | 1.4.10 |

Limits: the contrast pass skips gradients, images and semi-transparent layers (screenshot those), and treats a pseudo-element label as missing. Report them under manual checks.

## Scaled frames

Prototype pages often draw tablet and desktop frames at real size and scale them with `transform: scale()`. Measured sizes then shrink by the scale: divide `getBoundingClientRect()` sizes by the frame's scale before comparing with 24 px or 44 px, and run reflow checks on the real page at real widths, not on the frames.
