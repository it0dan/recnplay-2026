"""Base comum das ferramentas: caminhos do repositório, leitura do src/deck.json e
abertura do deck no Chromium (Playwright). Não é executado diretamente."""
import contextlib, json, pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
SRC = ROOT / 'src'
DECK = ROOT / 'presentation.html'          # gerado por tools/build.py
DIST = ROOT / 'dist'


def manifest():
    """src/deck.json → dict, com a lista achatada de slides em 'order'."""
    m = json.loads((SRC / 'deck.json').read_text(encoding='utf-8'))
    m['order'] = [s for sec in m['sections'] for s in sec['slides']]
    return m


def require_deck():
    if not DECK.exists():
        raise SystemExit('presentation.html não encontrado: rode python3 tools/build.py')


@contextlib.asynccontextmanager
async def open_deck(width=1600, height=900, **page_opts):
    """Abre o presentation.html e entrega (page, errors), com os erros de JS coletados."""
    from playwright.async_api import async_playwright
    require_deck()
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page(viewport={'width': width, 'height': height}, **page_opts)
        errors = []
        page.on('pageerror', lambda e: errors.append(str(e)))
        page.on('console', lambda m: errors.append(m.text) if m.type == 'error' else None)
        await page.goto(DECK.as_uri() + '#0')
        await page.evaluate('document.fonts.ready')          # mede com as fontes do deck, não com as de fallback
        await page.wait_for_timeout(500)
        try:
            yield page, errors
        finally:
            await browser.close()


async def goto_slide(page, i, wait_ms=400):
    await page.evaluate(f"location.hash='#{i}'"); await page.wait_for_timeout(wait_ms)


async def slide_count(page):
    return await page.evaluate('RP.core.slides.length')
