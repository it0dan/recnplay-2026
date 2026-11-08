#!/usr/bin/env python3
"""Monta o presentation.html (raiz) a partir de src/: esqueleto + painéis + slides na ordem
do src/deck.json + o CSS de cada slide. Só usa a biblioteca padrão.

    python3 tools/build.py           # gera presentation.html
    python3 tools/build.py --check   # não grava; falha se o presentation.html estiver desatualizado (CI)

Diretivas do src/shell.html:
    {{title}}                       título do src/deck.json
    <!-- @generated -->             aviso de arquivo gerado
    <!-- @slide-styles -->          <link> do slide.css de cada slide que tiver um
    <!-- @include caminho.html -->  conteúdo de src/caminho.html (recursivo)
    <!-- @slides -->                os slides, agrupados pelas seções do deck.json
    <!--# … -->                     comentário só do esqueleto (não vai para o HTML gerado)

Também valida cada slide (id, data-t, HUD, notas) e confere se a soma dos tempos-alvo
(data-t) fecha com a duração da palestra.
"""
import re, sys
from _deck import ROOT, SRC, DECK, manifest

GENERATED = ('<!-- GERADO por tools/build.py a partir de src/. Não edite aqui: '
             'edite src/ e rode "python3 tools/build.py". -->')
REQUIRED = {  # o que todo slide precisa ter, para HUD, notas e timer funcionarem
    'data-t="m:ss"': r'<section class="slide[^"]*" id="slide-{name}" data-t="\d+:\d\d"',
    'cabeçalho <div class="hud-top">': r'<div class="hud-top"></div>',
    'índice <span class="hb-idx">': r'<span class="hb-idx"></span>',
    'notas <aside class="notes">': r'<aside class="notes">',
}


class BuildError(Exception):
    pass


def include(path, seen=()):
    f = SRC / path
    if not f.exists(): raise BuildError(f'@include: src/{path} não existe')
    if path in seen: raise BuildError(f'@include circular: {" → ".join(seen + (path,))}')
    text = f.read_text(encoding='utf-8')
    return re.sub(r'<!-- @include (\S+) -->', lambda m: include(m.group(1), seen + (path,)).rstrip('\n'), text)


def slide_html(name):
    f = SRC / 'slides' / name / 'slide.html'
    if not f.exists(): raise BuildError(f'slide "{name}" está no deck.json, mas src/slides/{name}/slide.html não existe')
    html = f.read_text(encoding='utf-8').strip('\n')
    for what, pat in REQUIRED.items():
        if not re.search(pat.format(name=re.escape(name)), html):
            raise BuildError(f'src/slides/{name}/slide.html: falta {what} (id esperado: slide-{name})')
    if html.count('<section') != 1: raise BuildError(f'src/slides/{name}/slide.html: deve ter exatamente um <section>')
    return html


def seconds(t):
    m, s = t.split(':'); return int(m) * 60 + int(s)


def build():
    deck = manifest()
    order = deck['order']
    if len(set(order)) != len(order): raise BuildError('deck.json: slide repetido')
    orphans = sorted(p.name for p in (SRC / 'slides').iterdir() if p.is_dir() and p.name not in order)

    parts, total, n = [], 0, 0
    for sec in deck['sections']:
        parts.append(f'\n<!-- ═════════════ {sec["title"]} ═════════════ -->')
        for name in sec['slides']:
            html = slide_html(name)
            total += seconds(re.search(r'data-t="(\d+:\d\d)"', html).group(1))
            parts.append(f'<!-- {n:02d}-{name} -->\n{html}')
            n += 1
    styles = '\n'.join(f'<link rel="stylesheet" href="src/slides/{s}/slide.css"/>'
                       for s in order if (SRC / 'slides' / s / 'slide.css').exists())

    out = include('shell.html')
    out = re.sub(r'<!--#.*?-->\n?', '', out, flags=re.S)
    out = (out.replace('{{title}}', deck['title'])
              .replace('<!-- @generated -->', GENERATED)
              .replace('<!-- @slide-styles -->', styles)
              .replace('<!-- @slides -->', '\n'.join(parts).lstrip('\n')))
    left = re.findall(r'<!-- @\S+[^>]*-->|\{\{\w+\}\}', out)
    if left: raise BuildError(f'diretivas não resolvidas no shell.html: {left}')

    notes = [f'{n} slides', f'tempo-alvo {total // 60}:{total % 60:02d} de {deck["minutes"]}:00']
    if total != deck['minutes'] * 60: notes.append('ATENÇÃO: a soma dos data-t não fecha com a duração')
    if orphans: notes.append(f'pastas fora do deck.json (ignoradas): {", ".join(orphans)}')
    return out, notes


def main():
    try:
        html, notes = build()
    except BuildError as e:
        raise SystemExit(f'build: {e}')
    if '--check' in sys.argv:
        current = DECK.read_text(encoding='utf-8') if DECK.exists() else ''
        if current != html:
            raise SystemExit('presentation.html desatualizado: rode python3 tools/build.py e faça commit')
        print('presentation.html em dia · ' + ' · '.join(notes)); return
    DECK.write_text(html, encoding='utf-8')
    print(f'{DECK.relative_to(ROOT)} · ' + ' · '.join(notes))


if __name__ == '__main__':
    main()
