// ═══════════════════════════════════════════
// UTIL — formatação compartilhada
// ═══════════════════════════════════════════
// contrato: RP.util = { pad(n), fmtT(seconds) }
// depende de: (nada)
(function (RP) {
  'use strict';

  const pad = n => String(n).padStart(2, '0');
  // segundos → "mm:ss" (negativo vira "-mm:ss", quando o timer passa do tempo)
  const fmtT = s => (s < 0 ? '-' : '') + pad(Math.floor(Math.abs(s) / 60)) + ':' + pad(Math.abs(s) % 60);

  RP.util = { pad, fmtT };
}(window.RP = window.RP || {}));
