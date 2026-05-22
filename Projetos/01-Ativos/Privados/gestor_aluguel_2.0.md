---
title: "gestor_aluguel_2.0 (Clonado)"
source: "d:/Documents/GitHub/gestor_aluguel_2.0"
language: TypeScript
private: true
description: "SaaS Imobiliário Enterprise: Next.js 15, Multi-tenant, AI-Driven."
updated: 2026-05-03
tags: [privados, nextjs, typescript, prisma, saas, ai, projetos]
date: 2026-04-27
---

# Gestor de Aluguel 2.0 🏠 [[../Projetos.md|Projetos]]

**Status**: 🚀 Produção / Estabilização
**Escala**: Enterprise Multi-tenant (43+ Models Prisma)

## 🌐 Visão Geral (Pública)
Plataforma SaaS imobiliário completo com gestão de imóveis, inquilinos, contratos dinâmicos (TipTap/Yjs), financeiro integrado (Asaas) e portal para o inquilino.

## 🛠️ Detalhes de Engenharia (Privado)
- **Framework**: Next.js 15 (App Router).
- **Inteligência**: Google Gemini para análise de risco de inadimplência.
- **Integrações**: WhatsApp (WAHA) e n8n para webhooks.
- **Segurança**: MFA/TOTP, Audit Logs e Rate Limiting.

## 🎯 Meta 90 Dias (Ciclo Abr/Jun 2026)
- [ ] Deploy do frontend em Vercel.
- [ ] Banco Postgres em Neon configurado.
- [ ] Autenticação Clerk com MFA funcionando.
- [ ] Fluxo de pagamento sandbox com Asaas/Stripe.

**Estratégia**: [[../EstudosFocados/gestor_aluguel_2.0|Roadmap de Evolução SaaS]]

## 📈 Atualizações Recentes (Maio 2026)
- **Editor de Contratos (TipTap)**: Implementada a `VariableExtension` atômica para proteger variáveis dinâmicas (`{{chave}}`) no modo de edição, preservando retrocompatibilidade total de regex.
- **Autosave Preditivo**: Introdução de salvamento automático com *debounce* reativo no `CollaborativeContractEditor.tsx`.
- **Governança de UI**: Formulários públicos protegidos com cooldown/rate limiting. Tela de recuperação de senha mantida em BLACKLIST de edição (`/auth/forgot-password`).
- **Resiliência de CI/CD**: Solução definitiva de falhas no Build/Lint/Type Check na Vercel via correção da árvore de JSX, escopo léxico de Hooks (`useEditor`) e higienização estrita de `react-hooks/exhaustive-deps`.

**Links:** [[gestor_aluguel_2.0-tcc-analise-evolucao|📄 Análise TCC]] | [[GitHub-Completo]] | [[Projetos/03-Estudos/EstudosPesquisas/README|🔬 Recursos]] #saas #enterprise #nextjs #prisma #tcc
