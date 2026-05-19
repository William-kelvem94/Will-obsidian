---
title: "Rollback and Release Strategies"
description: "Como agentes devem planejar rollback, canary, blue/green, e reduzir blast radius em releases."
tags: [software-engineering, release, rollback, agents]
date: 2026-05-08
updated: 2026-05-08
---

# Rollback and Release Strategies

Objetivo: agentes conseguirem entregar mudancas com capacidade real de desfazer, mesmo com migracoes.

## Rollback Reality Check

"Rollback" pode significar:
- reverter codigo (deploy anterior)
- desativar feature via flag
- parar job/consumer (kill switch)
- bloquear caminho de escrita (read-only mode)

Agentes devem explicitar qual tipo se aplica.

## Release Options (escolha por risco)

- Feature flags: melhor para mudancas de comportamento.
- Canary: melhor para mudancas de performance/infra.
- Blue/green: melhor para trocar stack sem downtime.
- Rolling: default, mas com risco se a mudanca nao e compat.

## DB + App: Rollback-safe Patterns

Quando tem migracao:
- primeiro deploy deve ser backward compatible
- evitar migracao irreversivel no mesmo deploy de mudanca de escrita
- separar schema change de behavior change

Pratico:
- Deploy A: expand schema e escrever compat
- Backfill: job separado
- Deploy B: ativar leitura/escrita nova
- Deploy C: contract (remover legado)

## Canary Checklist for Agents

Minimo:
- metricas alvo (p95 latencia, erro 5xx, backlog)
- tempo de observacao
- criterio de abortar
- capacidade de reverter rapidamente

## Kill Switches (Agent-Friendly)

O agente deve propor kill switch para:
- consumers de fila (pausar/reduzir concorrencia)
- rotas criticas (rate limit ou 503 controlado)
- tarefas de background (pausar scheduler)

Preferir kill switch:
- configuravel em runtime (env/flag/config service)
- auditavel (log de quem mudou)

## Post-Release Verification

Agente deve listar:
- queries de sanity para BD
- checks de API (smoke)
- eventos/DLQ/backlog

Ver tambem: [[feature-flags-for-agents]] e [[db-migrations-and-zero-downtime]].

