---
title: "Gerenciador_Financeiro-7.0 - suporte auth/push"
date: 2026-06-13
tags: [privados]
updated: 2026-06-13
---

# Gerenciador_Financeiro-7.0 - suporte auth/push

Data: 2026-06-12

Auditado:
- `src/lib/auth.ts`
- `src/lib/push.ts`

O que estava inconsistente:
- O callback JWT/session ainda usava `any` para ler/escrever `avatar` e `id`.
- O handler de push ainda usava `any` para inspecionar o erro de remoção de subscription.

O que foi corrigido:
- `auth.ts` passou a usar casts locais pequenos e explícitos.
- `push.ts` passou a inspecionar `statusCode` com tipo local mínimo.
- `type-check` continuou passando.

O que ainda falta:
- O restante dos utilitários genéricos fora do domínio financeiro principal.

Decisão:
- Foi uma correção pequena, mas real, que eliminou tipos fracos em um caminho de suporte usado pelo app inteiro.
