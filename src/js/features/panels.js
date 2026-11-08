// ═══════════════════════════════════════════
// PANELS — fontes (S) e glossário (G), para o Q&A
// ═══════════════════════════════════════════
// contrato: RP.panels = { toggle(id), close(), isOpen(), bind() }
// o conteúdo dos painéis está em src/partials/
// depende de: (nada)
(function (RP) {
  'use strict';

  const IDS = ['refpanel', 'glosspanel'];
  const el = id => document.getElementById(id);

  function toggle(id){
    const opening = !el(id).classList.contains('active');
    IDS.forEach(p => el(p).classList.toggle('active', p === id && opening));
  }
  const close = () => IDS.forEach(p => el(p).classList.remove('active'));
  const isOpen = () => IDS.some(p => el(p).classList.contains('active'));
  // clique dentro do painel não avança slide
  const bind = () => IDS.forEach(p => el(p).addEventListener('click', e => e.stopPropagation()));

  RP.panels = { toggle, close, isOpen, bind };
}(window.RP = window.RP || {}));
