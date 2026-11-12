#!/usr/bin/env python3
"""Gera docs/CUE-SHEET.md a partir de src/: ordem e seções do deck.json, tempo-alvo (data-t),
cliques internos (maior data-f) e falas (<aside class="notes">) de cada slide.

    python3 tools/make_cue_sheet.py

Rode depois de mexer em ordem, tempos ou notas, para o roteiro de palco não divergir do deck.
"""
import html, re
from _deck import ROOT, SRC, manifest

OUT = ROOT / 'docs/CUE-SHEET.md'
EVENT = "**TDC Stage · REC'n'Play 2026** · 12/11/2026 · 11:05 · CESAR Moinho, Sala Risoflora · Recife"
RESCUES = """## Resgates

- **Passador parou de responder**: use as setas ou `PageDown`/`PageUp` do notebook; o clique do mouse também avança.
- **Pulou um slide**: `←` volta um passo; `#N` no fim da URL abre o slide N com tudo revelado.
- **Tela errada / projetor cortando**: `F` (ou `F5`) entra e sai da tela cheia; o palco se ajusta sozinho a qualquer resolução.
- **Pergunta sobre fonte**: `S` abre as fontes; `G`, o glossário; `Esc` fecha.
- **Pausa ou problema técnico**: `B` ou `.` liga a tela de pausa com cronômetro.
- **Navegador sem acesso aos arquivos** (pendrive, e-mail): abra `dist/recnplay-2026.html`, a versão de arquivo único gerada por `tools/bundle.py`, ou o PDF de backup.
"""


def mmss(s):
    return f'{s // 60:02d}:{s % 60:02d}'


def slide(name):
    t = (SRC / 'slides' / name / 'slide.html').read_text(encoding='utf-8')
    m, s = re.search(r'data-t="(\d+):(\d\d)"', t).groups()
    label = html.unescape(re.search(r'<span class="sec">//\s*(.*?)</span>', t).group(1))
    notes = html.unescape(re.search(r'<aside class="notes">(.*?)</aside>', t, re.S).group(1)).strip()
    clicks = max([int(x) for x in re.findall(r'data-f="(\d+)"', t)] or [0])
    return {'name': name, 'label': label, 'secs': int(m) * 60 + int(s), 'target': f'{int(m)}:{s}', 'notes': notes, 'clicks': clicks}


def main():
    deck = manifest()
    total = deck['minutes'] * 60
    rows, talks, marks, acc, n = [], [], [], 0, 0
    for sec in deck['sections']:
        for name in sec['slides']:
            s = slide(name); acc += s['secs']
            rows.append(f"| {n:02d} | {s['label']} | `#{n}` | {s['target']} | {mmss(acc)} | {s['clicks'] or '—'} |")
            clicks = f"{s['clicks']} clique(s) internos antes de avançar" if s['clicks'] else 'sem cliques internos'
            talks.append(f"### {n:02d} · {s['label']}\n\n`slide-{name}` · alvo {s['target']} · {clicks}\n\n{s['notes']}\n")
            n += 1
        marks.append(f"| {sec['title']} | {n - 1:02d} | {mmss(acc)} | {mmss(total - acc)} |")
    out = [
        "# Cue sheet — Rec'n'Play 2026", '',
        '> Gerado por `tools/make_cue_sheet.py` a partir de `src/`. Não edite à mão: mude o slide e gere de novo.', '',
        'Mapa de palco: ordem dos slides, tempo-alvo de cada um, tempo acumulado e quantos cliques cada slide tem '
        'antes de avançar (fragmentos). As falas são as mesmas notas do apresentador que aparecem no deck com a tecla `N`.', '',
        f"{EVENT} · {deck['minutes']} min", '',
        '| # | Slide | Link | Alvo | Acumulado | Cliques |', '| --: | :-- | :-- | --: | --: | :--: |', *rows, '',
        f"Tempo-alvo total: **{mmss(acc)}** de {deck['minutes']} min; o tempo do último slide é o das perguntas.", '',
        '## Marcos para conferir no timer', '',
        'O timer da HUD (`T`) conta de 40:00 para baixo. Ao terminar cada bloco, ele deve estar perto de:', '',
        '| Bloco | Último slide | Decorrido | Timer marcando |', '| :-- | :--: | --: | --: |', *marks, '',
        RESCUES, '## Falas por slide', '', *talks,
    ]
    OUT.write_text('\n'.join(out).rstrip('\n') + '\n', encoding='utf-8')
    print(f'{OUT.relative_to(ROOT)} · {n} slides · {mmss(acc)}')


if __name__ == '__main__':
    main()
