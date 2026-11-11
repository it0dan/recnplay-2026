# Do monolito aos sistemas multiagentes — Rec'n'Play 2026

> **Padrões arquiteturais para aplicações agênticas: o que muda, o que permanece e onde a borda governa.**

Repositório de apoio da palestra no **TDC Stage do REC'n'Play 2026** (12/11/2026 · 11:05 · CESAR Moinho, Sala Rizoflora · Recife). Aqui estão o deck completo, o roteiro de palco e a bibliografia verificada. Para apresentar basta um navegador: o `presentation.html` já vem montado, com fontes e imagens locais.

## O que você encontra aqui

| Quer… | Vá direto |
| :-- | :-- |
| **Ver a apresentação** | Abra [`presentation.html`](./presentation.html) em qualquer navegador moderno |
| **Entender a tese e o roteiro** | Seções abaixo |
| **Usar o roteiro de palco** (tempos, cliques, falas, resgates) | [`docs/CUE-SHEET.md`](./docs/CUE-SHEET.md) |
| **Checar as fontes** | [`docs/REFERENCIAS.md`](./docs/REFERENCIAS.md) |
| **Editar ou adaptar o deck** | Seções *Estrutura do repositório* e *Reutilizar este deck* |

---

## Visão geral

A arquitetura de software evoluiu dividindo o sistema: monolito modular, microsserviços, eventos. Desde 30/11/2022, a linha do tempo mudou de eixo e passou a ser sobre **quem executa o trabalho**: primeiro no ciclo de desenvolvimento (AI-SDLC), depois dentro do próprio produto, com aplicações agênticas e sistemas multiagentes.

Todos os exemplos usam um único domínio, do primeiro ao último slide: **análise de crédito agêntica**.

**Tese central:** *o núcleo é probabilístico; a casca que decide quando ele para é determinística.* Não dá para tornar o modelo idempotente, mas dá para construir uma casca que seja. A autonomia que funciona em produção é autonomia com limites desenhados. Os padrões de sempre (hexagonal, database-per-service, saga, idempotência) continuam valendo. Os padrões não mudam, mudam de lugar: no contrato da resposta, no contexto de cada agente e na borda que governa o tráfego de IA.

## Palestrante

| Palestrante | Função e bio | Especialidade |
| :-- | :-- | :-- |
| **Dan (Danilo Amaral)** | **Arquiteto de Soluções @ Sensedia**. Especialista em integrações e estratégia de IA, ajuda clientes a habilitar ecossistemas digitais com práticas modernas de integração. Integra o comitê técnico do TDC. | `Agentic Architecture` `Harness Engineering` |

## Roteiro

| Bloco | Slides | Conteúdo |
| :-- | :-- | :-- |
| **Abertura** | 00 – 01 | Capa e linha do tempo: dos sistemas monolíticos aos sistemas agênticos |
| **01 · Formas modernas** | 02 – 04 | Microsserviços e EDA · monolito modular (com cases da indústria) · 30.11.2022 |
| **02 · Desenvolvendo com GenAI** | 05 | Do assistente à esteira agêntica (spec, gates humanos, evals, contexto versionado) |
| **03 · Multiagentes** | 06 – 08 | Contexto por agente · harness · loop |
| **04 · A tese** | 09 – 10 | Clean Architecture para LLM: o modelo é um detalhe (desenho + código) · então → agora (os padrões mudam de lugar) |
| **05 · NFRs e AI Gateway** | 11 | AI Gateway: gestão, governança e NFR (sem × com AI Gateway) |
| **Encerramento** | 12 – 13 | O desafio não é o modelo, é a arquitetura em volta dele · obrigado + QR code |


Os tempos-alvo, os cliques de cada slide e as falas completas estão no [cue sheet](./docs/CUE-SHEET.md).

---

## Atalhos

| Tecla | Ação |
| :--: | :-- |
| `Clique` · `→` `↓` `PgDn` `Espaço` `Enter` | Avança (slide ou próximo passo do slide); segurar a tecla percorre até o fim |
| `←` `↑` `PgUp` `Backspace` | Volta; segurar a tecla percorre até o início |
| `Home` / `End` | Primeiro / último slide |
| `F` ou `F5` | Tela cheia (o `F5` nunca recarrega a página) |
| `B` ou `.` | Tela de pausa com cronômetro |
| `S` / `G` | Fontes e referências / glossário (painéis para o Q&A) |
| `N` | Notas do apresentador |
| `T` / `R` | Inicia ou pausa / zera o timer de 40 min |
| `D` | Tema escuro / claro |
| `Esc` | Fecha painéis e pausa |

**Passadores de slide** (Logitech, Kensington, genéricos USB) funcionam sem configuração, porque emulam `PgDn`/`PgUp` (ou setas), `F5`/`Esc` e `.`. Para abrir direto num slide, acrescente `#N` à URL (ex.: `presentation.html#7`); o slide abre com todos os passos revelados.

### Celular e tablet

**Deitado**, o deck é o mesmo do palco: o 16:9 é escalado para caber inteiro na área útil do aparelho (fora de notch e barra de gestos). O que no notebook é atalho de teclado, no toque vira gesto ou botão:

| Gesto | Ação |
| :-- | :-- |
| Tocar na tela | Avança (slide ou próximo passo) |
| Tocar na faixa esquerda da tela | Volta |
| Deslizar para a esquerda / direita | Avança / volta |
| Botão `⋯` (canto inferior direito) | Menu com voltar, avançar, início, fim, notas, fontes, glossário, tema, timer, pausa e tela cheia |
| Botão `✕` | Fecha o menu, o painel ou a pausa |

**Em pé**, entra a **leitura vertical**: os slides viram uma página que se rola para cima, cada um reorganizado em uma coluna, com todos os passos já revelados. Grades viram listas, e os desenhos largos (monolito modular, hexagonal e sistema com AI Gateway) têm uma versão própria em pé. O menu `⋯` continua lá: notas, fontes e glossário valem para o slide que está na tela, e avançar/voltar rolam até o slide seguinte. Ao deitar o aparelho, o palco volta no mesmo slide.

"Tela cheia" já entra deitada onde o navegador permite; no iPhone, que não tem tela cheia para páginas, use *Compartilhar → Adicionar à Tela de Início*. Para ver no notebook: `presentation.html?touch=1` mostra os controles de toque e `presentation.html?read=1` liga a leitura vertical.

**Como a leitura vertical é feita** (para editar um slide): a classe `.read` no `<html>` liga as regras de `src/css/reader/reader.css` e os blocos `.read & …` no fim de cada `slide.css`. Um conteúdo que só existe em pé usa `class="only-read"`; o que some em pé, `class="no-read"`. Nada disso vale sem `.read`, então o palco não muda.

---

## Estrutura do repositório

O código-fonte fica em `src/`, um arquivo por responsabilidade. O `presentation.html` da raiz é **gerado** a partir dele por `tools/build.py` (Python puro, sem dependências) e fica versionado, para o deck abrir com duplo clique e no GitHub Pages sem nenhum passo extra.

```text
.
├── presentation.html            # GERADO por tools/build.py — não edite à mão
├── index.html                   # Redireciona para presentation.html (raiz do GitHub Pages)
├── manifest.webmanifest         # Permite instalar o deck no celular/tablet (tela cheia, deitado)
├── src/
│   ├── deck.json                # Ordem dos slides, seções, título e duração (40 min)
│   ├── shell.html               # Esqueleto da página: <head>, overlays, includes, <script>s
│   ├── partials/                # painéis S/G e controles de toque (celular e tablet)
│   │   ├── panel-fontes.html    #   painel de fontes (tecla S)
│   │   └── panel-glossario.html #   painel de glossário (tecla G)
│   ├── slides/                  # Um diretório por slide: markup + estilos juntos
│   │   └── <nome>/
│   │       ├── slide.html       #   <section id="slide-<nome>" data-t="m:ss"> + notas
│   │       └── slide.css        #   estilos só deste slide, escopados por #slide-<nome>
│   ├── css/
│   │   ├── main.css             # @import na ordem da cascata
│   │   ├── foundation/          #   fontes, tokens (temas), reset, palco, tipografia, reduced-motion
│   │   ├── components/          #   HUD, layout, card, motion, seta, diagrama SVG, codebox, fragmentos, cases
│   │   ├── chrome/              #   notas, tela de pausa, painéis S/G, controles de toque
│   │   └── reader/              #   leitura vertical (celular e tablet em pé)
│   └── js/                      # Módulos RP.* (IIFE no namespace window.RP), na ordem de carga
│       ├── config.js            #   evento, duração do timer, tema, tamanho do palco: o que muda por evento
│       ├── core/                #   util, deck (estado, fragmentos, navegação), router (#N), layout (escala)
│       ├── ui/                  #   highlight (puro), codebox, hud, dotgrid, theme, reader (leitura vertical)
│       ├── features/            #   timer, blackout, panels, notes
│       ├── input/               #   controls (teclado, passador, clique e toque) · touch (deslize e menu de toque)
│       └── boot.js              #   confere os módulos, faz as ligações e inicia
├── assets/
│   ├── fonts/                   # Montserrat e Roboto Mono (variáveis, locais: funciona offline)
│   ├── brand/                   # Logos do evento e dos cases (veja os READMEs das pastas)
│   └── qr.svg                   # QR code do último slide (gerado por tools/make_qr.py)
├── docs/
│   ├── CUE-SHEET.md             # Roteiro de palco (gerado por tools/make_cue_sheet.py)
│   └── REFERENCIAS.md           # Fontes citadas no palco e nas notas
├── tools/                       # Python; só o build é necessário para editar
│   ├── _deck.py                 #   base comum: caminhos, leitura do deck.json, abrir o deck no Chromium
│   ├── build.py                 #   src/ → presentation.html (valida os slides e soma os tempos-alvo)
│   ├── bundle.py                #   → dist/recnplay-2026.html (arquivo único, para backup)
│   ├── export_pdf.py            #   → dist/recnplay-2026.pdf (1 página por slide)
│   ├── check_layout.py          #   aponta texto vazando, sobreposto ou fora da forma, e erros de JS
│   ├── check_responsive.py      #   celular e tablet emulados: deitado (palco, toque, menu) e em pé (leitura vertical)
│   ├── check_links.py           #   testa os links das referências
│   ├── make_cue_sheet.py        #   regera docs/CUE-SHEET.md a partir dos slides (tempos, cliques, notas)
│   └── make_qr.py               #   regera assets/qr.svg para outra URL
├── Makefile                     # Atalhos: make build · check · pdf · bundle · dist · links · serve
└── .github/workflows/ci.yml     # CI: presentation.html em dia com src/ + checagem de layout
```

### Fluxo de edição

1. Edite em `src/` (slide, estilo, módulo ou painel).
2. Rode `python3 tools/build.py` (ou `make build`): ele valida cada slide, avisa se a soma dos tempos-alvo não fecha com a duração e regrava o `presentation.html`.
3. Se mexeu em ordem, tempos ou notas, rode também `python3 tools/make_cue_sheet.py`.
4. Faça commit de `src/` **e** do `presentation.html`. O CI falha se um ficar diferente do outro.

### Manutenção rápida

- **Mudar o conteúdo de um slide**: `src/slides/<nome>/slide.html`. O `id` (`slide-<nome>`) é o mesmo nome da pasta, e o build confere isso.
- **Mudar o visual de um slide**: `src/slides/<nome>/slide.css`. As regras ficam aninhadas em `#slide-<nome>{ … }` e não vazam para outros slides; `&` é o próprio `<section>` (ex.: `&.active`, `&[data-step="2"]`).
- **Reordenar, incluir ou tirar slides**: só o `src/deck.json`. A numeração (HUD, `#N`, comentários) acompanha sozinha.
- **Componente usado por mais de um slide**: `src/css/components/`. Cores e temas: `src/css/foundation/tokens.css`.
- **Mudar comportamento**: cada módulo em `src/js/` declara no cabeçalho o seu contrato (`RP.x = { … }`) e de quem depende. O `boot.js` confere se todos carregaram e, se faltar um, para e loga qual.

### Convenções dos slides

- **Passos dentro do slide (fragmentos)**: `class="frag frag-hide" data-f="2"` aparece no 2º avanço; `frag-ghost` deixa o elemento esmaecido até a vez dele. O passo atual também fica em `data-step` e `--step` no `<section>`, para CSS condicional.
- **Código**: `<script type="text/plain" class="code" data-lang="ts" data-file="…" data-hl="2,5-7">` vira uma caixa com realce de sintaxe. `data-hlg="1:3-5;2:8"` acende grupos de linhas conforme o passo; `data-size` escolhe o tamanho da fonte.
- **Pacotes animados em diagramas**: `<circle class="mpath" style="offset-path:path('…');animation-duration:3s">` (CSS motion path), que começam a andar no instante em que o slide aparece.
- **Notas do apresentador**: `<aside class="notes">` em cada slide (tecla `N`); o tempo-alvo vem do `data-t`.
- **Palco**: fixo em 1600×900 e escalado para a tela; as medidas em `px` no CSS são as do palco.

---

## Como executar

1. Clone ou baixe o repositório (`git clone` ou *Download ZIP*).
2. Abra [`presentation.html`](./presentation.html) com duplo clique. **Para apresentar não precisa de servidor, build, npm nem internet**: o arquivo já vem montado, e fontes e imagens são locais.
3. No palco: `F` para tela cheia e `T` para iniciar o timer.

**Requisitos:** qualquer navegador moderno (testado em Chromium/Chrome). Nada mais.

### Ferramentas

```bash
python3 tools/build.py            # src/ → presentation.html (só biblioteca padrão)

pip install -r requirements.txt   # qrcode, playwright, pillow — para as demais
python3 -m playwright install chromium
python3 tools/bundle.py           # → dist/recnplay-2026.html (arquivo único para pendrive/e-mail)
python3 tools/export_pdf.py       # → dist/recnplay-2026.pdf
python3 tools/check_layout.py     # checagem visual automática de todos os slides
python3 tools/check_responsive.py # celular e tablet emulados: deitado (palco, toque, menu) e em pé (leitura vertical)
python3 tools/check_links.py      # testa os links (precisa de internet)
python3 tools/make_qr.py <url>    # QR para outra URL
python3 tools/make_cue_sheet.py   # regera docs/CUE-SHEET.md (só biblioteca padrão)
```

Com `make`: `make build`, `make check` (o mesmo que o CI), `make cue` (cue sheet), `make dist` (bundle + PDF), `make serve`.

### Publicar no GitHub Pages

**Settings → Pages → Deploy from a branch → `main` / `(root)`.** O `index.html` da raiz redireciona para a apresentação, que é o endereço para onde o QR code do último slide aponta.

---

## Reutilizar este deck

O deck é HTML, CSS e JS puros, sem framework, e foi feito para ser reaproveitado:

1. **Conteúdo**: crie ou troque as pastas em `src/slides/` e a ordem no `src/deck.json`; as notas ficam no `<aside class="notes">` de cada slide.
2. **Identidade visual**: todos os tokens (cores e temas) estão em [`src/css/foundation/tokens.css`](./src/css/foundation/tokens.css), e as fontes em [`fonts.css`](./src/css/foundation/fonts.css). Trocar as variáveis de `:root` e `[data-theme="dark"]` muda o deck inteiro, inclusive os diagramas SVG.
3. **Evento**: cabeçalho dos slides (nome, data, local), duração do timer e tema inicial ficam num lugar só, em [`src/js/config.js`](./src/js/config.js). O título da página e a duração usada na conferência dos tempos ficam no [`src/deck.json`](./src/deck.json).
4. **QR code**: `python3 tools/make_qr.py <sua-url>`, e atualize o texto da URL em `src/slides/obrigado/slide.html`.

> Se transformar isto numa palestra sua, mantenha a atribuição ao autor original, conforme a seção de licença.

## Créditos

- **Dan (Danilo Amaral)**: arquitetura da palestra, deck e código ([GitHub · it0dan](https://github.com/it0dan)).
- REC'n'Play 2026 e TDC Stage por receber o conteúdo.
- Comunidade: fontes primárias em [`docs/REFERENCIAS.md`](./docs/REFERENCIAS.md) (Cockburn, Martin, Evans, Fowler, Thoughtworks, Anthropic, LangChain, especificações MCP, A2A, OpenTelemetry e IETF).

## Licença e direitos

- **Código e estrutura do deck** (`src/`, `tools/`, `presentation.html` gerado): [**MIT**](./LICENSE). Copie, adapte e reuse à vontade, mantendo o aviso de copyright.
- **Conteúdo editorial** (texto dos slides, narrativa, notas do apresentador e [CUE-SHEET](./docs/CUE-SHEET.md)): **© 2026 Danilo Amaral**. Você pode apresentar, adaptar e derivar apresentações deste material **com atribuição ao autor**, para fins educacionais e comunitários.
- **Marcas de terceiros** citadas em contexto educacional pertencem aos seus titulares: *Sensedia®, TDC, REC'n'Play, Anthropic, OpenAI, Google, LangChain, Thoughtworks*. A paleta visual da Sensedia é usada como identidade da palestra, sem representação oficial.
- As configurações de gateway mostradas nos slides são **ilustrativas** e não descrevem a sintaxe de nenhum produto.
