# Cue sheet — Rec'n'Play 2026

> Gerado por `tools/make_cue_sheet.py` a partir de `src/`. Não edite à mão: mude o slide e gere de novo.

Mapa de palco: ordem dos slides, tempo-alvo de cada um, tempo acumulado e quantos cliques cada slide tem antes de avançar (fragmentos). As falas são as mesmas notas do apresentador que aparecem no deck com a tecla `N`.

**TDC Stage · REC'n'Play 2026** · 12/11/2026 · 11:05 · CESAR Moinho, Sala Risoflora · Recife · 40 min

| # | Slide | Link | Alvo | Acumulado | Cliques |
| --: | :-- | :-- | --: | --: | :--: |
| 00 | CAPA | `#0` | 0:30 | 00:30 | — |
| 01 | LINHA DO TEMPO | `#1` | 2:45 | 03:15 | 6 |
| 02 | O MOMENTO | `#2` | 2:00 | 05:15 | 4 |
| 03 | MICROSSERVIÇOS · EDA | `#3` | 2:45 | 08:00 | — |
| 04 | MONOLITO MODULAR | `#4` | 2:45 | 10:45 | — |
| 05 | 30.11.2022 | `#5` | 0:30 | 11:15 | — |
| 06 | LINHA DO TEMPO AGÊNTICA | `#6` | 3:15 | 14:30 | 5 |
| 07 | PADRÕES ARQUITETURAIS | `#7` | 0:30 | 15:00 | — |
| 08 | CONTEXTO POR AGENTE | `#8` | 3:15 | 18:15 | — |
| 09 | HARNESS | `#9` | 3:15 | 21:30 | — |
| 10 | LOOP | `#10` | 3:15 | 24:45 | — |
| 11 | HEXAGONAL PARA LLM | `#11` | 4:15 | 29:00 | 4 |
| 12 | ENTÃO → AGORA | `#12` | 3:00 | 32:00 | 3 |
| 13 | AI GATEWAY | `#13` | 3:00 | 35:00 | 1 |
| 14 | FECHAMENTO | `#14` | 2:45 | 37:45 | — |
| 15 | OBRIGADO | `#15` | 2:15 | 40:00 | — |

Tempo-alvo total: **40:00** de 40 min; o tempo do último slide é o das perguntas.

## Marcos para conferir no timer

O timer da HUD (`T`) conta de 40:00 para baixo. Ao terminar cada bloco, ele deve estar perto de:

| Bloco | Último slide | Decorrido | Timer marcando |
| :-- | :--: | --: | --: |
| ABERTURA | 00 | 00:30 | 39:30 |
| 01 · FORMAS MODERNAS | 05 | 11:15 | 28:45 |
| 02 · DESENVOLVENDO COM GENAI | 06 | 14:30 | 25:30 |
| 03 · MULTIAGENTES | 10 | 24:45 | 15:15 |
| 04 · A TESE: CLEAN ARCHITECTURE PARA LLM | 12 | 32:00 | 08:00 |
| 05 · NFRs E AI GATEWAY | 13 | 35:00 | 05:00 |
| ENCERRAMENTO | 15 | 40:00 | 00:00 |

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

`slide-linha-do-tempo` · alvo 2:45 · 6 clique(s) internos antes de avançar

Slide interativo: cada → acende uma era (6 cliques antes de avançar). Para cada uma, uma frase: qual acoplamento ela atacou e o que deixou de padrão. Monolito: tudo num artefato, resposta foi camadas e depois ports & adapters. SOA: integração ponto a ponto, resposta foi contrato e barramento. Microsserviços: times e deploys presos ao mesmo ciclo, resposta foi API gateway e estado por serviço. Event-driven e serverless: acoplamento temporal, resposta foi pub/sub, saga e consumidores idempotentes. Depois, IA generativa (2023): entra um componente probabilístico, mas o humano ainda executa, via assistentes e copilotos. Por fim, agentes (2025): o modelo passa a decidir e agir. A partir daqui, a palestra percorre essas formas de construir software e chega aos agentes.

### 02 · O MOMENTO

`slide-mercado-2026` · alvo 2:00 · 4 clique(s) internos antes de avançar

Antes de entrar nos padrões, o momento, com dados deste semestre. Quatro cliques. Primeiro: segundo o Gartner, 71% das organizações esperam implantar IA agêntica nos próximos 12 meses, mas só 21% têm hoje capacidade de governança para agentes; a pesquisa é com mais de dois mil CIOs, divulgada no Symposium de outubro. Segundo: a McKinsey, no State of AI de agosto, mostra que entre as empresas acima de um bilhão de dólares de receita, 40% já escalam agentes; um ano antes eram 27%. Ou seja, está saindo do piloto. Terceiro, o contraponto: só 13% dos CIOs dizem ter obtido valor significativo ou transformacional com IA, também Gartner, outubro, 2.002 CIOs; o próprio Gartner resumiu como "o risco de IA cresce mais rápido que o valor". Quarto: até 2028, um quarto das violações de segurança corporativa vai ter origem em abuso de agentes de IA. Embaixo, o mesmo recado de outros lados: a Forrester batizou as previsões de 2027 de "a busca e o perigo do controle"; o AI100 de Stanford, publicado esta semana, destaca agentes agindo sem supervisão humana; e no top 10 de tendências 2027 do Gartner aparecem, com esse nome, harness de agentes de código e identidade de agentes. Todo mundo quer agentes; o que separa valor de risco não é o modelo, é arquitetura e governança. É disso que a palestra trata.

### 03 · MICROSSERVIÇOS · EDA

`slide-microsservicos-eda` · alvo 2:45 · sem cliques internos

Daqui até o fim, um único domínio: análise de crédito. Uma fintech de crédito em três domínios. Originação cuida da entrada: proposta e status na esteira, cadastro e KYC do cliente, documentos com OCR e simulação de parcelas e CET. Análise de risco consulta bureaus e o SCR, comprova renda via Open Finance e avalia risco de identidade e golpe. Contratação e desembolso emite a CCB com assinatura digital, libera o crédito via Pix e acompanha a cobrança. Cada serviço tem time, pipeline e banco próprios: repare nas versões avançando de forma independente e, ao lado de cada pipeline, o banco que só aquele serviço acessa. Database-per-service: ninguém faz join no banco do outro; a integração é por evento ou API. E cada time escolhe o banco que serve ao seu problema: relacional para proposta e contrato, documento para extratos de renda, objeto para comprovantes, grafo para fraude, cache para simulação. Guardem essa imagem: é ela que volta adiante, quando cada agente for dono da sua janela de contexto. Entre domínios, eventos: ProposalReceived, ScoreCalculated, ProposalApproved, CreditDisbursed. Quando o proposal-svc publica ProposalReceived, o score-svc consome e, antes de consultar o bureau, verifica se aquele eventId já foi processado, porque a entrega é at-least-once e consultar o bureau duas vezes custa dinheiro. Guardem essa ideia: idempotência volta no fim, quando o modelo passar a decidir e a regra de negócio precisar garantir efeito uma vez só. Dois cases da confirmação. Netflix: depois de uma corrupção de banco em 2008 que parou o envio de DVDs por três dias, migrou de um monolito em data center próprio para centenas de microsserviços na AWS, concluindo em janeiro de 2016; no período, a audiência cresceu cerca de mil vezes. Amazon: entre 2001 e 2006, saiu de um monolito em duas camadas para uma plataforma de serviços descentralizada, com times donos do serviço de ponta a ponta, o "you build it, you run it" do Werner Vogels. O ponto em comum: microsserviço é uma decisão organizacional e de escala, não de moda.

### 04 · MONOLITO MODULAR

`slide-monolito-modular` · alvo 2:45 · sem cliques internos

Depois de distribuir, o movimento de volta. Monolito modular: uma unidade de deploy e um processo, mas dividido em módulos com fronteiras de verdade. Cada módulo é um bounded context e tem duas partes. O contrato do módulo (facade, DTOs e os eventos que ele publica) é a única parte visível para os outros módulos; "visível" aqui é visibilidade de código, dentro do mesmo processo, e não uma API HTTP pública. O resto (domínio, aplicação e persistência) fica encapsulado. A comunicação entre módulos acontece de duas formas: chamada in-process ao contrato (Propostas chamando Risco para pedir a análise) ou eventos de domínio in-process (ProposalApproved, que Contratos escuta para emitir a CCB), que mantêm os módulos desacoplados. Acessar o interno de outro módulo é barrado por teste de arquitetura no build (ArchUnit, Spring Modulith, regras de módulo do Nx ou Packwerk). Os dados seguem a mesma regra: um banco, mas cada módulo só acessa o próprio schema, sem joins entre módulos. O host é quem expõe HTTP, consome filas e roda jobs, e despacha para os contratos. No repositório, isso vira contract/ e internal/ por módulo, mais um shared kernel mínimo. Se um módulo precisar de escala ou deploy próprios, ele já nasce extraível para serviço: o contrato vira API e os eventos in-process viram eventos no broker. Dois cases do "recuo". Prime Video, 2023: o serviço de monitoramento de qualidade de áudio e vídeo rodava distribuído em Step Functions, Lambda e S3, não escalava e custava caro; juntaram os componentes num único processo no ECS e o custo caiu cerca de 90%. Atenção ao recorte: foi uma ferramenta, não o Prime Video inteiro, e a lição é granularidade errada, não "microsserviço é ruim". Segment, 2018: mais de 140 microsserviços, um por destino, viraram um serviço e um monorepo, porque o custo operacional por serviço tinha passado do benefício. E a Shopify é o exemplo de quem nunca saiu do monolito: tornou-o modular, com fronteiras verificadas por ferramenta (Packwerk).

### 05 · 30.11.2022

`slide-30-11-2022` · alvo 0:30 · sem cliques internos

Pausa. Deixar a data na tela por alguns segundos antes de falar. 30 de novembro de 2022: o lançamento do ChatGPT. Em cinco dias, um milhão de usuários. É a data em que a IA generativa saiu do laboratório e entrou no cotidiano de quem desenvolve software. Daqui em diante, a linha do tempo muda de eixo: deixa de ser sobre como dividimos o sistema e passa a ser sobre quem executa o trabalho.

### 06 · LINHA DO TEMPO AGÊNTICA

`slide-linha-do-tempo-agentica` · alvo 3:15 · 5 clique(s) internos antes de avançar

Slide interativo: cada clique acende uma fase. O eixo é quem executa. 2022, assistente: o humano faz tudo, o modelo só responde num chat. 2023, copiloto: o modelo sugere dentro da IDE e o humano aceita linha a linha. 2024 e 2025, agente de código: o modelo executa a tarefa inteira, lê o repositório, edita arquivos, roda os testes; o humano revisa o diff. 2025 e 2026, esteira agêntica: agentes em background no SDLC, do issue ao PR, e o humano define a intenção e aprova nos gates. Último clique, a esteira de perto, e é por isso que ela está numa palestra sobre sistemas: a disciplina que a gente aprendeu a usar para desenvolver com agentes é a mesma que o produto vai pedir. Uma intenção vira spec antes de virar código (SDD; a variação que usamos, SPDD, encadeia proposal, design, spec, tasks e prompt); agentes de código guiados por AGENTS.md e skills, contexto versionado no repositório; review com testes e LLM-as-judge; e humanos nos gates. Spec é contrato, gate é HITL, review é eval. Guardem esses três: eles voltam no harness e no loop.

### 07 · PADRÕES ARQUITETURAIS

`slide-padroes-arquiteturais` · alvo 0:30 · sem cliques internos

Transição. Deixar o título na tela por alguns segundos. Até aqui, vimos como a gente divide sistemas e como a IA entrou no jeito de desenvolver. Agora, o produto: que padrões arquiteturais um sistema com agentes pede. Contexto por agente, harness, loop, e a tese que amarra tudo.

### 08 · CONTEXTO POR AGENTE

`slide-contexto-por-agente` · alvo 3:15 · sem cliques internos

A mesma regra do database-per-service, agora para agentes. À esquerda, os serviços da análise de crédito: cada um é dono do seu banco, e ninguém faz join no banco do outro; a integração é por evento ou API. À direita, a análise de crédito agêntica: o orquestrador delega a três agentes, e cada um é dono da sua janela de contexto. O agente de risco enche a janela com bureau, SCR e histórico; o de renda, com extratos via Open Finance; o de documentos, com RG, comprovante e selfie. Nenhum agente lê a janela do outro, e o que sobe para o orquestrador é só o handoff: um resumo com teto de tokens, um contrato. Esse é o pilar isolate de context engineering (os outros três são write, persistir fora da janela; select, trazer só o relevante; e compress, resumir o histórico). Por que isolar: janela menor é mais barata, mais precisa e sofre menos context rot; e um documento com prompt injection contamina só a janela do agente de documentos, não a decisão inteira. É um bulkhead de contexto. Os chips são as chaves de isolamento do estado durável: tenant, usuário e thread em toda leitura e escrita, inclusive no cache semântico e no índice vetorial; identidade propagada on-behalf-of (token exchange, RFC 8693); PII mascarada antes de entrar no modelo; e checkpoint por thread para retomar e auditar.

### 09 · HARNESS

`slide-harness` · alvo 3:15 · sem cliques internos

Harness é tudo que envolve o modelo para transformar previsão de texto em comportamento confiável. A animação segue o ciclo: guias acendem antes da ação (feedforward: prompts, specs, contratos, AGENTS.md, skills); o modelo decide; sensores acendem depois (feedback: traces, guardrails e testes determinísticos, LLM-as-judge para o subjetivo e humano para o crítico); e os evals fecham o ciclo, medindo trajetória, resultado e custo por tarefa. Toda falha detectada vira um guia novo. É aqui que se resolve o que as regras determinísticas não resolvem: elas garantem consistência; o harness persegue correção. Em um sistema multiagêntico, cada agente tem o seu harness.

### 10 · LOOP

`slide-loop` · alvo 3:15 · sem cliques internos

Loop engineering: desenhar o ciclo que o agente repete, e principalmente quando ele para. Quatro tipos pelo gatilho: turn-based (um prompt, o agente decide que terminou), goal-based (uma meta verificável, e quem decide parar é um evaluator), time-based (agenda) e proactive (evento externo, sem humano no gatilho). Quanto menos humano no gatilho, mais harness. Embaixo, as três falhas documentadas e a contramedida de cada uma: doom loop pede teto de iterações e budget; goal drift pede avaliador separado de quem gera; context rot pede compressão e isolamento em subagentes. E custo e latência são NFRs de primeira classe do loop: o budget de tokens e de tempo por tarefa é uma condição de parada no próprio loop, e o teto por app é aplicado no gateway, como veremos no fim.

### 11 · HEXAGONAL PARA LLM

`slide-hexagonal-para-llm` · alvo 4:15 · 4 clique(s) internos antes de avançar

Depois de contexto, harness e loop, a tese que amarra tudo, e que é a promessa desta palestra: desacoplar o provedor de LLM com Clean Architecture. O desafio: integrar IA não é adicionar um componente de modelo. É acomodar uma peça probabilística e imprevisível dentro de sistemas determinísticos, que exigem governança e disponibilidade. A resposta já existe: Hexagonal, de Cockburn, Onion, de Palermo, e Clean, de Uncle Bob, dizem a mesma coisa. O núcleo, domínio e casos de uso, decide; a infraestrutura fica na borda; as dependências apontam para dentro. No crédito: entradas por REST, fila ou chat chamam o mesmo caso de uso, EvaluateProposal, que fala só com a porta CreditEvaluator. Cada provedor de LLM é um adapter, inclusive um Fake para testes. Messages e choices nunca cruzam a porta; o que entra no núcleo é um Assessment validado, e quem decide é a CreditPolicy, não o modelo. O que se ganha: trocar de provedor sem tocar a regra, que é mitigar acoplamento tecnológico; testar o núcleo sem rede; e resiliência na borda. E tudo que vimos até aqui tem endereço: contexto, harness e loop moram na casca, em volta do núcleo. É esse adapter que, daqui a pouco, a gente coloca atrás do AI Gateway, sem mudar uma linha do núcleo. Agora o mesmo desenho, em código, em quatro cliques; a legenda embaixo do desenho acompanha cada bloco. Clique um, a porta: CreditEvaluator mora no domínio e fala a língua do negócio, Proposal entra, Assessment sai, nada de LLM. Clique dois, o caso de uso: EvaluateProposal recebe a porta e a política; o modelo sugere o Assessment, a CreditPolicy decide. Clique três, o adapter: um por provedor, é a ACL; traduz para o SDK e valida o retorno na fronteira, messages nunca passam da porta. Clique quatro, a composição: é aqui, e só aqui, que se escolhe o provedor, ou se injeta um Fake para testar, sem mudar uma linha do núcleo.

### 12 · ENTÃO → AGORA

`slide-entao-agora` · alvo 3:00 · 3 clique(s) internos antes de avançar

Lembram do começo? A história se repete. Este slide é o fecho dessa promessa: cada padrão que a gente usou para dividir sistemas reaparece, no mesmo papel, num sistema com agentes. Três cliques. Primeiro clique, a estrutura: monolito modular vira agente único com tools: o ponto de partida certo. Microsserviço vira agente como serviço: um agente é, na prática, mais um serviço, com dono, deploy, escala e contexto próprios, falando com os outros por protocolo, A2A, e não por banco compartilhado. Database-per-service vira contexto por agente. Segundo clique, a fronteira e a resiliência: ports and adapters e ACL viram o modelo como adapter. Timeout, retry e saga viram o loop com condição de parada. Terceiro clique, qualidade e borda: testes de contrato viram evals. E o API Gateway, que virou a borda do tráfego de APIs, ganha um irmão: o AI Gateway, a borda do tráfego de IA. A lição que vem junto é a mesma do ESB: a borda governa o tráfego, mas não decide regra de negócio.

### 13 · AI GATEWAY

`slide-ai-gateway` · alvo 3:00 · 1 clique(s) internos antes de avançar

Até aqui a gente resolveu o que é de cada aplicação: porta e adapter, contexto isolado, harness e loop. Agora o que é do sistema inteiro. Sem AI Gateway, cada aplicação agêntica fala direto com cada provedor de modelo, cada tool e cada agente de outro domínio. Três apps e quatro destinos já são doze integrações, e cada uma carrega a sua chave de provedor, o seu retry, o seu log e o seu jeito de contar token. É o mesmo problema que a gente tinha com API antes do API Gateway, só que agora o tráfego é de modelo, de tool e de agente. Clique 1: com AI Gateway, todo o tráfego de IA passa por um ponto de controle. As apps se autenticam com a própria identidade, pedem um modelo por alias, e a borda cuida de credencial, política, roteamento, trace e custo. Por quê, em uma frase: o que é de todos (credencial, roteamento, fallback, custo, política, trace) sai do código de cada aplicação e vai para a borda. O que o gateway não faz: ele não decide crédito e não valida o contrato do domínio; isso continua no núcleo, como o próximo slide mostra no código. Se perguntarem de produto: é esse papel que o Sensedia AI Gateway cumpre; os nomes de políticas nos próximos slides são ilustrativos.

### 14 · FECHAMENTO

`slide-fechamento` · alvo 2:45 · sem cliques internos

Para fechar, a imagem que resume a palestra. No centro, o modelo: probabilístico, imprevisível, e é assim que ele deve ser; os pontinhos não param quietos. Em volta, camada por camada, o que a gente desenhou para acomodar esse núcleo num sistema que exige governança e disponibilidade. Primeiro, porta e adapter: Clean Architecture, para o provedor de LLM ser um detalhe trocável, e é assim que se mitiga o acoplamento tecnológico. Depois, contexto isolado por agente: cada um com a sua janela. Depois, harness e loop: guias, sensores e uma regra explícita de quando parar, que é o que torna a orquestração de vários agentes gerenciável. E por fora, a borda: o AI Gateway, com identidade, política, fallback e custo, que é de onde vem a resiliência sistêmica. Do monolítico ao agente autônomo, os padrões não mudaram, mudaram de lugar. O desafio não é o modelo; é a arquitetura em volta dele. E cada anel desses tem um custo: mais latência, mais componentes, mais coisa para operar. Por isso a primeira lei da arquitetura de software, de Mark Richards e Neal Ford: arquitetura é sobre tradeoffs. Não existe o desenho certo; existe o tradeoff consciente para o seu contexto.

### 15 · OBRIGADO

`slide-obrigado` · alvo 2:15 · sem cliques internos

Para levar: não estamos mudando o que fazemos, e sim como fazemos. Contrato, isolamento, orquestração, resiliência e governança continuam sendo o trabalho; o que muda é onde cada padrão mora quando um componente probabilístico entra no sistema: contexto isolado, harness, loop com critério de parada e a borda que governa o tráfego de IA. Obrigado! Deixar este slide na tela durante as perguntas: cerca de 2 minutos reservados para o Q&A. O QR aponta para o GitHub Pages da apresentação, com slides, código e fontes.
