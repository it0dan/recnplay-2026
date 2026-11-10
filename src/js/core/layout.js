// ═══════════════════════════════════════════
// LAYOUT — palco de tamanho fixo escalado para qualquer tela: TV, projetor, notebook, tablet ou celular
// ═══════════════════════════════════════════
// contrato: RP.layout = { fit(), bind() }
// O palco é sempre o mesmo (RP.config.stage); fit() calcula a escala (--s) e o centro (--cx/--cy)
// dentro da área segura do aparelho (sem notch, cantos arredondados nem barra de gestos).
// depende de: RP.config
(function (RP) {
  'use strict';

  const { width, height } = RP.config.stage;
  const stage = document.getElementById('stage'), probe = document.getElementById('safearea');

  // recorte do aparelho, lido do padding da sonda #safearea (env(safe-area-inset-*)); 0 em telas comuns
  function insets(){
    if (!probe) return { top: 0, right: 0, bottom: 0, left: 0 };
    const cs = getComputedStyle(probe), px = k => parseFloat(cs.getPropertyValue(k)) || 0;
    return { top: px('padding-top'), right: px('padding-right'), bottom: px('padding-bottom'), left: px('padding-left') };
  }

  function fit(){
    const i = insets();
    const w = window.innerWidth - i.left - i.right, h = window.innerHeight - i.top - i.bottom;
    stage.style.setProperty('--s', Math.min(w / width, h / height));
    stage.style.setProperty('--cx', (i.left + w / 2) + 'px');
    stage.style.setProperty('--cy', (i.top + h / 2) + 'px');
  }

  function bind(){
    window.addEventListener('resize', fit);
    window.addEventListener('orientationchange', fit);
    // barra de endereço do celular aparecendo/sumindo muda a altura visível sem disparar resize em todo navegador
    if (window.visualViewport) window.visualViewport.addEventListener('resize', fit);
  }

  RP.layout = { fit, bind };
}(window.RP = window.RP || {}));
