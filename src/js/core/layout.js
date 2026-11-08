// ═══════════════════════════════════════════
// LAYOUT — palco de tamanho fixo escalado para qualquer tela ou projetor
// ═══════════════════════════════════════════
// contrato: RP.layout = { fit(), bind() }
// depende de: RP.config
(function (RP) {
  'use strict';

  const { width, height } = RP.config.stage;

  function fit(){
    const s = Math.min(window.innerWidth / width, window.innerHeight / height);
    document.getElementById('stage').style.setProperty('--s', s);
  }
  function bind(){ window.addEventListener('resize', fit); }

  RP.layout = { fit, bind };
}(window.RP = window.RP || {}));
