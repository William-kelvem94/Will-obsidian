---
title: "Inventario Mestre do Vault"
date: 2026-06-10
updated: 2026-06-10
type: analysis
status: active
tags: [inventory, vault, coverage, maturity, audit]
summary: "Baseline operacional do vault com cobertura, densidade e prioridades de expansao."
---

# Inventario Mestre do Vault

## Snapshot verificavel

| Indicador | Valor |
|---|---:|
| Arquivos markdown detectados no vault | 1187 |
| Arquivos totais detectados no vault | 2083 |
| Tamanho total detectado | 103694531 bytes |
| Trilhas de alto nivel em `skills/` | 29 |
| Markdown em `skills/` (legacy/curado) | 225 |
| Skills curadas em `.agents/skills` | 82 |
| Skills espelhadas em `.continue/skills` | 82 |
| Markdown em `05-Skills/` | 3 |
| Markdown em `09-Sistema/` | 6 |
| Markdown em `01-Hubs/` | 10 |
| Subpastas em `raw/` | 6 |
| Subpastas em `wiki/` | 5 |
| Servidor MCP local principal | 1 |
| Camadas tecnicas principais | `09-Sistema/`, `.scripts/`, `.agents/`, `.continue/` |

## Leitura por dominio

### Knowledge layer

- `raw/` ja separa fontes em `assets`, `books`, `Clippings`, `ideas`, `papers` e `web`.
- `wiki/` ja esta preparado para `analysis`, `concepts`, `entities`, `sources` e `summaries`, mas ainda precisa de maior volume util e mais ligacoes cruzadas.
- `schema/` ja define rubricas e padroes de evolucao, o que permite escala com controle.

### Skills layer

- `skills/` tem boa cobertura inicial, especialmente em agentic intelligence, software engineering, infrastructure, knowledge systems, devops, frontend e AI.
- A profundidade eh desigual: alguns hubs ja sao quase mini-cursos, enquanto outras trilhas ainda sao apenas pontos de partida.
- O principal gap eh padronizacao de forma: estrutura, metadados, checklist, exemplos, metricas e links internos ainda variam demais entre trilhas.
- `05-Skills/` ainda funciona como a nova camada fisica canônica em construcao, entao a expansao deve priorizar padrao e indexacao antes de copiar volume.

### MCP and tool layer

- Existe um MCP vault local funcional, mas ainda falta registry, classificacao por sensibilidade, contrato por tool e estrategia multi-MCP.
- A expansao mais valiosa nao eh so adicionar tools, e sim separar classes de ferramentas por risco e por tipo de automacao.

### Technical ops layer

- `09-Sistema/` ja concentra scripts, testes, benchmarks, simuladores e schema.
- Ha uma base muito boa para virar um sistema operacional do vault, mas ainda falta consolidar saidas padronizadas e rotinas geradas.

## Mapa de maturidade

| Area | Maturidade atual | Gap principal | Proxima alavanca |
|---|---|---|---|
| Knowledge Systems | alta base, cobertura irregular | falta massa de `wiki/` com ligações fortes | ingestao em lote e analises reutilizaveis |
| Skills | boa cobertura inicial | falta padrao e expansao das trilhas rasas | normalizar estrutura e fechar gaps |
| MCPs | funcional, mas unico | falta registry e governanca de tools | catalogo multi-MCP com contratos |
| Data mass | forte intencao, pouca formalizacao | falta separacao operacional de evidence/synth/synthetic | gerar corpora e fixtures estruturados |
| Observability | scripts presentes | falta execucao recorrente e scorecards consistentes | dashboards e reports automatizados |
| Governance | schema forte | falta pipeline de promocao de regras | schema proposals e policy review |

## Prioridades de expansao

1. Formalizar registry de MCPs e contratos de ferramentas.
2. Criar geracao padronizada de inventario e cobertura.
3. Expandir `wiki/` com massa util por dominio.
4. Fechar a estrutura canônica das skills mais importantes.
5. Separar dados sintenticos de evidencias reais.
6. Automatizar scorecards, gaps e auditorias.

## Critério de "massa boa"

Uma expansao so conta quando:

- tem categoria clara;
- tem metadados consistentes;
- aponta para outro node do grafo;
- possui confianca ou status;
- entra num fluxo de manutencao;
- pode ser auditada por script.
