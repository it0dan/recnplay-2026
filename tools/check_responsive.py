#!/usr/bin/env python3
"""Checagem de celular e tablet: abre o deck em aparelhos emulados.
Deitado: o palco cabe inteiro na tela, toque e deslize navegam e o menu de toque alcança o que é atalho de teclado.
Em pé: a leitura vertical liga, nenhum conteúdo vaza para o lado, rolar troca o slide atual, o menu leva
de um slide a outro e, ao deitar o aparelho, o palco volta no mesmo slide.
No fim confere que, no notebook, nem os controles de toque nem a leitura vertical aparecem.

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


OVERFLOW = """(() => { const W = innerWidth, out = [];
  const clipped = el => { for (let e = el.parentElement; e && !e.classList.contains('slide'); e = e.parentElement) {
    if (getComputedStyle(e).overflowX !== 'visible') return true; } return false; };
  RP.core.slides.forEach((s, i) => s.querySelectorAll('.body *').forEach(el => {
    const r = el.getBoundingClientRect();
    if (r.width && (r.right > W + 1 || r.left < -1) && !clipped(el)) out.push(i + ':' + el.tagName + '.' + (el.className.baseVal ?? el.className)); }));
  return out.slice(0, 6); })()"""


async def reader(page, label, w, h, ok, shots):
    """Celular ou tablet em pé: leitura vertical."""
    ok(await page.evaluate("document.documentElement.classList.contains('read')"), 'leitura vertical não ligou em pé')
    over = await page.evaluate(OVERFLOW)
    ok(not over, f'conteúdo vazando para o lado: {over}')
    n = await page.evaluate('RP.core.slides.length')
    widths = await page.evaluate("RP.core.slides.map(s => Math.round(s.getBoundingClientRect().width))")
    ok(all(abs(x - w) <= 1 for x in widths), f'slides sem a largura da tela: {set(widths)}')
    await page.evaluate("RP.core.slides[7].scrollIntoView({block: 'start'})"); await page.wait_for_timeout(400)
    ok(await page.evaluate('RP.core.idx') == 7, 'rolar até um slide não o tornou o atual')
    await page.tap('#tfab'); await page.tap('#tmenu [data-act="next"]'); await page.wait_for_timeout(900)
    top = await page.evaluate("RP.core.slides[8].getBoundingClientRect().top")
    ok(await page.evaluate('RP.core.idx') == 8 and abs(top) < 4, 'menu "avançar" não rolou até o próximo slide')
    if not await page.is_visible('#tmenu'): await page.tap('#tfab')      # "avançar" mantém o menu aberto
    await page.tap('#tmenu [data-act="refs"]'); await page.wait_for_timeout(150)
    ok(await page.is_visible('#refpanel'), 'fontes não abriram na leitura vertical')
    await page.tap('#tfab'); await page.wait_for_timeout(150)
    idx_before = await page.evaluate('RP.core.idx')
    await page.touchscreen.tap(w * 0.7, h * 0.5); await page.wait_for_timeout(200)
    ok(await page.evaluate('RP.core.idx') == idx_before, 'toque na leitura vertical trocou de slide (deveria só rolar)')
    if shots: SHOTS.mkdir(parents=True, exist_ok=True); await page.screenshot(path=str(SHOTS / f"read-{label.replace(' ', '_')}.png"))
    # deitar o aparelho: volta ao palco, no mesmo slide
    await page.set_viewport_size({'width': h, 'height': w}); await page.wait_for_timeout(500)
    ok(not await page.evaluate("document.documentElement.classList.contains('read')"), 'ao deitar, a leitura vertical não desligou')
    ok(await page.evaluate('RP.core.idx') == idx_before, 'ao deitar, o palco não ficou no mesmo slide')
    l, t_, r, b, ww, hh = await page.evaluate(STAGE)
    ok(abs((r - l) / (b - t_) - 16 / 9) < 0.01 and r <= ww + 0.5 and b <= hh + 0.5, 'ao deitar, o palco não voltou ao 16:9 na tela')


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
    if not landscape:
        await reader(page, label, d['viewport']['width'], d['viewport']['height'], ok, shots)
        ok(not errors, f'erros JS: {errors}')
        await browser.close()
        print(('OK ' if not fails else 'ERR'), label, '· leitura vertical', *(['· ' + '; '.join(fails)] if fails else []))
        return not fails
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
    hidden = not await page.is_visible('#tfab') and not await page.evaluate("document.documentElement.classList.contains('touch') || document.documentElement.classList.contains('read')")
    await page.mouse.click(100, 450); await page.wait_for_timeout(100)      # com mouse, clicar à esquerda também avança
    fwd = await page.evaluate('RP.core.idx') == 1
    await browser.close()
    print(('OK ' if hidden and fwd else 'ERR'), 'notebook 1600×900 · sem controles de toque nem leitura vertical, clique sempre avança')
    return hidden and fwd


SHOTS = DIST / 'shots'

async def main(shots):
    require_deck()
    async with async_playwright() as p:
        res = [await device(p, n, l, shots) for n, l in DEVICES] + [await desktop(p)]
    sys.exit(0 if all(res) else 1)

asyncio.run(main('--shots' in sys.argv))
