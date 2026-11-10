// ═══════════════════════════════════════════
// BOOT — checagem de módulos, ligações tardias e inicialização (carregado por último)
// ═══════════════════════════════════════════
(function (RP) {
  'use strict';

  const REQUIRED = ['config', 'util', 'core', 'router', 'layout', 'highlight', 'code', 'hud', 'dotgrid',
                    'theme', 'timer', 'blackout', 'panels', 'notes', 'input', 'touch'];
  const missing = REQUIRED.filter(k => !RP[k]);
  if (missing.length){
    console.error('[RP boot] módulos ausentes:', missing.join(', '), '— deck não inicializado.');
    return;
  }

  // o core avisa os demais módulos a cada troca de slide
  RP.core.bind.routerSync = RP.router.sync;
  RP.core.bind.hudSync    = RP.hud.sync;
  RP.core.bind.notesSync  = RP.notes.sync;

  // conteúdo gerado antes do primeiro show
  RP.code.render();
  RP.hud.mount();

  // listeners
  RP.layout.bind(); RP.dotgrid.bind(); RP.router.bind();
  RP.panels.bind(); RP.notes.bind();   RP.input.bind();  RP.touch.bind();

  // init
  RP.theme.init();
  RP.layout.fit();
  RP.timer.render();
  RP.core.slides.forEach(s => s.classList.remove('active'));
  RP.core.show(RP.router.read(), true);
}(window.RP = window.RP || {}));
