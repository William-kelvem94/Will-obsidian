---
title: "Hub de Projetos (MOC)"
description: "Mapa de Conteúdo para todos os projetos públicos e privados."
tags: [hub, projetos, moc]
updated: 2026-04-21
---

# 🛠️ Hub de Projetos — [[Will-Pessoal/01-Identidade/Perfil/Cerebro-Will|Cérebro Will]] 

## 📡 Radar de Projetos (Ativos)
```dataview
TABLE
  priority as "Prioridade",
  status as "Status",
  area as "Área",
  file.mtime as "Última Modificação"
FROM "Projetos/01-Ativos" OR "Projetos/03-Estudos"
WHERE contains(tags, "projetos") OR contains(tags, "privados")
SORT priority asc, file.mtime desc
```

## 📂 Coleções por Categoria

### 🚀 01. Ativos (Em Execução)
- [[Projetos/01-Ativos/Privados/README|MOC Privados]] — Projetos de alto valor.
- [[Projetos/01-Ativos/Python/README|Python Stack]] — Automações e scripts ativos.

### 📚 03. Estudos & Roadmaps
- [[Projetos/03-Estudos/EstudosFocados/README|Estudos Focados]] — Diário de bordo técnico.
- [[Projetos/03-Estudos/EstudosPesquisas/README|Estudos e Pesquisas]] — Referências de mercado.

### 🗄️ 02. Arquivo Histórico
- [[Projetos/02-Arquivo/PHP/README|Legacy PHP]] — CRUDs e sistemas antigos.
- [[Projetos/02-Arquivo/Java/README|Legacy Java]] — Atividades acadêmicas.
- [[Projetos/02-Arquivo/Outros/README|Outros]] — Design e projetos variados.

---

## 📈 Inteligência de Repositórios
- [[Projetos/04-Master-Plan/GitHub-Completo|📦 Inventário GitHub]] — Mapeamento de 67 repositórios.
- [[Projetos/04-Master-Plan/Organizacao-Completa|📐 Planejamento de Estrutura]] — Visão de longo prazo.

## 🩺 Health Check & Skills Gap

> Relatório gerado automaticamente por `project_health_checker.py`.

![[.logs/skills_gap.md]]

**Links:** [[Bem-vindo]] | [[Projetos/01-Ativos/Plano-de-Acao|🚀 Plano de Ação]] | [[Vault-Ops]]
