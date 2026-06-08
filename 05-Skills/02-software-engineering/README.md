---
tags: [skills, skills-eng, hub, index]
updated: 2026-06-08
title: "Fullstack Skills"
date: 2026-04-27
---

# Fullstack Skills

Hub central para desenvolvimento fullstack com foco em IA, automacao e projetos praticos. Este diretorio reune pads e tecnicas para backend, frontend e banco de dados, com exemplos prontos para uso em assistentes de codigo e agentes de IA como o JARVIS.

## Taxonomia de Habilidades Fullstack

### Por Camada

| Camada | Skill | Tecnologias | Nivel |
|--------|-------|------------|-------|
| Apresentacao | [[frontend|Frontend]] | React, Vue, Tailwind, Web Components | Intermediario |
| Logica | [[backend|Backend]] | FastAPI, Express, Pydantic, JWT | Avancado |
| Persistencia | [[database|Database]] | PostgreSQL, MongoDB, Prisma, Alembic | Intermediario |
| Infraestrutura | [[05-Skills/03-infrastructure-mcp/mcp-servers|MCP Servers]] | Docker, K8s, MCP Protocol | Intermediario |

### Por Competencia

```python
SKILL_MATRIX = {
    "backend": {
        "nivel": 4,
        "descricao": "APIs REST/GraphQL, autenticacao, filas, cache",
        "framework_principal": "FastAPI",
        "anos_experiencia": 3
    },
    "frontend": {
        "nivel": 3,
        "descricao": "Componentes reativos, estado global, testes E2E",
        "framework_principal": "React",
        "anos_experiencia": 3
    },
    "database": {
        "nivel": 3,
        "descricao": "Modelagem, indices, migracoes, otimizacao",
        "framework_principal": "PostgreSQL + Prisma",
        "anos_experiencia": 4
    }
}
```

## Indice de Conteudo Detalhado

### [[backend|Backend Skills]]
- Padroes FastAPI: injecao de dependencia, middlewares, tratamento de erros
- Fluxos de autenticacao: JWT, OAuth2, hashing de senhas
- Validacao com Pydantic: schemas, tipos, validacao customizada
- Testes de API com TestClient e pytest
- Estrutura de projeto: services, repositories, schemas, endpoints

### [[frontend|Frontend Skills]]
- Padroes de componentes React: hooks, render props, composicao
- Gerenciamento de estado: Zustand, Context API, Redux
- Frameworks Vue: composables, Pinia, Vue Router
- Estrategias de teste: Vitest, Testing Library, Playwright
- Acessibilidade e performance

### [[database|Database Skills]]
- Padroes de migracao: Alembic (Python), Prisma (Node.js)
- Otimizacao de consultas: EXPLAIN ANALYZE, indices compostos
- Estrategias de indices: B-tree, GIN, HNSW, GiST
- Pool de conexoes: SQLAlchemy async, psycopg2 pool
- MongoDB: pipelines de agregacao, indices textuais

## Prompts de Exemplo para Agentes

### Prompt para gerar uma API completa

```
Crie uma API FastAPI com as seguintes caracteristicas:
- Modelo User com campos: id, nome, email, criado_em
- CRUD completo com validacao Pydantic
- Autenticacao JWT com OAuth2
- Tratamento de erros centralizado
- Testes com pytest
- Middleware de logging e auditoria

Consulte [[backend]] para pads e exemplos.
```

### Prompt para criar um componente React

```
Gere um componente React TypeScript que:
- Exiba uma lista de usuarios com loading e erro
- Tenha busca e filtragem por nome
- Use Zustand para estado global
- Seja testado com Testing Library
- Siga padroes de acessibilidade WCAG

Consulte [[frontend]] para pads.
```

## Arquitetura Tipica de Projeto

```
project/
  backend/
    app/
      core/         config, security, exceptions
      models/       SQLAlchemy models
      schemas/      Pydantic schemas
      services/     business logic
      api/v1/       route handlers
      main.py       FastAPI app
    tests/          pytest tests
    alembic/        database migrations
    requirements.txt
  frontend/
    src/
      components/   React components
      hooks/        custom hooks
      stores/       Zustand stores
      pages/        route pages
      test/        Vitest tests
    package.json
    tailwind.config.js
  docker-compose.yml
  Makefile
```

## Como Usar Este Hub

1. **Identifique o dominio** do seu trabalho (backend, frontend ou database)
2. **Navegue ate o arquivo** especifico usando os links da taxonomia
3. **Use os prompts** como ponto de partida para gerar codigo
4. **Adapte os exemplos** ao contexto do seu projeto
5. **Combine skills** — por exemplo, backend + database para uma API completa
6. **Integre com MCP** usando [[05-Skills/03-infrastructure-mcp/mcp-servers|infraestrutura MCP]]

## Boas Praticas Transversais

- **Separacao de responsabilidades**: validacao, logica de negocio e persistencia em camadas distintas
- **Contratos tipados**: DTOs ou schemas (Pydantic/TypeScript) para contratos claros entre camadas
- **Tratamento de erros**: respostas semanticas e consistentes em toda a API
- **Documentacao**: endpoints documentados via OpenAPI/Swagger
- **Testes**: TDD ou test-first sempre que possivel
- **Versionamento de API**: prefira `/api/v1/`, `/api/v2/` para mudanças que quebram compatibilidade

## Metricas de Qualidade

```python
QUALITY_METRICS = {
    "api": {
        "cobertura_testes": "> 80%",
        "latencia_p95": "< 200ms",
        "taxa_erro": "< 0.1%"
    },
    "frontend": {
        "cobertura_testes": "> 60%",
        "lighthouse_performance": "> 90",
        "acessibilidade": "WCAG AA"
    },
    "database": {
        "slow_queries": "< 1%",
        "conexoes_ativas": "< 80% pool",
        "hit_rate_cache": "> 90%"
    }
}
```

## Referencias Relacionadas

- [[05-Skills/README|Skills — Taxonomia Pessoal]] — Hub central de skills
- [[05-Skills/ai/MLOps|MLOps]] — Pipelines de deploy e monitoramento de modelos
- [[05-Skills/devops/Observabilidade|Observabilidade]] — Metricas, logs e tracing para servicos
- [[05-Skills/04-knowledge-systems/INDEX|Knowledge Systems]] — RAG e memoria para agentes de IA
- [[05-Skills/03-infrastructure-mcp/mcp-servers|MCP Servers]] — Infraestrutura para agentes
- [[advanced-backend-architecture|Arquitetura Avancada de Backend]] — Padroes para sistemas complexos
- [[05-Skills/03-infrastructure-mcp/advanced-mcp-integrations|MCP Avancado]] — Orquestracao multicamada
