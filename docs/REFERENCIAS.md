# Referências

Tudo que é citado no palco ou nas notas do apresentador. É o mesmo conteúdo do painel de fontes do deck (tecla `S`). Links verificados em novembro de 2026.

## Arquitetura · fundamentos

- [Hexagonal Architecture (Ports & Adapters)](https://alistair.cockburn.us/hexagonal-architecture) — Alistair Cockburn · 2005
- [The Onion Architecture](https://jeffreypalermo.com/2008/07/the-onion-architecture-part-1/) — Jeffrey Palermo · 2008
- [The Clean Architecture](https://blog.cleancoder.com/uncle-bob/2012/08/13/the-clean-architecture.html) — Robert C. Martin · 2012
- [Domain-Driven Design (bounded context, ACL)](https://www.domainlanguage.com/ddd/) — Eric Evans · 2003

## Monolito modular · microsserviços · EDA

- [Spring Modulith](https://spring.io/projects/spring-modulith/) — Spring · VMware Tanzu
- [ArchUnit](https://www.archunit.org/) — testes de arquitetura em Java
- [Nx · Enforce module boundaries](https://nx.dev/docs/platform-features/code-organization/enforce-module-boundaries) — Nx docs
- [Packwerk](https://github.com/Shopify/packwerk) — Shopify
- [Microservices](https://martinfowler.com/articles/microservices.html) — James Lewis & Martin Fowler · 2014
- [Sagas](https://doi.org/10.1145/38713.38742) — Garcia-Molina & Salem · SIGMOD 1987

## Cases da indústria (slides 02–03)

- [Prime Video: de serverless distribuído a um processo, −90% de custo](https://www.infoq.com/news/2023/05/prime-ec2-ecs-saves-costs/) — InfoQ · mai/2023
- [Goodbye Microservices: From 100s of problem children to 1 superstar](https://twilio.com/en-us/blog/developers/best-practices/goodbye-microservices) — Alexandra Noonan · Segment · jul/2018
- [Deconstructing the Monolith](https://shopify.engineering/deconstructing-monolith-designing-software-maximizes-developer-productivity) — Kirsten Westeinde · Shopify Engineering · 2019
- [Completing the Netflix Cloud Migration](https://about.netflix.com/en/news/completing-the-netflix-cloud-migration) — Netflix · fev/2016
- [A Conversation with Werner Vogels](https://queue.acm.org/detail.cfm?id=1142065) — ACM Queue vol. 4 nº 4 · 2006

## IA no ciclo de desenvolvimento · AI-SDLC

- [Introducing ChatGPT](https://openai.com/index/chatgpt/) — OpenAI · 30/nov/2022
- [Spec Kit (spec-driven development)](https://github.com/github/spec-kit) — GitHub
- [OpenSpec](https://github.com/Fission-AI/OpenSpec) — Fission AI
- [Structured-Prompt-Driven Development (SPDD)](https://martinfowler.com/articles/structured-prompt-driven/) — martinfowler.com
- [AGENTS.md](https://agents.md/) — formato aberto
- [Agent Skills (SKILL.md)](https://agentskills.io/) — formato aberto

## Agentes · contexto

- [Effective context engineering for AI agents](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents) — Anthropic
- [Context Engineering (write · select · compress · isolate)](https://www.langchain.com/blog/context-engineering-for-agents) — LangChain

## Harness · loop · evals

- [Harness engineering for coding agent users](https://martinfowler.com/articles/harness-engineering.html) — Birgitta Böckeler · martinfowler.com
- [Demystifying evals for AI agents](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents) — Anthropic
- [Getting started with loops](https://claude.com/blog/getting-started-with-loops) — Claude blog · jun/2026
- [The Art of Loop Engineering](https://www.langchain.com/blog/the-art-of-loop-engineering) — LangChain · jun/2026

## Protocolos e padrões abertos

- [Model Context Protocol (MCP)](https://modelcontextprotocol.io/) — especificação aberta
- [Agent2Agent Protocol (A2A)](https://a2a-protocol.org/latest/specification/) — Linux Foundation
- [Semantic conventions · Gen AI](https://opentelemetry.io/docs/specs/semconv/registry/attributes/gen-ai/) — OpenTelemetry
- [RFC 8693 · OAuth 2.0 Token Exchange](https://www.rfc-editor.org/rfc/rfc8693.html) — IETF · 2020
- [MCP · Enterprise-Managed Authorization (ID-JAG)](https://modelcontextprotocol.io/extensions/auth/enterprise-managed-authorization) — extensão de autorização do MCP
- [MCP Authorization (baseada em OAuth 2.1)](https://modelcontextprotocol.io/specification/latest/basic/authorization) — especificação MCP
- [Identity Assertion JWT Authorization Grant (ID-JAG)](https://datatracker.ietf.org/doc/draft-ietf-oauth-identity-assertion-authz-grant/) — IETF OAuth WG · draft
- [SPIFFE (identidade de workload)](https://spiffe.io/) — CNCF

## AgentOps · AI FinOps

Base do painel de métricas (slide de AgentOps e AI FinOps). Os valores do painel são ilustrativos; as faixas de referência de AgentOps são a régua de maturidade descrita no primeiro artigo.

- [AgentOps: como provar valor dos seus agentes de IA?](https://www.sensedia.com.br/post/agentops-como-provar-valor-agentes-ia) — Danilo Amaral · Sensedia · set/2026
- [AI FinOps é um problema de arquitetura](https://www.sensedia.com.br/post/ai-finops-ai-gateway) — Gabriel Zessin · Sensedia · set/2026
- [O que é AI FinOps e por que é essencial para o controle de custos com IA?](https://www.sensedia.com.br/post/ai-finops-controle-de-custos-ia) — Sensedia · set/2026
- [AI FinOps: como evitar surpresas nos custos dos LLMs?](https://www.sensedia.com.br/post/ai-finops-custos-llms) — Lisa Arthur · Sensedia · out/2026

As configurações de gateway mostradas nos slides são **ilustrativas**: explicam o padrão e não descrevem a sintaxe de nenhum produto.
