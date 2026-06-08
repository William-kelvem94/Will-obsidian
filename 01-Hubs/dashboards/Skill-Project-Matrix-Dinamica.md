---
title: "Painel Dinâmico – Skills em Uso por Projeto"
tags: [painel, dataview, skills, projetos, dashboard]
updated: 2026-05-24
status: ativo
category: painel
---

# Skills em Uso por Projeto – Painel Dinâmico

> Este painel mostra, automaticamente (via Dataview), os projetos ativos vinculados a cada skill (e vice-versa). Útil para visualizar gaps, concentração de expertise, e orientar priorização/cross-skilling.

## Projetos → Skills usados
```dataview
table skills_usados as "Skills", status, deadline
from "03-Projetos/01-Ativos"
where !empty(skills_usados)
sort status asc
```

---

## Skills → Projetos Relacionados
```dataview
table projetos_relacionados as "Projetos", categoria
from "skills"
where !empty(projetos_relacionados)
sort categoria asc
```

**Como usar:**
- Preencha o campo `skills_usados: [SkillA, SkillB]` no frontmatter de cada projeto.
- Em skills, relacione com `projetos_relacionados: [ProjetoX, ProjetoY]`.

Sempre vincule este painel nos READMEs de skills e projetos.

[[INDEX]]
