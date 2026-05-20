---
title: "Risco Operacional (Minimo)"
category: "Tecnologia-e-Sociedade"
description: "Um modelo simples para pensar risco operacional em sistemas e operacao assistida por agentes."
date: 2026-05-08
updated: 2026-05-08
tags: [conhecimento, risco, operacao, confiabilidade, seguranca]
---

# Risco Operacional (Minimo)

Modelo simples: risco = probabilidade x impacto.

## Fontes comuns de probabilidade

- Mudancas frequentes sem revisao
- Dependencias externas instaveis
- Falta de testes e rollback
- Acesso excessivo (permissoes amplas)
- Observabilidade fraca (voce nao ve a falha chegando)

## Fontes comuns de impacto

- Dados sensiveis expostos
- Perda de dados (sem backup testado)
- Interrupcao prolongada (sem runbook)
- Danos reputacionais (comunicacao ruim)

## Como reduzir risco sem burocracia

- Torne mudancas reversiveis: feature flags, rollback rapido.
- Adote um conjunto pequeno de alertas de alto sinal.
- Escreva runbooks para os 3 incidentes mais provaveis.
- Registre decisoes e evidencias durante incidentes.
- Separe credenciais por ambiente e limite privilegios.

## Agentes e risco

Agentes reduzem custo de execucao, mas podem aumentar probabilidade se:
- tiverem acesso demais
- nao pararem em condicoes de risco
- nao registrarem evidencias e mudancas

Operacao segura com agentes depende de: guardrails + auditoria + runbooks verificaveis.


[[Conhecimento-Geral/Tecnologia-e-Sociedade/INDEX|← Voltar ao índice de Tecnologia e Sociedade]]
