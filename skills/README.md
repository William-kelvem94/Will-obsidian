---
tags: [skills, hub, index]
updated: 2026-04-29
title: "🧠 Skills - Taxonomia Pessoal"
date: 2026-04-27
---

# 🧠 Skills - Taxonomia Pessoal

Esta base converge competências técnicas e estratégicas em um inventário vivo, pronto para alimentar o growth do seu segundo cérebro.

## 📂 Dashboard de Skills
```dataview
TABLE
  category as "Categoria",
  level as "Nível",
  description as "Descrição",
  projects as "Projetos Práticos"
FROM "skills"
WHERE file.name != "README" AND file.name != "SFIA-Mapping"
SORT category asc, level desc
```

## 🗺️ Mapeamento SFIA (Skills Framework for the Information Age)
| Categoria SFIA | Subcategoria | Minha Skill Correspondente |
|----------------|--------------|---------------------------|
| Strategy & architecture | Enterprise architecture | [[skills/devops/FinOps|FinOps]] |
| Development & implementation | Systems design | [[skills/frontend/Web-Components|Web Components]] |
| Delivery & operation | Service operation | [[skills/devops/FinOps|FinOps]] |
| Data management | Data modeling | [[skills/ai/MLOps|MLOps]] |
| Digital strategy | Artificial intelligence | [[skills/ai/Engenharia-de-Prompts|Engenharia de Prompts]] |

---

## 🚀 Próximos passos
- Use `Templates/Skill-Template.md` para criar novas notas de skill.
- Mantenha o frontmatter completo e vincule skills relacionadas.
- Registre projetos práticos em `projects` para conectar aprendizado e execução.

---

*Mantenha suas skills afiadas. O progresso é iterativo.*
