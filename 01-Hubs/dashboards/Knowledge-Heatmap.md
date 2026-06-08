---
title: "🔥 Mapa de Calor do Conhecimento"
description: "Heatmap visual da proficiência por domínio, com sugestões de cores CSS"
tags: [dashboard, heatmap, proficiencia, dataview, progresso]
updated: 2026-05-18
aliases: ["Heatmap", "Knowledge Heatmap", "Mapa de Calor"]
---

# 🔥 Mapa de Calor do Conhecimento

> Matriz de proficiência por área do conhecimento. Use `#level-basic`, `#level-intermediate`, `#level-advanced` ou `#level-expert` nas notas para preencher automaticamente.

---

## 📋 Legenda de Níveis

| Nível | Tag | Cor Sugerida |
|-------|-----|-------------|
| 🟢 Beginner / Básico | `#level-basic` | `#8bc34a` |
| 🟡 Intermediate / Intermediário | `#level-intermediate` | `#ffc107` |
| 🟠 Advanced / Avançado | `#level-advanced` | `#ff9800` |
| 🔴 Expert / Especialista | `#level-expert` | `#f44336` |

---

## 1. Heatmap Automático — Contagem de Níveis por Área

```dataview
TABLE 
  length(filter(rows, (x) => contains(x.file.tags, "level-basic"))) as "🟢 Básico",
  length(filter(rows, (x) => contains(x.file.tags, "level-intermediate"))) as "🟡 Interm.",
  length(filter(rows, (x) => contains(x.file.tags, "level-advanced"))) as "🟠 Avançado",
  length(filter(rows, (x) => contains(x.file.tags, "level-expert"))) as "🔴 Expert",
  length(rows) as "Total"
FROM "Conhecimento-Geral" or "skills"
WHERE area
GROUP BY area
SORT length(rows) desc
```

---

## 2. Heatmap com DataviewJS — Porcentagem por Nível

```dataviewjs
const pages = dv.pages('("Conhecimento-Geral" or "skills") and area');
const levels = ["level-basic", "level-intermediate", "level-advanced", "level-expert"];
const levelLabels = ["🟢 Básico", "🟡 Interm.", "🟠 Avançado", "🔴 Expert"];
const areas = {};

for (const p of pages) {
  const area = p.area || "Sem área";
  if (!areas[area]) {
    areas[area] = { total: 0 };
    for (const l of levels) areas[area][l] = 0;
  }
  areas[area].total++;
  for (const l of levels) {
    if (p.file.tags && p.file.tags.includes(l)) {
      areas[area][l]++;
    }
  }
}

const rows = Object.entries(areas)
  .sort((a, b) => b[1].total - a[1].total)
  .map(([area, data]) => {
    const row = [area];
    for (const l of levels) {
      const pct = data.total > 0 ? ((data[l] / data.total) * 100).toFixed(0) : "0";
      row.push(`${data[l]} (${pct}%)`);
    }
    row.push(data.total);
    return row;
  });

dv.table(["Área", ...levelLabels, "Total"], rows);
```

---

## 3. Lista de Notas por Nível de Proficiência

### 🟢 Básico
```dataview
TABLE area as Área, file.mtime as "Última Atualização"
FROM "Conhecimento-Geral" or "skills"
WHERE contains(file.tags, "level-basic")
SORT area asc, file.mtime desc
```

### 🟡 Intermediário
```dataview
TABLE area as Área, file.mtime as "Última Atualização"
FROM "Conhecimento-Geral" or "skills"
WHERE contains(file.tags, "level-intermediate")
SORT area asc, file.mtime desc
```

### 🟠 Avançado
```dataview
TABLE area as Área, file.mtime as "Última Atualização"
FROM "Conhecimento-Geral" or "skills"
WHERE contains(file.tags, "level-advanced")
SORT area asc, file.mtime desc
```

### 🔴 Expert / Especialista
```dataview
TABLE area as Área, file.mtime as "Última Atualização"
FROM "Conhecimento-Geral" or "skills"
WHERE contains(file.tags, "level-expert")
SORT area asc, file.mtime desc
```

---

## 4. Heatmap Manual com Sugestões de Cores CSS

> *Preencha manualmente com ● (preenchido) ou ○ (vazio) para uma visualização rápida.*

| Área | 🟢 Básico | 🟡 Interm. | 🟠 Avançado | 🔴 Expert |
|------|:---------:|:----------:|:-----------:|:---------:|
| Filosofia | ● | ● | ○ | ○ |
| Psicologia | ● | ● | ● | ○ |
| Neurociência | ● | ● | ○ | ○ |
| Matemática para IA | ● | ● | ● | ○ |
| Ética | ● | ● | ● | ○ |
| Cultura e Sociedade | ● | ● | ○ | ○ |
| Economia Digital | ● | ● | ● | ○ |
| Direito e Regulação | ● | ● | ○ | ○ |
| Tecnologia e Sociedade | ● | ● | ● | ○ |
| Linguística | ● | ● | ○ | ○ |
| Programação | ● | ● | ● | ● |
| DevOps | ● | ● | ● | ○ |
| Inteligência Artificial | ● | ● | ● | ○ |
| Agentes Inteligentes | ● | ● | ● | ● |
| Sistemas de Conhecimento | ● | ● | ● | ○ |

---

## 5. CSS Customizado para Heatmap (adicione em `.obsidian/snippets/heatmap.css`)

> *Crie este arquivo e ative em Configurações → Aparência → CSS snippets para colorir a tabela.*

```css
/* Heatmap do Conhecimento — Cores por Nível */
.heatmap-basic {
  background-color: #8bc34a;
  color: #1a1a1a;
  text-align: center;
  font-weight: bold;
}
.heatmap-intermediate {
  background-color: #ffc107;
  color: #1a1a1a;
  text-align: center;
  font-weight: bold;
}
.heatmap-advanced {
  background-color: #ff9800;
  color: #fff;
  text-align: center;
  font-weight: bold;
}
.heatmap-expert {
  background-color: #f44336;
  color: #fff;
  text-align: center;
  font-weight: bold;
}
.heatmap-empty {
  background-color: #2a2a2a;
  color: #666;
  text-align: center;
}

/* Gradiente para células da tabela */
.heatmap-cell-0 { background-color: #1a1a2e; color: #555; }
.heatmap-cell-1 { background-color: #0a4d0a; color: #8bc34a; }
.heatmap-cell-2 { background-color: #3a3a00; color: #ffc107; }
.heatmap-cell-3 { background-color: #4a2a00; color: #ff9800; }
.heatmap-cell-4 { background-color: #4a0a0a; color: #f44336; }
```

---

## 6. Distribuição Geral de Níveis no Vault

```dataviewjs
const pages = dv.pages('("Conhecimento-Geral" or "skills")');
let basic = 0, interm = 0, adv = 0, expert = 0, none = 0;

for (const p of pages) {
  const tags = p.file.tags || [];
  let found = false;
  if (tags.includes("level-basic")) { basic++; found = true; }
  if (tags.includes("level-intermediate")) { interm++; found = true; }
  if (tags.includes("level-advanced")) { adv++; found = true; }
  if (tags.includes("level-expert")) { expert++; found = true; }
  if (!found) none++;
}

const total = pages.length;
dv.paragraph(`**Distribuição Geral de Proficiência** (${total} notas no total)`);
dv.table(
  ["Nível", "Quantidade", "Percentual"],
  [
    ["🟢 Básico", basic, ((basic/total)*100).toFixed(1) + "%"],
    ["🟡 Intermediário", interm, ((interm/total)*100).toFixed(1) + "%"],
    ["🟠 Avançado", adv, ((adv/total)*100).toFixed(1) + "%"],
    ["🔴 Expert", expert, ((expert/total)*100).toFixed(1) + "%"],
    ["⚪ Sem nível", none, ((none/total)*100).toFixed(1) + "%"]
  ]
);
```

---

## 7. Nível de Proficiência por Skill (SFIA)

```dataview
TABLE nivel as "Nível Atual", file.mtime as Atualizado
FROM "skills"
WHERE nivel
SORT nivel asc
```

---

## Links Relacionados

- [[01-Hubs/dashboards/INDEX|📊 Dashboard Principal]]
- [[01-Hubs/dashboards/Gap-Analysis|🔍 Análise de Gaps]]
- [[01-Hubs/dashboards/Evolution-Tracker|📈 Rastreador de Evolução]]
- [[GAPS|📋 Gaps Detectados]]
- [[05-Skills/SFIA-Mapping|📐 Mapeamento SFIA]]
- [[TAXONOMY|🏷️ Taxonomia]]

---

*Adicione `#level-basic`, `#level-intermediate`, `#level-advanced` ou `#level-expert` no frontmatter de cada nota para alimentar este heatmap automaticamente.*
