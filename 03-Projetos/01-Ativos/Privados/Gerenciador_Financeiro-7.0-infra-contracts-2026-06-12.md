---
title: "Gerenciador_Financeiro-7.0 - contratos de infraestrutura"
date: 2026-06-13
tags: [privados]
updated: 2026-06-13
---

# Gerenciador_Financeiro-7.0 - contratos de infraestrutura

Data: 2026-06-12

Auditado:
- `src/core/infrastructure/events/EventBus.ts`
- `src/core/infrastructure/cache/RedisCache.ts`
- `src/core/infrastructure/observability/Logger.ts`

O que estava inconsistente:
- O barramento de eventos usava `any` para payloads.
- O cache aceitava `any` como valor armazenado.
- O logger aceitava `Record<string, any>` nos contextos estruturados.

O que foi corrigido:
- `EventBus` passou a usar payloads `unknown` internamente com API pública genérica.
- `RedisCache.set` passou a aceitar genéricos e armazenar `unknown`.
- `Logger` passou a usar `Record<string, unknown>` nos contextos.
- `type-check` continuou passando após a correção.

O que ainda falta:
- Ainda existem pontos de infraestrutura com tipos fracos fora deste bloco, mas já não são os suportes mais centrais para o domínio financeiro.

Decisão:
- Valeu a pena fechar esta frente agora porque ela reduz propagação de `any` para o restante do sistema.
