---
title: "Gerenciador_Financeiro-7.0 - infraestrutura oculta"
date: 2026-06-13
tags: [privados]
updated: 2026-06-13
---

# Gerenciador_Financeiro-7.0 - infraestrutura oculta

Data: 2026-06-12

Auditado:
- `src/core/infrastructure/cache/CacheDecorator.ts`
- `src/core/infrastructure/di/Container.ts`
- `src/core/infrastructure/monitoring/PerformanceMonitor.ts`

O que estava inconsistente:
- Decorators ainda usavam `any` em `target` e argumentos.
- O container de DI ainda carregava aliases e mapas com `any`.
- O monitor de performance ainda usava `Record<string, any>` e decorators com `any`.

O que foi corrigido:
- Decorators passaram a usar `unknown` e `TypedPropertyDescriptor`.
- O container passou a armazenar serviços e singletons com tipos explícitos.
- O monitoramento passou a usar `Record<string, unknown>` e wrapper tipado.
- `type-check` continuou passando.

O que ainda falta:
- Ainda pode haver `any` em outros pontos de infraestrutura, mas os suportes mais centrais já foram tratados.

Decisão:
- Esse bloco ajuda a evitar que tipos fracos vazem para a camada financeira por baixo, então valeu a pena fechar agora.
