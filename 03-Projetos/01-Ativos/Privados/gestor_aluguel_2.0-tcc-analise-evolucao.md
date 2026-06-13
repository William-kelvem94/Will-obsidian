---
title: "TCC - Análise de Evolução: gestor_aluguel_2.0"
description: "Documentação completa da análise comparativa entre o TCC 1 (documento Monografia) e o código real do projeto gestor_aluguel_2.0. Tecnologias removidas, acrescentadas, e o que precisa mudar em cada seção do TCC."
tags:
  - gestor
  - privados
  - projetos
  - tcc
  - analise
  - evolucao
  - documentacao
updated: 2026-06-13
date: 2026-05-22
private: true
source: "D:/GitHub/gestor_aluguel_2.0"
---

# TCC - Análise de Evolução: gestor_aluguel_2.0

**Nota canônica:** [[gestor_aluguel_2.0]]
**Docx de referência:** `D:\Downloads\Modelo TCC - Monografia.docx`
**Código fonte:** `D:\GitHub\gestor_aluguel_2.0`

---

## 1. Objetivos Específicos do TCC

### Atuais no documento:
1. ✅ Implementar uma interface gráfica intuitiva que centralize as operações de cadastro, controle de pagamentos e geração de relatórios financeiros.
2. ⚠️ Integrar notificações automáticas via WhatsApp para envio de lembretes e informações aos inquilinos.
3. ✅ Aplicar princípios de engenharia de software e arquitetura em camadas, visando modularidade, manutenção facilitada e qualidade no desenvolvimento do sistema.

### Diagnóstico:
- **Objetivo 1** → COMPLETO (Dashboard com 21 módulos, CRUDs, gráficos Recharts, relatórios PDF/DOCX)
- **Objetivo 2** → EM REAVALIAÇÃO. A integração WhatsApp via WAHA API existe mas o objetivo precisa ser substituído por algo 100% entregue
- **Objetivo 3** → COMPLETO (Arquitetura em camadas, TypeScript strict, testes Jest/Playwright, Docker, CI/CD)

### Sugestão de novo Objetivo 2 (<- *aguardando decisão*):
**Opção A** — *"Implementar um portal do inquilino autônomo com consulta de contratos, pagamentos, documentos e comunicação em tempo real com o administrador."*
**Opção B** — *"Implementar módulos de Inteligência Artificial Generativa para automação de análise de documentos e suporte à tomada de decisão."*

**Recomendação:** Opção A (portal do inquilino é mais tangível e visual).

---

## 2. Tecnologias Descritas no TCC que Foram Removidas/Alteradas

| Tecnologia no TCC | Status | Substituída por | Localização |
|-------------------|--------|-----------------|-------------|
| **PostgreSQL 16** | ❌ Alterado | PostgreSQL 15 (docker-compose) | `docker-compose.yml` usa `postgres:15-alpine` |
| **Ollama (LLaMA/Mistral local)** | ❌ Removido | Google Gemini API (`@google/generative-ai`) | `src/lib/ai/gemini-client.ts` |
| **LangChain** | ❌ Removido | Tool definitions + function calls próprios | `src/lib/ai/functions/tool-definitions.ts` (18 funções) |
| **EasyOCR / PyTesseract** | ❌ Removido | Tesseract.js (`tesseract.js: ^7.0.0`) | `src/lib/ai/` rodando em Node.js |
| **MLflow (stack principal)** | ⚠️ Existe no microsserviço | Apenas no Python AI microservice | `infrastructure/microservices/ai-service/` |
| **Serviço de IA Python/FastAPI** | ⚠️ Existe mas desacoplado | IA principal migrou para Gemini no Node.js | `infrastructure/microservices/ai-service/` |

---

## 3. Tecnologias Acrescentadas (Não estavam no TCC)

### Infraestrutura & DevOps
- [[Docker-Prod-Gratis|Docker]] Hot Reload — `docker-compose.hot.yml`
- **n8n** — Engine de automação de workflows (`infrastructure/microservices/n8n/`)
- **Render.yaml** — Deploy alternativo no Render
- **GitHub Actions CI/CD** — `.github/workflows/ci.yml`, `deploy.yml`
- **Dependabot** — `.github/dependabot.yml`
- **Prometheus / Grafana / Promtail** — `scripts/monitoring/`
- **Vercel + Supabase** — Stack de produção

### Comunicação & Tempo Real
- **Socket.IO** (`socket.io: ^4.7.2`, `socket.io-client: ^4.8.1`) — Chat em tempo real
- **Yjs** (`yjs: ^13.6.10`, `y-websocket: ^1.5.4`, `y-protocols: ^1.0.6`, `y-prosemirror: ^1.2.0`) — Edição colaborativa CRDT
- **TipTap** (`@tiptap/core: ^2.27.2` + 15+ extensions) — Editor de texto rico colaborativo
- **Web Push API** (`web-push: ^3.6.7`) — Notificações push nativas
- **WAHA API** — Integração WhatsApp HTTP API

### Frontend & UI
- **Framer Motion 10** (`framer-motion: ^10.18.0`) — Animações
- **Recharts** (`recharts: ^2.15.4`) — Gráficos (dashboard)
- **Zustand** (`zustand: ^4.4.7`) — Gerenciamento de estado
- **Lucide React** (`lucide-react: ^0.294.0`) — Sistema de ícones
- **Sonner** (`sonner: ^1.7.4`) — Toast notifications
- **cmdk** (`cmdk: ^0.2.0`) — Command palette (Ctrl+K)
- **Vaul** (`vaul: ^0.7.9`) — Drawers responsivos
- **React Hook Form** (`react-hook-form: ^7.65.0`) + **@hookform/resolvers** — Formulários
- **TanStack React Table v8** (`@tanstack/react-table: ^8.10.7`) — Tabelas virtuais
- **React Day Picker** (`react-day-picker: ^9.11.1`) — Calendário
- **React Resizable Panels** (`react-resizable-panels: ^4.5.8`) — Painéis redimensionáveis
- **React Window** (`react-window: ^2.2.5`) — Virtualização de listas
- **shadcn/ui** (`shadcn: ^4.1.2`) — Componentes base
- **class-variance-authority + clsx + tailwind-merge** — Utilitários de estilo
- **next-themes** (`next-themes: ^0.4.4`) — Dark/Light mode
- **canvas-confetti** — Efeitos visuais
- **PWA** — Service Worker com cache e push notifications (`public/sw.js`, `public/manifest.json`)
- **Skeleton Loading** — Feedback visual em carregamentos
- **Design System fluid** — Classes `u-input-fluid`, `u-btn-fluid` com `clamp()`

### Backend & Serviços
- **Pino** (`pino: ^9.0.0`, `pino-http: ^9.0.0`, `pino-pretty: ^11.0.0`) — Logging estruturado
- **BullMQ** (`bullmq: ^5.0.0`) — Filas de processamento assíncrono
- **ioredis** (`ioredis: ^5.3.2`) — Cliente Redis
- **Nodemailer** (`nodemailer: ^7.0.11`) — Emails transacionais
- **otplib** (`otplib: ^12.0.1`) — Autenticação MFA/TOTP
- **jsonwebtoken** (`jsonwebtoken: ^9.0.2`) — Tokens JWT (portal inquilino)
- **qrcode** (`qrcode: ^1.5.3`) — QR Code (MFA + Pix)
- **jspdf + jspdf-autotable** (`jspdf: ^4.0.0`) — Geração de PDF
- **docx** (`docx: ^9.5.1`) — Geração de documentos Word
- **axios** (`axios: ^1.6.0`) — HTTP Client
- **@vercel/speed-insights** (`^2.0.0`) — Métricas de performance

### IA e Dados
- **Google Gemini** (`@google/generative-ai: ^0.24.0`) — Modelo `gemini-2.5-flash`
- **Tesseract.js** (`tesseract.js: ^7.0.0`) — OCR local em Node.js
- **BullMQ Workers** — `src/lib/ai/workers/ai-worker.ts`
- **Sistema de Personalidade Adaptativa** — `src/lib/ai/personality/personality-system.ts` + `AIPersonality` model
- **Feedback Loop** — `ConversationFeedback`, `AIPredictionOutcome`
- **Cache Manager** — `src/lib/ai/cache/cache-manager.ts` (Redis + compressão gzip)
- **RAG** — Retrieval-Augmented Generation (`/api/rag/ingest`, `/api/rag/query`)
- **Business Intelligence** — `src/lib/ai/services/bi-service.ts`
- **Recomendação Inteligente** — `src/lib/ai/services/recommendation-service.ts`
- **18 Tool Definitions** — `src/lib/ai/functions/tool-definitions.ts` (funções chamáveis pelo Gemini)
- **Motor de Insights** — `src/lib/ai/services/insights-service.ts`
- **Serviço de Risco** — `src/lib/ai/services/risk-analysis-service.ts`
- **Serviço de Documentos** — `src/lib/ai/services/document-intelligence-service.ts`
- **nlp-service.ts** — Análise de linguagem natural

### Segurança
- **Rate Limiting** — Edge runtime rate limiter no middleware
- **MFA/TOTP** — `otplib` + QR Code (Google Authenticator / Authy)
- **Audit Log** — `AuditLog` model (quem, quando, onde, o quê)
- **RBAC** — `TeamRole` (OWNER, ADMIN, MANAGER, VIEWER) + `Permission` enum
- **Sessão com timeout** — 30 min inatividade + 7 dias absoluto
- **Bloqueio brute force** — 5 tentativas, lockout 15 min
- **Isolamento Multi-tenant** — `saasTenantId` em toda query Prisma
- **Sentry** — Error tracking + performance (`@sentry/nextjs: ^8.0.0`)
- **Senha segura** — Mínimo 12 chars, maiúscula, número e especial
- **LGPD/GDPR** — Modo de compliance com retenção configurável
- **Session Manager** — Auto-refresh + validação periódica + relogin modal

### Módulos Funcionais Novos
- **Portal do Inquilino** — `/portal/` (dashboard, contratos, pagamentos, chat, documentos, notificações)
- **Chat em Tempo Real** — Socket.IO admin ↔ inquilino
- **Editor Colaborativo** — TipTap + Yjs (CRDT, múltiplos usuários simultâneos)
- **Integração Asaas** — PIX, Boleto, Cartão + Webhooks (`/api/integrations/asaas/`)
- **Webhooks** — Sistema completo (`/api/webhooks/`)
- **Contract Templates** — `ContractTemplate` model com variáveis
- **Calendário** — `/calendario` com eventos e vencimentos
- **Backup** — Serviço de backup e restore (`/api/backup/`)
- **PWA** — Service Worker, manifest, offline fallback
- **Internacionalização (i18n)** — pt-BR, en-US, es-ES
- **User Simulators** — `automation/user-simulators/`
- **Acessibilidade** — `src/lib/a11y/` (auditoria, screen reader, testes)
- **Busca Global** — Ctrl+K com `cmdk`
- **Atalhos de Teclado** — `KeyboardShortcutsContext`
- **Comando de Voz** — `useVoiceInput`, `useSpeechRecognition`
- **Geolocalização** — `useGeolocation`
- **Templates de Email** — `src/lib/email/` (welcome, payment-reminder, payment-receipt, password-reset, etc.)
- **Contas de Utilidade** — `UtilityOwner`, `UtilityAccount` (água, luz, gás)

---

## 4. Stack Tecnológica Real do Projeto (comparativo)

| Camada | Descrito no TCC | Real (código) |
|--------|-----------------|---------------|
| **Frontend** | Next.js 15, Tailwind CSS, Radix UI | Next.js 15.5.6, TailwindCSS 3.4, Radix UI, shadcn/ui, Framer Motion 10, Recharts, Zustand, TanStack Query v5, TanStack Table v8, TipTap 2 |
| **Backend** | Next.js API Routes, Prisma ORM 5 | Next.js API Routes, TypeScript 5.7, Node.js 20, Socket.io 4, BullMQ 5, Pino |
| **Banco** | PostgreSQL 16, Prisma ORM 5, Redis 7 | PostgreSQL 15, Prisma 5.22 (43 models), Redis 7 (ioredis) |
| **IA** | Ollama (Llama/Mistral), LangChain, EasyOCR/PyTesseract, MLflow | Google Gemini (`gemini-2.5-flash`), Tesseract.js, BullMQ Workers, MLflow (apenas microsserviço) |
| **Autenticação** | NextAuth.js 4, bcryptjs, Zod | NextAuth.js v4, bcryptjs, otplib (MFA/TOTP), jsonwebtoken, Zod |
| **Container** | Docker + Docker Compose | Docker Compose (app, db, redis, ai-service), Nginx, Hot Reload |
| **Qualidade** | Jest, Playwright, ESLint, Prettier | Jest 29, Playwright, ESLint, Prettier, TypeScript strict, Zod |
| **Monitoramento** | Sentry, MLflow | Sentry, Pino, Web Vitals, Speed Insights |
| **Integrações** | — | Asaas (PIX/Boleto/Cartão), n8n (workflows), WAHA (WhatsApp), Nodemailer, Web Push API |
| **Infra** | Docker | Docker, Vercel (free), Supabase (free), Render, GitHub Actions |

---

## 5. Ações por Seção do TCC

### 5.1. Introdução / Objetivos
**Remover:**
- Menções a WhatsApp como objetivo específico
- Texto sobre notificações automáticas via WhatsApp

**Adicionar:**
- Novo objetivo específico (Portal do Inquilino ou IA Generativa)
- Atualizar descrição do escopo para refletir funcionalidades reais

### 5.2. Stack Tecnológica
**Remover:**
- Ollama (Llama/Mistral)
- LangChain
- EasyOCR/PyTesseract
- PostgreSQL 16 (mudar para 15)
- MLflow da stack principal

**Adicionar:**
- Google Gemini API (`gemini-2.5-flash`)
- Tesseract.js (OCR local em Node.js)
- Socket.IO (chat em tempo real)
- Yjs + TipTap (edição colaborativa)
- BullMQ (filas de processamento)
- Pino (logging estruturado)
- Asaas (gateway de pagamento PIX/Boleto)
- n8n (automação de workflows)
- WAHA (WhatsApp HTTP API)
- Portal do Inquilino
- MFA/TOTP (otplib)
- TanStack Query v5 + TanStack Table v8
- Framer Motion + Recharts
- Zustand
- Internationalização (i18n)
- PWA + Service Worker
- GitHub Actions CI/CD

### 5.3. Arquitetura do Sistema (Material e Métodos)
**Remover:**
- "Serviço de IA isolado em Python com FastAPI" como principal (mencionar como secundário)
- Menções a "será", "pretende-se", "o projeto consistirá na concepção"

**Adicionar:**
- Google Gemini como IA principal no Node.js (tool definitions, function calls)
- Tesseract.js para OCR local
- Socket.IO para chat em tempo real
- Yjs + TipTap para edição colaborativa de contratos
- Descrição do schema Prisma (43 modelos multi-tenant)
- Arquitetura de cache Redis com cache manager
- BullMQ para filas de processamento
- Sistema de logging com Pino
- Autenticação com MFA/TOTP
- RBAC com hierarquia de permissões
- Descrição das integrações (Asaas, n8n, WAHA, Web Push, Nodemailer)
- Portal do inquilino separado

### 5.4. Material e Métodos (Backend)
**REESCREVER para descrever o Backend como está funcionando:**

- **Stack:** Next.js 15 (API Routes) + TypeScript 5.7 + Prisma 5.22 + PostgreSQL 15
- **Autenticação:** NextAuth.js v4 com JWT, suporte MFA/TOTP, rate limiting, bloqueio brute force
- **DB:** 43 modelos Prisma, schema multi-tenant (`saasTenantId`), migrations versionadas
- **Cache:** Redis via ioredis + cache manager com compressão gzip e invalidação por evento
- **Filas:** BullMQ para jobs assíncronos (treinamento de IA, análise de portfólio, relatórios)
- **Logging:** Pino com AsyncLocalStorage (requestId, userId, tenantId), logger client-safe
- **Monitoramento:** Sentry (erros + performance), Web Vitals, Pino structured logs
- **IA:**
  - Google Gemini API (`gemini-2.5-flash`) com 18 tool definitions para CRUD
  - Tesseract.js para OCR local (PDFs e imagens)
  - Serviço Python FastAPI (separado) para ML (scikit-learn, PyTorch) com MLflow
  - Cache de IA com Redis
  - Personalidade adaptativa por usuário
  - Feedback loop com ConversationFeedback
- **WebSocket:**
  - Socket.IO para chat admin ↔ inquilino
  - Yjs + y-websocket para edição colaborativa de contratos
- **Integrações:**
  - Asaas (PIX, Boleto, Cartão) com webhooks
  - n8n para automação de workflows
  - WAHA (WhatsApp HTTP API)
  - Web Push API (notificações push)
  - Nodemailer (emails transacionais: welcome, cobrança, recibo, convite)
- **Segurança:**
  - Isolamento multi-tenant via middleware Prisma (`saasTenantId`)
  - AuditLog (quem, quando, onde, o quê)
  - RBAC (TeamRole + Permission)
  - Rate limiting no Edge (auth: 5 req/15min, api: 1000 req/15min)
  - Validação Zod em todas as boundaries de API
  - Sessão com timeout de inatividade (30 min) + expiração absoluta (7 dias)

### 5.5. Análise e Discussão dos Resultados (Frontend)
**PREENCHER subseções com descrição do Frontend:**

**4.1 Implementação da Interface Gráfica Intuitiva** (Objetivo 1)
- Dashboard com KPIs financeiros, ocupação, alertas (Recharts)
- 21 módulos protegidos via `/(protected)/`:
  - Imóveis (CRUD + galeria de fotos + status)
  - Inquilinos (cadastro + score de crédito + documentos)
  - Contratos (editor colaborativo TipTap + templates + exportação PDF/DOCX)
  - Financeiro (lançamentos + Asaas PIX/Boleto + relatórios)
  - Manutenção (chamados com fotos + fornecedores + histórico)
  - Calendário (vencimentos + vistorias)
  - Chat (tempo real admin ↔ inquilino)
  - Arquivos (gestão de documentos + OCR)
  - Analytics + Insights + Relatórios
  - Configurações (perfil + equipe + integrações)
  - Assistente IA (chat contextual com Gemini)
- Design responsivo mobile-first com Tailwind CSS
- Dark/Light mode via `next-themes`
- Componentes acessíveis (Radix UI + testes de acessibilidade)
- Tabelas virtuais com busca global, filtros, ordenação e paginação
- Geração de relatórios em PDF (jsPDF) e DOCX
- Skeleton loading em todos os carregamentos

**4.2 Portal do Inquilino Autônomo** (Novo Objetivo 2 - *se escolhido*)
- Ambiente separado em `/portal/` com autenticação própria
- Dashboard pessoal do inquilino
- Consulta de contratos com detalhes e documentos
- Histórico de pagamentos e visualização de boletos
- Chat em tempo real com o administrador (Socket.IO)
- Notificações push e por email
- Aceite de convite por token JWT (`/portal/invite/[token]`)
- Documentos do contrato disponíveis para download

**4.3 Aplicação de Engenharia de Software** (Objetivo 3)
- Arquitetura em camadas (Apresentação → Lógica de Negócio → Acesso a Dados)
- TypeScript strict em toda a base de código
- Prisma ORM com schema versionado (43 modelos, migrations)
- Testes:
  - Jest (unitários: validações, utilitários, permissões, acessibilidade)
  - Playwright (E2E: fluxos completos)
  - Testes de acessibilidade (contraste, ARIA, heading hierarchy, keyboard)
- Containerização Docker com docker-compose (app, db, redis, ai-service)
- Pipeline CI/CD (GitHub Actions: lint → type-check → test → build)
- Monitoramento com Sentry (erros + performance)
- Documentação técnica em `docs/` (~70 arquivos)

### 5.6. Considerações Finais
**ESCREVER novo texto conclusivo** abordando:
- Que os objetivos foram alcançados
- Que o sistema foi implementado com sucesso
- Limitações identificadas
- Trabalhos futuros (deploy em produção, monetização, AI local como fallback)

### 5.7. Referências
**Adicionar fontes das novas tecnologias:**
- Google Gemini API docs
- Prisma ORM docs
- Socket.IO docs
- Yjs docs
- TipTap docs
- Asaas API docs
- n8n docs
- TanStack Query docs
- Framer Motion docs
- Recharts docs

---

## 6. Estrutura Completa do Projeto (para referência)

```
src/
├── app/
│   ├── (protected)/          # 21 módulos administrativos
│   ├── portal/               # Portal do inquilino (6 rotas)
│   ├── api/                  # ~200 endpoints REST
│   └── auth/                 # Login, cadastro, recuperação
├── components/
│   ├── ui/                   # shadcn/ui primitives
│   ├── forms/                # React Hook Form + Zod
│   ├── layout/               # Header, Sidebar, BottomNav, Dock
│   ├── ai/                   # Chat IA, predição
│   ├── editor/               # TipTap + Yjs colaborativo
│   ├── dashboard/            # Cards, gráficos, KPIs
│   └── settings/             # Configurações
├── lib/
│   ├── ai/                   # Motor de IA (42 arquivos)
│   ├── auth/                 # NextAuth + Zero Trust + MFA
│   ├── security/             # Rate limiting, audit
│   ├── integrations/         # Asaas, n8n, WAHA, email
│   ├── validations/          # Zod schemas (7 domínios)
│   ├── email/                # Templates transacionais
│   ├── cache/                # Redis + Memory cache
│   ├── metrics/              # Web Vitals, API perf
│   ├── logger/               # Pino structured logging
│   ├── a11y/                 # Acessibilidade
│   └── services/             # Lógica de negócio
├── hooks/                    # 36 custom React hooks
├── types/                    # 8 arquivos de tipos
├── config/                   # Business rules, navigation
├── middleware.ts             # Edge runtime
├── middleware-tenant.ts      # Multi-tenant isolation
└── server.ts                 # Custom server (Socket.IO + Yjs)

prisma/
├── schema.prisma             # 43 modelos, multi-tenant
├── seed.ts                   # Seed (70+ imóveis, inquilinos, contratos)
└── migrations/

infrastructure/
├── microservices/
│   ├── ai-service/           # Python FastAPI + MLflow
│   └── n8n/                  # Workflow automation
└── monitoring/               # Prometheus, Grafana

scripts/                      # 80+ arquivos (deploy, AI, dados, docker)
tools/                        # Geradores, dev tools
docs/                         # ~70 documentos técnicos
tests/                        # Testes E2E, integração
automation/                   # User simulators
```

---

## 7. Próximos Passos (TCC)

- [ ] Decidir novo objetivo específico 2 (Portal do Inquilino ou IA Generativa)
- [ ] Reescrever **Material e Métodos** para descrever o Backend real
- [ ] Preencher **Análise e Discussão dos Resultados** com o Frontend
- [ ] Escrever **Considerações Finais**
- [ ] Atualizar **Stack Tecnológica** no documento
- [ ] Atualizar **Referências Bibliográficas**
- [ ] Remover menções a tecnologias obsoletas (Ollama, LangChain, EasyOCR)

---

## 8. Links Relacionados

- [[gestor_aluguel_2.0]] — Nota principal do projeto
- [[../EstudosFocados/gestor_aluguel_2.0]] — Estratégia e roadmap
- [[../EstudosPesquisas/gestor_aluguel_2.0]] — Pesquisas técnicas
- [[../EstudosPesquisas/Next.js-SaaS-Evolution]] — Evolução Next.js
- [[../EstudosPesquisas/AI-Local-Gratuita]] — Pesquisa IA local
- [[../EstudosPesquisas/Docker-Prod-Gratis]] — Deploy gratuito

#tcc #gestor #projetos #analise #evolucao #documentacao
