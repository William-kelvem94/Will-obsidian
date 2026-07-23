---
title: "Vault Health Dashboard"
icon: "lucide/activity"
tags: [system, operational, dashboard, jarvis-sistema]
date: 2026-05-03
updated: 2026-06-13
---

# 🚀 Vault Health Dashboard

## 📊 Estatísticas Gerais
```dataview
TABLE length(rows) as "Total de Notas"
FROM ""
GROUP BY ""
```

## 📂 Atividade Recente (Últimas 24h)
```dataview
LIST FROM ""
WHERE file.mday = date(today)
SORT file.mtime DESC
LIMIT 10
```

## 🏗️ Projetos Ativos
```dataview
TABLE status as "Status", priority as "Prioridade"
FROM "Projetos"
WHERE status = "Ativo"
SORT priority DESC
```

## 🛠️ Status dos Scripts
- [ ] **Daily Logger**: Rodar ao fim do dia.
- [ ] **GitHub Sync**: Rodar semanalmente.
- [ ] **Vault Cleanup**: Rodar quando houver muitos anexos órfãos.

## 🔗 Atalhos Rápidos
- [[TODO|📋 Minha Lista de Tarefas]]
- [[02-JARVIS/03-Memory/Logs/INDEX|📅 Índice de Logs]]
- [[03-Projetos|🚧 Painel de Projetos]]

---
*Atualizado dinamicamente via Dataview*

[[02-JARVIS/README|← Voltar ao Command Center]]
