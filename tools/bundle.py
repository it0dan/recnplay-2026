#!/usr/bin/env python3
"""Gera dist/recnplay-2026.html: o deck inteiro num único arquivo, com CSS (inclusive os
@import), JS, fontes e imagens embutidos. É o backup para pendrive ou e-mail.

    python3 tools/bundle.py

Parte do presentation.html gerado; rode tools/build.py antes se mudou algo em src/.
"""
import base64, mimetypes, re
from _deck import ROOT, DECK, DIST, require_deck

OUT = DIST / 'recnplay-2026.html'
URL = re.compile(r"""url\((['"]?)(?!data:|https?:|#)([^'")]+)\1\)""")
IMPORT = re.compile(r'@import url\("([^"]+)"\);')


def data_uri(path):
    mime = mimetypes.guess_type(path.name)[0] or ('font/woff2' if path.suffix == '.woff2' else 'application/octet-stream')
    return f'data:{mime};base64,{base64.b64encode(path.read_bytes()).decode()}'


def css(path):
    """CSS de um arquivo com @import resolvidos (na mesma ordem) e url() relativos embutidos."""
    text = path.read_text(encoding='utf-8')
    text = IMPORT.sub(lambda m: css((path.parent / m.group(1)).resolve()), text)
    return URL.sub(lambda m: f'url({data_uri((path.parent / m.group(2)).resolve())})', text)


def main():
    require_deck()
    html = DECK.read_text(encoding='utf-8')
    html = re.sub(r'<!--.*?-->', '', html, flags=re.S)        # comentários (inclui exemplos de <img>)
    html = re.sub(r'<link rel="stylesheet" href="([^"]+)"/>', lambda m: f'<style>\n{css(ROOT / m.group(1))}</style>', html)
    html = re.sub(r'<script src="([^"]+)"></script>',
                  lambda m: '<script>\n' + (ROOT / m.group(1)).read_text(encoding='utf-8').replace('</script', '<\\/script') + '</script>', html)
    html = re.sub(r'<link rel="manifest"[^>]*/>\n?', '', html)   # o arquivo único não é instalável: sem manifesto
    html = re.sub(r'<link rel="icon" href="(assets/[^"]+)"', lambda m: f'<link rel="icon" href="{data_uri(ROOT / m.group(1))}"', html)
    html = re.sub(r'<img ([^>]*?)src="(assets/[^"]+)"', lambda m: f'<img {m.group(1)}src="{data_uri(ROOT / m.group(2))}"', html)
    leftovers = re.findall(r'(?:href|src)="(?!data:|https?:|#)[^"]+"|@import', html)
    assert not leftovers, f'referências locais não embutidas: {leftovers[:5]}'
    OUT.parent.mkdir(exist_ok=True)
    OUT.write_text(html, encoding='utf-8')
    print(f'{OUT.relative_to(ROOT)} · {len(html) // 1024} KB')


if __name__ == '__main__':
    main()
