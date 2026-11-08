// ═══════════════════════════════════════════
// NOTES — barra de notas do apresentador (N), lida do <aside class="notes"> de cada slide
// ═══════════════════════════════════════════
// contrato: RP.notes = { toggle(), sync(), bind() }
// depende de: RP.core, RP.util
(function (RP) {
  'use strict';

  const bar = document.getElementById('notesbar');

  function sync(){
    const s = RP.core.slides[RP.core.idx], a = s.querySelector('aside.notes');
    document.getElementById('notesHead').textContent =
      'notas · slide ' + RP.util.pad(RP.core.idx) + ' · alvo ' + (s.dataset.t || '—');
    document.getElementById('notesText').textContent = a ? a.textContent : '—';
  }
  const toggle = () => bar.classList.toggle('active');
  const bind = () => bar.addEventListener('click', e => e.stopPropagation());

  RP.notes = { toggle, sync, bind };
}(window.RP = window.RP || {}));
