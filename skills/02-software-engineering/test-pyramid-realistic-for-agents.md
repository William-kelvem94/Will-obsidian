---
title: "Test Pyramid (Realistic) for Agents"
description: "Piramide de testes pragmatica para agentes: unit, integration, contract, e2e, e testes de migracao."
tags: [software-engineering, testing, agents, skills-eng]
date: 2026-05-08
updated: 2026-06-01
---

# Test Pyramid (Realistic) for Agents

Objetivo: guiar agentes a escolher o menor conjunto de testes que reduz risco de regressao, sem "test theater".

## A piramide real (na pratica)

Uma piramide saudavel costuma parecer:
- muitos unit tests (baratos, rapidos)
- um numero razoavel de integration tests (BD, filas, servicos internos)
- alguns contract tests (API / eventos)
- poucos E2E (fluxos criticos)

O agente deve ajustar ao risco:
- codigo novo em area critica -> mais integration/contract
- refactor interno -> unit + alguns integration focalizados

## Before Adding Any Test: Risk Scan

Perguntas:
1. O que pode quebrar do lado do usuario/sistema?
2. Quais invariantes de negocio precisam se manter?
3. Quais dependencias externas participam?
4. Existe area historicamente fragil?

## Unit Tests (quando valem)

Use para:
- logica de negocio pura
- parsers/validators
- mapeamentos e transformacoes

Evite:
- mocks profundos do framework inteiro
- testar implementacao ao inves de comportamento

Regra para agentes:
- se o teste precisa de 8 mocks, provavelmente e integration test disfarçado.

## Integration Tests (onde agentes ganham mais)

Bom para:
- repositorio + BD real (local container, ou in-memory equivalente quando aceitavel)
- endpoints com stack real (sem rede externa)
- eventos: publisher/consumer com broker local (ou double confiavel do broker)

Checklist:
- fixtures controladas
- dados deterministas
- timeouts pequenos
- asserts por invariantes observaveis

## Contract Tests (API e eventos)

Use para:
- garantir compatibilidade entre produtor/consumidor
- evitar breaking changes silenciosas

Tipos:
- provider contract: garante que API do provedor mantem o contrato
- consumer contract: garante que consumidor continua aceitando respostas/eventos

Minimo para agentes:
- especificar: campos obrigatorios, defaults, enums, e erros
- versionamento: suportar N e N-1 quando possivel

Ver tambem: [[api-contracts-and-compatibility]].

## E2E Tests (raros e valiosos)

Use para:
- 1-3 fluxos que sustentam receita/operacao
- smoke tests apos deploy

Evite:
- cobrir tudo com E2E
- suites que demoram 30+ min para rodar

Estrutura recomendada:
- "smoke": 3-10 min
- "nightly": cobertura maior, flakey controlado e com quarantines

## Testes para Migracoes

Agentes devem incluir testes de migracao quando:
- migra schema com impacto em leitura/escrita
- mexe em indices
- altera constraints

Minimo:
- migrate up em BD limpa
- migrate up em BD com dados existentes
- (quando aplicavel) rollback/down ou estrategia equivalente

Ver tambem: [[db-migrations-and-zero-downtime]] e [[rollback-and-release-strategies]].

## Flakiness Budget e Quarantine

Regras de ouro:
- teste flakey sem quarantine vira "barulho" e mata o CI
- quarantine deve ter dono, motivo e data de expiracao

O agente deve propor:
- rotulo `flaky`
- dashboard simples: taxa de falha por suite
- processo: consertar, ou remover se nao agrega

## Agent Output Template (para PR)

Inclua:
- risco coberto (1 frase)
- testes adicionados (lista curta)
- por que nao adicionou outros testes
- como rodar local (comandos)

