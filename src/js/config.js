// ═══════════════════════════════════════════
// CONFIG — tudo o que muda de um evento para outro, num lugar só
// ═══════════════════════════════════════════
// contrato: RP.config (somente leitura)
// depende de: (nada) — carregado antes de todos os módulos
(function (RP) {
  'use strict';

  RP.config = Object.freeze({
    // cabeçalho de todos os slides (js/ui/hud.js)
    event: ['RECNPLAY://LIVE', '12/11/2026 · 11:05', 'TDC STAGE · CESAR Moinho · Sala Rizoflora · Recife'],
    // palco: o mesmo tamanho de .stage em src/css/foundation/stage.css
    stage: Object.freeze({ width: 1600, height: 900 }),
    // timer regressivo da HUD (T inicia/pausa · R zera); fica laranja nos últimos minutos
    timer: Object.freeze({ totalSeconds: 40 * 60, warnAtSeconds: 5 * 60 }),
    // tema inicial e chave em que a escolha do apresentador fica guardada
    theme: Object.freeze({ initial: 'dark', storageKey: 'recnplay-theme-mode' }),
    // tecla segurada: intervalo entre um slide e o próximo · toque: faixa esquerda da tela que volta (fração da
    // largura) e deslocamento mínimo, em px, para um deslize contar
    input: Object.freeze({ holdStepMs: 140, backZone: 0.28, swipeMinPx: 56 }),
    // leitura vertical (celular/tablet em pé): largura da coluna, em px; é ampliada para a largura da tela
    reader: Object.freeze({ width: 540 }),
    // textura de pontos do fundo
    dotgrid: Object.freeze({ gap: 42, radius: 1.1 }),
  });
}(window.RP = window.RP || {}));
