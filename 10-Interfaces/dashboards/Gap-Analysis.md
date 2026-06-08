---
title: "🔍 Análise de Gaps de Conhecimento"
description: "Dashboard para identificar lacunas por área, comparar estado atual vs alvo e priorizar próximos estudos"
tags: [dashboard, gaps, analise, priorizacao, dataview, estudo]
updated: 2026-05-18
aliases: ["Gap Analysis", "Análise de Lacunas", "Priorização de Estudos"]
---

# 🔍 Análise de Gaps de Conhecimento

> Identifique tópicos ausentes, compare proficiência atual vs desejada e monte sua prioridade de estudos.

---

## 1. Gaps Automáticos — Taxonomia vs Notas Existentes

> *Gera automaticamente a partir de [[GAPS]] (produzido por `scripts/scan_gaps.py`).*

```dataview
TABLE file.ctime as "Criado em", file.mtime as "Atualizado"
FROM "GAPS"
```

```dataviewjs
// Comparação direta: áreas na taxonomia vs notas existentes
const taxonomia = [
  "Inteligência Artificial", "Machine Learning", "Segurança de Dados",
  "Automação", "Neurociência", "Gestão", "Desenvolvimento de Software",
  "Infraestrutura e DevOps", "Filosofia e Ética", "Ciência da Computação"
];

const skillsTaxonomia = [
  "RAG", "Engenharia de Prompts", "Data Cleaning", "Integração de APIs",
  "Criação de Plugins (Obsidian)", "LangChain", "PromptLayer",
  "Scikit-Learn", "Airflow", "Docker", "Kubernetes", "Terraform",
  "FastAPI", "Next.js", "React", "PostgreSQL", "pgvector",
  "Python", "TypeScript", "Ciência de Dados"
];

const allNotes = dv.pages("").map(p => p.file.name.toLowerCase());
const allTags = new Set();
for (const p of dv.pages("")) {
  if (p.file.tags) {
    for (const t of p.file.tags) allTags.add(t.toLowerCase().replace("#", ""));
  }
}

function hasCoverage(item) {
  const lower = item.toLowerCase();
  // check in note names
  for (const name of allNotes) {
    if (name.includes(lower)) return true;
  }
  // check in tags
  for (const tag of allTags) {
    if (tag.includes(lower) || lower.includes(tag)) return true;
  }
  return false;
}

const areasComCobertura = taxonomia.map(a => [a, hasCoverage(a) ? "✅ Presente" : "❌ Gap"]);
const skillsComCobertura = skillsTaxonomia.map(s => [s, hasCoverage(s) ? "✅ Presente" : "❌ Gap"]);

dv.paragraph("### Áreas da Taxonomia vs Cobertura");
dv.table(["Área", "Status"], areasComCobertura);

dv.paragraph("### Skills da Taxonomia vs Cobertura");
dv.table(["Skill", "Status"], skillsComCobertura);
```

---

## 2. Estado Atual vs Estado Desejado

> *Para usar esta seção, adicione `target-level: básico | intermediário | avançado | expert` no frontmatter das notas de skill.*

```dataview
TABLE 
  nivel as "🟢 Nível Atual",
  target-level as "🎯 Nível Alvo",
  file.mtime as "Última Atualização"
FROM "skills"
WHERE nivel AND target-level
SORT 
  choice(nivel = target-level, 0, 1) desc,
  file.mtime asc
```

### Gap de Proficiência (Diferença entre Atual e Alvo)

```dataviewjs
const levelOrder = { "básico": 1, "intermediário": 2, "avançado": 3, "expert": 4 };
const pages = dv.pages('"skills"').where(p => p.nivel && p["target-level"]);

const gaps = pages.map(p => {
  const atual = levelOrder[p.nivel] || 0;
  const alvo = levelOrder[p["target-level"]] || 0;
  const gap = Math.max(0, alvo - atual);
  return [
    p.file.link,
    p.nivel,
    p["target-level"],
    gap > 0 ? `📈 ${gap} nível(is)` : "✅ No alvo"
  ];
});

dv.table(["Skill", "Nível Atual", "Nível Alvo", "Gap"], gaps.sort((a, b) => {
  const gA = a[3].includes("📈") ? parseInt(a[3]) : 0;
  const gB = b[3].includes("📈") ? parseInt(b[3]) : 0;
  return gB - gA;
}));
```

---

## 3. Matriz de Priorização (O que Estudar Primeiro)

> *Combina: gap de proficiência + relevância + última atualização.*

```dataviewjs
const levelOrder = { "básico": 1, "intermediário": 2, "avançado": 3, "expert": 4 };
const pages = dv.pages('"skills"').where(p => p.nivel);

const prioritario = pages.map(p => {
  const atual = levelOrder[p.nivel] || 0;
  const alvo = levelOrder[p["target-level"]] || atual;
  const gap = Math.max(0, alvo - atual);
  const diasSemUpdate = p.file.mtime ? 
    Math.floor((new Date() - new Date(p.file.mtime)) / (1000*60*60*24)) : 999;
  
  // Score de prioridade: gap*10 + diasSemUpdate (maior = mais prioritário)
  const score = gap * 10 + Math.min(diasSemUpdate, 90);
  
  let prioridade;
  if (score >= 50) prioridade = "🔴 Alta";
  else if (score >= 20) prioridade = "🟡 Média";
  else if (gap > 0) prioridade = "🟢 Baixa";
  else prioridade = "✅ OK";
  
  return [
    p.file.link,
    p.nivel,
    p["target-level"] || p.nivel,
    gap > 0 ? `${gap} nível(is)` : "—",
    `${diasSemUpdate}d`,
    prioridade
  ];
});

dv.table(
  ["Skill", "Atual", "Alvo", "Gap", "Sem Atualizar", "Prioridade"],
  prioritario.sort((a, b) => {
    const ordem = { "🔴 Alta": 3, "🟡 Média": 2, "🟢 Baixa": 1, "✅ OK": 0 };
    return ordem[b[5]] - ordem[a[5]];
  })
);
```

---

## 4. Tópicos com Baixa Cobertura por Área

```dataview
TABLE 
  length(rows) as "Notas",
  join(rows.file.link, ", ") as "Notas Existentes"
FROM "Conhecimento-Geral"
GROUP BY area
SORT length(rows) asc
```

---

## 5. Notas Desatualizadas (Mais de 60 Dias)

```dataview
TABLE 
  area as Área,
  file.mtime as "Última Atualização",
  (date(today) - file.mtime).days as "Dias desde atualização"
FROM "Conhecimento-Geral" or "skills"
WHERE (date(today) - file.mtime).days > 60
SORT (date(today) - file.mtime).days desc
```

---

## 6. Áreas sem Nenhuma Nota (Gap Total)

```dataviewjs
const areasComNotas = new Set();
for (const p of dv.pages('"Conhecimento-Geral"')) {
  if (p.area) areasComNotas.add(p.area);
}

const taxonomiaAreas = [
  "Inteligência Artificial", "Machine Learning", "Segurança de Dados",
  "Automação", "Neurociência", "Gestão"
];

const semCobertura = taxonomiaAreas.filter(a => !areasComNotas.has(a));
if (semCobertura.length > 0) {
  dv.paragraph("### ❌ Áreas da Taxonomia sem Notas no Conhecimento-Geral");
  dv.list(semCobertura);
} else {
  dv.paragraph("### ✅ Todas as áreas da taxonomia têm pelo menos uma nota!");
}
```

---

## 7. Skills sem Nota Dedicada (Gap no skills/)

```dataviewjs
const skillsDir = dv.pages('"skills"').map(p => p.file.name.toLowerCase());
const skillsEssenciais = [
  "LangChain", "Scikit-Learn", "Airflow", "Dagster",
  "Terraform", "PromptLayer", "Data Cleaning"
];

const semNota = skillsEssenciais.filter(s => {
  const lower = s.toLowerCase();
  return !skillsDir.some(name => name.includes(lower));
});

if (semNota.length > 0) {
  dv.paragraph("### ❌ Skills Essenciais sem Nota Dedicada");
  dv.list(semNota.map(s => `- [ ] **${s}** — Criar nota em \`skills/\``));
} else {
  dv.paragraph("### ✅ Todas as skills essenciais têm nota dedicada!");
}
```

---

## 8. Recomendação de Próximos Passos

```dataviewjs
const now = new Date();
const trintaDias = 30;
const pages = dv.pages('("Conhecimento-Geral" or "skills") and area');
const areas = {};

for (const p of pages) {
  const area = p.area || "Sem área";
  if (!areas[area]) areas[area] = { total: 0, antigos: 0, comGap: 0 };
  areas[area].total++;
  const dias = p.file.mtime ? Math.floor((now - new Date(p.file.mtime)) / (1000*60*60*24)) : 999;
  if (dias > trintaDias) areas[area].antigos++;
}

const recomendacoes = Object.entries(areas)
  .filter(([_, v]) => v.antigos > 0)
  .sort((a, b) => b[1].antigos - a[1].antigos)
  .map(([area, data]) => [
    area,
    `${data.antigos}/${data.total}`,
    data.antigos > data.total/2 ? "🔴 Revisar urgente" : "🟡 Revisão pendente"
  ]);

dv.table(
  ["Área", "Notas Desatualizadas", "Recomendação"],
  recomendacoes
);
```

---

## 9. Checklist de Estudos Recomendados

```dataviewjs
dv.paragraph("### 🎯 Próximos Tópicos para Estudar");

// Prioridade 1: áreas com muitas notas desatualizadas
// Prioridade 2: skills com gap de proficiência
// Prioridade 3: áreas sem cobertura

const sugestoes = [
  "- [ ] **Machine Learning** — Criar nota dedicada (gap na taxonomia)",
  "- [ ] **Segurança de Dados** — Criar nota dedicada (gap na taxonomia)",
  "- [ ] **Automação** — Criar nota dedicada (gap na taxonomia)",
  "- [ ] **LangChain** — Aprofundar conhecimento prático",
  "- [ ] **Data Cleaning** — Documentar técnicas e ferramentas",
  "- [ ] **Kubernetes Avançado** — Revisar e atualizar",
  "- [ ] **Arquitetura de Agentes** — Estudar padrões multi-agente",
  "- [ ] **Observabilidade** — Práticas de monitoring e alerting"
];

dv.list(sugestoes);
```

---

## Links Relacionados

- [[dashboards/INDEX|📊 Dashboard Principal]]
- [[dashboards/Knowledge-Heatmap|🔥 Mapa de Calor]]
- [[dashboards/Evolution-Tracker|📈 Rastreador de Evolução]]
- [[GAPS|📋 Gaps Automáticos]]
- [[TAXONOMY|🏷️ Taxonomia]]
- [[skills/SFIA-Mapping|📐 Mapeamento SFIA]]

---

*Para melhores resultados, mantenha o frontmatter das notas com `area`, `nivel`, `target-level` e `status` preenchidos.*
