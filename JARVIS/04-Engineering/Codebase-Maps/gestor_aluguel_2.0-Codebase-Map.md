---
title: "gestor_aluguel_2.0 Codebase Map"
description: "Mapa RAG-friendly do gestor_aluguel_2.0 para agentes de programacao."
created: 2026-05-08
updated: 2026-05-08
type: codebase-map
project: gestor_aluguel_2.0
domain: engineering
language_primary: TypeScript
language_secondary: SQL
code_root: "D:/Documents/GitHub/gestor_aluguel_2.0"
vault_sources:
  - "Projetos/01-Ativos/Privados/gestor_aluguel_2.0.md"
  - "Projetos/03-Estudos/EstudosPesquisas/gestor_aluguel_2.0.md"
confidence: vault-notes-only
tags:
  - gestor-aluguel
  - nextjs
  - prisma
  - multi-tenant
  - saas
  - rag
  - codebase-map
---

# gestor_aluguel_2.0 Codebase Map

## One-liner

gestor_aluguel_2.0 e um SaaS imobiliario multi-tenant em Next.js 15 com Prisma/Postgres, contratos, financeiro, portal do inquilino, integracoes de pagamento/mensagem e IA para risco de inadimplencia.

## Fontes locais relevantes

- Nota de projeto: [[Projetos/01-Ativos/Privados/gestor_aluguel_2.0]]
- Nota de evolucao: [[Projetos/03-Estudos/EstudosPesquisas/gestor_aluguel_2.0]]
- Cheat sheets relacionados: [[JARVIS/04-Engineering/Wiki/CheatSheets/Next.js]], [[JARVIS/04-Engineering/Wiki/CheatSheets/Prisma]]
- Observacao: nesta rodada nao houve leitura do codigo real de `D:/Documents/GitHub/gestor_aluguel_2.0`; este mapa consolida o que ja esta no vault.

## Stack documentada

| Camada | Tecnologia citada | Funcao provavel |
|---|---|---|
| App | Next.js 15 App Router | Interface SaaS e API routes/server actions. |
| Linguagem | TypeScript | Tipagem de dominio, UI e backend. |
| ORM | Prisma com 43+ models | Modelo multi-tenant e regras de persistencia. |
| Banco | Postgres/Neon planejado | Dados principais, auditoria e financeiro. |
| Auth | Clerk com MFA/TOTP planejado | Identidade, organizacoes, seguranca. |
| IA | Gemini, possivel Ollama local | Analise de risco de inadimplencia/predicao financeira. |
| Pagamentos | Asaas sandbox e Stripe fallback | Cobranca, boletos, webhooks e reconciliacao. |
| Mensageria | WhatsApp WAHA + n8n | Notificacoes e automacoes via webhook. |
| Editor | TipTap/Yjs | Contratos dinamicos e colaborativos. |
| Seguranca | Audit logs e rate limiting | Governanca e protecao de operacoes sensiveis. |

## Dominios principais

- Imoveis, unidades, proprietarios e inquilinos.
- Contratos, renovacoes, documentos e assinaturas.
- Cobrancas, pagamentos, inadimplencia, repasses e conciliacao.
- Portal do inquilino e comunicacoes via WhatsApp.
- Multi-tenant: organizacoes, usuarios, permissoes e isolamento de dados.
- Auditoria: logs de eventos, alteracoes financeiras e operacoes administrativas.
- IA: classificacao de risco, alertas e previsao financeira.

## Estrutura esperada em um Next.js SaaS

| Caminho esperado | Papel para agentes |
|---|---|
| `app/` ou `src/app/` | Rotas App Router, layouts e server components. |
| `components/` | UI reutilizavel, tabelas, formularios e dialogs. |
| `lib/` | Clientes, helpers, auth, rate limit, AI e integracoes. |
| `prisma/schema.prisma` | Fonte critica de verdade do dominio. |
| `prisma/migrations/` | Historico de schema; nao editar manualmente sem plano. |
| `src/lib/ai/` | Local citado para substituir Gemini por Ollama. |
| `middleware.ts` | Auth, tenant routing, rate limit ou i18n. |
| `.env` | Segredos de banco, auth e pagamentos; nao abrir nem copiar. |

## Modelo mental para agentes

1. Usuario autenticado pertence a um tenant/organizacao.
2. Todas as queries de dominio precisam carregar tenant scope.
3. Financeiro depende de contratos, imoveis, inquilinos e agenda de cobranca.
4. Webhooks de Asaas/Stripe/n8n devem ser idempotentes.
5. IA deve ser assistiva, com explicacao e fallback manual para decisoes financeiras.
6. Audit logs devem registrar operacoes criticas: pagamento, exclusao, alteracao contratual, permissao.

## Areas que pedem cuidado

- Multi-tenancy: qualquer query sem `tenantId` ou escopo equivalente e risco alto.
- Prisma migrations: o vault cita projeto bloqueado por migrations em outro dashboard; validar estado antes de alterar schema.
- Pagamentos: webhooks precisam assinatura, idempotencia e reconciliacao.
- Auth/MFA: nao enfraquecer middleware ou server-side checks por conveniencia.
- Contratos com TipTap/Yjs podem ter estado colaborativo dificil de migrar.
- IA de risco financeiro nao deve tomar acao automatica sem confirmacao e trilha de auditoria.

## Proximos probes seguros

- Rodar `rg --files` no projeto real e localizar `prisma/schema.prisma`, `app/`, `src/`, `middleware.ts`, `src/lib/ai`.
- Ler README, `package.json`, `prisma/schema.prisma` e docs de deploy antes de executar.
- Mapear modelos Prisma por dominio e marcar quais tem `tenantId`.
- Mapear webhooks com `rg -n "webhook|asaas|stripe|waha|n8n"`.
- Mapear autenticacao com `rg -n "clerk|auth|session|tenant|organization|mfa|totp"`.
- Mapear IA com `rg -n "gemini|ollama|risk|inadimpl|prediction|ai"`.

## Tarefas provaveis para agentes

- Corrigir migrations Prisma e documentar fluxo `dev`, `deploy` e rollback.
- Implementar testes de tenant isolation.
- Criar camada de repositorio ou helpers para impor tenant scope.
- Stabilizar sandbox de pagamentos com webhooks idempotentes.
- Criar provider de IA substituivel: Gemini remoto, Ollama local e mock de teste.
- Preparar deploy Vercel + Neon com variaveis documentadas sem expor segredos.

## Perguntas abertas

- Clerk ja esta integrado ou ainda e meta de 90 dias?
- Asaas e Stripe coexistem ou Stripe e apenas fallback de teste?
- O Prisma schema atual tem tenant scope em todos os modelos financeiros?
- O bloqueio de migrations ainda existe no codigo real?

[[JARVIS/04-Engineering/Codebase-Maps/INDEX|← Voltar ao índice de Codebase-Maps]]
