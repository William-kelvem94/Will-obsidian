---
title: "Gerenciador Financeiro 7.0 - Backend 2026-06-12"
date: 2026-06-12
tags:
  - privados
  - backend
  - financeiro
  - mapeamento
updated: 2026-06-13
---

# Backend - Estado atual

## O que já está alinhado
- `prisma/schema.prisma`: os campos monetários centrais já estão em `Decimal`, incluindo contas, transações, orçamentos e metas.
- `prisma/migrations/20260612010000_normalize_transaction_amount/migration.sql`: normalização anterior de transações preservada.
- `prisma/migrations/20260612020000_budget_goal_decimal_contract/migration.sql`: migração nova para consolidar `budgets.amount`, `budgets.spent`, `goals.targetAmount` e `goals.currentAmount` em `DECIMAL(65,30)`.
- `src/core/infrastructure/repositories/PrismaBudgetRepository.ts`: leitura e escrita de orçamento já passam por normalização com `toMoneyNumber`.
- `src/modules/goals/view.ts`: view de metas serializa `targetAmount` e `currentAmount` para número plano na API.
- `src/services/contact-service.ts`: contatos já têm fluxo de normalização, migração de legado e CRUD por usuário.
- `src/app/api/budgets/route.ts` e `src/app/api/budgets/[id]/route.ts`: escrita de orçamento normalizada na entrada com `toMoneyNumber`.
- `src/app/api/goals/route.ts` e `src/app/api/goals/[id]/route.ts`: escrita de metas normalizada na entrada com `toMoneyNumber`.
- `src/app/api/accounts/route.ts` e `src/app/api/accounts/[id]/route.ts`: saldo inicial e saldo atual normalizados na entrada com `toMoneyNumber`.
- `src/app/api/credit-cards/route.ts` e `src/app/api/credit-cards/[id]/route.ts`: saldo inicial e saldo atual normalizados na entrada com `toMoneyNumber`.
- `src/core/infrastructure/repositories/PrismaAccountRepository.ts` e `src/services/account-service.ts`: escrita de contas alinhada ao mesmo contrato numérico.
- `src/app/api/investments/route.ts` e `src/app/api/investments/[id]/route.ts`: quantidade e preço-base reforçados com normalização numérica na entrada.
- `src/app/api/reports/route.ts`, `src/app/api/dashboard/monthly-data/route.ts`, `src/app/api/dashboard/expenses-by-category/route.ts` e `src/modules/dashboard/view.ts`: totais e agregações usam `toMoneyNumber`/helpers monetários na leitura.
- `src/core/domain/entities/Account.ts`: domínio de conta reconhece `CREDIT_CARD` como tipo válido, alinhado com a persistência e as rotas de cartão.

## Pontos observados no runtime
- `npm.cmd run type-check` passou com o estado atual do backend.
- As rotas de `goals` e `contacts` já estão separadas por recurso e usam validação + serialização centralizadas.
- `src/lib/socket-handler.ts` ainda merece revisão de consistência, mas já está tipado o suficiente para não travar a compilação.

## Decisões registradas
- Não mover regras de aluguel para o financeiro.
- Não tocar no frontend nesta frente.
- Manter o Domni apenas como referência de organização técnica.
- Tratar valores monetários como `Decimal` na persistência e como `number` na borda da API.

## Próximos blocos sugeridos
- Revisar o restante das rotas que escrevem valores monetários para garantir `toMoneyNumber` no ponto de entrada.
- Verificar se há mais repositórios ou serviços ainda esperando `number` cru onde o banco já virou `Decimal`.
- Consolidar qualquer duplicação de domínio em `contacts` e `goals` antes de avançar para relatórios e agregações.
- Auditar relatórios e agregações de investimento para conferir se usam a mesma semântica de cálculo em todos os pontos.

## Observação
- O que está feito aqui não é só repetição: o backend já entrou no contrato decimal correto, mas ainda precisa de fechamento por blocos para ficar realmente consistente em toda a superfície de API e persistência.
