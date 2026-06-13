---
title: "Gerenciador Financeiro 7.0 - Backend Env 2026-06-12"
date: 2026-06-12
tags:
  - privados
  - backend
  - ambiente
  - supabase
updated: 2026-06-13
---

# Ambiente do backend

- `DATABASE_URL` local alinhada ao Supabase PostgreSQL.
- Health do aplicativo ficou `healthy` com `database=true` e `redis=true`.
- A validação final depende desse ambiente para manter a prova de runtime reproduzível.
