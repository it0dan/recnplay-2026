// ═══════════════════════════════════════════
// HUD — cabeçalho do evento em todo slide + índice "07 / 13" no rodapé
// ═══════════════════════════════════════════
// contrato: RP.hud = { mount(), sync() }
// o cabeçalho vem de RP.config.event e é montado em cada <div class="hud-top"></div>
// depende de: RP.config, RP.core, RP.util
(function (RP) {
  'use strict';

  function mount(){
    const html = '<div class="l">' + RP.config.event.map(t => '<span>' + t + '</span>').join('') + '</div>' +
                 '<div class="r"><span class="pulse"></span><span class="hud-timer">--:--</span></div>';
    document.querySelectorAll('.hud-top').forEach(el => { el.innerHTML = html; });
  }
  // cada slide mostra o próprio número: no palco só o atual aparece; na leitura vertical, todos
  function sync(){
    const { pad } = RP.util, tot = pad(RP.core.slides.length - 1);
    RP.core.slides.forEach((s, i) => s.querySelectorAll('.hb-idx').forEach(el => { el.textContent = pad(i) + ' / ' + tot; }));
  }

  RP.hud = { mount, sync };
}(window.RP = window.RP || {}));
