---
title: "Gerenciador Financeiro 7.0 Security Hardening 2026 06 12"
date: 2026-06-13
tags: [privados]
updated: 2026-06-13
---

﻿# 2026-06-12 - Hardening de ambiente e credenciais

- Seed saiu de credenciais demo fixas e passou a aceitar `DEMO_SEED_USER_EMAIL` e `DEMO_SEED_USER_PASSWORD`.
- `scripts/setup-project.ts` agora gera `NEXTAUTH_SECRET` forte para novos setups.
- `.env.example` deixou de sugerir `gerenciador123` e secret de exemplo reutilizável.
- `npm run check:env` continua verde.
- Pendência: revisar o runtime real e a saúde do banco sem mexer em `src/app/api/auth/register/route.ts`.
