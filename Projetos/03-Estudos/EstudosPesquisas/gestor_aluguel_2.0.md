---
title: "Evolução gestor_aluguel_2.0 [[README]]"
date: 2026-06-01
tags: [projetos]
updated: 2026-06-01
---

﻿---
title: "Evolução gestor_aluguel_2.0"
description: "Snapshot técnico consolidado do projeto para contexto rápido e baixo consumo de tokens."
tags:
  - gestor
  - projetos
  - evolucao
  - arquitetura
  - portal
updated: 2026-06-01
date: 2026-04-27
---

# Evolução gestor_aluguel_2.0 [[README]]

## Estado Atual (2026-06-01)
- Stack: Next.js App Router + React + TypeScript + Prisma + PostgreSQL.
- Modelo: SaaS multi-tenant com isolamento por `saasTenantId`.
- Auth: NextAuth (área admin) + auth dedicada no portal do inquilino.
- Domínios principais: imóveis, inquilinos, contratos, pagamentos, manutenção, documentos, notificações.
- Integrações: Asaas, SMTP, push web, IA (chat/recomendações/previsões).

## Estrutura de produto
- Área administrativa: `/dashboard` e módulos de gestão.
- Portal do inquilino: `/portal` com dashboard, contrato, pagamentos, imóvel, manutenção, notificações, perfil e senha.
- APIs: `src/app/api/**` (admin) e `src/app/portal/api/**` (portal).

## Arquitetura resumida
- UI: `src/app/**`, `src/components/**`.
- Regras e serviços: `src/lib/**`, `src/services/**`.
- Persistência: Prisma (`prisma/schema.prisma`).
- Real-time/infra: Socket.IO, WebSocket/Yjs, Redis/BullMQ (quando habilitado).

## Status de UI/UX (admin + portal)
### Padrão consolidado
- Uso de tokens de tema (`primary`, `muted`, etc.) no lugar de cores hardcoded.
- Navegação com componentes responsivos (desktop/mobile) e feedback visual consistente.
- Reserva de espaço de navegação inferior por variáveis CSS do app (`--app-bottom-chrome-reserve`).

### Entrega aplicada (dock/menu portal)
- Criado dock desktop do portal com comportamento visual no padrão do dock principal:
  - arquivo: `src/components/portal/PortalDesktopDock.tsx`
  - animações de hover/active/indicator alinhadas ao padrão do `DesktopDock`.
- Integração no layout do portal:
  - arquivo: `src/components/portal/PortalLayoutClient.tsx`
- Padronização de cores do portal para tokens:
  - `src/components/portal/PortalHeader.tsx`
  - `src/components/portal/PortalMobileMenu.tsx`
  - `src/components/portal/PortalSidebar.tsx`
  - `src/components/portal/TenantAuthGuard.tsx`
- Resultado: removidos hardcodes azuis no fluxo principal de navegação/guard do portal.

## Qualidade e validação
- Type-check: `npm run type-check` passando após as mudanças de UI.
- Estratégia aplicada: mudanças incrementais + validação técnica curta por etapa.

## Como reduzir tokens nas próximas sessões (operacional)
1. Sempre começar por esta nota + `README.md` do repositório.
2. Consultar apenas arquivos-alvo com `rg` (evitar leituras amplas).
3. Registrar decisões em formato curto: `Problema -> Decisão -> Arquivos -> Validação`.
4. Evitar repetir contexto histórico já consolidado aqui.

## Backlog objetivo (alto impacto)
- Revisar acessibilidade completa do portal (foco/teclado/labels/contraste).
- Unificar microinterações entre admin e portal (timings e easing).
- Cobrir navegação portal com testes E2E críticos.
- Consolidar guia de design tokens em documento único para governança visual.

## Referências
- Projeto: `D:\DOCUMENTOS\GitHub\gestor_aluguel_2.0`
- Nota original: `Projetos/03-Estudos/EstudosPesquisas/gestor_aluguel_2.0.md`
- Docs locais: `docs/README.md`, `docs/guias/ui-ux/*`
