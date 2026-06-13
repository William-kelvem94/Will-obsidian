---
title: "Gerenciador_Financeiro-7.0 - bloco ML/domínio"
date: 2026-06-13
tags: [privados]
updated: 2026-06-13
---

# Gerenciador_Financeiro-7.0 - bloco ML/domínio

Data: 2026-06-12

Fechamento do bloco:
- Removidos os últimos `any` da camada `src/lib/ai/ml/financial-ml.ts` e `src/services/ai/ml/financial-ml.ts`.
- Substituído o cast fraco de `Budget.spent` por tipo local explícito com conversão monetária segura.
- Removido filtro Prisma inválido `NOT: { categoryId: null }` porque `Transaction.categoryId` é obrigatório no schema.
- `npm.cmd run type-check` voltou a passar após a correção.

Por que foi feito:
- A camada de ML ainda tinha contratos fracos que misturavam domínio financeiro com suposições implícitas.
- O schema real do Prisma exigia alinhamento com os campos obrigatórios.

Próximo foco:
- Auditar os módulos de domínio restantes que normalizam budgets, goals, accounts e transactions.
- Procurar duplicidade ou abstração fraca entre views, adapters e services.
