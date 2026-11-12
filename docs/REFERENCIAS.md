# Referências

Tudo que é citado no palco ou nas notas do apresentador. É o mesmo conteúdo do painel de fontes do deck (tecla `S`). Links verificados em novembro de 2026.

## Panorama de mercado · 2º semestre de 2026 (slide 02)

- [Gartner Says AI Risk is Rising Faster Than AI Value](https://www.gartner.com/en/newsroom/press-releases/2026-10-19-gartner-it-symposium-xpo-keynote-release-2026) — Gartner · 19/out/2026 (71% esperam implantar IA agêntica em 12 meses; 21% têm governança de IA agêntica)
- [Only 13% of CIOs Say Their Enterprise Has Realized Significant or Transformational Value from AI](https://www.gartner.com/en/newsroom/press-releases/2026-10-19-gartner-survey-finds-only-13-percent-of-cios-say-their-enterprise-has-realized-significant-or-transformational-value-from-ai) — Gartner · CIO Agenda 2027 · 19/out/2026 · n = 2.002
- [Top Strategic Technology Trends for 2027](https://www.gartner.com/en/newsroom/press-releases/2026-10-20-gartner-identifies-the-top-strategic-technology-trends-for-2027) — Gartner · 20/out/2026 (até 2028, 25% das violações ligadas a abuso de agentes de IA)
- [The State of AI: Global Survey 2026](https://www.mckinsey.com/capabilities/quantumblack/our-insights/the-state-of-ai) — McKinsey · 25/ago/2026 · n = 1.719 (40% das empresas acima de US$ 1 bi escalam agentes; eram 27%)
- [Predictions 2027: The Pursuit And Peril Of Control](https://www.forrester.com/blogs/predictions-2027-the-pursuit-and-peril-of-control/) — Forrester · 21/out/2026
- [Stanford's century-long AI study (AI100 2026)](https://www.theregister.com/ai-and-ml/2026/11/10/stanfords-century-long-ai-study-admits-its-already-out-of-date/5308574) — The Register sobre o relatório AI100 de Stanford · 10/nov/2026
- [Fundamentals of Software Architecture](https://www.oreilly.com/library/view/fundamentals-of-software/9781492043447/) — Mark Richards & Neal Ford · O’Reilly · 2020 (primeira lei: tudo em arquitetura de software é um tradeoff)

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

## Cases da indústria (slides 03–04)

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


As configurações de gateway mostradas nos slides são **ilustrativas**: explicam o padrão e não descrevem a sintaxe de nenhum produto.
