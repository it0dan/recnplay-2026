// ═══════════════════════════════════════════
// DECK — estado da apresentação: slide atual, fragmentos e navegação
// ═══════════════════════════════════════════
// contrato:
//   RP.core = { slides, idx (getter), show(n, allFrags), next(), prev(), setStep(slide, n), setFlat(on),
//               bind: { routerSync, hudSync, notesSync, readerSync } }
// modo plano (setFlat, usado pela leitura vertical): sem passos; todo slide fica com os fragmentos revelados
//   e data-step="0", que é o estado em que nada está esmaecido.
// fragmentos: elementos .frag com data-f="N" aparecem no N-ésimo avanço;
//   o passo atual fica em data-step e --step no <section>, para CSS condicional.
// depende de: (nada) — bind.* é preenchido pelo js/boot.js
(function (RP) {
  'use strict';

  const slides = Array.from(document.querySelectorAll('.slide'));
  let idx = 0;
  const bind = { routerSync: null, hudSync: null, notesSync: null, readerSync: null };
  let flat = false;

  const frags = s => Array.from(s.querySelectorAll('.frag'));
  const maxStep = s => frags(s).reduce((m, f) => Math.max(m, +f.dataset.f || 0), 0);

  function setStep(s, n){
    if (flat){
      s.dataset.step = 0; s.style.setProperty('--step', maxStep(s));
      return frags(s).forEach(f => f.classList.add('on'));
    }
    n = Math.max(0, Math.min(maxStep(s), n));
    s.dataset.step = n; s.style.setProperty('--step', n);
    frags(s).forEach(f => f.classList.toggle('on', (+f.dataset.f || 0) <= n));
  }

  // reinicia as animações SMIL (<animate>, <animateMotion>) do slide que acabou de entrar
  function restartSvg(s){
    requestAnimationFrame(() => s.querySelectorAll('svg').forEach(v => {
      try { if (v.setCurrentTime && !v.parentNode.closest('svg')) v.setCurrentTime(0); } catch (e) {}
    }));
  }

  function sync(){ ['routerSync', 'hudSync', 'notesSync', 'readerSync'].forEach(k => bind[k] && bind[k]()); }

  // allFrags: entra com todos os fragmentos revelados (ao voltar ou ao abrir por #N)
  function show(n, allFrags){
    slides[idx].classList.remove('active');
    idx = Math.max(0, Math.min(slides.length - 1, n));
    const s = slides[idx];
    setStep(s, allFrags ? Infinity : 0);
    s.classList.add('active');
    restartSvg(s); sync();
  }

  function next(){
    const s = slides[idx], cur = +(s.dataset.step || 0);
    if (!flat && cur < maxStep(s)) return setStep(s, cur + 1);
    show(idx + 1, false);
  }

  function prev(){
    const s = slides[idx], cur = +(s.dataset.step || 0);
    if (!flat && cur > 0) return setStep(s, cur - 1);
    show(idx - 1, true);
  }

  function setFlat(on){
    flat = !!on;
    slides.forEach((s, i) => setStep(s, i === idx ? Infinity : 0));
  }

  RP.core = { slides, get idx(){ return idx; }, show, next, prev, setStep, setFlat, bind };
}(window.RP = window.RP || {}));
