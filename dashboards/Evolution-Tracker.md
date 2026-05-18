---
title: "📈 Rastreador de Evolução do Conhecimento"
description: "Acompanhe seu progresso mensal, notas recentes por área e streaks de estudo"
tags: [dashboard, evolucao, progresso, streak, dataview, estudo]
updated: 2026-05-18
aliases: ["Evolution Tracker", "Rastreador de Progresso", "Monthly Review"]
---

# 📈 Rastreador de Evolução do Conhecimento

> Monitore seu progresso ao longo do tempo, visualize notas recentes e mantenha streaks de estudo.

---

## 1. Progresso Mensal — Notas Criadas por Mês

```dataview
TABLE 
  length(rows) as "Notas Criadas",
  join(rows.file.link, ", ") as "Arquivos"
FROM ""
WHERE file.ctime >= date(today) - dur(30 days)
GROUP BY date(file.ctime, "yyyy-MM") as Mês
SORT Mês desc
```

### Últimos 12 Meses

```dataviewjs
const hoje = new Date();
const meses = {};
const mesesNomes = [
  "Jan", "Fev", "Mar", "Abr", "Mai", "Jun",
  "Jul", "Ago", "Set", "Out", "Nov", "Dez"
];

for (let i = 0; i < 12; i++) {
  const d = new Date(hoje.getFullYear(), hoje.getMonth() - i, 1);
  const key = `${d.getFullYear()}-${String(d.getMonth()+1).padStart(2, "0")}`;
  meses[key] = { label: `${mesesNomes[d.getMonth()]}/${d.getFullYear()}`, count: 0 };
}

for (const p of dv.pages("")) {
  if (p.file.ctime) {
    const c = new Date(p.file.ctime);
    const key = `${c.getFullYear()}-${String(c.getMonth()+1).padStart(2, "0")}`;
    if (meses[key]) meses[key].count++;
  }
}

const sorted = Object.entries(meses).reverse();
const maxCount = Math.max(...sorted.map(([_, v]) => v.count), 1);

dv.table(
  ["Mês", "Notas", "Barra"],
  sorted.map(([_, v]) => [
    v.label,
    v.count,
    "█".repeat(Math.round(v.count / maxCount * 20))
  ])
);
```

---

## 2. Notas Modificadas Recentemente por Área

### Últimos 7 Dias

```dataview
TABLE 
  area as Área,
  file.folder as Pasta,
  file.mtime as "Modificado"
FROM ""
WHERE file.mtime >= date(today) - dur(7 days)
SORT file.mtime desc
```

### Últimos 30 Dias

```dataview
TABLE 
  area as Área,
  file.folder as Pasta,
  file.mtime as "Modificado"
FROM ""
WHERE file.mtime >= date(today) - dur(30 days)
SORT file.mtime desc
LIMIT 30
```

### Últimas Modificações por Área (Agrupado)

```dataview
TABLE 
  length(rows) as "Modificações",
  date(max(rows.file.mtime)) as "Mais Recente"
FROM "Conhecimento-Geral" or "skills"
WHERE file.mtime >= date(today) - dur(30 days)
GROUP BY area
SORT max(rows.file.mtime) desc
```

---

## 3. Streak de Estudo

```dataviewjs
// Calcula streak de estudo baseado em dias com modificações
const dias = {};
for (const p of dv.pages("")) {
  if (p.file.mtime) {
    const d = new Date(p.file.mtime);
    const key = `${d.getFullYear()}-${String(d.getMonth()+1).padStart(2,"0")}-${String(d.getDate()).padStart(2,"0")}`;
    dias[key] = true;
  }
}

const hoje = new Date();
let streak = 0;
let streakStart = null;
let d = new Date(hoje);

// Check if studied today
const hojeKey = `${d.getFullYear()}-${String(d.getMonth()+1).padStart(2,"0")}-${String(d.getDate()).padStart(2,"0")}`;
const estudouHoje = !!dias[hojeKey];

// Count consecutive days backward
while (true) {
  const key = `${d.getFullYear()}-${String(d.getMonth()+1).padStart(2,"0")}-${String(d.getDate()).padStart(2,"0")}`;
  if (dias[key]) {
    streak++;
    if (!streakStart) streakStart = key;
    d.setDate(d.getDate() - 1);
  } else {
    break;
  }
}

dv.paragraph(`## 🔥 Streak de Estudo`);

if (streak > 0) {
  dv.paragraph(`**${streak} dia(s) consecutivo(s)**${estudouHoje ? " (incluindo hoje! 🎉)" : " (última atualização: " + streakStart + ")"}`);
} else {
  dv.paragraph("Nenhum streak ativo. Estude hoje para começar um! 📚");
}

// Mostrar os últimos 14 dias
dv.paragraph("### Últimos 14 Dias");
const calendar = [];
for (let i = 13; i >= 0; i--) {
  const dia = new Date(hoje.getFullYear(), hoje.getMonth(), hoje.getDate() - i);
  const key = `${dia.getFullYear()}-${String(dia.getMonth()+1).padStart(2,"0")}-${String(dia.getDate()).padStart(2,"0")}`;
  const diaSemana = ["Dom", "Seg", "Ter", "Qua", "Qui", "Sex", "Sáb"][dia.getDay()];
  const ativo = !!dias[key];
  calendar.push(`${diaSemana} ${String(dia.getDate()).padStart(2,"0")} ${ativo ? "🟢" : "⚪"}`);
}

dv.paragraph(calendar.join(" · "));
```

---

## 4. Evolução Mensal por Área

```dataviewjs
const hoje = new Date();
const mesAtual = `${hoje.getFullYear()}-${String(hoje.getMonth()+1).padStart(2,"0")}`;
const mesPassado = new Date(hoje.getFullYear(), hoje.getMonth() - 1, 1);
const mesAnterior = `${mesPassado.getFullYear()}-${String(mesPassado.getMonth()+1).padStart(2,"0")}`;

const areas = {};

for (const p of dv.pages('("Conhecimento-Geral" or "skills") and area')) {
  const area = p.area || "Sem área";
  if (!areas[area]) areas[area] = { total: 0, mesAtual: 0, mesAnterior: 0 };
  areas[area].total++;
  
  if (p.file.mtime) {
    const m = new Date(p.file.mtime);
    const key = `${m.getFullYear()}-${String(m.getMonth()+1).padStart(2,"0")}`;
    if (key === mesAtual) areas[area].mesAtual++;
    if (key === mesAnterior) areas[area].mesAnterior++;
  }
}

dv.table(
  ["Área", "Total", `Modificadas ${mesAnterior}`, `Modificadas ${mesAtual}`, "Tendência"],
  Object.entries(areas)
    .sort((a, b) => b[1].total - a[1].total)
    .map(([area, data]) => {
      let tendencia = "➡️ Estável";
      if (data.mesAtual > data.mesAnterior) tendencia = "📈 Crescendo";
      if (data.mesAtual < data.mesAnterior) tendencia = "📉 Caindo";
      if (data.mesAtual === 0 && data.mesAnterior === 0) tendencia = "⚪ Inativo";
      return [area, data.total, data.mesAnterior, data.mesAtual, tendencia];
    })
);
```

---

## 5. Notas Novas vs Revisadas (Últimos 30 Dias)

```dataviewjs
const trintaDias = 30;
const novas = [];
const revisadas = [];

for (const p of dv.pages("")) {
  if (p.file.ctime) {
    const diasCriacao = Math.floor((new Date() - new Date(p.file.ctime)) / (1000*60*60*24));
    if (diasCriacao <= trintaDias) {
      novas.push([p.file.link, p.file.folder, p.file.ctime]);
    }
  }
  if (p.file.mtime && p.file.ctime) {
    const diasMod = Math.floor((new Date() - new Date(p.file.mtime)) / (1000*60*60*24));
    const diasCriacao = Math.floor((new Date() - new Date(p.file.ctime)) / (1000*60*60*24));
    // Revisada: modificada nos últimos 30 dias mas criada há mais de 30 dias
    if (diasMod <= trintaDias && diasCriacao > trintaDias) {
      revisadas.push([p.file.link, p.file.folder, p.file.mtime]);
    }
  }
}

dv.paragraph(`### 🆕 Notas Novas (${novas.length})`);
dv.table(["Nota", "Pasta", "Criado em"], novas.sort((a, b) => b[2] - a[2]).slice(0, 15));

dv.paragraph(`### 🔄 Notas Revisadas (${revisadas.length})`);
dv.table(["Nota", "Pasta", "Revisado em"], revisadas.sort((a, b) => b[2] - a[2]).slice(0, 15));
```

---

## 6. Marcadores de Progresso

```dataview
TABLE 
  area as Área,
  status as Status,
  file.mtime as "Última Atualização",
  (date(today) - file.mtime).days as "Dias desde atualização"
FROM "Conhecimento-Geral" or "skills"
WHERE status
SORT status asc, file.mtime desc
```

---

## 7. Resumo de Atividade Semanal

```dataviewjs
const hoje = new Date();
const inicioSemana = new Date(hoje);
inicioSemana.setDate(hoje.getDate() - hoje.getDay()); // Domingo

let totalSemana = 0;
let areasSemana = new Set();
let pastasSemana = new Set();

for (const p of dv.pages("")) {
  if (p.file.mtime) {
    const m = new Date(p.file.mtime);
    if (m >= inicioSemana) {
      totalSemana++;
      if (p.area) areasSemana.add(p.area);
      pastasSemana.add(p.file.folder);
    }
  }
}

dv.paragraph("### 📅 Resumo desta Semana");
dv.paragraph(`- **Total de modificações:** ${totalSemana}`);
dv.paragraph(`- **Áreas trabalhadas:** ${areasSemana.size}`);
dv.paragraph(`- **Pastas modificadas:** ${pastasSemana.size}`);
dv.paragraph(`- **Streak atual:** ${totalSemana > 0 ? "🔥 Ativo" : "⚪ Inativo"}`);
```

---

## 8. Linha do Tempo de Atividades

```dataview
TABLE 
  file.folder as Pasta,
  file.mtime as "Data"
FROM ""
WHERE file.mtime >= date(today) - dur(7 days)
SORT file.mtime desc
LIMIT 25
```

---

## 9. Metas de Estudo

> *Adicione `target: "YYYY-MM-DD"` e `target-level` no frontmatter das skills para acompanhar metas.*

```dataview
TABLE 
  nivel as "Nível Atual",
  target-level as "Meta",
  target as "Prazo",
  (date(target) - date(today)).days as "Dias Restantes"
FROM "skills"
WHERE target
SORT (date(target) - date(today)).days asc
```

---

## Links Relacionados

- [[dashboards/INDEX|📊 Dashboard Principal]]
- [[dashboards/Knowledge-Heatmap|🔥 Mapa de Calor]]
- [[dashboards/Gap-Analysis|🔍 Análise de Gaps]]
- [[Objetivos/OKRs|🎯 OKRs e Metas]]
- [[Objetivos/90-dias|📆 Plano 90 Dias]]

---

*Mantenha hábitos de estudo consistentes! Cada nota modificada conta para seu streak diário. 🚀*
