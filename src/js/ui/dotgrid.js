// ═══════════════════════════════════════════
// DOTGRID — textura de pontos no fundo (canvas), na cor do tema (--dot)
// ═══════════════════════════════════════════
// contrato: RP.dotgrid = { draw(), bind() }
// depende de: RP.config
(function (RP) {
  'use strict';

  const canvas = document.getElementById('dotgrid'), ctx = canvas.getContext('2d');
  const { gap, radius } = RP.config.dotgrid;

  function draw(){
    const W = canvas.width = innerWidth, H = canvas.height = innerHeight;
    ctx.clearRect(0, 0, W, H);
    ctx.fillStyle = getComputedStyle(document.documentElement).getPropertyValue('--dot').trim();
    for (let y = 0; y < H; y += gap) for (let x = 0; x < W; x += gap) {
      ctx.beginPath(); ctx.arc(x, y, radius, 0, Math.PI * 2); ctx.fill();
    }
  }
  const bind = () => window.addEventListener('resize', draw);

  RP.dotgrid = { draw, bind };
}(window.RP = window.RP || {}));
