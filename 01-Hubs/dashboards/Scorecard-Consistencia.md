---
title: "Scorecard de Consistência Semanal"
description: "Métricas de consistência do vault: streaks, heatmap semanal, produtividade por dia/hora"
tags: [dashboard, dataviewjs, consistencia, streak, produtividade]
updated: 2026-05-19
aliases:
  - "Scorecard de Consistência"
  - "Consistency Scorecard"
  - "D3"
---

# 📊 Scorecard de Consistência Semanal

> Métricas de consistência do vault baseadas no histórico git. Atualize executando `python .scripts/consistency_scorecard.py --update-dashboard`.

---

```dataviewjs
// ================================================================
//  DADOS — Gerados por .scripts/consistency_scorecard.py
//  Para atualizar: python .scripts/consistency_scorecard.py --update-dashboard
// ================================================================
// <DATA_START>
const DATA = {
  "generated_at": "2026-05-19T13:44:02",
  "total_commits_all_time": 87,
  "last_30_days": {
    "days_with_commits": 14,
    "total_commits": 48,
    "notes_created": 817,
    "total_possible_days": 30,
    "consistency_pct": 46.7
  },
  "last_90_days": {
    "days_with_commits": 21,
    "total_commits": 87,
    "total_possible_days": 90,
    "consistency_pct": 23.3
  },
  "streaks": {
    "current": 4,
    "longest_ever": 4,
    "longest_streak_end": "2026-04-12"
  },
  "productivity": {
    "by_day_of_week": {
      "Seg": 7,
      "Ter": 8,
      "Qua": 8,
      "Qui": 20,
      "Sex": 15,
      "Sáb": 8,
      "Dom": 21
    },
    "by_hour": {
      "0": 8,
      "1": 9,
      "10": 8,
      "11": 9,
      "12": 2,
      "13": 1,
      "14": 4,
      "15": 6,
      "16": 1,
      "17": 6,
      "18": 4,
      "19": 2,
      "2": 6,
      "20": 2,
      "21": 1,
      "22": 1,
      "23": 5,
      "3": 9,
      "9": 3
    }
  },
  "weekly_heatmap": [
    {
      "week_start": "2026-04-27",
      "week_label": "27/04",
      "days": {
        "Seg": 4,
        "Ter": 1,
        "Qua": 3,
        "Qui": 0,
        "Sex": 2,
        "Sáb": 0,
        "Dom": 2
      }
    },
    {
      "week_start": "2026-05-04",
      "week_label": "04/05",
      "days": {
        "Seg": 0,
        "Ter": 0,
        "Qua": 0,
        "Qui": 0,
        "Sex": 0,
        "Sáb": 0,
        "Dom": 0
      }
    },
    {
      "week_start": "2026-05-11",
      "week_label": "11/05",
      "days": {
        "Seg": 1,
        "Ter": 0,
        "Qua": 3,
        "Qui": 0,
        "Sex": 0,
        "Sáb": 7,
        "Dom": 3
      }
    },
    {
      "week_start": "2026-05-18",
      "week_label": "18/05",
      "days": {
        "Seg": 2,
        "Ter": 2,
        "Qua": 0,
        "Qui": 0,
        "Sex": 0,
        "Sáb": 0,
        "Dom": 0
      }
    }
  ],
  "notes_per_day": {
    "2026-05-19": 96,
    "2026-05-18": 70,
    "2026-05-17": 138,
    "2026-05-16": 299,
    "2026-05-13": 8,
    "2026-05-03": 2,
    "2026-04-29": 24,
    "2026-04-27": 34,
    "2026-04-24": 6,
    "2026-04-23": 131,
    "2026-04-21": 9
  },
  "best": {
    "most_commits_in_day": {
      "date": "2026-04-12",
      "count": 16
    },
    "most_notes_in_day": {
      "date": "2026-05-16",
      "count": 299
    },
    "longest_streak_ever": 4,
    "longest_streak_end": "2026-04-12"
  }
};
// <DATA_END>

// ================================================================
//  HELPER FUNCTIONS
// ================================================================
const DAY_KEYS = ['Seg', 'Ter', 'Qua', 'Qui', 'Sex', 'Sáb', 'Dom'];
const DAY_NAMES = ['Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado', 'Domingo'];

function heatColor(count, max) {
  if (max === 0 || count === 0) return 'var(--background-modifier-border, #3a3a3a)';
  const r = count / max;
  if (r >= 0.75) return '#2e7d32';
  if (r >= 0.50) return '#4caf50';
  if (r >= 0.25) return '#81c784';
  return '#c8e6c9';
}

function heatTextColor(count) {
  return count === 0 ? 'var(--text-muted, #888)' : '#fff';
}

function el(tag, attrs, parent) {
  const e = document.createElement(tag);
  if (attrs) {
    if (attrs.text) e.textContent = attrs.text;
    if (attrs.html) e.innerHTML = attrs.html;
    if (attrs.css) e.style.cssText = attrs.css;
    if (attrs.title) e.title = attrs.title;
    if (attrs.cls) e.className = attrs.cls;
  }
  (parent || dv.container).appendChild(e);
  return e;
}

// ================================================================
//  1. STREAK COUNTER
// ================================================================
dv.paragraph('---');
dv.header(2, '🔥 Streak Atual');

const s = DATA.streaks;
if (s.current > 0) {
  dv.paragraph(`🔥 **${s.current} dias** consecutivos com commit 🚀`);
} else {
  dv.paragraph(`💤 Nenhuma streak ativa — faça um commit hoje!`);
}
dv.paragraph(`🏆 Maior streak já registrada: **${s.longest_ever} dias**${s.longest_streak_end ? ` (terminou em ${s.longest_streak_end})` : ''}`);

// ================================================================
//  2. CONSISTENCY OVERVIEW
// ================================================================
dv.header(3, '📈 Visão Geral de Consistência');

dv.table(
  ['Período', 'Dias c/ Commits', 'Total Commits', 'Notas Criadas', 'Consistência'],
  [
    [
      'Últimos 30 dias',
      `${DATA.last_30_days.days_with_commits}/${DATA.last_30_days.total_possible_days}`,
      String(DATA.last_30_days.total_commits),
      String(DATA.last_30_days.notes_created),
      `${DATA.last_30_days.consistency_pct}%`
    ],
    [
      'Últimos 90 dias',
      `${DATA.last_90_days.days_with_commits}/${DATA.last_90_days.total_possible_days}`,
      String(DATA.last_90_days.total_commits),
      '—',
      `${DATA.last_90_days.consistency_pct}%`
    ]
  ]
);

// ================================================================
//  3. WEEKLY HEATMAP
// ================================================================
dv.paragraph('---');
dv.header(2, '🗓️ Heatmap Semanal (Commits por Dia)');

if (!DATA.weekly_heatmap || DATA.weekly_heatmap.length === 0) {
  dv.paragraph('*Ainda não há dados de heatmap. Execute o script para gerar.*');
} else {
  const maxHm = Math.max(
    ...DATA.weekly_heatmap.flatMap(w => DAY_KEYS.map(d => w.days[d] || 0)),
    1
  );

  const tbl = el('table', { css: 'width:100%;border-collapse:collapse;font-size:0.9em;' });

  const thead = tbl.createTHead();
  const headRow = thead.insertRow();
  el('th', { text: 'Semana', css: 'text-align:left;padding:6px 8px;font-weight:600;' }, headRow);
  for (const d of DAY_KEYS) {
    el('th', { text: d, css: 'text-align:center;padding:6px 4px;font-weight:600;' }, headRow);
  }

  const tbody = tbl.createTBody();
  for (const week of DATA.weekly_heatmap) {
    const tr = tbody.insertRow();
    el('td', { text: week.week_label, css: 'padding:4px 8px;white-space:nowrap;font-size:0.85em;' }, tr);
    for (const d of DAY_KEYS) {
      const count = week.days[d] || 0;
      el('td', {
        text: String(count),
        css: `text-align:center;padding:6px 4px;border-radius:4px;background:${heatColor(count, maxHm)};color:${heatTextColor(count)};font-weight:${count > 0 ? '600' : '400'};font-size:0.95em;`
      }, tr);
    }
  }
}

// ================================================================
//  4. PERSONAL BEST
// ================================================================
dv.paragraph('---');
dv.header(2, '🏅 Recordes Pessoais');

const b = DATA.best;
dv.table(
  ['Métrica', 'Valor', 'Data'],
  [
    ['🔥 Maior streak', `${b.longest_streak_ever} dias consecutivos`, b.longest_streak_end || '—'],
    ['💻 Mais commits em um dia', `${b.most_commits_in_day.count} commits`, b.most_commits_in_day.date || '—'],
    ['📝 Mais notas em um dia', `${b.most_notes_in_day.count} notas`, b.most_notes_in_day.date || '—']
  ]
);

// ================================================================
//  5. PRODUCTIVITY BY DAY OF WEEK (horizontal bar chart)
// ================================================================
dv.paragraph('---');
dv.header(2, '📊 Produtividade por Dia da Semana');

const byDay = DATA.productivity.by_day_of_week;
const dayVals = DAY_KEYS.map(k => byDay[k] || 0);
const maxDay = Math.max(...dayVals, 1);

const chartDiv = el('div', { css: 'width:100%;padding:8px 0;' });

for (let i = 0; i < DAY_KEYS.length; i++) {
  const val = dayVals[i];
  const pct = (val / maxDay) * 100;

  const row = el('div', { css: 'display:flex;align-items:center;margin:5px 0;gap:10px;' }, chartDiv);
  el('span', { text: DAY_NAMES[i], css: 'width:75px;text-align:right;font-size:0.85em;flex-shrink:0;' }, row);

  const barOuter = el('div', { css: 'flex:1;background:var(--background-modifier-border,#3a3a3a);border-radius:6px;overflow:hidden;height:24px;' }, row);
  const barInner = el('div', {
    css: `width:${Math.max(pct, val > 0 ? 8 : 0)}%;height:100%;background:linear-gradient(90deg,#66bb6a,#2e7d32);border-radius:6px;display:flex;align-items:center;justify-content:flex-end;padding-right:6px;box-sizing:border-box;min-width:${val > 0 ? '24px' : '0'};`
  }, barOuter);

  if (val > 0) {
    el('span', { text: String(val), css: 'color:#fff;font-size:0.8em;font-weight:600;line-height:24px;' }, barInner);
  }
}

// ================================================================
//  6. PRODUCTIVITY BY HOUR
// ================================================================
dv.paragraph('---');
dv.header(2, '⏰ Picos de Produtividade por Hora');

const byHour = DATA.productivity.by_hour;
const hourVals = [];
for (let h = 0; h < 24; h++) hourVals.push(byHour[String(h)] || 0);
const maxHour = Math.max(...hourVals, 1);

if (maxHour === 1 && hourVals.every(v => v === 0)) {
  dv.paragraph('*Sem dados de commits por hora. Execute o script para gerar.*');
} else {
  const grid = el('div', { css: 'display:grid;grid-template-columns:repeat(24,1fr);gap:3px;margin:8px 0;' });
  for (let h = 0; h < 24; h++) {
    const count = hourVals[h];
    el('div', {
      text: count > 0 ? String(count) : '',
      css: `text-align:center;padding:6px 2px;border-radius:4px;background:${heatColor(count, maxHour)};color:${heatTextColor(count)};font-size:0.75em;font-weight:${count > 0 ? '600' : '400'};line-height:1.2;`,
      title: `${String(h).padStart(2, '0')}:00 — ${count} commit(s)`
    }, grid);
  }

  const labels = el('div', { css: 'display:grid;grid-template-columns:repeat(24,1fr);gap:3px;font-size:0.65em;color:var(--text-muted,#888);text-align:center;' });
  for (let h = 0; h < 24; h++) {
    el('span', { text: String(h).padStart(2, '0') }, labels);
  }

  const sortedHours = Object.entries(byHour)
    .filter(([_, v]) => v > 0)
    .sort((a, b) => b[1] - a[1])
    .slice(0, 5);

  if (sortedHours.length > 0) {
    dv.paragraph(`**Horários de pico:** ${sortedHours.map(([h, c]) => `${String(h).padStart(2, '0')}h (${c})`).join(' · ')}`);
  }
}

// ================================================================
//  FOOTER
// ================================================================
dv.paragraph('---');
dv.paragraph(`*Dados gerados em ${DATA.generated_at}. Para atualizar: \`python .scripts/consistency_scorecard.py --update-dashboard\`*`);
dv.paragraph('*Dashboard alimentado por `.scripts/consistency_scorecard.py`*');
```

---

## 🔗 Links Relacionados

- [[01-Hubs/dashboards/INDEX|📊 Dashboard Principal]]
- [[01-Hubs/dashboards/Evolution-Tracker|📈 Rastreador de Evolução]]
- [[01-Hubs/dashboards/Knowledge-Heatmap|🔥 Mapa de Calor]]
- [[01-Hubs/dashboards/Gap-Analysis|🔍 Análise de Gaps]]

---

*Atualizado em {{date:2026-05-19}}.*
