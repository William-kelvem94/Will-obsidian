---
title: "Arquitetura Web Moderna"
date: 2026-06-07
updated: 2026-06-07
type: guide
status: active
tags: [conhecimento-geral, engenharia-software, arquitetura, web, fullstack]
related: [[Docker-e-DevOps]], [[APIs-Backend-Banco]], [[../01-IA-e-Agentes/RAG-e-Memoria-para-Agentes]]
summary: "Mapa prático de arquitetura web moderna para projetar sistemas manuteníveis e fáceis de evoluir."
---

# Arquitetura Web Moderna

Arquitetura web moderna é a organização de frontend, backend, banco, autenticação, infraestrutura, logs e automação para entregar sistemas confiáveis.

## Camadas principais

| Camada | Função | Exemplos |
|---|---|---|
| Interface | interação com usuário | React, Next.js, Vue |
| API | comunicação entre cliente e servidor | REST, GraphQL, tRPC |
| Domínio | regras de negócio | serviços, casos de uso |
| Persistência | dados duráveis | PostgreSQL, MySQL, MongoDB |
| Infraestrutura | execução | Docker, VPS, cloud |
| Observabilidade | diagnóstico | logs, métricas, tracing |

## Princípios

### 1. Separar interface de regra de negócio

Frontend não deve guardar regra crítica. Regra importante fica no backend ou na camada de domínio.

### 2. API precisa ter contrato claro

Endpoints, payloads, erros e status precisam ser previsíveis.

### 3. Validação em múltiplas camadas

Validar no frontend melhora a experiência. Validar no backend mantém consistência.

### 4. Logs desde cedo

Logs bons reduzem tempo de debugging e ajudam a entender falhas reais.

## Arquitetura fullstack simples

```txt
Browser
  ↓
Frontend React ou Next
  ↓
API Backend
  ↓
Service Layer
  ↓
Repository ou ORM
  ↓
Database
```

## Decisões importantes

| Decisão | Melhor para simplicidade | Melhor para escala |
|---|---|---|
| Monolito ou microsserviço | monolito modular | microsserviços |
| REST ou GraphQL | REST | GraphQL |
| SQL ou NoSQL | SQL | depende do domínio |
| SSR ou SPA | SSR para conteúdo público | SPA para app interno |
| Docker local ou instalação direta | Docker | instalação direta só em casos pequenos |

## Estrutura recomendada

```txt
project/
├── apps/
│   ├── web/
│   └── api/
├── packages/
│   ├── shared/
│   └── config/
├── docker-compose.yml
├── README.md
└── docs/
```

## Qualidade mínima

Um projeto web saudável precisa ter README, `.env.example`, scripts de desenvolvimento, validação de dados, tratamento de erro, logs básicos, migrações de banco e decisões registradas.

## Erros comuns

- começar com arquitetura grande demais;
- colocar regra crítica no frontend;
- ignorar logs;
- não versionar migrações;
- não ter ambiente local reproduzível;
- criar abstrações antes da dor real;
- não documentar decisões.

## Checklist

- [ ] Qual problema o sistema resolve?
- [ ] Quais entidades principais existem?
- [ ] Quem são os usuários?
- [ ] Quais permissões existem?
- [ ] Como o sistema roda localmente?
- [ ] Como faz deploy?
- [ ] Como recuperar de erro?
- [ ] Como logs são acessados?
- [ ] Como novas pessoas entendem o projeto?

## Links internos

- [[Docker-e-DevOps]]
- [[APIs-Backend-Banco]]
- [[../08-Vida-Pratica/Produtividade/Decisao-e-Priorizacao]]
- [[../03-Dados-e-Analytics/Taxonomia-Metadados-e-Ontologia]]
