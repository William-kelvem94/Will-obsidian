---
title: "Feature Flags for Agents"
description: "Guia pratico para agentes usarem feature flags com seguranca: rollout, kill switch, limpeza e testes."
tags: [software-engineering, feature-flags, release, agents, skills-eng]
date: 2026-05-08
updated: 2026-06-10
---

# Feature Flags for Agents

Objetivo: permitir rollout gradual e rollback rapido sem depender de re-deploy imediato.

## When to Use Flags

Use feature flags para:
- mudanca de comportamento (novo fluxo, nova regra)
- migracao (ler novo vs legado)
- performance/infra (novo cache, novo provider)

Nao use para:
- esconder codigo morto para sempre
- parametrizar tudo (vira caos operacional)

## Flag Types

- Release flag: habilita feature nova (temporaria).
- Ops flag: kill switch / degradacao (pode ser permanente).
- Experiment flag: A/B (precisa de metricas e analise).

## Agent Design Checklist

Cada flag deve ter:
- dono (time/pessoa)
- motivo e escopo
- data de expiracao (ou criterio)
- plano de limpeza (quando remover)
- fallback claro (o que acontece quando off)

## Rollout Patterns

Padrao recomendado:
1. flag off por default
2. habilitar para dev/staging
3. habilitar para 1% / subset (quando houver segmentacao)
4. aumentar gradualmente
5. estabilizar e remover flag (quando for release flag)

Sem segmentacao:
- use allowlist por tenant/user
- ou "canary instance" por deploy

## Testing Flags (nao esquecer)

Agentes devem:
- testar `flag=off` e `flag=on` nos pontos criticos
- evitar branches profundas: extrair estrategia/funcoes
- criar contract/integration tests para garantir compat

## Flag Hygiene (o que mata times)

Cheiros ruins:
- flags sem dono
- flags sem expiracao
- flags que mudam schema
- flags em cascata (A depende de B depende de C)

Regras:
- toda release flag tem expiracao
- remover flags logo apos estabilizar

## Kill Switch Guidance

Ops flags devem:
- ser rapidas de mudar (runtime config)
- ter audit trail
- ser documentadas em playbook

Ver tambem: [[rollback-and-release-strategies]].

