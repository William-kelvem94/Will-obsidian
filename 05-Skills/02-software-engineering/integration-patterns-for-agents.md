---
title: "Integration Patterns (Agent-Friendly)"
description: "Padroes de integracao e prompts para agentes: idempotencia, outbox, sagas, retries, DLQ e observabilidade."
tags: [software-engineering, backend, integration, agents, skills-eng]
date: 2026-05-08
updated: 2026-06-08
---

# Integration Patterns (Agent-Friendly)

Objetivo: ajudar agentes a escolher e implementar padroes de integracao sem causar regressao, duplicacao de eventos ou perda de dados.

## Agent Rules of Engagement

1. Preferir mudancas pequenas, reversiveis e observaveis.
2. Antes de propor um padrao, localizar: "source of truth" do dado, fronteiras (servicos), e garantias atuais (at-least-once, at-most-once, exactly-once).
3. Nunca assumir exatamente-uma-vez: em sistemas reais, duplicacao e reordem acontecem.
4. Sempre propor como detectar falha e como recuperar.

## Quick Triage (Escolha do padrao)

- Precisa publicar evento quando uma transacao de BD confirma?
  - Use Transactional Outbox.
- Precisa coordenar varias etapas entre servicos?
  - Use Saga (orquestrada ou coreografada).
- Consumidor pode falhar e reprocessar?
  - Use Idempotent Consumer + retry com backoff.
- Mensagens podem se acumular e "travar"?
  - Use DLQ + circuit breaker operacional.

## Transactional Outbox (Padrao recomendado para agentes)

Problema: publicar em broker e gravar em BD no mesmo fluxo pode gerar inconsistencias.

Sinal para usar:
- "Quando salvar X, precisamos emitir evento Y" e nao pode perder o evento.

Checklist minimo:
- Tabela `outbox` com: `id`, `aggregate_id`, `event_type`, `payload_json`, `created_at`, `published_at`, `attempts`, `last_error`.
- Producer grava no mesmo commit da mudanca de negocio.
- Dispatcher publica fora do request path (job/worker).
- Dispatcher idempotente: `outbox.id` como `message_key`.
- Observabilidade: taxa de backlog, idade do backlog, erros por tipo.

Anti-padroes comuns:
- Publicar no broker antes do commit.
- Publicar dentro do request sem protecao e sem retry controlado.
- Deixar dispatcher sem lock/claim e gerar duplicacao massiva.

## Idempotency (Produtor e Consumidor)

O agente deve procurar no codebase por:
- chaves de idempotencia (header `Idempotency-Key`, `request_id`, `event_id`)
- persistencia de dedupe (tabela `processed_events` ou cache com TTL)

Consumidor idempotente (regras):
- side effects devem ser "set-to-value", nao "add-to-value" sem protecao
- usar upsert com chave natural quando possivel
- gravar marcador "event processed" apenas apos aplicar efeitos

## Retries, Backoff, Jitter

Regras praticas:
- retry apenas para falhas transitivas (timeouts, 429, 5xx temporario)
- backoff exponencial com jitter
- limite de tentativas + DLQ (nao retry infinito)

O agente deve propor:
- politicas por endpoint/tipo de evento
- valores default (ex.: 5 tentativas, 200ms base, max 10s)
- circuit breaker quando dependencia cai

## DLQ e Reprocessing Seguro

DLQ nao e "lixeira"; e uma fila de quarentena.

Requisitos:
- motivo do erro + stack + payload
- playbook para reprocessar: como corrigir, como reemitir, como evitar duplicacao
- ferramenta de "replay" com filtros (por tempo, aggregate_id, event_type)

## Sagas: Orquestrada vs Coreografada

Orquestrada:
- um orchestrator manda comandos, rastreia estado e executa compensacoes
- mais facil de visualizar e operar, menos acoplamento temporal

Coreografada:
- eventos encadeiam passos
- tende a ficar dificil de entender e depurar conforme cresce

Recomendacao para agentes:
- preferir orquestracao quando ha compensacao e varias etapas
- limitar coreografia a fluxos simples e estaveis

## Observability "Sempre"

Minimo para qualquer integracao:
- `correlation_id` propagado (request -> logs -> eventos)
- metricas: latencia, taxa de erro, backlog, retries, DLQ count
- logs estruturados (incluindo `event_id`, `aggregate_id`)
- traces quando existir infra

## Agent Prompt Template (use em PR / review)

Perguntas que o agente deve responder:
- Quais garantias existiam e quais passam a existir?
- Onde podem acontecer duplicacao, reordem e perda?
- Qual e a chave de idempotencia e onde ela e validada?
- Como detectar backlog/erro e como recuperar?
- Qual e o rollback/kill switch?

