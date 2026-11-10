#!/usr/bin/env python3
"""Checagem de celular e tablet: abre o deck em aparelhos emulados e confere que o palco cabe
inteiro na tela, que toque e deslize navegam e que o menu de toque alcança o que é atalho de teclado.
No fim confere que, no notebook, os controles de toque não aparecem.

    python3 tools/check_responsive.py           # só relatório
    python3 tools/check_responsive.py --shots   # + screenshots em dist/shots/
"""
import asyncio, sys
from playwright.async_api import async_playwright
from _deck import DECK, DIST, require_deck

DEVICES = [  # (nome do Playwright, deitado?)
    ('iPhone 13', True), ('iPhone 13', False), ('Pixel 7', True), ('iPad (gen 7)', True), ('iPad (gen 7)', False),
]
STAGE = "(() => { const r = document.getElementById('stage').getBoundingClientRect(); return [r.left, r.top, r.right, r.bottom, innerWidth, innerHeight]; })()"
SWIPE = """(dx) => { const el = document.querySelector('.slide.active'), y = innerHeight / 2, x0 = innerWidth / 2;
  const T = x => new Touch({ identifier: 1, target: el, clientX: x, clientY: y });
  el.dispatchEvent(new TouchEvent('touchstart', { bubbles: true, touches: [T(x0)], changedTouches: [T(x0)] }));
  el.dispatchEvent(new TouchEvent('touchend', { bubbles: true, touches: [], changedTouches: [T(x0 + dx)] })); }"""


async def device(p, name, landscape, shots):
    d = dict(p.devices[name]); fails = []
    if landscape: d['viewport'] = {'width': d['viewport']['height'], 'height': d['viewport']['width']}
    label = f"{name} {'deitado' if landscape else 'em pé'} {d['viewport']['width']}×{d['viewport']['height']}"
    browser = await p.chromium.launch()
    ctx = await browser.new_context(**{k: v for k, v in d.items() if k != 'default_browser_type'})
    page = await ctx.new_page(); errors = []
    page.on('pageerror', lambda e: errors.append(str(e)))
    await page.goto(DECK.as_uri() + '#0'); await page.evaluate('document.fonts.ready'); await page.wait_for_timeout(400)
    idx = lambda: page.evaluate('RP.core.idx')
    ok = lambda cond, msg: None if cond else fails.append(msg)

    ok(await page.evaluate("document.documentElement.classList.contains('touch')"), 'html.touch ausente')
    l, t, r, b, w, h = await page.evaluate(STAGE)
    ok(l >= -0.5 and t >= -0.5 and r <= w + 0.5 and b <= h + 0.5, f'palco fora da tela: {l:.0f},{t:.0f},{r:.0f},{b:.0f} em {w}×{h}')
    ok(abs((r - l) - w) < 1.5 or abs((b - t) - h) < 1.5, 'palco não ocupa a largura nem a altura')
    ok(abs((r - l) / (b - t) - 16 / 9) < 0.01, 'palco fora de 16:9')

    await page.touchscreen.tap(w * 0.7, h * 0.5); await page.wait_for_timeout(150)
    ok(await idx() == 1, 'toque à direita não avançou')
    await page.touchscreen.tap(w * 0.1, h * 0.5); await page.wait_for_timeout(150)
    ok(await idx() == 0, 'toque na faixa esquerda não voltou')
    await page.evaluate(SWIPE, -120); await page.wait_for_timeout(150)
    ok(await idx() == 1, 'deslizar para a esquerda não avançou')
    await page.evaluate(SWIPE, 120); await page.wait_for_timeout(150)
    ok(await idx() == 0, 'deslizar para a direita não voltou')

    await page.tap('#tfab'); await page.wait_for_timeout(150)
    ok(await page.is_visible('#tmenu'), 'menu de toque não abriu')
    if shots: SHOTS.mkdir(parents=True, exist_ok=True); await page.screenshot(path=str(SHOTS / f"touch-{label.replace(' ', '_')}.png"))
    mb = await page.evaluate("(() => { const r = document.getElementById('tmenu').getBoundingClientRect(); return [r.left, r.top, r.right, r.bottom]; })()")
    ok(mb[0] >= 0 and mb[1] >= 0 and mb[2] <= w and mb[3] <= h, 'menu de toque sai da tela')
    await page.tap('#tmenu [data-act="refs"]'); await page.wait_for_timeout(150)
    ok(await page.is_visible('#refpanel') and not await page.is_visible('#tmenu'), 'fontes não abriram pelo menu')
    over = await page.evaluate("(() => { const b = document.querySelector('#refpanel .bkp-body'); return b.scrollWidth > b.clientWidth + 1; })()")
    ok(not over, 'painel de fontes com rolagem horizontal')
    await page.tap('#tfab'); await page.wait_for_timeout(150)
    ok(not await page.is_visible('#refpanel'), 'botão ✕ não fechou o painel')
    await page.tap('#tfab'); await page.tap('#tmenu [data-act="notes"]'); await page.wait_for_timeout(150)
    ok(await page.is_visible('#notesbar'), 'notas não abriram pelo menu')
    await page.tap('#tfab'); await page.tap('#tmenu [data-act="pause"]'); await page.wait_for_timeout(150)
    ok(await page.is_visible('#blackout'), 'pausa não abriu pelo menu')
    await page.touchscreen.tap(w * 0.5, h * 0.5); await page.wait_for_timeout(150)
    ok(not await page.is_visible('#blackout') and await idx() == 0, 'toque não saiu da pausa (ou avançou o slide)')
    ok(not errors, f'erros JS: {errors}')
    await browser.close()
    print(('OK ' if not fails else 'ERR'), label, *(['· ' + '; '.join(fails)] if fails else []))
    return not fails


async def desktop(p):
    browser = await p.chromium.launch()
    page = await browser.new_page(viewport={'width': 1600, 'height': 900})
    await page.goto(DECK.as_uri() + '#0'); await page.wait_for_timeout(300)
    hidden = not await page.is_visible('#tfab') and not await page.evaluate("document.documentElement.classList.contains('touch')")
    await page.mouse.click(100, 450); await page.wait_for_timeout(100)      # com mouse, clicar à esquerda também avança
    fwd = await page.evaluate('RP.core.idx') == 1
    await browser.close()
    print(('OK ' if hidden and fwd else 'ERR'), 'notebook 1600×900 · sem controles de toque, clique sempre avança')
    return hidden and fwd


SHOTS = DIST / 'shots'

async def main(shots):
    require_deck()
    async with async_playwright() as p:
        res = [await device(p, n, l, shots) for n, l in DEVICES] + [await desktop(p)]
    sys.exit(0 if all(res) else 1)

asyncio.run(main('--shots' in sys.argv))
