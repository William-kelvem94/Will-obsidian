---
title: "APIs, Backend e Banco de Dados"
date: 2026-06-07
updated: 2026-06-07
type: guide
status: active
tags: [conhecimento-geral, backend, api, banco-de-dados, engenharia-software]
related: [[Arquitetura-Web-Moderna]], [[Docker-e-DevOps]], [[../05-Dados/Taxonomia-Metadados-e-Ontologia]]
summary: "Guia prático sobre APIs, backend, modelagem de dados e persistência em sistemas web."
---

# APIs, Backend e Banco de Dados

Backend é a parte do sistema responsável por regras de negócio, persistência, validação, autenticação e integração com outros serviços. APIs são contratos de comunicação entre sistemas.

## Funções do backend

- receber requisições;
- validar dados;
- aplicar regras de negócio;
- consultar e gravar no banco;
- retornar respostas previsíveis;
- registrar logs;
- controlar permissões;
- integrar serviços externos.

## API boa

Uma API boa é previsível, documentada, consistente e fácil de testar.

## Padrões de endpoint

| Ação | Método comum | Exemplo |
|---|---|---|
| listar | GET | `/users` |
| buscar um item | GET | `/users/:id` |
| criar | POST | `/users` |
| atualizar tudo | PUT | `/users/:id` |
| atualizar parte | PATCH | `/users/:id` |
| remover | DELETE | `/users/:id` |

## Status HTTP comuns

| Código | Uso |
|---|---|
| 200 | sucesso com resposta |
| 201 | criado |
| 204 | sucesso sem corpo |
| 400 | requisição inválida |
| 401 | não autenticado |
| 403 | sem permissão |
| 404 | não encontrado |
| 409 | conflito |
| 422 | validação semântica |
| 500 | erro interno |

## Camadas recomendadas

```txt
Controller
  ↓
Service / Use Case
  ↓
Repository
  ↓
Database
```

## Banco de dados

### SQL

Bom para dados relacionais, transações e consistência.

Exemplos: PostgreSQL, MySQL, SQLite.

### NoSQL

Bom para documentos flexíveis, dados semi-estruturados e alguns cenários de escala horizontal.

Exemplos: MongoDB, DynamoDB.

## Modelagem de dados

Uma boa modelagem começa pelas entidades centrais.

Perguntas úteis:

- Quais objetos existem no domínio?
- Quem cria esses dados?
- Quem pode editar?
- O que precisa ser histórico?
- O que pode ser calculado?
- O que precisa ser auditável?
- Quais campos são obrigatórios?
- Quais relações existem?

## Migrações

Migração é a evolução versionada do banco. Ela evita alterações manuais invisíveis.

Boas práticas:

- versionar migrações;
- revisar impacto antes de aplicar;
- evitar apagar dados sem backup;
- manter ambiente local parecido com produção;
- documentar mudanças grandes.

## Erros comuns

- endpoints inconsistentes;
- respostas sem padrão;
- regras espalhadas em controllers;
- ausência de validação;
- banco sem migrações;
- nomes ruins de tabelas e campos;
- não pensar em permissões desde cedo;
- retornar dados demais sem necessidade.

## Checklist de backend

- [ ] API tem padrão de rotas?
- [ ] Erros seguem formato comum?
- [ ] Validação está clara?
- [ ] Regras ficam em services ou use cases?
- [ ] Banco tem migrações?
- [ ] Permissões foram pensadas?
- [ ] Logs ajudam a diagnosticar problemas?
- [ ] README explica setup?

## Links internos

- [[Arquitetura-Web-Moderna]]
- [[Docker-e-DevOps]]
- [[../05-Dados/Taxonomia-Metadados-e-Ontologia]]
- [[../01-IA/Token-Economy]]
