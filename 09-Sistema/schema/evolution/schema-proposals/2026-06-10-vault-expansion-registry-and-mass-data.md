---
title: "Vault Expansion Registry and Mass Data"
date: 2026-06-10
updated: 2026-06-10
type: schema-proposal
status: draft
tags: [schema, proposal, mcp, mass-data, governance]
summary: "Proposta para padronizar registry de MCPs, dados massivos, e qualidade de expansao em larga escala."
---

# Vault Expansion Registry and Mass Data

## Problema

O vault ja possui boa arquitetura, mas a expansao esta distribuida entre muitos arquivos, muitas camadas e varias superficies de automacao. Sem um registry comum, a escala tende a virar drift.

## Proposta

Formalizar quatro contratos permanentes:

1. `MCP Registry`
2. `Skill Canonical Format`
3. `Mass Data Classification`
4. `Expansion Quality Gates`

## MCP Registry

Cada MCP deve declarar:

- nome;
- proposito;
- transporte;
- autenticacao;
- leitura;
- escrita;
- sensibilidade;
- dependencias;
- status de maturidade;
- modo de falha;
- auditoria.

## Mass Data Classification

Toda massa nova deve entrar em uma de tres classes:

- `evidence` - fonte real imutavel;
- `synthesis` - sintese gerada a partir de evidencia;
- `synthetic` - dados de benchmark, simulacao ou teste.

Regra: nunca misturar as tres classes sem marcacao explicita.

## Skill Canonical Format

Cada skill precisa seguir uma estrutura comum com:

- overview;
- prerequisites;
- use cases;
- anti-patterns;
- prompts;
- checklists;
- metrics;
- related projects.

## Expansion Quality Gates

Antes de promover uma expansao:

- existe categoria clara?
- existe metadado suficiente?
- existe link interno util?
- existe dono ou caminho de manutencao?
- existe teste, score ou validacao?
- a nota evita duplicacao inutil?

## Resultado esperado

Com esses contratos, o vault pode crescer em volume sem perder:

- navegabilidade;
- auditabilidade;
- separacao de evidencias;
- compatibilidade com agentes;
- capacidade de manutencao.

