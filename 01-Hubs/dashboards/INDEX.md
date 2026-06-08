---
title: "Dashboard Principal — Evolução do Conhecimento"
description: "Painel central para monitorar progresso, gaps e evolução do vault"
tags: [dashboard, hub, index, dataview, progresso]
updated: 2026-05-18
aliases: ["Dashboard Central", "Painel de Evolução"]
---

# Dashboards — Navegação Central

Acesse painéis críticos do vault, scoring, health, queries dinâmicas Dataview e monitore tudo num só lugar.

- [[01-Hubs/dashboards/Skill-Project-Matrix-Dinamica|Skills em uso por Projeto – Matrix Dinâmica]]
- [[01-Hubs/dashboards/Arquivos-Orfaos|Painel – Arquivos Órfãos/Manutenção]]
- [[01-Hubs/dashboards/Scorecard-Consistencia]]
- [[01-Hubs/dashboards/TOKEN-COST-DASHBOARD|💰 Token Cost — Monitoramento de Custos]]
- [[01-Hubs/Painel-Cockpit]]  

Consulte o [[INDEX]] central para navegação geral dos hubs.

---

# 📊 Dashboard Principal do Conhecimento

> Visão unificada de todas as notas, áreas, status e tags do vault.

---

## 1. Visão Geral — Notas por Área

```dataview
TABLE rows.file.link as Notas, length(rows) as Total
FROM "Conhecimento-Geral" or "skills" or "Projetos"
GROUP BY area
SORT length(rows) desc
```

---

## 2. Notas por Status de Progresso

```dataview
TABLE file.link as Nota, area as Área, status as Status, file.mtime as "Última Atualização"
FROM "Conhecimento-Geral" or "skills"
WHERE status
SORT status asc, file.mtime desc
```

---

## 3. Porcentagem de Conclusão por Domínio

> *Nota: Para usar esta seção, adicione `status: concluído | em_andamento | rascunho` no frontmatter das notas.*

```dataview
TABLE 
  length(filter(rows, (x) => x.status = "concluído")) as "✅ Concluído",
  length(filter(rows, (x) => x.status = "em_andamento")) as "🔄 Em Andamento",
  length(filter(rows, (x) => x.status = "rascunho")) as "📝 Rascunho",
  length(rows) as "Total"
FROM "Conhecimento-Geral" or "skills"
WHERE status
GROUP BY area
SORT length(rows) desc
```

```dataviewjs
// Cálculo percentual de conclusão por área
const pages = dv.pages('("Conhecimento-Geral" or "skills") and status');
const areas = {};

for (const p of pages) {
  const area = p.area || "Sem área";
  if (!areas[area]) areas[area] = { total: 0, concluido: 0 };
  areas[area].total++;
  if (p.status === "concluído") areas[area].concluido++;
}

dv.table(
  ["Área", "Total", "Concluído", "% Conclusão"],
  Object.entries(areas)
    .sort((a, b) => b[1].total - a[1].total)
    .map(([area, data]) => [
      area,
      data.total,
      data.concluido,
      (data.concluido / data.total * 100).toFixed(1) + "%"
    ])
);
```

---

## 4. Progresso Baseado em Tags

```dataview
TABLE length(rows) as "Total de Notas"
FROM "Conhecimento-Geral" or "skills" or "Projetos"
GROUP BY tags
SORT length(rows) desc
LIMIT 30
```

---

## 5. Últimas Notas Modificadas (Todas as Áreas)

```dataview
TABLE file.etags as Tags, file.folder as Pasta
FROM ""
SORT file.mtime desc
LIMIT 20
```

---

## 6. Distribuição por Domínio do Conhecimento

```dataview
TABLE length(rows) as "Notas", join(rows.file.link, ", ") as Arquivos
FROM "Conhecimento-Geral"
GROUP BY area
SORT length(rows) desc
```

---

## 7. Skills — Distribuição por Categoria

```dataview
TABLE length(rows) as Skills
FROM "skills"
GROUP BY file.folder
SORT length(rows) desc
```

---

## 8. Projetos — Visão Rápida

```dataview
TABLE file.ctime as Criado, file.mtime as Atualizado
FROM "Projetos"
SORT file.mtime desc
LIMIT 15
```

---

## 9. Mapa de Calor de Navegação (Tags Mais Frequentes)

```dataviewjs
const tagCount = {};
for (const p of dv.pages("")) {
  if (p.file.tags) {
    for (const t of p.file.tags) {
      tagCount[t] = (tagCount[t] || 0) + 1;
    }
  }
}

const sorted = Object.entries(tagCount)
  .sort((a, b) => b[1] - a[1])
  .slice(0, 40);

dv.table(
  ["Tag", "Frequência"],
  sorted.map(([tag, count]) => [tag, count])
);
```

---

## 10. Notas Órfãs (Sem Área Definida)

```dataview
TABLE file.folder as Pasta, file.etags as Tags
FROM "Conhecimento-Geral" or "skills"
WHERE !area
SORT file.folder asc
```

---

## Atalhos Rápidos

- [[01-Hubs/dashboards/Knowledge-Heatmap|🔥 Mapa de Calor do Conhecimento]]
- [[01-Hubs/dashboards/Gap-Analysis|🔍 Análise de Gaps]]
- [[01-Hubs/dashboards/Evolution-Tracker|📈 Rastreador de Evolução]]
- [[GAPS|📋 Gaps Detectados (auto-scan)]]
- [[TAXONOMY|🏷️ Taxonomia do Vault]]

---

*Dashboard gerado com [Dataview](https://blacksmithgu.github.io/obsidian-dataview/) — atualizado em {{date:YYYY-MM-DD}}.*
