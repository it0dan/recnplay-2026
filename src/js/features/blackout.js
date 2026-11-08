// ═══════════════════════════════════════════
// BLACKOUT — tela de pausa com cronômetro (B ou ".", o botão "tela preta" do passador)
// ═══════════════════════════════════════════
// contrato: RP.blackout = { toggle(), isOpen() }
// depende de: RP.util
(function (RP) {
  'use strict';

  const el = document.getElementById('blackout'), clock = document.getElementById('breakClock');
  let secs = 0, handle = null;

  function toggle(){
    const on = el.classList.toggle('active');
    clearInterval(handle);
    if (!on) return;
    secs = 0; clock.textContent = RP.util.fmtT(0);
    handle = setInterval(() => { clock.textContent = RP.util.fmtT(++secs); }, 1000);
  }
  const isOpen = () => el.classList.contains('active');

  RP.blackout = { toggle, isOpen };
}(window.RP = window.RP || {}));
