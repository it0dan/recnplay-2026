# Cue sheet — Rec'n'Play 2026

> Gerado por `tools/make_cue_sheet.py` a partir de `src/`. Não edite à mão: mude o slide e gere de novo.

Mapa de palco: ordem dos slides, tempo-alvo de cada um, tempo acumulado e quantos cliques cada slide tem antes de avançar (fragmentos). As falas são as mesmas notas do apresentador que aparecem no deck com a tecla `N`.

**TDC Stage · REC'n'Play 2026** · 12/11/2026 · 11:05 · CESAR Moinho, Sala Rizoflora · Recife · 40 min

| # | Slide | Link | Alvo | Acumulado | Cliques |
| --: | :-- | :-- | --: | --: | :--: |
| 00 | CAPA | `#0` | 0:30 | 00:30 | — |
| 01 | LINHA DO TEMPO | `#1` | 3:00 | 03:30 | 6 |
| 02 | MICROSSERVIÇOS · EDA | `#2` | 2:45 | 06:15 | — |
| 03 | MONOLITO MODULAR | `#3` | 2:30 | 08:45 | — |
| 04 | 30.11.2022 | `#4` | 0:30 | 09:15 | — |
| 05 | LINHA DO TEMPO AGÊNTICA | `#5` | 3:15 | 12:30 | 5 |
| 06 | HEXAGONAL PARA LLM | `#6` | 3:30 | 16:00 | — |
| 07 | CONTEXTO POR AGENTE | `#7` | 3:15 | 19:15 | — |
| 08 | HARNESS E LOOP | `#8` | 4:00 | 23:15 | 1 |
| 09 | ONDE CADA PEÇA MORA | `#9` | 3:15 | 26:30 | 4 |
| 10 | ENTÃO → AGORA | `#10` | 3:30 | 30:00 | 4 |
| 11 | AI GATEWAY | `#11` | 2:45 | 32:45 | 1 |
| 12 | SISTEMA COM AI GATEWAY | `#12` | 4:00 | 36:45 | — |
| 13 | OBRIGADO | `#13` | 3:15 | 40:00 | — |

Tempo-alvo total: **40:00** de 40 min; o tempo do último slide é o das perguntas.

## Marcos para conferir no timer

O timer da HUD (`T`) conta de 40:00 para baixo. Ao terminar cada bloco, ele deve estar perto de:

| Bloco | Último slide | Decorrido | Timer marcando |
| :-- | :--: | --: | --: |
| ABERTURA | 00 | 00:30 | 39:30 |
| 01 · FORMAS MODERNAS | 04 | 09:15 | 30:45 |
| 02 · DESENVOLVENDO COM GENAI | 05 | 12:30 | 27:30 |
| 03 · APLICAÇÕES AGÊNTICAS | 06 | 16:00 | 24:00 |
| 04 · MULTIAGENTES | 10 | 30:00 | 10:00 |
| 05 · NFRs E AI GATEWAY | 12 | 36:45 | 03:15 |
| ENCERRAMENTO | 13 | 40:00 | 00:00 |

## Resgates

- **Passador parou de responder**: use as setas ou `PageDown`/`PageUp` do notebook; o clique do mouse também avança.
- **Pulou um slide**: `←` volta um passo; `#N` no fim da URL abre o slide N com tudo revelado.
- **Tela errada / projetor cortando**: `F` (ou `F5`) entra e sai da tela cheia; o palco se ajusta sozinho a qualquer resolução.
- **Pergunta sobre fonte**: `S` abre as fontes; `G`, o glossário; `Esc` fecha.
- **Pausa ou problema técnico**: `B` ou `.` liga a tela de pausa com cronômetro.
- **Navegador sem acesso aos arquivos** (pendrive, e-mail): abra `dist/recnplay-2026.html`, a versão de arquivo único gerada por `tools/bundle.py`, ou o PDF de backup.

## Falas por slide

### 00 · CAPA

`slide-capa` · alvo 0:30 · sem cliques internos

Bom dia, Recife! Hoje vou contar uma história de 30 anos de arquitetura, e spoiler: ela se repete. O título fala em agente autônomo, e vou ser honesto desde já: a autonomia que funciona em produção é autonomia com limites desenhados. É sobre esses limites, e sobre onde eles moram na arquitetura, que é esta conversa.

### 01 · LINHA DO TEMPO

`slide-linha-do-tempo` · alvo 3:00 · 6 clique(s) internos antes de avançar

Slide interativo: cada → acende uma era (6 cliques antes de avançar). Para cada uma, uma frase: qual acoplamento ela atacou e o que deixou de padrão. Monolito: tudo num artefato, resposta foi camadas e depois ports & adapters. SOA: integração ponto a ponto, resposta foi contrato e barramento. Microsserviços: times e deploys presos ao mesmo ciclo, resposta foi API gateway e estado por serviço. Event-driven e serverless: acoplamento temporal, resposta foi pub/sub, saga e consumidores idempotentes. Depois, IA generativa (2023): entra um componente probabilístico, mas o humano ainda executa, via assistentes e copilotos. Por fim, agentes (2025): o modelo passa a decidir e agir. A partir daqui, a palestra percorre essas formas de construir software e chega aos agentes.

### 02 · MICROSSERVIÇOS · EDA

`slide-microsservicos-eda` · alvo 2:45 · sem cliques internos

Daqui até o fim, um único domínio: análise de crédito. Uma fintech de crédito em três domínios. Originação cuida da entrada: proposta e status na esteira, cadastro e KYC do cliente, documentos com OCR e simulação de parcelas e CET. Análise de risco consulta bureaus e o SCR, comprova renda via Open Finance e avalia risco de identidade e golpe. Contratação e desembolso emite a CCB com assinatura digital, libera o crédito via Pix e acompanha a cobrança. Cada serviço tem time, pipeline e banco próprios: repare nas versões avançando de forma independente e, ao lado de cada pipeline, o banco que só aquele serviço acessa. Database-per-service: ninguém faz join no banco do outro; a integração é por evento ou API. E cada time escolhe o banco que serve ao seu problema: relacional para proposta e contrato, documento para extratos de renda, objeto para comprovantes, grafo para fraude, cache para simulação. Guardem essa imagem: é ela que volta adiante, quando cada agente for dono da sua janela de contexto. Entre domínios, eventos: ProposalReceived, ScoreCalculated, ProposalApproved, CreditDisbursed. Quando o proposal-svc publica ProposalReceived, o score-svc consome e, antes de consultar o bureau, verifica se aquele eventId já foi processado, porque a entrega é at-least-once e consultar o bureau duas vezes custa dinheiro. Guardem essa ideia: idempotência volta no fim, quando o modelo passar a decidir e a regra de negócio precisar garantir efeito uma vez só. Dois cases da confirmação. Netflix: depois de uma corrupção de banco em 2008 que parou o envio de DVDs por três dias, migrou de um monolito em data center próprio para centenas de microsserviços na AWS, concluindo em janeiro de 2016; no período, a audiência cresceu cerca de mil vezes. Amazon: entre 2001 e 2006, saiu de um monolito em duas camadas para uma plataforma de serviços descentralizada, com times donos do serviço de ponta a ponta, o "you build it, you run it" do Werner Vogels. O ponto em comum: microsserviço é uma decisão organizacional e de escala, não de moda.

### 03 · MONOLITO MODULAR

`slide-monolito-modular` · alvo 2:30 · sem cliques internos

Depois de distribuir, o movimento de volta. Monolito modular: uma unidade de deploy e um processo, mas dividido em módulos com fronteiras de verdade. Cada módulo é um bounded context e tem duas partes. O contrato do módulo (facade, DTOs e os eventos que ele publica) é a única parte visível para os outros módulos; "visível" aqui é visibilidade de código, dentro do mesmo processo, e não uma API HTTP pública. O resto (domínio, aplicação e persistência) fica encapsulado. A comunicação entre módulos acontece de duas formas: chamada in-process ao contrato (Propostas chamando Risco para pedir a análise) ou eventos de domínio in-process (ProposalApproved, que Contratos escuta para emitir a CCB), que mantêm os módulos desacoplados. Acessar o interno de outro módulo é barrado por teste de arquitetura no build (ArchUnit, Spring Modulith, regras de módulo do Nx ou Packwerk). Os dados seguem a mesma regra: um banco, mas cada módulo só acessa o próprio schema, sem joins entre módulos. O host é quem expõe HTTP, consome filas e roda jobs, e despacha para os contratos. No repositório, isso vira contract/ e internal/ por módulo, mais um shared kernel mínimo. Se um módulo precisar de escala ou deploy próprios, ele já nasce extraível para serviço: o contrato vira API e os eventos in-process viram eventos no broker. Dois cases do "recuo". Prime Video, 2023: o serviço de monitoramento de qualidade de áudio e vídeo rodava distribuído em Step Functions, Lambda e S3, não escalava e custava caro; juntaram os componentes num único processo no ECS e o custo caiu cerca de 90%. Atenção ao recorte: foi uma ferramenta, não o Prime Video inteiro, e a lição é granularidade errada, não "microsserviço é ruim". Segment, 2018: mais de 140 microsserviços, um por destino, viraram um serviço e um monorepo, porque o custo operacional por serviço tinha passado do benefício. E a Shopify é o exemplo de quem nunca saiu do monolito: tornou-o modular, com fronteiras verificadas por ferramenta (Packwerk).

### 04 · 30.11.2022

`slide-30-11-2022` · alvo 0:30 · sem cliques internos

Pausa. Deixar a data na tela por alguns segundos antes de falar. 30 de novembro de 2022: o lançamento do ChatGPT. Em cinco dias, um milhão de usuários. É a data em que a IA generativa saiu do laboratório e entrou no cotidiano de quem desenvolve software. Daqui em diante, a linha do tempo muda de eixo: deixa de ser sobre como dividimos o sistema e passa a ser sobre quem executa o trabalho.

### 05 · LINHA DO TEMPO AGÊNTICA

`slide-linha-do-tempo-agentica` · alvo 3:15 · 5 clique(s) internos antes de avançar

Slide interativo: cada clique acende uma fase. O eixo é quem executa. 2022, assistente: o humano faz tudo, o modelo só responde num chat. 2023, copiloto: o modelo sugere dentro da IDE e o humano aceita linha a linha. 2024 e 2025, agente de código: o modelo executa a tarefa inteira, lê o repositório, edita arquivos, roda os testes; o humano revisa o diff. 2025 e 2026, esteira agêntica: agentes em background no SDLC, do issue ao PR, e o humano define a intenção e aprova nos gates. Último clique, a esteira de perto, e é por isso que ela está numa palestra sobre sistemas: a disciplina que a gente aprendeu a usar para desenvolver com agentes é a mesma que o produto vai pedir. Uma intenção vira spec antes de virar código (SDD; a variação que usamos, SPDD, encadeia proposal, design, spec, tasks e prompt); agentes de código guiados por AGENTS.md e skills, contexto versionado no repositório; review com testes e LLM-as-judge; e humanos nos gates. Spec é contrato, gate é HITL, review é eval. Guardem esses três: eles voltam no harness e no loop.

### 06 · HEXAGONAL PARA LLM

`slide-hexagonal-para-llm` · alvo 3:30 · sem cliques internos

Hexagonal, Onion e Clean Architecture nasceram em momentos diferentes (Alistair Cockburn em 2005, Jeffrey Palermo em 2008, Robert Martin em 2012), mas dizem a mesma coisa: o que importa, o domínio e os casos de uso, fica no centro; o que muda, banco, framework, provedor, fica na borda; e as dependências apontam para dentro. Por quê: para trocar o detalhe sem tocar a regra, para testar o núcleo sem rede e para conter o raio de impacto de um sistema externo. Como: o núcleo declara portas na língua do negócio, e adapters implementam essas portas traduzindo o modelo de fora, que é a anti-corruption layer do DDD. No desenho, a análise de crédito: entradas por REST, fila ou chat chamam o mesmo caso de uso, EvaluateProposal; ele conversa só com a porta CreditEvaluator; e cada provedor de LLM é um adapter, inclusive um Fake para testes. O ponto para aplicações com LLM: o modelo é um detalhe de infraestrutura. Messages, choices e content blocks nunca cruzam a porta; o que entra no núcleo é um Assessment validado. E quem decide é a regra de negócio, não o modelo. É esse adapter que, no fim da palestra, a gente troca por um que passa pelo AI Gateway, sem mudar uma linha do núcleo.

### 07 · CONTEXTO POR AGENTE

`slide-contexto-por-agente` · alvo 3:15 · sem cliques internos

A mesma regra do database-per-service, agora para agentes. À esquerda, os serviços da análise de crédito: cada um é dono do seu banco, e ninguém faz join no banco do outro; a integração é por evento ou API. À direita, a análise de crédito agêntica: o orquestrador delega a três agentes, e cada um é dono da sua janela de contexto. O agente de risco enche a janela com bureau, SCR e histórico; o de renda, com extratos via Open Finance; o de documentos, com RG, comprovante e selfie. Nenhum agente lê a janela do outro, e o que sobe para o orquestrador é só o handoff: um resumo com teto de tokens, um contrato. Esse é o pilar isolate de context engineering (os outros três são write, persistir fora da janela; select, trazer só o relevante; e compress, resumir o histórico). Por que isolar: janela menor é mais barata, mais precisa e sofre menos context rot; e um documento com prompt injection contamina só a janela do agente de documentos, não a decisão inteira. É um bulkhead de contexto. Os chips são as chaves de isolamento do estado durável: tenant, usuário e thread em toda leitura e escrita, inclusive no cache semântico e no índice vetorial; identidade propagada on-behalf-of (token exchange, RFC 8693); PII mascarada antes de entrar no modelo; e checkpoint por thread para retomar e auditar.

### 08 · HARNESS E LOOP

`slide-harness-e-loop` · alvo 4:00 · 1 clique(s) internos antes de avançar

Harness é tudo que envolve o modelo para transformar previsão de texto em comportamento confiável. A animação segue o ciclo: guias acendem antes da ação (feedforward: prompts, specs, contratos, AGENTS.md, skills); o modelo decide; sensores acendem depois (feedback: traces, guardrails e testes determinísticos, LLM-as-judge para o subjetivo e humano para o crítico); e os evals fecham o ciclo, medindo trajetória, resultado e custo por tarefa. Toda falha detectada vira um guia novo. Clique: o loop. Agir, verificar, corrigir, disparado por um prompt, uma meta, uma agenda ou um evento; quanto menos humano no gatilho, mais harness. Projetar o loop é projetar quando ele para: meta confirmada por um avaliador, teto de iterações, budget de tokens e de tempo, ou escalonamento para um humano. São essas regras que evitam as três falhas documentadas: doom loop, goal drift e context rot. Repare na precisão: o modelo continua probabilístico, e o juiz também; o que é determinístico é a regra que decide quando o loop para. Em um sistema multiagêntico, cada agente tem o seu harness e o seu loop.

### 09 · ONDE CADA PEÇA MORA

`slide-onde-cada-peca-mora` · alvo 3:15 · 4 clique(s) internos antes de avançar

Harness e loop não são conceitos soltos: eles têm endereço na mesma arquitetura hexagonal que a gente já viu, desenhada aqui como os anéis do hexágono. Quatro cliques, cada um acende uma cor. (1) Guias, o feedforward: AGENTS.md e skills no repositório; o contrato da saída no domínio; o prompt versionado dentro do adapter, porque prompt é detalhe de infraestrutura. (2) Sensores, o feedback: a CreditPolicy no domínio é o guardrail determinístico; o LLM-as-judge entra atrás de uma porta, como qualquer outro adapter, para poder ser trocado e testado com um fake; e no CI ficam os evals, sobre casos de referência, medindo trajetória, resultado e custo, mais o teste de arquitetura que barra SDK no núcleo. (3) O loop mora no caso de uso: agir, verificar, corrigir, falando só com portas, sem SDK e sem prompt. (4) E as condições de parada também moram ali, como regra explícita: meta atingida, teto de iterações, budget, ou escalonamento para um humano. É a tese da palestra num desenho: o núcleo é probabilístico, e a casca que decide quando ele para é determinística.

### 10 · ENTÃO → AGORA

`slide-entao-agora` · alvo 3:30 · 4 clique(s) internos antes de avançar

Lembram do começo? A história se repete. Este slide é o fecho dessa promessa: cada padrão que a gente usou para dividir sistemas reaparece, no mesmo papel, num sistema com agentes. Três cliques. Monolito modular vira agente único com tools: o ponto de partida certo. Microsserviço vira agente como serviço: um agente é, na prática, mais um serviço, com dono, deploy, escala e contexto próprios, falando com os outros por protocolo, A2A, e não por banco compartilhado. Database-per-service vira contexto por agente. Ports and adapters e ACL viram o modelo como adapter. Timeout, retry e saga viram o loop com condição de parada. Testes de contrato viram evals. E o API Gateway, que virou a borda do tráfego de APIs, ganha um irmão: o AI Gateway, a borda do tráfego de IA. A lição que vem junto é a mesma do ESB: a borda governa o tráfego, mas não decide regra de negócio. Quarto clique, o espelho do monolito modular: quando não ir para multiagente. Se é uma tarefa, com um dono e um contexto que cabe na janela, um agente com tools basta. Multiagente se paga quando contexto, dono ou permissão precisam se separar, e cada handoff custa tokens, latência e mais um ponto de falha. É a mesma pergunta de Prime Video e Segment, agora para agentes: granularidade.

### 11 · AI GATEWAY

`slide-ai-gateway` · alvo 2:45 · 1 clique(s) internos antes de avançar

Até aqui a gente resolveu o que é de cada aplicação: porta e adapter, contexto isolado, harness e loop. Agora o que é do sistema inteiro. Sem AI Gateway, cada aplicação agêntica fala direto com cada provedor de modelo, cada tool e cada agente de outro domínio. Três apps e quatro destinos já são doze integrações, e cada uma carrega a sua chave de provedor, o seu retry, o seu log e o seu jeito de contar token. É o mesmo problema que a gente tinha com API antes do API Gateway, só que agora o tráfego é de modelo, de tool e de agente. Clique 1: com AI Gateway, todo o tráfego de IA passa por um ponto de controle. As apps se autenticam com a própria identidade, pedem um modelo por alias, e a borda cuida de credencial, política, roteamento, trace e custo. Por quê, em uma frase: o que é de todos (credencial, roteamento, fallback, custo, política, trace) sai do código de cada aplicação e vai para a borda. O que o gateway não faz: ele não decide crédito e não valida o contrato do domínio; isso continua no núcleo, como o próximo slide mostra no código. Se perguntarem de produto: é esse papel que o Sensedia AI Gateway cumpre; os nomes de políticas nos próximos slides são ilustrativos.

### 12 · SISTEMA COM AI GATEWAY

`slide-sistema-com-ai-gateway` · alvo 4:00 · sem cliques internos

Do conceito para uma arquitetura de solução: o que existe hoje e o que entra agora, no mesmo desenho. Embaixo, o antes, que continua em produção: o monolito modular de originação, com Propostas, Risco e Contratos, os microsserviços de score, fraude, desembolso e cobrança, e o broker de eventos. Os canais chegam por um API Gateway, como sempre. Em cima, o agora: o sistema multiagente de análise de crédito, com um orquestrador e agentes especialistas, cada um com dono, deploy e janela de contexto próprios. Ele é exposto pelo mesmo API Gateway, e também é disparado por evento: um ProposalReceived no broker começa a análise. O ponto da palestra: agentes não substituem os sistemas, eles se integram a eles. As tools dos agentes são as APIs que já existem, publicadas como tools MCP: consultar proposta no monolito, emitir contrato, pedir score ao score-svc. E todo o tráfego de IA passa por uma segunda borda, o AI Gateway. MCP Gateway para tools, com Enterprise-Managed Authorization: o IdP da empresa emite o ID-JAG e decide o acesso. Agent Gateway para falar com o agente antifraude, de outro domínio, por A2A e on-behalf-of, o token exchange da RFC 8693. LLM Gateway para os modelos, com OAuth 2.1, roteamento e fallback. Nenhuma API key de provedor mora nos serviços. Dois gateways, dois tráfegos: o API Gateway governa o tráfego de APIs, o AI Gateway governa o tráfego de IA. E nenhum dos dois decide regra de negócio. Se alguém perguntar sobre trocar de modelo: vira configuração na borda, mas não sem evals, porque o comportamento muda entre provedores. Agent Gateway é padrão em evolução no mercado.

### 13 · OBRIGADO

`slide-obrigado` · alvo 3:15 · sem cliques internos

Para levar: o núcleo é probabilístico, e a casca que decide quando ele para é determinística. Não dá para tornar o modelo idempotente, mas dá para construir em volta dele uma casca que seja: contrato, contexto isolado, harness, loop com critério de parada e a borda que governa o tráfego de IA. Obrigado! Deixar este slide na tela durante as perguntas: pouco menos de 3 minutos reservados para o Q&A. O QR aponta para o GitHub Pages da apresentação, com slides, código e fontes.
