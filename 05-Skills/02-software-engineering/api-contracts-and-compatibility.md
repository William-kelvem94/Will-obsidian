---
title: "API Contracts and Compatibility"
description: "Como agentes devem definir contratos, evitar breaking changes e operar versionamento de APIs e eventos."
tags: [software-engineering, api, contracts, agents, skills-eng]
date: 2026-05-08
updated: 2026-06-13
---

# API Contracts and Compatibility

Objetivo: agentes conseguirem mexer em APIs sem quebrar consumidores (humanos, servicos e agentes).

## Contract Surface (o que e contrato)

Para HTTP/JSON:
- endpoints + metodos
- request: campos, tipos, validacoes, limites
- response: shape, campos obrigatorios, defaults
- erros: codigos, mensagens, formato, causas
- semantica: o que significa "sucesso", "idempotente", "eventual"

Para eventos (pub/sub):
- schema do evento + version
- semantica de entrega (at-least-once)
- ordenacao (por aggregate_id? nenhuma?)
- compatibilidade N e N-1

## Compatibility Rules (Agent-Friendly)

Mudancas geralmente seguras:
- adicionar campo opcional com default
- adicionar novo endpoint
- adicionar novo valor de enum (somente se consumidores toleram)
- tornar erro mais especifico mantendo formato

Mudancas de risco:
- renomear/remover campo
- mudar tipo (string -> int)
- mudar semantica (ex.: endpoint antes era idempotente e vira nao-idempotente)
- trocar codigo de erro em casos comuns
- mudar ordenacao/paginacao sem migracao

Regra para agentes:
- quando mudar contrato, propor "compat mode" e periodo de deprecacao.

## Deprecation Protocol (mini)

1. Marcar campo/endpoint como deprecated na doc (ou note interna).
2. Manter compatibilidade por janela definida.
3. Telemetria: medir uso do campo/endpoint antigo.
4. Comunicar e remover no marco (sem surpresa).

## Versioning Approaches

HTTP:
- version no path: `/v1/...` (simples, mais pesado)
- version por header: `Accept: application/vnd...` (flexivel, mais complexo)
- version por compat: "v1 com campos opcionais" (ideal para mudancas pequenas)

Eventos:
- `event_version` no payload
- topicos/streams por versao quando necessario
- manter consumidor capaz de ler versoes antigas

## Schema Discipline (para agentes)

Checklist de schema:
- campos obrigatorios minimizados
- defaults explicitados
- exemplos (request/response)
- limites (max size, max items)
- ids consistentes (`request_id`, `correlation_id`)

## Error Contract (nao negligencie)

Formato recomendado (exemplo):
```json
{
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "email is invalid",
    "details": [{"field": "email", "reason": "format"}],
    "request_id": "..."
  }
}
```

Regras:
- `code` estavel, `message` pode mudar
- `request_id` sempre que possivel
- nao retornar 500 para erro do usuario

## Backward Compatibility for Agents

Quando o agente altera API:
- atualizar/adicionar contract tests
- garantir "reader can read old, writer writes new" quando houver migracao
- propor feature flag para liberar gradualmente

Ver tambem: [[feature-flags-for-agents]] e [[test-pyramid-realistic-for-agents]].

