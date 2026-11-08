# Cue sheet — Rec'n'Play 2026

Mapa de palco: ordem dos slides, tempo-alvo de cada um, tempo acumulado e quantos cliques cada slide tem antes de avançar (fragmentos). As falas abaixo são as mesmas notas do apresentador que aparecem no deck com a tecla `N`.

**TDC Stage · REC'n'Play 2026** · 12/11/2026 · 11:05 · CESAR Moinho, Sala Rizoflora · Recife · 40 min

| # | Slide | Link | Alvo | Acumulado | Cliques |
| --: | :-- | :-- | --: | --: | :--: |
| 00 | Capa | `#0` | 0:45 | 00:45 | — |
| 01 | Linha do tempo | `#1` | 3:30 | 04:15 | 6 |
| 02 | Microsserviços · EDA | `#2` | 3:30 | 07:45 | — |
| 03 | Monolito modular | `#3` | 3:00 | 10:45 | — |
| 04 | 30.11.2022 | `#4` | 0:45 | 11:30 | — |
| 05 | Linha do tempo agêntica | `#5` | 3:00 | 14:30 | 4 |
| 06 | AI-SDLC | `#6` | 3:30 | 18:00 | — |
| 07 | Hexagonal para LLM | `#7` | 3:30 | 21:30 | — |
| 08 | Contexto por agente | `#8` | 3:00 | 24:30 | — |
| 09 | Harness | `#9` | 3:00 | 27:30 | — |
| 10 | Loop | `#10` | 3:00 | 30:30 | — |
| 11 | Código com AI Gateway | `#11` | 3:30 | 34:00 | 4 |
| 12 | Sistema com AI Gateway | `#12` | 3:00 | 37:00 | — |
| 13 | Obrigado | `#13` | 3:00 | 40:00 | — |

Tempo-alvo total: **40 min**, distribuído entre os slides; os 3 min do Obrigado são para perguntas. Marcos para conferir no timer (`T`, que conta de 40:00 para baixo): fim das formas modernas (slide 04) com **11:30** decorridos (timer em 28:30), fim do AI-SDLC (slide 06) com **18:00** (timer em 22:00), fim do loop (slide 10) com **30:30** (timer em 9:30).

## Resgates

- **Passador parou de responder**: use as setas ou `PageDown`/`PageUp` do notebook; o clique do mouse também avança.
- **Pulou um slide**: `←` volta um passo; `#N` no fim da URL abre o slide N com tudo revelado.
- **Tela errada / projetor cortando**: `F` (ou `F5`) entra e sai da tela cheia; o palco se ajusta sozinho a qualquer resolução.
- **Pergunta sobre fonte**: `S` abre as fontes; `G`, o glossário; `Esc` fecha.
- **Pausa ou problema técnico**: `B` ou `.` liga a tela de pausa com cronômetro.
- **Navegador sem acesso aos arquivos** (pendrive, e-mail): abra `dist/recnplay-2026.html`, a versão de arquivo único gerada por `tools/bundle.py`, ou o PDF de backup.

## Falas por slide

### 00 · Capa

`slide-capa` · alvo 0:45 · sem cliques internos

Boa tarde, Recife! Hoje vou contar uma história de 30 anos de arquitetura em 35 minutos. Spoiler: ela se repete.

### 01 · Linha do tempo

`slide-linha-do-tempo` · alvo 3:30 · 6 clique(s) internos antes de avançar

Slide interativo: cada → acende uma era (6 cliques antes de avançar). Para cada uma, uma frase: qual acoplamento ela atacou e o que deixou de padrão. Monolito: tudo num artefato, resposta foi camadas e depois ports & adapters. SOA: integração ponto a ponto, resposta foi contrato e barramento. Microsserviços: times e deploys presos ao mesmo ciclo, resposta foi API gateway e estado por serviço. Event-driven e serverless: acoplamento temporal, resposta foi pub/sub, saga e consumidores idempotentes. Depois, IA generativa (2023): entra um componente probabilístico, mas o humano ainda executa, via assistentes e copilotos. Por fim, agentes (2025): o modelo passa a decidir e agir. A partir daqui, a palestra percorre essas formas de construir software e chega aos agentes.

### 02 · Microsserviços · EDA

`slide-microsservicos-eda` · alvo 3:30 · sem cliques internos

Daqui até o fim, um único domínio: análise de crédito. Uma fintech de crédito em três domínios. Originação cuida da entrada: proposta e status na esteira, cadastro e KYC do cliente, documentos com OCR e simulação de parcelas e CET. Análise de risco consulta bureaus e o SCR, comprova renda via Open Finance e avalia risco de identidade e golpe. Contratação e desembolso emite a CCB com assinatura digital, libera o crédito via Pix e acompanha a cobrança. Cada serviço tem time, pipeline e banco próprios: repare nas versões avançando de forma independente e, ao lado de cada pipeline, o banco que só aquele serviço acessa. Database-per-service: ninguém faz join no banco do outro; a integração é por evento ou API. E cada time escolhe o banco que serve ao seu problema: relacional para proposta e contrato, documento para extratos de renda, objeto para comprovantes, grafo para fraude, cache para simulação. Guardem essa imagem: é ela que volta adiante, quando cada agente for dono da sua janela de contexto. Entre domínios, eventos: ProposalReceived, ScoreCalculated, ProposalApproved, CreditDisbursed. Quando o proposal-svc publica ProposalReceived, o score-svc consome e, antes de consultar o bureau, verifica se aquele eventId já foi processado, porque a entrega é at-least-once e consultar o bureau duas vezes custa dinheiro. Guardem essa ideia: idempotência volta no fim, quando o modelo passar a decidir e a regra de negócio precisar garantir efeito uma vez só. Dois cases da confirmação. Netflix: depois de uma corrupção de banco em 2008 que parou o envio de DVDs por três dias, migrou de um monolito em data center próprio para centenas de microsserviços na AWS, concluindo em janeiro de 2016; no período, a audiência cresceu cerca de mil vezes. Amazon: entre 2001 e 2006, saiu de um monolito em duas camadas para uma plataforma de serviços descentralizada, com times donos do serviço de ponta a ponta, o "you build it, you run it" do Werner Vogels. O ponto em comum: microsserviço é uma decisão organizacional e de escala, não de moda.

### 03 · Monolito modular

`slide-monolito-modular` · alvo 3:00 · sem cliques internos

Depois de distribuir, o movimento de volta. Monolito modular: uma unidade de deploy e um processo, mas dividido em módulos com fronteiras de verdade. Cada módulo é um bounded context e tem duas partes. O contrato do módulo (facade, DTOs e os eventos que ele publica) é a única parte visível para os outros módulos; "visível" aqui é visibilidade de código, dentro do mesmo processo, e não uma API HTTP pública. O resto (domínio, aplicação e persistência) fica encapsulado. A comunicação entre módulos acontece de duas formas: chamada in-process ao contrato (Propostas chamando Risco para pedir a análise) ou eventos de domínio in-process (ProposalApproved, que Contratos escuta para emitir a CCB), que mantêm os módulos desacoplados. Acessar o interno de outro módulo é barrado por teste de arquitetura no build (ArchUnit, Spring Modulith, regras de módulo do Nx ou Packwerk). Os dados seguem a mesma regra: um banco, mas cada módulo só acessa o próprio schema, sem joins entre módulos. O host é quem expõe HTTP, consome filas e roda jobs, e despacha para os contratos. No repositório, isso vira contract/ e internal/ por módulo, mais um shared kernel mínimo. Se um módulo precisar de escala ou deploy próprios, ele já nasce extraível para serviço: o contrato vira API e os eventos in-process viram eventos no broker. Dois cases do "recuo". Prime Video, 2023: o serviço de monitoramento de qualidade de áudio e vídeo rodava distribuído em Step Functions, Lambda e S3, não escalava e custava caro; juntaram os componentes num único processo no ECS e o custo caiu cerca de 90%. Atenção ao recorte: foi uma ferramenta, não o Prime Video inteiro, e a lição é granularidade errada, não "microsserviço é ruim". Segment, 2018: mais de 140 microsserviços, um por destino, viraram um serviço e um monorepo, porque o custo operacional por serviço tinha passado do benefício. E a Shopify é o exemplo de quem nunca saiu do monolito: tornou-o modular, com fronteiras verificadas por ferramenta (Packwerk).

### 04 · 30.11.2022

`slide-30-11-2022` · alvo 0:45 · sem cliques internos

Pausa. Deixar a data na tela por alguns segundos antes de falar. 30 de novembro de 2022: o lançamento do ChatGPT. Em cinco dias, um milhão de usuários. É a data em que a IA generativa saiu do laboratório e entrou no cotidiano de quem desenvolve software. Daqui em diante, a linha do tempo muda de eixo: deixa de ser sobre como dividimos o sistema e passa a ser sobre quem executa o trabalho.

### 05 · Linha do tempo agêntica

`slide-linha-do-tempo-agentica` · alvo 3:00 · 4 clique(s) internos antes de avançar

Slide interativo: cada → acende uma fase. O eixo é quem executa. 2022, assistente: o humano faz tudo, o modelo só responde num chat. 2023, copiloto: o modelo sugere dentro da IDE e o humano aceita linha a linha. 2024 e 2025, agente de código: o modelo executa a tarefa inteira, lê o repositório, edita vários arquivos, roda os testes; o humano revisa o diff. 2025 e 2026, esteira agêntica: agentes rodam em background no SDLC, do issue ao PR, e o humano define a intenção e aprova nos gates. No produto, o mesmo movimento: primeiro o LLM entra como componente chamado por API, com o código decidindo o fluxo; depois o modelo passa a decidir. Cada passo transfere execução do humano para o modelo, e é isso que exige arquitetura.

### 06 · AI-SDLC

`slide-ai-sdlc` · alvo 3:30 · sem cliques internos

AI-SDLC é a última fase da linha do tempo, a esteira agêntica, olhada de perto. Uma intenção vira spec antes de virar código: spec-driven development (SDD, como no Spec Kit e no OpenSpec). A variação que usamos, SPDD, encadeia cinco artefatos: proposal (o porquê), design (como, com ADRs), spec (contrato verificável, critérios de aceite), tasks (passos pequenos) e, por fim, o prompt pronto para o agente. Nenhuma implementação começa sem essa cadeia. Do lado direito, o repositório vira contexto versionado: AGENTS.md é a fonte canônica de convenções, padrão aberto e agnóstico de ferramenta; o CLAUDE.md, ou equivalente, só importa o AGENTS.md e acrescenta o específico; e as skills (cada uma uma pasta com SKILL.md) são procedimentos carregados sob demanda, como gerar um ADR ou criar um adapter. Humanos ficam nos gates: aprovar a spec e aprovar o merge. E é aqui que hexagonal e clean pagam dividendos: fronteiras claras cabem numa janela de contexto, e testes por porta viram sensores do agente.

### 07 · Hexagonal para LLM

`slide-hexagonal-para-llm` · alvo 3:30 · sem cliques internos

Hexagonal, Onion e Clean Architecture nasceram em momentos diferentes (Alistair Cockburn em 2005, Jeffrey Palermo em 2008, Robert Martin em 2012), mas dizem a mesma coisa: o que importa, o domínio e os casos de uso, fica no centro; o que muda, banco, framework, provedor, fica na borda; e as dependências apontam para dentro. Por quê: para trocar o detalhe sem tocar a regra, para testar o núcleo sem rede e para conter o raio de impacto de um sistema externo. Como: o núcleo declara portas na língua do negócio, e adapters implementam essas portas traduzindo o modelo de fora, que é a anti-corruption layer do DDD. No desenho, a análise de crédito: entradas por REST, fila ou chat chamam o mesmo caso de uso, EvaluateProposal; ele conversa só com a porta CreditEvaluator; e cada provedor de LLM é um adapter, inclusive um Fake para testes. O ponto para aplicações com LLM: o modelo é um detalhe de infraestrutura. Messages, choices e content blocks nunca cruzam a porta; o que entra no núcleo é um Assessment validado. E quem decide é a regra de negócio, não o modelo. É esse adapter que, no fim da palestra, a gente troca por um que passa pelo AI Gateway, sem mudar uma linha do núcleo.

### 08 · Contexto por agente

`slide-contexto-por-agente` · alvo 3:00 · sem cliques internos

A mesma regra do database-per-service, agora para agentes. À esquerda, os serviços da análise de crédito: cada um é dono do seu banco, e ninguém faz join no banco do outro; a integração é por evento ou API. À direita, a análise de crédito agêntica: o orquestrador delega a três agentes, e cada um é dono da sua janela de contexto. O agente de risco enche a janela com bureau, SCR e histórico; o de renda, com extratos via Open Finance; o de documentos, com RG, comprovante e selfie. Nenhum agente lê a janela do outro, e o que sobe para o orquestrador é só o handoff: um resumo com teto de tokens, um contrato. Esse é o pilar isolate de context engineering (os outros três são write, persistir fora da janela; select, trazer só o relevante; e compress, resumir o histórico). Por que isolar: janela menor é mais barata, mais precisa e sofre menos context rot; e um documento com prompt injection contamina só a janela do agente de documentos, não a decisão inteira. É um bulkhead de contexto. Os chips são as chaves de isolamento do estado durável: tenant, usuário e thread em toda leitura e escrita, inclusive no cache semântico e no índice vetorial; identidade propagada on-behalf-of (token exchange, RFC 8693); PII mascarada antes de entrar no modelo; e checkpoint por thread para retomar e auditar.

### 09 · Harness

`slide-harness` · alvo 3:00 · sem cliques internos

Harness é tudo que envolve o modelo para transformar previsão de texto em comportamento confiável. A animação segue o ciclo: guias acendem antes da ação (feedforward: prompts, specs, contratos, AGENTS.md, skills); o modelo decide; sensores acendem depois (feedback: traces, guardrails e testes determinísticos, LLM-as-judge para o subjetivo e humano para o crítico); e os evals fecham o ciclo, medindo trajetória, resultado e custo por tarefa. Toda falha detectada vira um guia novo. É aqui que se resolve o que as regras determinísticas não resolvem: elas garantem consistência; o harness persegue correção. Em um sistema multiagêntico, cada agente tem o seu harness.

### 10 · Loop

`slide-loop` · alvo 3:00 · sem cliques internos

Loop engineering: desenhar o ciclo que o agente repete, e principalmente quando ele para. Quatro tipos pelo gatilho: turn-based (um prompt, o agente decide que terminou), goal-based (uma meta verificável, e quem decide parar é um evaluator), time-based (agenda) e proactive (evento externo, sem humano no gatilho). Quanto menos humano no gatilho, mais harness. Embaixo, as três falhas documentadas e a contramedida de cada uma: doom loop pede teto de iterações e budget; goal drift pede avaliador separado de quem gera; context rot pede compressão e isolamento em subagentes. E custo e latência são NFRs de primeira classe do loop: o budget de tokens e de tempo por tarefa é uma condição de parada no próprio loop, e o teto por app é aplicado no gateway, como veremos no fim.

### 11 · Código com AI Gateway

`slide-codigo-com-ai-gateway` · alvo 3:30 · 4 clique(s) internos antes de avançar

Fecho do hexagonal: a porta CreditEvaluator é a mesma do hexagonal, o caso de uso EvaluateProposal não mudou uma linha, e entra um adapter novo, GatewayCreditEvaluator, que manda tudo pela borda. Quatro cliques; cada um acende um trecho do código e o caminho correspondente no desenho. (1) Model Gateway: o cliente aponta para AI_GATEWAY_URL e se autentica com a identidade do workload, sem chave de provedor; o código pede o alias credit-deep e a política decide o modelo primário, o fallback, o mascaramento de PII e o budget de tokens. (2) MCP Gateway: a consulta ao bureau de crédito é uma tool MCP (get_score) que passa pela borda, com escopo mínimo e auditoria por chamada. (3) Agent Gateway: o pedido de score de fraude é uma tarefa A2A para o agente de outro domínio, com identidade e limite entre agentes. (4) O que fica no código, porque depende do domínio: o contrato da resposta (schema validado na fronteira), a decisão de crédito pela CreditPolicy, a idempotência por intenção e o contexto isolado por agente. O gateway governa o tráfego; ele não decide crédito. As políticas no desenho são ilustrativas. Se perguntarem do apiKey: workloadToken() é um bearer token de vida curta que representa o workload (OIDC, SPIFFE); o gateway valida esse token e usa a credencial do provedor que ele mesmo guarda. Nenhuma credencial de provedor mora no serviço.

### 12 · Sistema com AI Gateway

`slide-sistema-com-ai-gateway` · alvo 3:00 · sem cliques internos

Do código para o sistema inteiro: o mesmo desenho, agora com a borda. Em cima, cinco aplicações agênticas, cada uma com seus agentes: Onboarding (KYC e documentos), Crédito (risco e renda), Antifraude, Atendimento e Cobrança. Todo tráfego de IA dessas apps passa por um ponto de controle, com três módulos. Model Gateway, para os LLMs: credenciais em vault, roteamento e fallback entre provedores, mascaramento de PII, token budget por app. MCP Gateway, para ferramentas: autorização por tool, allowlist e a transformação de APIs existentes em MCP. Agent Gateway, para o tráfego entre agentes via A2A: identidade, limites e discovery. Por cima, um control plane com identidade, política, custo, auditoria e traces no padrão OpenTelemetry GenAI. A legenda explica as cores dos fluxos: roxo é app chamando modelo, azul é app chamando tools e APIs, laranja é um agente chamando agente de outra app; por exemplo, o agente de risco da App Crédito pedindo um score à App Antifraude. É a mesma história dos microsserviços: o que é transversal sai do código e vai para a borda. A lição do ESB continua valendo: a borda governa, mas não decide regra de negócio. Na Sensedia, é esse o desenho do AI Gateway; governar o tráfego entre agentes ainda é um padrão em evolução no mercado, inclusive no nosso roadmap.

### 13 · Obrigado

`slide-obrigado` · alvo 3:00 · sem cliques internos

Para levar: o núcleo é probabilístico, a casca é determinística. Não dá para tornar o modelo idempotente, mas dá para construir em volta dele uma casca que seja: contrato, contexto isolado, harness, loop com critério de parada e a borda que governa o tráfego de IA. Obrigado! Deixar este slide na tela durante as perguntas: cerca de 3 minutos reservados para o Q&A. O QR aponta para o GitHub Pages da apresentação, com slides, código e fontes.
