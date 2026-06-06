---
title: "William-kelvem94/gestor_aluguel_2.0"
source: "https://github.com/William-kelvem94/gestor_aluguel_2.0?tab=readme-ov-file"
author:
  - "William Pereira"
published:
created: 2026-04-09
description: "Resumo técnico do repositório Gestor de Aluguel 2.0, com arquitetura, stack e recursos principais."
tags:
  - projetos
  - clippings
  - nextjs
  - saas
  - prisma
  - ai
date: 2026-04-27
updated: 2026-06-05
---

## ?? Gestor de Aluguel 2.0 [[../Projetos|Projetos]]

> Plataforma SaaS para gestão imobiliária de alto desempenho. Desenvolvida com **Next.js 15.5.6 (App Router)**, **TypeScript 5.7**, **Prisma 5.22**, **PostgreSQL**, **Docker** e integração com inteligência artificial generativa.

## ?? Visão Geral

- Sistema completo para administradoras e imobiliárias com **multitenant**, gestão de imóveis, inquilinos, contratos, financeiro, manutenção, calendário e notificações.
- Portal do gestor e **PWA móvel** com navegação adaptada e experiência de app em tela pequena.
- Integração com **AI**, chat contextual, OCR de documentos e automação de eventos.
- Proposta de produto: um ERP imobiliário moderno com foco em usabilidade e performance.

## ?? O que entrega

- **Painel administrativo** (`src/app/(protected)/`)
- **Autenticação** com cadastro, login, convite e sessão segura
- **Multi-tenant** isolado por `saasTenantId`
- **Assistente IA** contextual via Gemini
- **Editor colaborativo** de contratos com Yjs + TipTap
- **Pagamentos** via integrações e boletos
- **Portal de notificações** com filtro e exportação
- **Configurações completas** de perfil, segurança, equipe e integrações
- **PWA / mobile** com navegação bottom nav e experiência nativa

## ?? Tecnologias principais

- **Frontend**: Next.js 15.5.6, React 18, TailwindCSS 3.4, Radix UI, shadcn/ui, Framer Motion
- **State / Dados**: react-hook-form, zustand, TanStack Query 5, TanStack Table 8
- **Editor rico**: TipTap 2 + Yjs + y-websocket + y-prosemirror
- **Backend**: Next.js API Routes, Node.js 20, bcryptjs, NextAuth.js v4
- **Banco**: PostgreSQL + Prisma 5.22 + Redis
- **AI / OCR**: @google/generative-ai, Tesseract.js
- **Integrações**: Asaas, WAHA WhatsApp, n8n, Nodemailer / SMTP / AWS SES
- **Logs / Observabilidade**: Pino, Sentry
- **Testes**: Jest, Playwright

## ??? Arquitetura e organização

### Pasta principal

- `src/app/`  rotas do Next.js App Router.
- `src/app/auth/`  fluxo de login / registro / convite.
- `src/app/(protected)/`  painel autenticado.
- `src/app/api/`  API routes e backend custom.
- `src/components/`  componentes compartilhados e UI.
- `src/lib/`  serviços, utilitários, integração e regras de negócio.
- `src/middleware-tenant.ts`  middleware responsável pelo isolamento de tenant em APIs.
- `config/docker/`  compose e ambiente Docker.

### Arquitetura de restrição

- `src/middleware-tenant.ts` extrai `tenantId` do usuário e insere `x-tenant-id` nas requisições.
- `src/lib/tenant/isolation.ts` e `src/lib/prisma` garantem que queries Prisma usem o tenant correto.
- Login e convite criam `SAAS Tenant` + `TeamMember OWNER` automaticamente.

## ?? Módulos-chave do produto

### Core

- **Dashboard**  visão geral de KPIs e atividade.
- **Imóveis**  CRUD, fotos, filtros, mapas e situação.
- **Inquilinos**  cadastro, score, documentos e histórico.
- **Contratos**  editor colaborativo, templates e assinatura.
- **Financeiro**  lançamentos, pagamentos e cobranças.
- **Manutenção**  chamados, fornecedores e histórico.
- **Calendário**  vencimentos, inspeções e eventos.
- **Notificações**  central com filtros, exportação e ações em lote.
- **Configurações**  perfil, notificações, preferências, segurança, time, titulares e suporte.

### Integração de IA

- **Assistente** com contexto financeiro/jurídico/técnico.
- **Análise de risco** de contratos e inquilinos.
- **Predição de inadimplência**.
- **Extração OCR** de documentos e imagens.
- **Recomendações** e insights proativos.

### Integrações específicas

- **WAHA/WhatsApp**  controle de sessão e envio via API.
- **Asaas**  cobrança PIX/Boleto.
- **n8n**  orquestração e automações.
- **Email**  SMTP/SendGrid/SES.

## ?? Segurança

- Honeypot anti-bot no registro (`website` + validação server-side).
- **NextAuth** com autenticação social/base.
- **Senha segura** com bcryptjs.
- **MFA/TOTP** via `otplib`.
- **Audit log** de ações importantes.
- **Rate limiting** e controles de API.
- **Sessões adaptativas** e timeout de inatividade.

## ?? PWA e mobile

- Design responsivo com `BottomNav` e layout adaptado.
- Experiência mobile-first em `src/components/layout/BottomNav.tsx` e `AIFloatingWidget.tsx`.
- Página de ajuda / onboarding móvel disponível.
- Uso consistente de `safe-area-inset` para rodapés e botões flutuantes.

## ?? Observações de implementação

- `package.json` contém scripts de Docker, testes, geração de Prisma e workflows de AI.
- Dependências incluem `@google/generative-ai`, `@tiptap/*`, `yjs`, `socket.io`, `bullmq`, `tesseract.js`.
- Há suporte a geração de releases manuais via `docker:build:optimized`.
- O projeto já faz `useTransition` em várias telas para melhorar INP.
- `src/app/api/whatsapp/` gerencia integração WAHA com autenticação via API key.

## ?? Documentação interna relevante

- `docs/ANALISE_TELA_IA_COMPLETA.md`
- `docs/ANALISE_COMPLETA_CONFIGURACOES_SISTEMA.md`
- `docs/CI_CD_GUIDE.md`
- `docs/EMAIL_SYSTEM.md`
- `docs/FEATURES-IMPLEMENTADAS.md`
- `docs/BACKUP-RESTORE.md`
- `docs/IMPLEMENTACAO_FINAL_CHECKLIST.md`
- `docs/INSTRUCOES-RAPIDAS.md`

## ?? Estrutura resumida do projeto

- `src/components/ui/`  primitives UI e componentes customizados.
- `src/components/settings/`  abas de perfil, notificações, preferências, segurança, team, suporte.
- `src/components/ai/`  widgets de assistente e chat.
- `src/components/layout/`  layouts, header e navegação.
- `src/lib/ai/`  serviços, workers e integração de IA.
- `src/lib/push-notifications/`  push e notificações.
- `src/lib/services/`  backend services para imóveis, contratos, pagamentos, etc.
- `src/app/api/`  endpoints de API usados pelo painel e integrações externas.

## ?? Pontos de atenção atuais

- O projeto já é robusto e encontro mais detalhes operacionais do que lacunas essenciais.
- A documentação do Obsidian precisava de um resumo técnico mais profundo, com arquitetura, tecnologia e módulos reais.
- Se for expandir, incluir também o **roadmap de produto** e o **fluxo do portal de inquilino PWA**.

**Links:** [[../Projetos]] | [[../../Bem-vindo]] | [[../../Clippings]] #projetos #saas #typescript #nextjs #prisma #ai
