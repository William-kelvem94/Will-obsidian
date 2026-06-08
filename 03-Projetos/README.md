---
title: "README - Projetos"
tags: [projetos, gerenciador, dashboard, index]
updated: 2026-06-08
date: 2026-06-01
---

# Projetos

Esta e a area canonica para projetos, objetivos, planos, estudos aplicados e historico de execucao.

## Caminho principal

- [[../01-Hubs/Hub-Projetos|Hub de Projetos]]

## Subpastas

- **01-Ativos:** projetos em andamento, privados e planos de acao
- **02-Arquivo:** projetos finalizados ou de referencia
- **03-Estudos:** pesquisas, estudos experimentais e workspaces exploratorios
- **04-Master-Plan:** estrategias globais e macro-roadmaps
- **Documentacao de apoio:** README, status, decisoes, riscos e runbooks

## Regra de organizacao

Cada projeto importante deve ter:

- README ou INDEX;
- objetivo;
- status;
- stack;
- decisoes;
- riscos;
- proximos passos;
- links para conhecimento usado;
- templates de bug, ADR ou postmortem quando necessario.

## Referencias cruzadas

- Veja tambem: [[05-Skills/README]], [[01-Hubs/dashboards/INDEX]], [[../INDEX]], [[../01-Hubs/Painel-Cockpit.md]]
- Em cada projeto, use campos `skills_usados`, `deadline`, `status` no frontmatter para integracao e rastreio automatico.

## Dashboards e gestao

- [[01-Hubs/dashboards/Scorecard-Consistencia]]
- [[01-Hubs/dashboards/Skill-Project-Matrix-Dinamica]]

## Padrao recomendado

```txt
Nome-do-Projeto/
├── README.md
├── Objetivos.md
├── Roadmap.md
├── Decisoes/
├── Bugs/
├── Estudos/
├── Runbooks/
└── Reunioes/
```

> Sempre criar ou atualizar README e INDEX em cada subpasta de projeto relevante.
