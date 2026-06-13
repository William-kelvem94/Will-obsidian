---
title: "Gerenciador_Financeiro-7.0 - auditoria de domínio"
date: 2026-06-13
tags: [privados]
updated: 2026-06-13
---

# Gerenciador_Financeiro-7.0 - auditoria de domínio

Data: 2026-06-12

Auditado:
- `src/modules/budgets/view.ts`
- `src/modules/goals/view.ts`
- `src/modules/transactions/types.ts`
- `src/modules/transactions/service.ts`
- `src/core/infrastructure/repositories/PrismaBudgetRepository.ts`
- `src/core/infrastructure/repositories/PrismaAccountRepository.ts`
- `src/core/infrastructure/repositories/PrismaTransactionRepository.ts`
- `prisma/schema.prisma`
- `src/core/domain/entities/Account.ts`
- `src/core/domain/entities/Budget.ts`
- `src/core/domain/entities/Transaction.ts`

Conclusão da auditoria:
- Budgets, accounts e transactions estão alinhados com o schema e com as views de normalização monetária.
- `Transaction.categoryId` é obrigatório no schema, então qualquer filtro `categoryId: null` era inconsistente e já foi removido na camada de ML.
- `Goal` hoje aparece mais como contrato de view/serviço do que como entidade de domínio central, então a comparação de metas depende mais de módulos de aplicação do que de uma entidade dedicada.

O que ainda falta na camada de domínio:
- Revisar possíveis inconsistências fora do núcleo principal, como helpers, event bus, observability e serviços de apoio que ainda usam `any`.
- Confirmar se há duplicidade restante entre service e repository em módulos secundários.

Decisão:
- Não foi necessário mexer em budgets/goals/accounts/transactions nesta rodada além da validação.
- O próximo bloco deve atacar os últimos `any` fora do domínio central, sem reabrir o que já está consistente.
