#!/usr/bin/env python3
"""Exporta o deck para PDF: uma página por slide, com todos os passos revelados.

    python3 tools/export_pdf.py   # → dist/recnplay-2026.pdf

Requer: pip install -r requirements.txt && python3 -m playwright install chromium
Cada slide é capturado depois que as animações de entrada terminam.
"""
import asyncio, tempfile, pathlib
from PIL import Image
from _deck import ROOT, DIST, manifest, open_deck, goto_slide, slide_count

OUT = DIST / 'recnplay-2026.pdf'
DEFAULT_WAIT_MS = 3600
WAIT_MS = {'contexto-por-agente': 4500}   # slides com animação de entrada mais longa


async def main():
    order = manifest()['order']
    tmp = pathlib.Path(tempfile.mkdtemp())
    shots = []
    async with open_deck(1920, 1080) as (page, _):
        for i in range(await slide_count(page)):
            await goto_slide(page, i, WAIT_MS.get(order[i], DEFAULT_WAIT_MS))
            f = tmp / f's{i:02d}.png'; await page.screenshot(path=str(f)); shots.append(f)
    imgs = [Image.open(f).convert('RGB') for f in shots]
    OUT.parent.mkdir(exist_ok=True)
    imgs[0].save(OUT, save_all=True, append_images=imgs[1:], resolution=150)
    print(f'{OUT.relative_to(ROOT)} · {len(imgs)} páginas')

asyncio.run(main())
