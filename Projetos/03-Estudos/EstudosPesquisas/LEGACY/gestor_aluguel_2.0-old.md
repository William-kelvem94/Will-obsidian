---
title: "Evolução gestor_aluguel_2.0"
description: "SaaS Next.js: Supabase free tier, Ollama AI local, Prisma Neon serverless."
tags:
  - gestor
  - projetos
  - evolucao
date: 2026-04-27
updated: 2026-05-03
---

# Evolução gestor_aluguel_2.0 [[README]]

**Atual**: Next.js 15 Prisma Postgres Gemini Asaas multi-tenant.

**Melhorias gratuitas**:

1. **DB Serverless Free**:
   - Migre Prisma para Neon Postgres free tier (serverless)
   - Tut: https://neon.tech/docs/connect/prisma

2. **AI Local Ollama**:
   - Substitua Gemini por Ollama no src/lib/ai/
   - Model qwen2.5-coder para predição financeira local
   - Next.js API route proxy Ollama

3. **Pagamentos Local Test**:
   - Asaas sandbox gratuito para test e2e
   - Stripe test cards gratuitos fallback

4. **Deploy Vercel Free**:
   - Vercel hobby tier ilimitado para Next.js SaaS
   - Neon + Vercel Edge Functions (zero cold start)

**Roadmap**:
- [ ] Neon serverless DB
- [ ] Ollama predição inadimplência local
- [ ] Vercel deploy gratuito

Recursos: [[AI-Local-Gratuita]] [[README]] #nextjs #prisma #neon
