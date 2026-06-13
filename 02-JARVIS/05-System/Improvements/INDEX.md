---
title: "JARVIS Improvements - Review Queue"
description: "Fila de sugestoes de melhoria geradas pelo JARVIS, dream cycle e agentes externos."
tags: [jarvis, improvements, review, queue, jarvis-sistema]
updated: 2026-06-13
status: active
date: 2026-06-01
---

# JARVIS Improvements - Review Queue

Este indice centraliza sugestoes de melhoria geradas automaticamente. Elas devem ser revisadas antes de virarem mudancas canonicas no vault ou no `PROJECT_JARVIS_5.0`.

## Regra de Uso

- Sugestoes novas devem ser criadas nesta pasta quando possivel.
- Arquivos antigos `JARVIS/Improvement_*.md` ainda existem na raiz do `JARVIS/` e devem ser tratados como backlog legado.
- Nao aplique sugestoes automaticamente em arquivos de identidade, preferencias, arquitetura ou projeto sem revisao humana.

## Backlog Legado

```dataview
TABLE file.mtime as "Atualizado"
FROM "JARVIS"
WHERE startswith(file.name, "Improvement_")
SORT file.name DESC
```

## Backlog Novo

```dataview
TABLE status as "Status", file.mtime as "Atualizado"
FROM "02-JARVIS/05-System/Improvements"
WHERE file.name != "INDEX"
SORT file.mtime DESC
```

## Fluxo de Revisao

1. Ler sugestao.
2. Classificar como `accepted`, `rejected`, `duplicate` ou `needs-research`.
3. Se aceita, transformar em issue, decisao ou nota tecnica.
4. Se virar mudanca permanente, registrar em `JARVIS/02-Operational/Decisions/`.

