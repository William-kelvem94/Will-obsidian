---
title: "Painel – Arquivos Órfãos e Não Referenciados (Dataview)"
tags: [painel, dataview, órfãos, arquivos, limpeza]
updated: 2026-05-24
status: ativo
category: painel
---

# Painel – Arquivos Órfãos e Não Referenciados

> Lista automática de notas não referenciadas no INDEX nem linkadas por outros MOCs, útil para manutenção e reciclagem.

```dataview
TABLE file.name, file.mtime as Modificado
WHERE !contains(file.outlinks, "INDEX")
  AND !contains(file.outlinks, "README")
  AND !contains(file.path, "/.obsidian/")
  AND !contains(file.path, "/Templates/")
  AND !contains(file.tags, "template")
  AND !contains(file.tags, "README")
  AND !contains(file.name,"Painel")
  AND !contains(file.name,"INDEX")
SORT file.mtime desc
```

Acione esta query periodicamente para identificar órfãos e manter a saúde do vault.

[[INDEX]]
