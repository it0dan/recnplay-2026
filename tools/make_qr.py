#!/usr/bin/env python3
"""Gera assets/qr.svg: QR code estilizado do último slide.

Módulos em pontos com degradê roxo → laranja (paleta Sensedia), marcadores de canto
arredondados e, no centro, o hexágono da tese ("núcleo probabilístico, casca
determinística"). Usa correção de erro H (30%), que cobre com folga a área do emblema.

    pip install qrcode opencv-python-headless   # opencv só para a verificação
    python3 tools/make_qr.py                    # URL padrão abaixo
    python3 tools/make_qr.py https://outra.url/
"""
import math, sys
import qrcode
from qrcode.constants import ERROR_CORRECT_H
from _deck import ROOT

URL = sys.argv[1] if len(sys.argv) > 1 else 'https://it0dan.github.io/recnplay-2026/'
OUT = ROOT / 'assets/qr.svg'

# cores escuras o bastante para contraste com fundo branco (leitura confiável)
C_START, C_END = '#4A1D6B', '#C2410C'     # degradê dos módulos
C_FINDER, C_EYE = '#4A1D6B', '#C2410C'    # moldura e "olho" dos marcadores

qr = qrcode.QRCode(error_correction=ERROR_CORRECT_H, border=0)
qr.add_data(URL); qr.make(fit=True)
M = qr.get_matrix(); N = len(M)
Q = 2                                       # zona de silêncio (módulos)
S = N + 2 * Q
c = S / 2                                   # centro

def in_finder(r, k):
    return any(r0 <= r < r0 + 7 and k0 <= k < k0 + 7 for r0, k0 in ((0, 0), (0, N - 7), (N - 7, 0)))

# emblema central: hexágono de raio ~ 17% do código
R_HEX = N * 0.17
def in_emblem(r, k):
    x, y = k + Q + .5 - c, r + Q + .5 - c
    return math.hypot(x, y) < R_HEX + 0.9

dots = []
for r in range(N):
    for k in range(N):
        if M[r][k] and not in_finder(r, k) and not in_emblem(r, k):
            dots.append(f'<circle cx="{k + Q + .5}" cy="{r + Q + .5}" r=".46"/>')

def finder(r0, k0):
    x, y = k0 + Q, r0 + Q
    return (f'<rect x="{x + .5}" y="{y + .5}" width="6" height="6" rx="2" fill="none" stroke="{C_FINDER}" stroke-width="1"/>'
            f'<rect x="{x + 2}" y="{y + 2}" width="3" height="3" rx="1" fill="{C_EYE}"/>')

def hexagon(r, **attrs):
    pts = ' '.join(f'{c + r * math.cos(math.radians(a)):.3f},{c + r * math.sin(math.radians(a)):.3f}' for a in range(0, 360, 60))
    return '<polygon points="' + pts + '" ' + ' '.join(f'{k.replace("_", "-")}="{v}"' for k, v in attrs.items()) + '/>'

emblem = ''.join([
    hexagon(R_HEX, fill='#FFFFFF', stroke=C_END, stroke_width='.55'),
    hexagon(R_HEX * .74, fill='none', stroke=C_FINDER, stroke_width='.35', stroke_opacity='.55'),
    hexagon(R_HEX * .50, fill=C_FINDER),
    f'<text x="{c}" y="{c + .62}" text-anchor="middle" font-family="Montserrat, Arial, sans-serif" '
    f'font-weight="800" font-size="{R_HEX * .36:.2f}" fill="#FFFFFF">LLM</text>',
])

svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {S} {S}" role="img" aria-label="QR code: {URL}">
<defs><linearGradient id="qrg" x1="0" y1="0" x2="1" y2="1">
<stop offset="0" stop-color="{C_START}"/><stop offset="1" stop-color="{C_END}"/></linearGradient></defs>
<rect width="{S}" height="{S}" fill="#FFFFFF"/>
<g fill="url(#qrg)">{''.join(dots)}</g>
{finder(0, 0)}{finder(0, N - 7)}{finder(N - 7, 0)}
{emblem}
</svg>
'''
OUT.write_text(svg, encoding='utf-8')
print(f'assets/qr.svg → {URL} (versão {qr.version}, {N}×{N}, correção H)')
print('lembre de atualizar o texto da URL (classe .qr-url) em src/slides/obrigado/slide.html e rodar tools/build.py')
