---
title: "Gerenciador Financeiro 7.0 Domain Consistency 2026 06 12"
date: 2026-06-13
tags: [privados]
updated: 2026-06-13
---

﻿# 2026-06-12 - Consistência de domínio em accounts e recomendações

- Removi o `any` do engine de recomendações em `src/services/ai/models/recommendation-engine.ts` e `src/lib/ai/models/recommendation-engine.ts` com contrato explícito de budget.
- Ajustei `accounts` para usar `MoneyValue` no adapter de view, alinhando com `toMoneyNumber`.
- `npm run type-check` voltou a passar.
- Próximo foco provável: outros módulos com normalização fraca em `src/app/api/ai/*` e adapters restantes.
