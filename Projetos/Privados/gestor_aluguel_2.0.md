---
title: "gestor_aluguel_2.0 (Clonado)"
source: "d:/Documents/GitHub/gestor_aluguel_2.0"
language: TypeScript
private: true
description: "Plataforma SaaS Imobiliária Enterprise: Next.js 15, Multi-tenant, AI-Driven."
updated: 2026-04-12
tags: [privados, nextjs, typescript, prisma, saas, ai]
---

# Gestor de Aluguel 2.0 🏠 [[../Projetos.md|Projetos]] [[GitHub-Completo]]

**Status**: 🚀 Produção / Estabilização
**Escala**: Enterprise Multi-tenant (43+ Models Prisma)

O projeto mais robusto do portfolio, focando em automação total do ciclo de vida imobiliário, desde o anúncio até a gestão de inadimplência assistida por IA.

## 🛠️ Enterprise Tech Stack
| Camada | Tecnologia |
|---|---|
| **Framework** | Next.js 15 (App Router) |
| **Linguagem** | TypeScript (Strict Mode) |
| **ORM / DB** | Prisma + PostgreSQL / MongoDB |
| **Autenticação** | NextAuth.js + MFA/TOTP |
| **Inteligência** | Google Gemini API (Análise de Risco/OCR) |
| **Financeiro** | Asaas (Webhooks / Split de Pagamentos) |
| **Infra** | Docker + Traefik + Sentry |

## 🏗️ Arquitetura e Estrutura
- `src/app/(auth)` / `(dashboard)` / `(tenant)`: Estrutura de rotas protegidas e multi-tenancy.
- `src/lib/ai/`: Wrappers para Gemini e análise preditiva de pagamentos.
- `prisma/schema.prisma`: Schema complexo com 43 modelos (Imóveis, Contratos, Tickets, AuditLogs).
- `infrastructure/`: Configurações de CI/CD e Docker de produção.

## 💎 Funcionalidades Nucleares
- **Multi-tenancy Físico/Lógico**: Separação rigorosa de dados por imobiliária.
- **Contratos Dinâmicos**: Editor TipTap com colaboração real-time via Yjs.
- **Inteligência de Risco**: Predição de inadimplência baseada em histórico de pagamentos Asaas.
- **Manutenção Automatizada**: Abertura de tickets via WhatsApp (integrado com WAHA).

## 🚀 Próximas Implementações (Sprint Atual)
- [ ] Refatoração da camada de `UserService` para padrões de Clean Architecture.
- [ ] Implementação de Testes E2E complexos com Playwright.
- [ ] Integração nativa com o hub JARVIS para automação via voz de relatórios.

**Links:** [[Projetos/Outros/Gestor Aluguel 2.0]] | [[GitHub-Completo]] | [[Projetos/EstudosPesquisas/Prisma-Performance|Guia Prisma]] #saas #enterprise #nextjs
