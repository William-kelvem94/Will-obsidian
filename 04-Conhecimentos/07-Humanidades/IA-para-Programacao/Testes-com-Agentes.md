---
title: "Testes com Agentes"
description: "Como pedir e validar testes gerados por IA sem criar uma suite fragil ou lenta."
tags: [ia, testes, programacao, agentes, qualidade]
updated: 2026-05-08
status: active
---

# Testes com Agentes

IA ajuda muito a gerar testes, mas ela tende a:

- exagerar mocks;
- escrever testes acoplados em detalhes;
- ignorar casos de borda.

O objetivo e usar IA para acelerar cobertura com criterio.

## Primeiro, escolha o tipo certo

- unit: rapido, logica pura, edge cases.
- integration: boundaries reais (db, http), valida fluxo.
- e2e: caro, valida UX/fluxo completo, poucos.

## Regras de Ouro

- teste deve falhar antes da mudanca e passar depois;
- prefira fixtures pequenas e dados explicitos;
- nao teste implementacao, teste comportamento;
- evite asserts genericos ("status ok") sem validar o efeito.

## Perguntas para o Agente

- qual caso esse teste pega que hoje nao pega?
- qual e o sinal de falha que ele captura?
- qual e o custo de manutencao?
- existe uma forma mais simples de validar?

## Relacionado

- [[04-Conhecimentos/07-Humanidades/IA-para-Programacao/Engenharia-de-Contexto]]
- [[02-JARVIS/02-Operational/Playbooks/Session-to-Learning-Protocol]]


[[04-Conhecimentos/07-Humanidades/IA-para-Programacao/INDEX|← Voltar ao índice de IA para Programação]]
