---
title: "Gerenciador Financeiro 7.0 - Env Hardening 2026-06-12"
date: 2026-06-12
tags:
  - privados
  - backend
  - ambiente
  - segurança
updated: 2026-06-13
---

# Hardening de ambiente

- `scripts/check-env.ts` agora valida que `DATABASE_URL` aponta para PostgreSQL.
- O script também alerta sobre `NEXTAUTH_SECRET` padrão ou curto.
- A checagem de ambiente continua passando no estado atual do projeto.
