---
title: "Mapa de Maturidade e Gaps"
date: 2026-06-10
updated: 2026-06-10
type: analysis
status: active
tags: [gaps, maturity, roadmap, vault, strategy]
summary: "Mapa prático das maiores lacunas do vault e da ordem sugerida para preencher cada uma."
---

# Mapa de Maturidade e Gaps

## 1. Knowledge

**Estado atual**
- arquitetura clara de `raw`, `wiki` e `schema`;
- varios pontos de conhecimento ja estruturados;
- conteudo ainda desigual entre dominios.

**Gap principal**
- falta massa consistente de notas sinteticas com links e perguntas abertas.

**O que produzir**
- sources por dominio;
- concepts reutilizaveis;
- entities para pessoas, projetos e sistemas;
- analysis pages com comparacoes, decisao e contradicoes.

## 2. Skills

**Estado atual**
- ha taxonomia ampla e varias trilhas boas;
- `01-agentic-intelligence`, `02-software-engineering`, `04-knowledge-systems`, `devops`, `frontend` e `ai` ja tem densidade razoavel.

**Gap principal**
- ausencia de contrato unico de skill e cobertura irregular nas trilhas menores.

**O que produzir**
- template canonical de skill;
- trilhas rasas expandidas;
- mapa de relacao skill -> projeto;
- metricas de uso e cobertura.

## 3. MCPs

**Estado atual**
- um servidor vault bem util;
- ferramentas suficientes para operar o proprio vault.

**Gap principal**
- falta registry, versao e separacao de risco entre classes de MCP.

**O que produzir**
- catalogo de MCPs;
- contratos de tool;
- allowlists;
- logs e testes por connector.

## 4. Mass data

**Estado atual**
- ha fontes, ideias, dashboards, simuladores e scripts.

**Gap principal**
- falta separar claramente evidencia real, sintese e dados sintenticos para benchmark.

**O que produzir**
- fixtures;
- corpora de teste;
- notas estruturadas em massa;
- analises que possam ser regeneradas.

## 5. Observability

**Estado atual**
- scripts de monitoramento, scorecards e limpeza ja existem.

**Gap principal**
- falta um loop recorrente de execucao, validacao e publicacao.

**O que produzir**
- dashboards de cobertura;
- detector de orfaos;
- scorecard de consistencia;
- auditoria de links e tags;
- relatorios semanais.

## Prioridade executiva

| Ordem | Foco | Resultado esperado |
|---|---|---|
| 1 | MCP registry | governanca de ferramentas |
| 2 | inventory generator | baseline confiavel |
| 3 | skill standardization | escala consistente |
| 4 | wiki mass generation | conhecimento utilizavel |
| 5 | synthetic fixture layer | testes e benchmarks |
| 6 | observability loops | manutencao continua |

