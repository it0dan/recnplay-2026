#!/usr/bin/env python3
"""Lista e testa todos os links externos do deck (painel de fontes, slides e docs).

    python3 tools/check_links.py            # testa via HTTP (HEAD, cai para GET)
    python3 tools/check_links.py --list     # só lista, sem rede

Aponta: status >= 400, erro de rede e redirecionamento para outro domínio
(sinal de link que não leva mais à fonte original).
"""
import re, sys, urllib.request, urllib.error
from urllib.parse import urlparse
from _deck import ROOT, SRC

FILES = sorted(SRC.rglob('*.html'))
REDIRECTORS = {'doi.org'}   # resolvedores cujo redirecionamento é esperado
UA = 'Mozilla/5.0 (link-check; recnplay-2026 deck)'


def links():
    seen = {}
    for f in FILES:
        for m in re.finditer(r'<a[^>]+href="(https?://[^"]+)"[^>]*>', f.read_text(encoding='utf-8')):
            seen.setdefault(m.group(1), f.relative_to(ROOT).as_posix())
    return seen


def check(url):
    for method in ('HEAD', 'GET'):
        try:
            req = urllib.request.Request(url, method=method, headers={'User-Agent': UA})
            with urllib.request.urlopen(req, timeout=20) as r:
                return r.status, r.geturl()
        except urllib.error.HTTPError as e:
            if method == 'HEAD' and e.code in (403, 405, 429): continue
            return e.code, url
        except Exception as e:
            if method == 'GET': return f'erro: {type(e).__name__}', url
    return '?', url


def main():
    all_links = links()
    if '--list' in sys.argv:
        for u, f in all_links.items(): print(f'{f:44} {u}')
        return
    bad = 0
    for u, f in all_links.items():
        status, final = check(u)
        moved = urlparse(u).netloc not in REDIRECTORS and urlparse(final).netloc.removeprefix('www.') != urlparse(u).netloc.removeprefix('www.')
        flag = 'OK ' if isinstance(status, int) and status < 400 and not moved else 'ERR'
        bad += flag == 'ERR'
        print(f'{flag} {status} {u}' + (f'  → {final}' if moved else ''))
    print(f'{len(all_links)} links · {bad} com problema')
    sys.exit(1 if bad else 0)


if __name__ == '__main__':
    main()
