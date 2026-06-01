---
title: "🖥️ Fullstack Agent Capabilities — Habilidades de Programação para Agentes IA"
tags: [skills, fullstack, agent-capabilities, programacao, backend, frontend, database, devops, architecture]
date: 2026-06-01
updated: 2026-06-01
category: skill
aliases: ["Fullstack Agent Skills", "Programador Fullstack IA", "Agente Programador Completo"]
related: ["skills/02-software-engineering/README", "skills/AGENT-RESEARCH-CAPABILITIES", "skills/01-agentic-intelligence/README"]
---

# 🖥️ Fullstack Agent Capabilities — Stack Completo para Agentes Programadores

Matriz de habilidades de programação fullstack que um agente IA deve dominar para atuar com máxima eficácia em desenvolvimento de software. Cobre todo o ciclo: ideação → arquitetura → implementação → teste → deploy → monitoramento.

---

## 🏗️ 1. Stack Técnico Completo

### 1.1 Backend

| Tecnologia | Nível Domínio | Frameworks | Padrões |
|-----------|--------------|------------|---------|
| **Python** | Expert | FastAPI, Flask, Django, Litestar | REST, GraphQL, gRPC, WebSocket |
| **TypeScript/Node** | Avançado | Express, NestJS, Hono, Elysia | REST, GraphQL, tRPC |
| **Go** | Intermediário | Gin, Fiber, Chi, Echo | REST, gRPC, microserviços |
| **Rust** | Básico | Axum, Actix, Rocket | Performance crítica |
| **Java/Kotlin** | Básico | Spring Boot, Quarkus, Micronaut | Enterprise, microsserviços |

**Habilidades Críticas:**
```
□ API Design (RESTful, GraphQL schemas, OpenAPI/Swagger)
□ Auth (JWT, OAuth2, OIDC, RBAC, API keys, session mgmt)
□ Rate limiting, throttling, backpressure
□ Middleware (logging, cors, error handling, request validation)
□ Background tasks (Celery, BullMQ, message queues)
□ WebSockets, SSE, real-time communication
□ Caching (Redis, in-memory, CDN, HTTP caching)
□ File upload/download, streaming
□ Error handling + structured error responses
□ API versioning (URL, header, content negotiation)
```

### 1.2 Frontend

| Tecnologia | Nível | Frameworks | Estilo |
|-----------|-------|------------|--------|
| **React/Next.js** | Expert | Next.js, Remix, React Router | SSR, SSG, ISR, SPA, RSC |
| **Vue/Nuxt** | Intermediário | Nuxt 3, Pinia | SSR, SSG, SPA |
| **TypeScript** | Expert | Zod, tRPC, TanStack Query | Type-safe end-to-end |
| **CSS/Tailwind** | Avançado | Tailwind, CSS Modules, Styled Components | Utility-first, design system |

**Habilidades Críticas:**
```
□ Component architecture (composition, compound, HOCs, render props)
□ State management (React Context, Zustand, Redux, Pinia)
□ Data fetching (SWR, TanStack Query, Apollo)
□ Forms (React Hook Form, Zod validation)
□ Routing (dynamic, nested, protected, parallel)
□ Performance (code splitting, lazy loading, memoization, virtualization)
□ Acessibilidade (WCAG 2.1 AA, ARIA, keyboard nav)
□ Responsividade (mobile-first, breakpoints, container queries)
□ Testing (Jest, Playwright, Cypress, Testing Library)
□ Bundle optimization (tree shaking, code splitting, image optimization)
```

### 1.3 Database & Storage

| Tipo | Tecnologias | Caso de Uso |
|------|-----------|-------------|
| **Relacional** | PostgreSQL, MySQL, SQLite, CockroachDB | Dados estruturados, transações ACID |
| **Document** | MongoDB, Firebase, CouchDB | Dados semi-estruturados, schemas flexíveis |
| **Key-Value** | Redis, Valkey, DynamoDB | Cache, sessões, filas, real-time |
| **Vector** | pgvector, ChromaDB, Qdrant, Pinecone | Embeddings, RAG, similaridade semântica |
| **Search** | Elasticsearch, Meilisearch, Typesense | Busca full-text, faceted search |
| **Time Series** | InfluxDB, TimescaleDB, ClickHouse | Métricas, logs, séries temporais |
| **Graph** | Neo4j, Dgraph, ArangoDB | Relações complexas, grafos de conhecimento |
| **Object Storage** | S3, MinIO, R2 | Arquivos, imagens, backups, assets |

**Habilidades Críticas:**
```
□ Schema design (normalization, indexing strategies, migrations)
□ Query optimization (EXPLAIN ANALYZE, query plans, composite indexes)
□ Connection pooling (PgBouncer, connection limits)
□ Transactions + isolation levels + locking
□ Backup/restore strategies (WAL, point-in-time recovery)
□ Replication (read replicas, streaming replication, CDC)
□ Sharding + partitioning (horizontal/vertical)
□ Migration tools (Alembic, Prisma Migrate, Flyway)
□ ORM vs raw SQL tradeoffs (SQLAlchemy, Prisma, Drizzle, Knex)
□ Data validation + constraints (check, unique, foreign key)
```

### 1.4 DevOps & Infra

| Área | Tecnologias | Skills |
|------|-----------|--------|
| **Containers** | Docker, Podman, Compose | Dockerfile multi-stage, compose networking, volumes |
| **Orquestração** | Kubernetes, Nomad, Swarm | Pods, services, ingress, configmaps, Helm |
| **CI/CD** | GitHub Actions, GitLab CI, Jenkins | Pipelines, matrix builds, caching, secrets |
| **IaC** | Terraform, Pulumi, Ansible, CloudFormation | State management, modules, remote backends |
| **Observability** | Prometheus, Grafana, Loki, OpenTelemetry | Metrics, logs, traces, dashboards, alerting |
| **Cloud** | AWS, GCP, Azure, Cloudflare, Vercel | Compute, storage, networking, serverless, edge |

**Habilidades Críticas:**
```
□ Dockerfile optimization (multi-stage, slim images, layer caching)
□ Docker Compose for local dev (volumes, networks, env vars)
□ K8s manifests + Helm charts + Kustomize
□ CI pipeline design (test → lint → build → deploy → verify)
□ GitHub Actions workflows (matrix, reusable, composite actions)
□ Terraform modules + state management + remote backends
□ Monitoring stack setup (metrics + logs + traces + alerts)
□ Secret management (Vault, Doppler, GitHub Secrets, 1Password)
□ Disaster recovery + backup automation
□ Cost optimization (resource sizing, reserved instances, spot)
```

---

## 🧩 2. Architecture & Design Patterns

### 2.1 Arquiteturas que o Agente Deve Dominar

```
□ Monolith First → Modular Monolith → Microservices
□ Clean Architecture / Hexagonal / Onion / Ports & Adapters
□ Event-Driven Architecture (Event Bus, Event Sourcing, CQRS)
□ Message-Driven (RabbitMQ, Kafka, NATS, Redis Streams)
□ Serverless (Lambda, Cloud Functions, Edge Functions)
□ Microfrontends (Module Federation, iframe, Web Components)
□ BFF (Backend for Frontend) pattern
□ Saga Pattern (choreography vs orchestration)
□ Strangler Fig Pattern (migração incremental)
□ Sidecar Pattern (service mesh, logging, proxy)
□ Circuit Breaker + Retry + Timeout patterns
□ Bulkhead + Rate Limiter patterns
```

### 2.2 Design Patterns Essenciais

```yaml
creational:
  - Factory / Abstract Factory
  - Builder
  - Singleton (cauteloso)
  - Prototype

structural:
  - Adapter / Facade / Proxy
  - Decorator
  - Composite
  - Bridge

behavioral:
  - Strategy
  - Observer / Event Emitter
  - Command
  - Chain of Responsibility
  - State
  - Mediator

architectural:
  - Repository
  - Unit of Work
  - Service Layer
  - Factory Method (in DI)
  - DTO / ViewModel
```

---

## 🧪 3. Testing Matrix

| Tipo | Foco | Ferramentas | Cobertura Alvo |
|------|------|-----------|---------------|
| **Unit** | Funções individuais, componentes isolados | pytest, Vitest, Jest | > 80% |
| **Integration** | Interação entre módulos, DB, API | pytest + httpx, Supertest | > 60% |
| **E2E** | Fluxo completo do usuário | Playwright, Cypress | Crítico: 100% |
| **API** | Contratos de API, schemas | Postman/Schemathesis, Zod | > 90% |
| **Snapshot** | UI regression | Vitest Snapshot, Storybook | Componentes base |
| **Property-based** | Propriedades invariantes | Hypothesis, fast-check | Lógicas complexas |
| **Performance** | Latência, throughput, memory | k6, autocannon, locust | SLA targets |
| **Security** | OWASP Top 10, auth, injection | OWASP ZAP, Semgrep | Zero critical |

**Workflow de Teste do Agente:**
```
1. TDD: Write test → Write code → Refactor
2. Para cada PR: Unit + Integration + API (CI gate)
3. Antes de deploy: E2E + Performance + Security
4. Em produção: Smoke tests + Canary + Rollback
```

---

## 🔄 4. Workflow de Desenvolvimento

### 4.1 Git Workflow

```yaml
branches:
  main: "produção (protegida)"
  develop: "integração"
  feat/*: "features novas"
  fix/*: "bug fixes"
  chore/*: "tarefas técnicas"

commit_pattern:
  type: feat|fix|chore|docs|refactor|test|perf|style
  format: "<type>(<scope>): <description>"
  body: "motivação + contexto"
  footer: "BREAKING CHANGE: ... | Closes #123"

code_review:
  checklist:
    - "Funciona? (testes passam)"
    - "É legível? (nomes claros, sem complexidade desnecessária)"
    - "É seguro? (entrada validada, sem injection)"
    - "É performático? (N+1 queries, tamanho de bundle)"
    - "Tem testes? (cobre o caso novo)"
    - "Documentação? (se mudou API ou comportamento)"
```

### 4.2 Prompt Template de Desenvolvimento

```yaml
task: implement
  - "<feature_description>"
tech_stack:
  backend: [Python, FastAPI, PostgreSQL, Redis]
  frontend: [Next.js, React, Tailwind, TypeScript]
arch: monolith-modular
constraints:
  - "TDD: escrever testes primeiro"
  - "Performance: < 200ms p95 nas APIs"
  - "Security: input validation + rate limiting"
output:
  - schema_prisma
  - api_router + handler
  - tests_unit + integration
  - frontend_component + page
  - migration_file
refs:
  - "[[skills/02-software-engineering/design-patterns]]"
  - "[[skills/02-software-engineering/api-design]]"
```

---

## 📊 5. Matriz de Proficiência

| Área | Nível | Critérios |
|------|-------|-----------|
| **Backend Python** | Expert | Cria APIs complexas, otimiza queries, modela DB, implementa cache, filas, async |
| **Backend JS/TS** | Avançado | NestJS/Express, tRPC, ORM, WebSockets, streaming |
| **Frontend React/Next** | Expert | Server Components, RSC, SSR/SSG/ISR, forms complexos, estado global |
| **Frontend CSS/UI** | Avançado | Design systems, Tailwind, animações, responsive complexo, acessibilidade |
| **Database SQL** | Expert | Schema design, query optimization, migrations, replication, sharding |
| **Database NoSQL** | Avançado | MongoDB aggregation, Redis patterns, vector search |
| **DevOps/Docker** | Avançado | Docker multi-stage, Compose, K8s básico, CI/CD |
| **Cloud** | Intermediário | AWS/GCP serviços core, serverless, storage, networking |
| **Testing** | Avançado | TDD, integration, e2e, performance, security |
| **Security** | Intermediário | OWASP, auth, input validation, secrets, dependency audit |
| **Performance** | Avançado | Profiling, caching, query optimization, bundle analysis, CDN |

---

## 🔗 Crosslinks

- [[skills/02-software-engineering/README]] — Engenharia de software fullstack
- [[skills/01-agentic-intelligence/README]] — Inteligência agentica
- [[skills/AGENT-RESEARCH-CAPABILITIES]] — Capacidades de pesquisa
- [[skills/02-software-engineering/design-patterns]] — Padrões de design
- [[skills/02-software-engineering/api-design]] — Design de API
- [[skills/devops/README]] — DevOps e infraestrutura
- [[skills/frontend/README]] — Frontend
- [[Knowledge-Base/DATA-TOKEN-GOVERNANCE]] — Governança de dados e tokens
- [[INDEX]]
