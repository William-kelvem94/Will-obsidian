---
title: "DB Migrations and Zero-Downtime Changes"
description: "Playbook para agentes: migracoes seguras, expand/contract, backfill, indices e locks."
tags: [software-engineering, database, migrations, agents]
date: 2026-05-08
updated: 2026-05-08
---

# DB Migrations and Zero-Downtime Changes

Objetivo: permitir que agentes mudem schema sem derrubar producao e sem travar o banco.

## Golden Rule (Expand/Contract)

Para mudancas grandes:
1. Expand: adicionar novo schema (coluna/tabela/indice) sem quebrar.
2. Backfill: preencher dados em background, com batches.
3. Switch: app passa a ler/escrever no novo.
4. Contract: remover legado depois de estabilizar.

## Agent Preflight Checklist

Antes de escrever migracao, o agente deve responder:
- Qual banco (Postgres, MySQL, etc) e qual volume?
- Existe janela de deploy? Ou precisa zero downtime?
- Qual e o caminho de rollback?
- Ha queries/indices que podem lockar tabelas grandes?
- Ha replicas/lag relevante?

## Add Column Safely (padrao)

Preferir:
- adicionar coluna NULLable sem default
- depois backfill
- depois (se necessario) adicionar NOT NULL/constraint quando dados ok

Evitar:
- adicionar coluna com default em tabelas grandes (pode reescrever tabela)
- migracao que faz backfill inteiro dentro da transacao do migrate

## Backfill Strategy

Regras praticas:
- batches pequenos (ex.: 1k-10k)
- commit por batch
- id range (por PK) para ser previsivel
- reentrante: pode retomar sem duplicar
- metricas: progresso, tempo estimado, erros

Opcao: job separado do deploy, com feature flag controlando leitura.

## Indexes and Locks

Agentes devem se preocupar com:
- criar indice concurrently quando suportado
- evitar `ALTER TABLE` que bloqueia por muito tempo
- medir query plan antes/depois

Probes seguros:
- explicar query (EXPLAIN) em ambiente de staging
- medir latencia p95 e locks

## Data Contract Between App and DB

Regras:
- "reader can read old + new" antes de ativar escrita nova
- "writer writes both" temporariamente quando necessario (dual-write) com cuidado
- remover dual-write apenas apos confirmacao

## Destructive Changes (sempre 2 passos)

Remover coluna/tabela:
- primeiro parar de usar (deploy)
- depois remover (migracao posterior)

## What Agents Should Log

Ao propor migracao:
- impacto esperado (locks, tempo)
- estrategia de backfill
- estrategia de rollback
- como verificar (queries de sanity)

Ver tambem: [[rollback-and-release-strategies]].

