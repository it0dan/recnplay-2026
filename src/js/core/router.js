// ═══════════════════════════════════════════
// ROUTER — posição via hash (#N sobrevive a recarga e serve de link direto)
// ═══════════════════════════════════════════
// contrato: RP.router = { read(), sync(), bind() }
// depende de: RP.core
(function (RP) {
  'use strict';

  function read(){
    const m = location.hash.match(/^#(\d{1,2})$/), n = m ? parseInt(m[1], 10) : 0;
    return n >= 0 && n < RP.core.slides.length ? n : 0;
  }
  function sync(){ try { history.replaceState(null, '', '#' + RP.core.idx); } catch (e) {} }
  function bind(){
    window.addEventListener('hashchange', () => { const n = read(); if (n !== RP.core.idx) RP.core.show(n, true); });
  }

  RP.router = { read, sync, bind };
}(window.RP = window.RP || {}));
