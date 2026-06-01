---
title: "Produtividade — Pomodoro Dashboard"
description: "Dashboard de pomodoros agregado das notas diárias"
tags: [dashboard, dataviewjs, produtividade, pomodoro, perfil]
updated: 2026-06-01
date: 2026-06-01
---

# 🍅 Produtividade — Pomodoro Tracker

> Dashboard agregado de pomodoros a partir das notas diárias (`#diario`).

---

## 📈 Visão Geral

```dataviewjs
const today = dv.date("today");
const startThisWeek = today.minus({ days: today.weekday - 1 });
const endThisWeek = startThisWeek.plus({ days: 6 });
const startLastWeek = startThisWeek.minus({ days: 7 });
const endLastWeek = startThisWeek.minus({ days: 1 });
const startMonth = dv.date({ year: today.year, month: today.month, day: 1 });

const pages = dv.pages("#diario")
  .where(p => p.date)
  .sort(p => p.date);

const data = [];
for (const p of pages) {
  for (const t of p.file.tasks) {
    if (!t.tags || !t.tags.some(tag => tag.replace("#", "") === "pomodoro")) continue;
    const countMatch = t.text.match(/(\d+)\s*pomodor/);
    const count = countMatch ? parseInt(countMatch[1]) : 0;
    let project = t.text
      .replace(/\d+\s*pomodor\w*/g, "")
      .replace(/#\w+/g, "")
      .replace(/[:–—-]\s*$/, "")
      .trim();
    if (!project && count === 0) continue;
    data.push({
      date: dv.date(p.date),
      project: project || "Sem projeto",
      count: count,
      completed: t.status === "x"
    });
  }
}

if (data.length === 0) {
  dv.paragraph("Nenhum pomodoro registrado ainda. Preencha os pomodoros nas notas diárias com a tag `#pomodoro`.");
} else {
  const thisWeek = data.filter(d => d.date >= startThisWeek && d.date <= endThisWeek);
  const lastWeek = data.filter(d => d.date >= startLastWeek && d.date <= endLastWeek);
  const thisMonth = data.filter(d => d.date >= startMonth);

  const totalThisWeek = thisWeek.reduce((s, d) => s + d.count, 0);
  const totalLastWeek = lastWeek.reduce((s, d) => s + d.count, 0);
  const totalThisMonth = thisMonth.reduce((s, d) => s + d.count, 0);

  let trend = "➡️ Estável";
  if (totalThisWeek > totalLastWeek) trend = "📈 Mais que semana passada";
  if (totalThisWeek < totalLastWeek) trend = "📉 Menos que semana passada";
  if (totalLastWeek === 0 && totalThisWeek > 0) trend = "🚀 Começou esta semana";
  if (totalThisWeek === 0 && totalLastWeek > 0) trend = "💤 Nada esta semana";

  dv.table(
    ["Métrica", "Valor"],
    [
      ["🍅 Pomodoros esta semana", `${totalThisWeek} (${trend})`],
      ["📆 Pomodoros este mês", String(totalThisMonth)],
      ["⏱ Horas de foco (esta semana)", `${(totalThisWeek * 25 / 60).toFixed(1)}h`],
      ["📅 Dias com pomodoro (esta semana)", `${thisWeek.length > 0 ? new Set(thisWeek.map(d => d.date.toFormat("yyyy-MM-dd"))).size : 0}/7`]
    ]
  );
}
```

---

## 📊 Por Projeto

```dataviewjs
const today = dv.date("today");
const pages = dv.pages("#diario").where(p => p.date);

const data = [];
for (const p of pages) {
  for (const t of p.file.tasks) {
    if (!t.tags || !t.tags.some(tag => tag.replace("#", "") === "pomodoro")) continue;
    const countMatch = t.text.match(/(\d+)\s*pomodor/);
    const count = countMatch ? parseInt(countMatch[1]) : 0;
    let project = t.text
      .replace(/\d+\s*pomodor\w*/g, "")
      .replace(/#\w+/g, "")
      .replace(/[:–—-]\s*$/, "")
      .trim();
    if (!project && count === 0) continue;
    data.push({
      date: dv.date(p.date),
      project: project || "Sem projeto",
      count: count
    });
  }
}

if (data.length > 0) {
  const perProject = {};
  for (const d of data) {
    if (!perProject[d.project]) perProject[d.project] = 0;
    perProject[d.project] += d.count;
  }
  const sorted = Object.entries(perProject).sort((a, b) => b[1] - a[1]);
  dv.table(
    ["Projeto", "Pomodoros", "Horas", "Barra"],
    sorted.map(([proj, qtd]) => [
      proj,
      String(qtd),
      (qtd * 25 / 60).toFixed(1) + "h",
      "🍅".repeat(Math.min(qtd, 15))
    ])
  );
}
```

---

## 📋 Últimos 7 Dias

```dataviewjs
const today = dv.date("today");
const pages = dv.pages("#diario").where(p => p.date);

const data = [];
for (const p of pages) {
  for (const t of p.file.tasks) {
    if (!t.tags || !t.tags.some(tag => tag.replace("#", "") === "pomodoro")) continue;
    const countMatch = t.text.match(/(\d+)\s*pomodor/);
    const count = countMatch ? parseInt(countMatch[1]) : 0;
    if (count > 0) {
      data.push({ date: dv.date(p.date), count });
    }
  }
}

const rows = [];
for (let i = 6; i >= 0; i--) {
  const day = today.minus({ days: i });
  const dayStr = day.toFormat("yyyy-MM-dd");
  const dayTotal = data
    .filter(d => d.date.toFormat("yyyy-MM-dd") === dayStr)
    .reduce((s, d) => s + d.count, 0);
  const dayName = ["Dom", "Seg", "Ter", "Qua", "Qui", "Sex", "Sáb"][day.weekday % 7];
  rows.push([
    `${dayName} ${day.toFormat("dd/MM")}`,
    String(dayTotal),
    dayTotal > 0 ? "🍅".repeat(Math.min(dayTotal, 10)) : "—"
  ]);
}
dv.table(["Dia", "Pomodoros", ""], rows);
```

---

## 📈 Tendência Semanal

```dataviewjs
const today = dv.date("today");
const pages = dv.pages("#diario").where(p => p.date);

const data = [];
for (const p of pages) {
  for (const t of p.file.tasks) {
    if (!t.tags || !t.tags.some(tag => tag.replace("#", "") === "pomodoro")) continue;
    const countMatch = t.text.match(/(\d+)\s*pomodor/);
    const count = countMatch ? parseInt(countMatch[1]) : 0;
    if (count > 0) data.push({ date: dv.date(p.date), count });
  }
}

// Group by week
const weeks = {};
for (const d of data) {
  const weekStart = d.date.minus({ days: d.date.weekday - 1 });
  const weekKey = weekStart.toFormat("yyyy-'W'WW");
  if (!weeks[weekKey]) weeks[weekKey] = { start: weekStart, total: 0 };
  weeks[weekKey].total += d.count;
}

const sortedWeeks = Object.entries(weeks).sort(([a], [b]) => a.localeCompare(b));
if (sortedWeeks.length >= 2) {
  const last2 = sortedWeeks.slice(-2);
  const prev = last2[0][1].total;
  const curr = last2[1][1].total;
  let diff = curr - prev;
  let arrow = diff > 0 ? "📈" : diff < 0 ? "📉" : "➡️";
  dv.paragraph(`${arrow} **${curr}** pomodoros esta semana vs **${prev}** na anterior (${diff > 0 ? "+" : ""}${diff})`);
} else if (sortedWeeks.length === 1) {
  dv.paragraph(`📊 **${sortedWeeks[0][1].total}** pomodoros nesta semana`);
} else {
  dv.paragraph("Nenhum dado semanal disponível");
}

// Show last 8 weeks
if (sortedWeeks.length > 0) {
  const recentWeeks = sortedWeeks.slice(-8).reverse();
  dv.table(
    ["Semana", "Pomodoros", "Barra"],
    recentWeeks.map(([key, w]) => [
      key,
      String(w.total),
      "🍅".repeat(Math.min(w.total, 15))
    ])
  );
}
```

---

*Dashboard gerado automaticamente via DataviewJS. Atualizado em `= date(today)`.*
