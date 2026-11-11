// ═══════════════════════════════════════════
// READER — leitura vertical: no celular ou tablet em pé, os slides viram uma página que se rola para cima
// ═══════════════════════════════════════════
// contrato: RP.reader = { isOn(), apply(), sync(), bind() }
// Liga quando o aparelho é de toque e está em pé (ou com ?read=1 na URL, para testar no notebook); deitado,
// volta ao palco 16:9 de sempre. Ligado, põe a classe .read no <html> (o CSS de src/css/reader/ e os blocos
// ".read &" de cada slide.css reorganizam o slide em uma coluna), tira os passos (RP.core.setFlat) e passa a
// trocar o slide atual conforme a rolagem. No notebook e na TV este módulo não faz nada.
// depende de: RP.config, RP.core
(function (RP) {
  'use strict';

  const root = document.documentElement, stage = document.getElementById('stage');
  const portrait = window.matchMedia('(orientation: portrait)');
  const coarse = window.matchMedia('(hover: none) and (pointer: coarse)');
  const forced = /[?&]read=1\b/.test(location.search);
  const { width } = RP.config.reader;

  let on = false, fromScroll = false, ticking = false, first = true;
  const isOn = () => on;

  // a coluna de leitura tem largura fixa (RP.config.reader.width) e é ampliada para a largura da tela
  function fit(){
    const z = window.innerWidth / width;
    stage.style.setProperty('--z', z);
    stage.style.setProperty('--rh', (window.innerHeight / z) + 'px');   // altura de uma tela, na escala da coluna
  }

  // slide que está cruzando a linha a 40% da altura da tela
  function current(){
    const y = window.innerHeight * 0.4, s = RP.core.slides;
    for (let i = 0; i < s.length; i++){ const r = s[i].getBoundingClientRect(); if (r.top <= y && r.bottom > y) return i; }
    return RP.core.idx;
  }

  function onScroll(){
    if (!on || ticking) return;
    ticking = true;
    requestAnimationFrame(() => {
      ticking = false;
      const n = current();
      if (on && n !== RP.core.idx){ fromScroll = true; RP.core.show(n, true); fromScroll = false; }
    });
  }

  // chamado pelo core a cada troca de slide: se a troca não veio da rolagem (menu, teclado, #N), rola até ele
  function sync(){
    if (!on || fromScroll) return;
    const s = RP.core.slides[RP.core.idx];
    window.scrollTo({ top: s.getBoundingClientRect().top + window.scrollY, behavior: first ? 'auto' : 'smooth' });
    first = false;
  }

  function apply(){
    const want = forced || (coarse.matches && portrait.matches);
    if (want === on) { if (on) fit(); return; }
    on = want;
    if (on) fit();                          // antes da classe: a coluna já nasce na escala da tela
    root.classList.toggle('read', on);
    RP.core.setFlat(on);
    if (on){ first = true; sync(); }
    else { window.scrollTo(0, 0); RP.core.show(RP.core.idx, true); }
  }

  function bind(){
    [portrait, coarse].forEach(m => m.addEventListener && m.addEventListener('change', apply));
    window.addEventListener('resize', () => { if (on) fit(); });
    window.addEventListener('scroll', onScroll, { passive: true });
    apply();
  }

  RP.reader = { isOn, apply, sync, bind };
}(window.RP = window.RP || {}));
