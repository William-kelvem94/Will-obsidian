---
tags: [software-engineering, index, hub, skills-eng, taxonomy]
updated: 2026-06-10
title: "Software Engineering & Architecture - Index"
date: 2026-06-01
---

# Software Engineering & Architecture

Hub central da engenharia de software do JARVIS. Este dominio cobre desde fundamentos de desenvolvimento full-stack ate arquitetura de sistemas distribuidos em escala de producao. Cada nota e autocontida, com exemplos praticos e referencias cruzadas para navegacao eficiente.

## Taxonomia Completa

```
02-software-engineering/
├── INDEX.md ....................... Hub central (voce esta aqui)
├── backend.md ..................... Fundamentos de backend (FastAPI, Node.js)
├── frontend.md .................... Fundamentos de frontend (Next.js, React)
├── database.md .................... Bancos de dados relacionais e NoSQL
├── api-design.md .................. Design de APIs (REST, GraphQL, gRPC)
├── performance.md ................. Engenharia de performance
├── advanced-backend-architecture.md  Arquitetura backend avancada
├── seguranca/
│   ├── INDEX.md ................... Hub de seguranca
│   ├── owasp-top-10.md ............ OWASP Top 10 2026
│   ├── prompt-injection-defense.md  Defesas contra injecao de prompt
│   ├── secrets-management.md ...... Gerenciamento de segredos
│   ├── secure-coding.md ........... Codigo seguro (SAST, DAST)
│   └── supply-chain-security.md ... Seguranca da cadeia de suprimentos
├── testing/
│   └── SKILL.md ................... Estrategias de teste full-stack
└── Bancos-de-Dados/
    └── PostgreSQL-Advanced.md ..... PostgreSQL avancado + pgvector
```

## Notas Ativas

### [[backend|Backend Fundamentals]]
Fundamentos de desenvolvimento backend com Python (FastAPI) e Node.js (Express/NestJS). Cobre roteamento, middleware, validacao de entrada, tratamento de erros, logging estruturado, e padroes de organizacao de codigo (controllers, services, repositories). Inclue exemplos de autenticacao JWT, upload de arquivos, e integracao com bancos de dados.

### [[frontend|Frontend Fundamentals]]
Desenvolvimento frontend moderno com Next.js, React e TypeScript. Aborda Server Components, Server Actions, roteamento por App Router, gestao de estado (Zustand, React Query), otimizacao de performance (lazy loading, code splitting), e acessibilidade. Inclui padroes de composicao de componentes e integracao com APIs backend.

### [[database|Database Fundamentals]]
Modelagem de dados, SQL avancado, e comparativo entre bancos relacionais (PostgreSQL, MySQL) e NoSQL (MongoDB, Redis, DynamoDB). Cobre indices, transacoes ACID, normalizacao, e padroes de migracao de schema. Base para entender escolhas arquiteturais de persistencia.

### [[api-design|API Design]]
Design de APIs com abordagem contract-first. Cobre OpenAPI 3.x, REST vs GraphQL vs gRPC, versionamento, padroes de erro (RFC 7807), rate limiting, paginacao, autenticacao (OAuth2, JWT, API keys), idempotencia, e documentacao-as-code. Referencia para construir APIs consistentes e bem documentadas.

### [[performance|Performance Engineering]]
Engenharia de performance full-stack. Cobre profiling (cProfile, Chrome DevTools), otimizacao de queries, caching strategies (Redis, CDN), load testing (k6, Locust), monitoring (OpenTelemetry, Datadog), e budgets de performance. Guia para identificar e resolver gargalos em producao.

### [[advanced-backend-architecture|Advanced Backend Architecture]]
Arquitetura backend avancada para sistemas distribuidos. Cobre microservices vs monolitos, event-driven architecture (RabbitMQ, Kafka, Redis Streams), CQRS e Event Sourcing, API Gateways, Service Mesh, estrategias de cache multi-camada, observabilidade (Prometheus, OpenTelemetry), filas de tarefas (Celery), e padroes de resiliencia (Circuit Breaker, Bulkhead).

### [[Bancos-de-Dados/PostgreSQL-Advanced|PostgreSQL Avancado]]
Tratado exaustivo sobre PostgreSQL com extensao pgvector para IA. Cobre arquitetura interna (MVCC, WAL, Postmaster), indexacao algoritmica (B-Tree, GIN, BRIN, HNSW), CTEs recursivas, Window Functions, Full Text Search, JSONB, e tuning avancado (EXPLAIN ANALYZE, work_mem). Referencia para RAG e buscas vetoriais.

### [[seguranca/INDEX|Seguranca]]
Hub de seguranca aplicacional. Cobre OWASP Top 10, defesas contra prompt injection, gerenciamento de segredos (Vault, SOPS), secure coding (SAST/DAST), e seguranca da cadeia de suprimentos (SBOM, supply chain attacks). Essencial para hardening de sistemas em producao.

### [[testing/SKILL|Testing Architecture]]
Estrategias de teste full-stack. Cobre piramide de testes, pytest (Python), Jest (TypeScript), Playwright (E2E), fixtures, factories, BDD, e CI/CD com GitHub Actions. Playbook de qualidade para o ecossistema JARVIS.

## Guia de Navegacao

### Iniciante -> Avancado

```
Iniciante:
  backend.md -> database.md -> frontend.md
     |              |              |
     v              v              v
Intermediario:
  api-design.md -> testing/SKILL.md -> seguranca/INDEX.md
     |                    |                  |
     v                    v                  v
Avancado:
  advanced-backend-architecture.md -> Bancos-de-Dados/PostgreSQL-Advanced.md
     |
     v
Especialista:
  performance.md + seguranca/supply-chain-security.md
```

### Por Trilha de Aprendizado

| Trilha | Sequencia | Objetivo |
|---|---|---|
| Backend Developer | [[backend]] -> [[database]] -> [[api-design]] -> [[advanced-backend-architecture]] | Construir APIs robustas |
| Full-Stack Developer | [[backend]] -> [[frontend]] -> [[database]] -> [[testing/SKILL]] | Desenvolver aplicacoes completas |
| Data Engineer | [[database]] -> [[Bancos-de-Dados/PostgreSQL-Advanced]] -> [[performance]] | Otimizar camada de dados |
| Security Engineer | [[seguranca/INDEX]] -> [[seguranca/owasp-top-10]] -> [[seguranca/secure-coding]] -> [[seguranca/supply-chain-security]] | Hardening de sistemas |
| SRE / Platform | [[advanced-backend-architecture]] -> [[performance]] -> [[testing/SKILL]] -> [[seguranca/secrets-management]] | Operar em escala |
| AI Engineer | [[Bancos-de-Dados/PostgreSQL-Advanced]] -> [[advanced-backend-architecture]] -> [[seguranca/prompt-injection-defense]] | Sistemas de IA em producao |

## Referencias Cruzadas

### Outros Dominios de Skills

| Dominio | Notas Relevantes | Conexao |
|---|---|---|
| [[../01-agentic-intelligence/INDEX|Agentic Intelligence]] | Agentes autonomos, LLM orchestration | Backend de agentes usa padroes deste dominio |
| [[../03-infrastructure-mcp/INDEX|Infrastructure & MCP]] | MCP servers, monitoring, local LLM ops | Infraestrutura que suporta o software |
| [[../04-knowledge-systems/INDEX|Knowledge Systems]] | Obsidian vaults, RAG pipelines | Conhecimento gerado por este dominio |
| [[../devops/Observabilidade|Observabilidade]] | Logging, metrics, tracing | Complementa advanced-backend-architecture |
| [[../devops/ci-cd|CI/CD]] | Pipelines de deploy | Integra com testing/SKILL.md |
| [[../data-engineering/INDEX|Data Engineering]] | ETL, streaming, data pipelines | Usa database.md e performance.md |
| [[../frontend/INDEX|Frontend Skills]] | React patterns, state management | Complementa frontend.md |

### Conhecimento Geral

| Nota | Conexao |
|---|---|
| [[../../../04-Conhecimentos/07-Humanidades/Computacao/Algoritmos-e-Estruturas|Algoritmos e Estruturas]] | Base para decisoes de performance |
| [[../../../04-Conhecimentos/07-Humanidades/Computacao/Ciencia-da-Computacao|Ciencia da Computacao]] | Fundamentos teoricos |
| [[../../../04-Conhecimentos/07-Humanidades/Computacao/NLP-Fundamentos|NLP Fundamentos]] | Para integracao com IA |

## Principios de Engenharia

- **Composicao sobre heranca** — Sistemas modulares com interfaces bem definidas
- **Observabilidade primeiro** — Logs, metricas e tracing sao requisitos, nao opcionais
- **Resiliencia por design** — Circuit breakers, retries com backoff, bulkheads
- **Dados como produto** — Cada servico e dono dos seus dados e os expoe via API
- **Privacidade embedded** — Privacy by design em cada camada
- **Contract-first** — APIs definidas antes da implementacao (OpenAPI, protobuf)
- **Fail fast, recover faster** — Detecao rapida de falhas com recuperacao automatica

## Pre-requisitos Recomendados

- [[../../../04-Conhecimentos/07-Humanidades/Matematica/Algebra-Linear-Essencial|Algebra Linear Essencial]] — Para embeddings e operacoes vetoriais
- [[../../../04-Conhecimentos/07-Humanidades/Matematica/Probabilidade-e-Estatistica|Probabilidade e Estatistica]] — Para metricas, benchmarks e testes A/B
- [[../04-knowledge-systems/obsidian-neural-vault|Obsidian Neural Vault]] — Contexto dos sistemas sendo construidos
- [[../01-agentic-intelligence/agent-architectures|Agent Architectures]] — Para entender agentes que consomem estas APIs

## Como Usar Este Hub

1. **Identifique sua trilha** na tabela acima
2. **Siga a sequencia** de notas na ordem recomendada
3. **Use as referencias cruzadas** para aprofundar em topicos relacionados
4. **Consulte os principios** ao tomar decisoes arquiteturais
5. **Contribua** adicionando exemplos praticos e atualizando referencias

## Status do Dominio

| Area | Cobertura | Ultima Atualizacao |
|---|---|---|
| Backend | Completa | 2026-05-16 |
| Frontend | Completa | 2026-05-16 |
| Database | Completa | 2026-05-16 |
| API Design | Nova | 2026-05-16 |
| Performance | Nova | 2026-05-16 |
| Arquitetura Avancada | Completa | 2026-05-16 |
| PostgreSQL Avancado | Completa | 2026-05-16 |
| Seguranca | Completa | 2026-05-16 |
| Testing | Completa | 2026-05-16 |
