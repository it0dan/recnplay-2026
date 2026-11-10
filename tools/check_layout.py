#!/usr/bin/env python3
"""Checagem de layout: abre cada slide do presentation.html e aponta texto vazando
do palco, texto de diagrama saindo da forma que o contém ou sobreposto a outro texto,
blocos de código com rolagem horizontal e erros de JavaScript.

    python3 tools/check_layout.py           # só relatório
    python3 tools/check_layout.py --shots   # + screenshots em dist/shots/
"""
import asyncio, json, sys
from _deck import DIST, open_deck, goto_slide, slide_count

SHOTS = DIST / 'shots'

PROBE = """() => {
  const s=document.querySelector('.slide.active'), sb=s.getBoundingClientRect();
  const foot=s.querySelector('.hud-bottom').getBoundingClientRect(), body=s.querySelector('.body');
  const over=[];
  s.querySelectorAll('.body *').forEach(el=>{ const r=el.getBoundingClientRect();
    if(r.width && (r.bottom>foot.top+1 || r.right>sb.right-40)) over.push(el.tagName+'.'+(el.className.baseVal??el.className)); });
  const pre=[...s.querySelectorAll('pre')].filter(p=>p.scrollWidth>p.clientWidth+1).map(p=>'pre '+p.scrollWidth+'/'+p.clientWidth);
  return {over:over.slice(0,6), pre, tall: body.scrollHeight>body.clientHeight+2};
}"""

SVG_TEXT = """() => { const out=[]; const s=document.querySelector('.slide.active');
 // caixas em coordenadas do <svg> (respeita transform dos grupos)
 const toRoot=(svg,el)=>svg.getScreenCTM().inverse().multiply(el.getScreenCTM());
 const bb=(svg,el)=>{ const b=el.getBBox(), m=toRoot(svg,el), P=(x,y)=>{const p=svg.createSVGPoint(); p.x=x; p.y=y; return p.matrixTransform(m);};
   const c=[P(b.x,b.y),P(b.x+b.width,b.y),P(b.x,b.y+b.height),P(b.x+b.width,b.y+b.height)];
   const xs=c.map(p=>p.x), ys=c.map(p=>p.y); return {x:Math.min(...xs),y:Math.min(...ys),width:Math.max(...xs)-Math.min(...xs),height:Math.max(...ys)-Math.min(...ys)}; };
 s.querySelectorAll('svg').forEach(svg=>{
  const shapes=[...svg.querySelectorAll('rect,polygon,ellipse,circle')].filter(r=>{const b=r.getBBox(); return b.width>24&&b.height>16;});
  svg.querySelectorAll('text').forEach(t=>{ const b=bb(svg,t); if(!b.width) return;
    const P=(x,y)=>{const p=svg.createSVGPoint(); p.x=x; p.y=y; return p;};
    const inside=(sh,p)=>{ try{ const q=p.matrixTransform(toRoot(svg,sh).inverse()); return sh.isPointInFill(q);}catch(e){return false;} };
    const c=P(b.x+b.width/2,b.y+b.height/2);
    const area=sh=>{const k=bb(svg,sh); return k.width*k.height;};
    const cont=shapes.filter(sh=>inside(sh,c)).sort((a,z)=>area(a)-area(z))[0];
    if(!cont) return;
    const ins=0.15*b.height;
    const corners=[P(b.x+1,b.y+ins),P(b.x+b.width-1,b.y+ins),P(b.x+1,b.y+b.height-ins),P(b.x+b.width-1,b.y+b.height-ins)];
    if(corners.some(p=>!inside(cont,p))){ const k=bb(svg,cont), f=v=>v.toFixed(1);
      out.push(t.textContent.trim().slice(0,46)+' ⊄ '+cont.tagName+' (texto x '+f(b.x)+'→'+f(b.x+b.width)+', forma x '+f(k.x)+'→'+f(k.x+k.width)+')'); }
  });});
 s.querySelectorAll('svg').forEach(svg=>{ const ts=[...svg.querySelectorAll('text')].map(t=>({t,b:bb(svg,t)})).filter(o=>o.b.width);
   for(let i=0;i<ts.length;i++) for(let j=i+1;j<ts.length;j++){ const a=ts[i].b,c=ts[j].b;
     const ox=Math.min(a.x+a.width,c.x+c.width)-Math.max(a.x,c.x), oy=Math.min(a.y+a.height,c.y+c.height)-Math.max(a.y,c.y);
     if(ox>2&&oy>3) out.push('OVERLAP '+ts[i].t.textContent.trim().slice(0,25)+' × '+ts[j].t.textContent.trim().slice(0,25)); } });
 return out; }"""


async def main(shots):
    if shots: SHOTS.mkdir(parents=True, exist_ok=True)
    problems = 0
    async with open_deck() as (page, errors):
        n = await slide_count(page)
        for i in range(n):
            await goto_slide(page, i)
            r = await page.evaluate(PROBE)
            r['svg_text'] = await page.evaluate(SVG_TEXT)
            if r['over'] or r['pre'] or r['tall'] or r['svg_text']:
                problems += 1; print(f'slide {i:02d}', json.dumps(r, ensure_ascii=False))
            if shots: await page.screenshot(path=str(SHOTS / f's{i:02d}.png'))
        fonts = await page.evaluate("[...document.fonts].map(f => f.family + ':' + f.status).join(', ')")
    print(f'{n} slides · {problems} com problema · erros JS: {errors or "nenhum"} · fontes: {fonts}')
    sys.exit(1 if problems or errors else 0)

asyncio.run(main('--shots' in sys.argv))
