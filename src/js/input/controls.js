// ═══════════════════════════════════════════
// CONTROLS — teclado, passador de slides e clique
// ═══════════════════════════════════════════
// contrato: RP.input = { bind(), fullscreen(), muteClick(ms) }
// Passadores (Logitech, Kensington, genéricos USB) emulam teclado:
//   avançar → ArrowRight/PageDown · voltar → ArrowLeft/PageUp
//   "apresentar" → F5 / Shift+F5 / Esc · "tela preta" → . ou B
// Segurar avançar/voltar percorre o deck slide a slide até o fim/início.
// Com pausa ou painel aberto, a navegação fica bloqueada.
// Toque (celular/tablet): tocar avança; tocar na faixa esquerda da tela volta. Com mouse, clicar sempre avança.
// Deslizar e o menu de toque ficam em js/input/touch.js.
// depende de: RP.config, RP.core, RP.timer, RP.blackout, RP.panels, RP.notes, RP.theme
(function (RP) {
  'use strict';

  const NEXT = new Set(['ArrowRight', 'ArrowDown', 'PageDown', ' ', 'Enter', 'MediaTrackNext']);
  const PREV = new Set(['ArrowLeft', 'ArrowUp', 'PageUp', 'Backspace', 'MediaTrackPrevious']);
  const NAV = k => NEXT.has(k) || PREV.has(k) || k === 'Home' || k === 'End';

  const blocked = () => RP.blackout.isOpen() || RP.panels.isOpen();

  function fullscreen(){
    try {
      if (document.fullscreenElement) return document.exitFullscreen();
      const p = document.documentElement.requestFullscreen();
      // em celular e tablet, tela cheia já entra deitada (onde o navegador permite travar a orientação)
      if (p && p.then) p.then(() => screen.orientation && screen.orientation.lock && screen.orientation.lock('landscape').catch(() => {})).catch(() => {});
    } catch (e) {}
  }

  // tecla (minúscula) → ação; atalhos de uma letra
  const KEYS = {
    t: () => RP.timer.toggle(),            r: () => RP.timer.reset(),
    s: () => RP.panels.toggle('refpanel'), g: () => RP.panels.toggle('glosspanel'),
    n: () => RP.notes.toggle(),            d: () => RP.theme.toggle(),
    f: fullscreen,
  };

  // tecla segurada (auto-repeat do teclado ou do passador): pula slide inteiro,
  // sem passar pelos fragmentos, num ritmo legível até o início ou o fim do deck
  let lastHeld = 0;
  function held(dir){
    const now = performance.now();
    if (now - lastHeld < RP.config.input.holdStepMs) return;
    lastHeld = now;
    const target = RP.core.idx + dir;
    if (target < 0 || target >= RP.core.slides.length) return;
    RP.core.show(target, dir < 0);                                   // voltando: slide já revelado
  }

  function onKey(e){
    if (e.ctrlKey || e.metaKey || e.altKey) return;                  // atalhos do navegador ficam com ele
    const k = e.key, letter = k.length === 1 ? k.toLowerCase() : '';

    if (k === 'F5'){ e.preventDefault(); if (!document.fullscreenElement) fullscreen(); return; } // nunca recarrega
    if (k === '.' || letter === 'b'){ e.preventDefault(); RP.blackout.toggle(); return; }
    if (k === 'Escape'){ RP.panels.close(); if (RP.blackout.isOpen()) RP.blackout.toggle(); return; }

    if (blocked()){
      if (NAV(k)) e.preventDefault();
      if (letter === 's' || letter === 'g') KEYS[letter]();             // alternar entre painéis
      return;
    }
    if (NEXT.has(k)){ e.preventDefault(); e.repeat ? held(+1) : RP.core.next(); }
    else if (PREV.has(k)){ e.preventDefault(); e.repeat ? held(-1) : RP.core.prev(); }
    else if (k === 'Home'){ e.preventDefault(); RP.core.show(0, true); }
    else if (k === 'End'){ e.preventDefault(); RP.core.show(RP.core.slides.length - 1, true); }
    else if (KEYS[letter]) KEYS[letter]();
  }

  // último tipo de ponteiro (mouse, touch ou pen) e janela em que o clique é ignorado (logo após um deslize)
  let pointer = 'mouse', mutedUntil = 0;
  const muteClick = ms => { mutedUntil = performance.now() + ms; };

  function onClick(e){
    if (e.button !== 0 || blocked() || e.target.closest('a')) return;
    if (performance.now() < mutedUntil) return;
    const sel = window.getSelection(); if (sel && String(sel).length) return;
    const back = pointer === 'touch' && e.clientX < window.innerWidth * RP.config.input.backZone;
    back ? RP.core.prev() : RP.core.next();
  }

  function bind(){
    window.addEventListener('keydown', onKey, true);                  // captura: vale com foco em link/painel
    document.addEventListener('click', onClick);
    window.addEventListener('pointerdown', e => { pointer = e.pointerType || 'mouse'; }, true);
    // foco nunca fica preso num link (Espaço/Enter do passador acionariam o link)
    document.addEventListener('mouseup', () => {
      const a = document.activeElement; if (a && a !== document.body && a.blur) a.blur();
    });
  }

  RP.input = { bind, fullscreen, muteClick };
}(window.RP = window.RP || {}));
