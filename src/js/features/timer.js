// ═══════════════════════════════════════════
// TIMER — contagem regressiva na HUD (T inicia/pausa · R zera)
// ═══════════════════════════════════════════
// contrato: RP.timer = { toggle(), reset(), render() }
// depende de: RP.config, RP.util
(function (RP) {
  'use strict';

  const { totalSeconds, warnAtSeconds } = RP.config.timer;
  let left = totalSeconds, handle = null;

  function render(){
    document.querySelectorAll('.hud-timer').forEach(el => {
      el.textContent = RP.util.fmtT(left);
      el.style.color = left <= warnAtSeconds ? 'var(--warn)' : '';
    });
  }
  function toggle(){
    if (handle) { clearInterval(handle); handle = null; return; }
    handle = setInterval(() => { left--; render(); }, 1000);
  }
  function reset(){ clearInterval(handle); handle = null; left = totalSeconds; render(); }

  RP.timer = { toggle, reset, render };
}(window.RP = window.RP || {}));
