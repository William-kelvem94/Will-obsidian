---
title: "Gerenciador_Financeiro-7.0 - contratos de suporte"
date: 2026-06-13
tags: [privados]
updated: 2026-06-13
---

# Gerenciador_Financeiro-7.0 - contratos de suporte

Data: 2026-06-12

Auditado:
- `src/lib/api-helpers.ts`
- `src/lib/audit-log.ts`

O que estava inconsistente:
- Helpers centrais de API ainda aceitavam `any` para detalhes e captura de erro.
- O audit log ainda modelava payloads genéricos com `Record<string, any>`.

O que foi corrigido:
- `details` passou a usar `Record<string, unknown>`.
- Erros em wrappers de API passaram a ser capturados como `unknown`.
- O audit log passou a registrar payloads sem `any`.
- `type-check` continuou passando após as mudanças.

O que ainda falta:
- Existem outros pontos de suporte com `any`, mas fora deste bloco e fora do núcleo financeiro principal.

Decisão:
- Foi suficiente para fechar uma frente real de consistência sem reabrir áreas já validadas.
