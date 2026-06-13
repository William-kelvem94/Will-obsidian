---
title: "Roadmap de Expansao de Skills"
date: 2026-06-10
updated: 2026-06-13
type: moc
status: active
tags: [skills, roadmap, gaps, taxonomy, governance]
summary: "Roadmap para consolidar a taxonomia de skills, reduzir drift entre mirrors e fechar lacunas de cobertura."
---

# Roadmap de Expansao de Skills

## Objetivo

Transformar `05-Skills/` na taxonomia canônica do vault para capacidades humanas e de agente, com estrutura previsivel, metadados consistentes e cobertura por dominio.

## Contrato canonico de uma skill

Cada skill deve ter, no minimo:

- visao geral;
- pre-requisitos;
- casos de uso;
- anti-padroes;
- prompts ou templates;
- checklist de execucao;
- metricas de qualidade;
- projetos relacionados;
- links de aprofundamento.

## Areas ja fortes

- `01-agentic-intelligence`
- `02-software-engineering`
- `04-knowledge-systems`
- `devops`
- `frontend`
- `ai`
- `gke-basics`
- `google-cloud-networking-observability`

## Areas que precisam de reforco

- `03-infrastructure-mcp`
- `data-engineering`
- `mobile`
- `Security`
- `Governanca`
- `obsidian-*`
- `json-canvas`
- `defuddle`
- `softskills`

## Skills ainda ausentes ou subcobertas

- prompt engineering mais operacional
- memory design e memory curation
- retrieval/RAG evaluation
- observability and alert design
- local models and inference ops
- browser automation
- data analytics and dashboarding
- product thinking
- technical writing
- workflow automation
- project operations

## Politica para `.agents` e `.continue`

1. `05-Skills/` eh a fonte canônica humana.
2. `.agents/skills` e `.continue/skills` devem ser mirrors ou bundles versionados.
3. Toda copia precisa de origem, hash ou lockfile.
4. Mudancas em skills canônicas devem refletir nos mirrors por processo controlado.
5. Drift entre camadas deve virar alerta, nao surpresa.

## Fases recomendadas

### Fase 1

- padronizar formato;
- completar hubs mais usados;
- criar inventario de lacunas.

### Fase 2

- expandir trilhas intermediarias;
- alinhar prompts, checklists e metricas;
- conectar skills com projetos.

### Fase 3

- gerar mass data de exemplos;
- criar testes e exercicios;
- medir uso real e refinar.

