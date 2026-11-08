// ═══════════════════════════════════════════
// THEME — tema escuro (padrão) / claro (tecla D), lembrado por navegador
// ═══════════════════════════════════════════
// contrato: RP.theme = { init(), toggle() }
// depende de: RP.config, RP.dotgrid
(function (RP) {
  'use strict';

  const { initial, storageKey } = RP.config.theme, root = document.documentElement;

  function apply(t){
    if (t === 'dark') root.setAttribute('data-theme', 'dark'); else root.removeAttribute('data-theme');
    RP.dotgrid.draw();
  }
  function toggle(){
    const t = root.getAttribute('data-theme') === 'dark' ? 'light' : 'dark';
    try { localStorage.setItem(storageKey, t); } catch (e) {}
    apply(t);
  }
  function init(){
    let saved = null; try { saved = localStorage.getItem(storageKey); } catch (e) {}
    apply(saved || initial);
  }

  RP.theme = { init, toggle };
}(window.RP = window.RP || {}));
