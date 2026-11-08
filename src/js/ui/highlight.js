// ═══════════════════════════════════════════
// HIGHLIGHT — realce de sintaxe (TS · JSON · YAML), sem dependências e sem DOM
// ═══════════════════════════════════════════
// contrato: RP.highlight = { html(src, lang), escape(s) }
//   devolve HTML com <span class="tk-*"> (k palavra-chave · s string · c comentário ·
//   t tipo · n número · f função · p propriedade); as cores estão em components/codebox.css
// depende de: (nada)
(function (RP) {
  'use strict';

  const KW = 'import|from|export|const|let|var|async|await|return|new|class|implements|interface|type|private|public|readonly|for|of|if|else|throw|try|catch|function|extends|this|true|false|null|undefined|constructor|in';
  const TS = new RegExp(
    '(\\/\\/[^\\n]*)' +                                                                   // 1 comentário
    '|("(?:\\\\.|[^"\\\\])*"|\'(?:\\\\.|[^\'\\\\])*\'|`(?:\\\\.|[^`\\\\])*`)' +            // 2 string
    '|\\b(\\d[\\d_]*(?:\\.\\d+)?)\\b' +                                                    // 3 número
    '|\\b(' + KW + ')\\b' +                                                                // 4 palavra-chave
    '|\\b([A-Z][A-Za-z0-9_]*)\\b' +                                                        // 5 tipo
    '|\\b([a-z_][A-Za-z0-9_]*)(?=\\s*[(<])', 'g');                                         // 6 função
  const JSON_RE = /("(?:\\.|[^"\\])*")(\s*:)?|\b(-?\d+(?:\.\d+)?)\b|\b(true|false|null)\b/g;

  const escape = s => s.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');
  const span = (cls, s) => '<span class="tk-' + cls + '">' + s + '</span>';

  function yaml(src){
    return src.split('\n').map(l => {
      if (/^\s*#/.test(l)) return span('c', escape(l));
      const m = l.match(/^(\s*-?\s*)([A-Za-z0-9_.\/-]+)(:)(.*)$/);
      if (!m) return escape(l);
      let rest = m[4], c = '';
      const h = rest.indexOf(' #'); if (h >= 0){ c = rest.slice(h); rest = rest.slice(0, h); }
      rest = escape(rest).replace(/(\b\d[\d_.]*\b)/g, span('n', '$1')).replace(/\b(true|false)\b/g, span('k', '$1'));
      return escape(m[1]) + span('p', escape(m[2])) + m[3] + rest + (c ? span('c', escape(c)) : '');
    }).join('\n');
  }

  function tokens(src, re, render){
    re.lastIndex = 0;
    let out = '', last = 0, m;
    while ((m = re.exec(src))){
      out += escape(src.slice(last, m.index)) + render(m);
      last = re.lastIndex;
    }
    return out + escape(src.slice(last));
  }

  const json = src => tokens(src, JSON_RE, m =>
    m[1] ? (m[2] ? span('p', escape(m[1])) + escape(m[2]) : span('s', escape(m[1])))
         : m[3] ? span('n', m[3]) : span('k', m[4]));

  const ts = src => tokens(src, TS, m =>
    span(m[1] ? 'c' : m[2] ? 's' : m[3] ? 'n' : m[4] ? 'k' : m[5] ? 't' : 'f', escape(m[0])));

  function html(src, lang){
    return lang === 'yaml' ? yaml(src) : lang === 'json' ? json(src) : ts(src);
  }

  RP.highlight = { html, escape };
}(window.RP = window.RP || {}));
