---
title: "gestor_aluguel_2.0 (Clonado)"
source: "C:/Users/willi/Documents/GitHub/gestor_aluguel_2.0"
language: TypeScript
private: true
description: "SaaS Imobiliário Next.js 15 enterprise com Prisma, AI Gemini, multi-tenant, Asaas pagamentos, portal inquilino."
updated: 2026-04-29
tags:
  - projetos
  - privados
  - nextjs
  - typescript
  - prisma
  - saas
  - ai
date: 2026-04-27
---

# gestor_aluguel_2.0 [[../Projetos.md|Projetos]] [[GitHub-Completo]]

**Private Clone | Next.js 15.5.6/TS | Atualizado 16h ago**

Plataforma SaaS gestão imobiliária: imóveis, inquilinos, contratos TipTap Yjs, financeiro Asaas, manutenção, AI Gemini (predição inadimplência, OCR), multi-tenant Prisma 43 models.

**Estrutura** (enterprise):
- `src/` (middleware-tenant, lib/ai, services, hooks)
- `docs/` (~70 arquivos: AI_SYSTEM.md, DEPLOY_CHECKLIST.md)
- Prisma schema, Docker, scripts data-massive, tests e2e Playwright

**Funcionalidades** (de README):
- MFA/TOTP, rate limiting, audit log, real-time Socket.io
- Portal inquilino separado, n8n integrações, WhatsApp WAHA
- Sentry, Pino logging, Dependabot security

**Run**: `npm run docker:dev`

**Links**: [[Projetos/Outros/Gestor Aluguel 2.0]] (versão anterior) | [[GitHub-Completo]] #saas #prisma #gemini
