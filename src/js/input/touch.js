// ═══════════════════════════════════════════
// TOUCH — celular e tablet: deslizar para navegar e menu com o que no notebook é atalho de teclado
// ═══════════════════════════════════════════
// contrato: RP.touch = { bind(), sync() }
// - põe a classe .touch no <html> em aparelhos de toque (ou com ?touch=1 na URL, para testar no notebook);
//   é ela que mostra os controles de src/partials/touch-controls.html. Sem ela, nada muda.
// - deslizar para a esquerda avança, para a direita volta (o toque simples fica em controls.js).
// - botão flutuante: abre o menu; com painel ou pausa abertos, vira ✕ e fecha.
// depende de: RP.config, RP.core, RP.input, RP.timer, RP.blackout, RP.panels, RP.notes, RP.theme
(function (RP) {
  'use strict';

  const root = document.documentElement;
  const ui = document.getElementById('touchui'), fab = document.getElementById('tfab'), menu = document.getElementById('tmenu');
  const coarse = window.matchMedia('(hover: none) and (pointer: coarse)');
  const forced = /[?&]touch=1\b/.test(location.search);

  const overlayOpen = () => RP.panels.isOpen() || RP.blackout.isOpen();
  const closeOverlays = () => { RP.panels.close(); if (RP.blackout.isOpen()) RP.blackout.toggle(); };

  // ação do menu → a mesma função que o atalho de teclado chama
  const ACTIONS = {
    prev:  () => RP.core.prev(),                 next:  () => RP.core.next(),
    first: () => RP.core.show(0, true),          last:  () => RP.core.show(RP.core.slides.length - 1, true),
    notes: () => RP.notes.toggle(),              theme: () => RP.theme.toggle(),
    refs:  () => RP.panels.toggle('refpanel'),   gloss: () => RP.panels.toggle('glosspanel'),
    timer: () => RP.timer.toggle(),              reset: () => RP.timer.reset(),
    pause: () => RP.blackout.toggle(),           full:  () => RP.input.fullscreen(),
  };
  const NAV = new Set(['prev', 'next', 'first', 'last']);
  const STAY_OPEN = new Set(['prev', 'next', 'timer', 'reset', 'theme']);   // ações que se repetem ou cujo efeito se vê com o menu aberto

  let menuOpen = false, idle = null;

  function sync(){
    const over = overlayOpen();
    ui.classList.toggle('open', menuOpen);
    ui.classList.toggle('overlay', over);
    fab.textContent = menuOpen || over ? '✕' : '⋯';
    fab.setAttribute('aria-expanded', String(menuOpen));
    fab.setAttribute('aria-label', menuOpen ? 'Fechar controles' : over ? 'Fechar' : 'Abrir controles');
  }
  function setMenu(open){ menuOpen = open; sync(); }

  // o botão fica discreto e acorda a cada toque na tela
  function wake(){
    ui.classList.add('awake'); clearTimeout(idle);
    idle = setTimeout(() => ui.classList.remove('awake'), 3000);
  }

  function onFab(e){
    e.stopPropagation();
    if (menuOpen) return setMenu(false);
    if (overlayOpen()) { closeOverlays(); return sync(); }
    setMenu(true);
  }

  function onMenu(e){
    e.stopPropagation();
    const b = e.target.closest('button[data-act]'); if (!b) return;
    const act = b.dataset.act;
    if (NAV.has(act) && overlayOpen()) return;               // mesma regra do teclado: painel aberto bloqueia a navegação
    ACTIONS[act]();
    setMenu(STAY_OPEN.has(act));
  }

  // deslize horizontal de um dedo, curto e sem zoom ativo
  let start = null;
  const inChrome = el => !!(el.closest && el.closest('#touchui, .bkp, #notesbar, a'));
  function onStart(e){
    wake();
    start = e.touches.length === 1 && !inChrome(e.target)
      ? { x: e.touches[0].clientX, y: e.touches[0].clientY, t: performance.now() } : null;
  }
  function onEnd(e){
    if (!start || e.touches.length) { start = null; return; }
    const t = e.changedTouches[0], dx = t.clientX - start.x, dy = t.clientY - start.y, dt = performance.now() - start.t;
    start = null;
    const zoomed = window.visualViewport && window.visualViewport.scale > 1.05;
    if (zoomed || overlayOpen() || dt > 700 || RP.reader.isOn()) return;
    if (Math.abs(dx) < RP.config.input.swipeMinPx || Math.abs(dx) < Math.abs(dy) * 1.5) return;
    RP.input.muteClick(450);                                  // o deslize não pode contar também como toque
    if (menuOpen) setMenu(false);
    dx < 0 ? RP.core.next() : RP.core.prev();
  }

  function mode(){ root.classList.toggle('touch', forced || coarse.matches); }

  function bind(){
    mode();
    if (coarse.addEventListener) coarse.addEventListener('change', mode);
    if (!document.fullscreenEnabled) menu.querySelector('[data-act="full"]').hidden = true;   // iPhone: sem API de tela cheia

    fab.addEventListener('click', onFab);
    menu.addEventListener('click', onMenu);
    document.addEventListener('touchstart', onStart, { passive: true });
    document.addEventListener('touchend', onEnd, { passive: true });
    // tocar fora do menu só o fecha: esse toque não avança o slide
    document.addEventListener('click', e => {
      if (menuOpen && !ui.contains(e.target)) { e.stopPropagation(); setMenu(false); }
    }, true);
    // na pausa não há teclado para sair: tocar na tela volta
    document.getElementById('blackout').addEventListener('click', e => {
      if (root.classList.contains('touch')) { e.stopPropagation(); RP.blackout.toggle(); }
    });
    // painéis e pausa também abrem pelo teclado: o botão acompanha o estado deles
    const watch = new MutationObserver(sync);
    ['refpanel', 'glosspanel', 'blackout'].forEach(id =>
      watch.observe(document.getElementById(id), { attributes: true, attributeFilter: ['class'] }));
    sync();
  }

  RP.touch = { bind, sync };
}(window.RP = window.RP || {}));
