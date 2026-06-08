---
title: "Programação — Índice"
date: 2026-05-16
area: "Programação e Engenharia de Software"
tags: [conhecimento, index, programacao, engenharia-de-software]
aliases: ["Sumário de Programação", "Software Engineering Index"]
related: ["04-Conhecimentos/07-Humanidades/Computacao/INDEX", "04-Conhecimentos/07-Humanidades/INDEX"]
---

# Índice — Programação e Engenharia de Software

## Área do Conhecimento
**Programação e Engenharia de Software** — princípios, práticas e ferramentas para projetar, construir, testar, entregar e manter sistemas de software de alta qualidade com segurança e eficiência.

## Notas nesta pasta

| # | Nota | Descrição |
|---|------|-----------|
| 1 | [[04-Conhecimentos/07-Humanidades/Programacao/Paradigmas-de-Programacao]] | Paradigmas de programação: imperativo, orientado a objetos, funcional, lógico, concorrente. Implementações em Python, TypeScript, Haskell, Prolog. Fundamentos de type systems (static vs dynamic, nominal vs structural, duck typing, Generics, ADTs). |

| 2 | [[04-Conhecimentos/07-Humanidades/Programacao/Arquitetura-de-Software]] | Padrões arquiteturais: MVC, Clean Architecture, Hexagonal Architecture, CQRS, Event Sourcing, Microservices, Monolith Modular. SOLID, coupling e cohesion, trade-offs arquiteturais, Documentação com C4 Model e ADRs. |

| 3 | [[04-Conhecimentos/07-Humanidades/Programacao/Design-Patterns]] | Padrões GoF (Creacionais, Estruturais, Comportamentais), padrões enterprise (PoEAA — Martin Fowler), padrões funcionais (Monad, Functor, Immutability). Implementações em Python e TypeScript, when to use vs when to avoid. |

| 4 | [[04-Conhecimentos/07-Humanidades/Programacao/APIs-e-Integracoes]] | Design de APIs RESTful, GraphQL, gRPC, WebSockets, webhooks. Versionamento, documentação (OpenAPI/Swagger), testes de API, integração com sistemas externos, message brokers (RabbitMQ, Kafka). |

| 5 | [[04-Conhecimentos/07-Humanidades/Programacao/Banco-de-Dados]] | Bancos relacionais (SQL, normalização, índices, transactions, ACID), NoSQL (documentos, key-value, grafos, colunas), ORMs vs raw SQL, migrations, query optimization, sharding, replication, CAP theorem. |

| 6 | [[04-Conhecimentos/07-Humanidades/Programacao/Testes-de-Software]] | Pirâmide de testes: unitários, integração, E2E. TDD, BDD, mocks/stubs/fakes, cobertura, property-based testing, testes de mutação, testes de carga (k6, locust), CI integrado. |

| 7 | [[04-Conhecimentos/07-Humanidades/Programacao/Performance-e-Otimizacao]] | Profiling, benchmark, otimização de CPU e memória, caching (Redis, CDN), lazy loading, code splitting, banco de dados (query optimization, índices), latência de rede, bottlenecks em sistemas distribuídos. |

| 8 | [[04-Conhecimentos/07-Humanidades/Programacao/Concorrencia-e-Paralelismo]] | Threads, async/await, corrotinas, workers, locks, race conditions, deadlocks, starvation. Modelos: actor (Erlang/Akka), CSP (Go), STM. GIL em Python, event loop em JS, goroutines em Go. |

| 9 | [[04-Conhecimentos/07-Humanidades/Programacao/DevOps-e-Infra]] | CI/CD (GitHub Actions, GitLab CI), Docker (multi-stage builds, compose), Kubernetes (pods, deployments, services, Helm), Cloud (AWS, GCP, Azure), IaC (Terraform, Pulumi, Ansible), Observabilidade (Prometheus, Grafana, OpenTelemetry, ELK/Loki), FinOps, SRE. |

| 10 | [[04-Conhecimentos/07-Humanidades/Programacao/Seguranca]] | OWASP Top 10, autenticação (bcrypt, Argon2, MFA), autorização (RBAC, ABAC, OPA), criptografia (AES, RSA, ECC, TLS), secure coding (input validation, prepared statements, XSS prevention), secret management (Vault), SCA/SBOM, API security (JWT, rate limiting, CORS). |

## Rota de Estudos Sugerida

### Trilha 1: Fundamentos de Programação
1. **Paradigmas-de-Programacao** — bases: POO → funcional → type systems
2. **Arquitetura-de-Software** — SOLID, Clean Architecture, C4
3. **Design-Patterns** — GoF + PoEAA + padrões funcionais
4. **APIs-e-Integracoes** — REST → GraphQL → gRPC → mensageria

### Trilha 2: Qualidade e Confiabilidade
1. **Testes-de-Software** — pirâmide, TDD, cobertura, mutantes
2. **Banco-de-Dados** — modelagem, índices, transactions, CAP
3. **Performance-e-Otimizacao** — profiling, caching, otimização
4. **Concorrencia-e-Paralelismo** — threads, async, locks, race conditions

### Trilha 3: Operações e Segurança
1. **DevOps-e-Infra** — CI/CD → Docker → K8s → Cloud → IaC → Observabilidade
2. **Seguranca** — OWASP → Auth → Crypto → Secure Coding → API Security
3. **Performance-e-Otimizacao** (revisitar com foco em produção)
4. **Concorrencia-e-Paralelismo** (revisitar com foco em sistemas distribuídos)

## Perguntas Transversais em Engenharia de Software

1. Como equilibrar velocidade de entrega com qualidade e segurança?
2. Quando um monolito é melhor que microsserviços (e vice-versa)?
3. Como projetar sistemas que evoluem sem reescritas catastróficas?
4. Qual o nível certo de abstração para cada camada do sistema?
5. Como garantir que o software faz o que o usuário precisa (não apenas o que foi especificado)?
6. Como medir e melhorar a produtividade de times de engenharia?
7. Quando dívida técnica deve ser paga vs. aceita como investimento?
8. Como projetar sistemas resilientes a falhas de rede, hardware e dependências externas?
9. Qual o trade-off entre acoplamento e performance em sistemas distribuídos?
10. Como garantir que mudanças não quebrem comportamento existente (regressão)?

## Referências Canônicas

| Livro | Autor(es) | Área |
|-------|-----------|------|
| *Code Complete* (2ª ed., 2004) | Steve McConnell | Construção de software |
| *The Pragmatic Programmer* (20th Anniversary, 2019) | Hunt & Thomas | Práticas de programação |
| *Clean Code* (2008) | Robert C. Martin | Código legível e sustentável |
| *Clean Architecture* (2017) | Robert C. Martin | Arquitetura de software |
| *Design Patterns* (GoF, 1994) | Gamma, Helm, Johnson, Vlissides | Padrões de projeto |
| *Patterns of Enterprise Application Architecture* (2002) | Martin Fowler | Padrões enterprise |
| *Refactoring* (2ª ed., 2018) | Martin Fowler | Melhoria de código existente |
| *Working Effectively with Legacy Code* (2004) | Michael Feathers | Código legado |
| *Domain-Driven Design* (2003) | Eric Evans | Modelagem de domínio |
| *The Mythical Man-Month* (1975/1995) | Frederick Brooks | Gerenciamento de projetos |
| *Peopleware* (3ª ed., 2013) | DeMarco & Lister | Fator humano em projetos |
| *The DevOps Handbook* (2016) | Kim, Humble, Debois, Willis | DevOps e entrega contínua |
| *Site Reliability Engineering* (2016) | Beyer et al. (Google) | Engenharia de confiabilidade |
| *Building Microservices* (2ª ed., 2021) | Sam Newman | Microsserviços |
| *Designing Data-Intensive Applications* (2017) | Martin Kleppmann | Sistemas distribuídos |
| *Security Engineering* (2ª ed., 2008) | Ross Anderson | Segurança de sistemas |

## Tags para Navegação

`#programacao` `#engenharia-de-software` `#arquitetura` `#padroes-de-projeto` `#testes` `#devops` `#seguranca` `#banco-de-dados` `#apis` `#performance` `#concorrencia`
