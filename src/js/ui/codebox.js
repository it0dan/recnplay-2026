// ═══════════════════════════════════════════
// CODEBOX — transforma <script type="text/plain" class="code"> em caixa de código
// ═══════════════════════════════════════════
// contrato: RP.code = { render() }
// uso no HTML do slide:
//   <script type="text/plain" class="code" data-lang="ts|json|yaml" data-file="nome"
//           data-size="sm|xs|xxs|md" data-hl="2,5-7" data-hlg="1:3-5;2:8"> código </script>
//   data-hl  → linhas sempre destacadas
//   data-hlg → grupos destacados conforme o fragmento atual (grupo N acende no passo N)
// depende de: RP.highlight
(function (RP) {
  'use strict';

  const LANG_LABEL = { ts: 'TypeScript', json: 'JSON', yaml: 'YAML' };

  // "2,5-7" → Set {2, 5, 6, 7}
  function lines(spec){
    const set = new Set(); if (!spec) return set;
    spec.split(',').forEach(p => { const [a, b] = p.split('-').map(Number); for (let i = a; i <= (b || a); i++) set.add(i); });
    return set;
  }

  // "1:3-5;2:8" → { 3: ['g1'], 4: ['g1'], 5: ['g1'], 8: ['g2'] }
  function groups(spec){
    const grp = {};
    (spec || '').split(';').filter(Boolean).forEach(g => {
      const [k, v] = g.split(':');
      lines(v).forEach(n => (grp[n] = grp[n] || []).push('g' + k));
    });
    return grp;
  }

  function box(s){
    const lang = s.dataset.lang || 'ts';
    const raw = s.textContent.replace(/^\n/, '').replace(/\s+$/, '');
    const hl = lines(s.dataset.hl), grp = groups(s.dataset.hlg);

    const el = document.createElement('div'); el.className = 'codebox';
    if (s.dataset.hlg) el.classList.add('hlg');
    el.innerHTML = '<div class="cbh"><i></i><i></i><i></i><span>' + RP.highlight.escape(s.dataset.file || '') +
                   '</span><span class="lang">' + (LANG_LABEL[lang] || LANG_LABEL.ts) + '</span></div>';

    const pre = document.createElement('pre'); if (s.dataset.size) pre.className = s.dataset.size;
    pre.innerHTML = RP.highlight.html(raw, lang).split('\n').map((l, i) =>
      '<span class="ln' + (hl.has(i + 1) ? ' on' : '') + (grp[i + 1] ? ' ' + grp[i + 1].join(' ') : '') + '">' + (l || ' ') + '</span>'
    ).join('');
    el.appendChild(pre);
    return el;
  }

  function render(){ document.querySelectorAll('script.code').forEach(s => s.replaceWith(box(s))); }

  RP.code = { render };
}(window.RP = window.RP || {}));
