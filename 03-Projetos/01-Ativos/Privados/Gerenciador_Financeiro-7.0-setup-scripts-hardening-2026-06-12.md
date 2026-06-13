---
title: "Gerenciador Financeiro 7.0 - Setup Scripts Hardening 2026-06-12"
date: 2026-06-12
tags:
  - privados
  - backend
  - segurança
  - scripts
updated: 2026-06-13
---

# Hardening dos scripts de setup

- `scripts/setup-project.ts`, `scripts/reset-db.ts`, `scripts/setup.bat` e `scripts/setup.sh` não exibem mais credenciais demo completas.
- A saída agora orienta a consultar seed/documentação interna para dados de teste.
