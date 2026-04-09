---
title: "Estudos Focado: Auto-boletos"
description: "Análise profunda + roadmap."
tags:
  - auto-boletos
  - analise
---

# Estudos Focado: Auto-boletos [[README]] [[Privados/Auto-boletos]]

**Quartel-General da Estratégia**
- Esta nota é o centro estratégico para o projeto Auto-boletos.
- Use-a para validar o roadmap, os riscos e as prioridades antes de abrir a implementação em [[Privados/Auto-boletos]].
- Pesquise ferramentas e referências em [[../EstudosPesquisas/README|Estudos e Pesquisas]].

**Status Atual** (clone):
- Tecnologias: Python Flask, Playwright login, Tesseract OCR, React/Vite Tailwind frontend, Docker compose.
- Forças: Funcional completo (login Equatorial, OCR boleto, AI chat light/ollama), docs GUIA/DOCKER, CI GitHub.
- Fraquezas: Regex heavy (erros edge cases), CAPTCHA manual fallback, DB SQLite (não scale), UI vanilla não shadcn.

**Análise**:
- Scope atual: MVP automação boletos 1 proprietário.
- Market fit: Imobiliárias pequenas/médias (10-100 imóveis).
- Ambitions: SaaS multi-prop, API Asaas pagamentos, app mobile React Native.

**Roadmap** (gratuito/local):

**MVP 1.0 (1 mês)**:
- Ollama qwen2.5 OCR semântico (substitua regex).
- Postgres Neon free + Prisma.
- Shadcn UI + dark mode.

**1.5 Prod (2 meses)**:
- Traefik HTTPS local, Portainer GUI.
- BullMQ jobs assíncronos extração.
- Vercel frontend deploy free.

**2.0 Scale (4 meses)**:
- Multi-prop/tenant Prisma.
- Stripe/Asaas sandbox pagamentos.
- Mobile PWA ou React Native Expo free.

**Cronograma**:
| Fase | Tempo | Deliver |
|------|-------|---------|
| 1.0 Ollama/Postgres | 4 sem | AI robusta, DB real |
| 1.5 Prod | 8 sem | Deploy local/prod |
| 2.0 SaaS | 16 sem | Multi-tenant monetizável |

Recursos: [[EstudosPesquisas/Auto-boletos]] [[AI-Local-Gratuita]] #roadmap

## Detalhamento Expandido
- Escopo atual: automação de boletos para um único proprietário, com captura de login, extração de dados e suporte a chat inteligente.
- Funcionalidades principais: login Equatorial automatizado, OCR de boleto, análise semântica de texto via AI, frontend React/Vite e Docker Compose.
- Necessidades imediatas: reduzir regex, tratar edge cases de OCR, robustecer workflows de pagamento e adicionar DB PostgreSQL para escalabilidade.
- Entregáveis chave:
  - implementação semântica de extração de boleto
  - transição SQLite -> Neon Postgres
  - interface mais profissional com shadcn

### Riscos e pontos de atenção
- OCR/Tesseract falha em boletos com layout diferente.
- CAPTCHA ou bloqueio de bot no login podem travar o fluxo.
- SQLite não atende multi-tenant ou vários imóveis.
- Pagamentos Asaas/Stripe exigem testes com dados sandbox e compliance.

## Diário de Bordo
- 09/04/2026 10:56:08: arquivo criado/atualizado com visão geral e roadmap.
- 09/04/2026 10:56:11: finalizadas as notas de status, forças, fraquezas e cronograma.
- Status de versão: nota local, sem histórico Git rastreado para este arquivo.

### Próximas ações concretas
- Converter parsing de boleto de regex para embeddings/OCR vetorial.
- Migrar backend para Postgres Neon e ajustar Prisma/ORM.
- Atualizar UI para shadcn + dark mode.
- Construir CI/CD para Docker Compose e deploy Vercel.
