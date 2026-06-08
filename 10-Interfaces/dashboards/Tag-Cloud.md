---
title: "☁️ Nuvem de Tags"
description: "Tag cloud interativa com visualização por frequência e recência"
tags: [dashboard, tags, dataview, visualizacao]
updated: 2026-05-19
aliases: ["Tag Cloud", "Nuvem de Tags", "Tag-Cloud"]
---

# ☁️ Nuvem de Tags

> Mapa visual das tags mais usadas no vault. **Tamanho** = frequência. **Cor** = idade (quente = recente, fria = antiga).

---

```dataviewjs
const tagData = {};
for (const p of dv.pages("")) {
  if (p.file.tags) {
    for (const t of p.file.tags) {
      const firstSeen = p.file.ctime || dv.date("2024-01-01");
      if (!tagData[t]) {
        tagData[t] = { count: 0, firstSeen: firstSeen };
      } else {
        tagData[t].count++;
        if (firstSeen < tagData[t].firstSeen) {
          tagData[t].firstSeen = firstSeen;
        }
      }
    }
  }
}

const sortedTags = Object.entries(tagData)
  .sort((a, b) => b[1].count - a[1].count);

const top60 = sortedTags.slice(0, 60);
const totalTags = sortedTags.length;
const maxCount = top60.length > 0 ? top60[0][1].count : 1;
const minCount = top60.length > 0 ? top60[top60.length - 1][1].count : 1;

const minDate = top60.length > 0
  ? top60.reduce((min, [, d]) => d.firstSeen < min ? d.firstSeen : min, top60[0][1].firstSeen)
  : dv.date("2024-01-01");
const maxDate = top60.length > 0
  ? top60.reduce((max, [, d]) => d.firstSeen > max ? d.firstSeen : max, top60[0][1].firstSeen)
  : dv.date("2024-01-01");
const dateRange = maxDate - minDate || 1;

const countRange = maxCount - minCount || 1;

const topTag = top60.length > 0 ? top60[0] : null;

function getFontSize(count) {
  const ratio = (count - minCount) / countRange;
  return 1 + ratio * 2.5;
}

function getColor(firstSeen) {
  const age = (firstSeen - minDate) / dateRange;
  const hue = Math.round(240 - age * 240);
  return `hsl(${hue}, 75%, 55%)`;
}

function getRotation() {
  return (Math.random() * 6 - 3).toFixed(1);
}

function formatDate(d) {
  return d.toFormat("dd/MM/yyyy");
}

const searchId = "tag-cloud-search-" + Math.random().toString(36).slice(2, 8);
const cloudId = "tag-cloud-" + Math.random().toString(36).slice(2, 8);

dv.span([
  `<div style="margin-bottom: 16px;">`,
    `<input id="${searchId}" type="text" placeholder="🔍 Filtrar tags..." `,
      `style="width: 100%; padding: 8px 12px; border: 1px solid var(--background-modifier-border); border-radius: 6px; background: var(--background-primary); color: var(--text-normal); font-size: 14px; outline: none; box-sizing: border-box;" `,
      `oninput="(function(){ `,
        `const q = document.getElementById('${searchId}').value.toLowerCase(); `,
        `document.querySelectorAll('#${cloudId} a').forEach(el => { `,
          `el.style.display = el.textContent.toLowerCase().includes(q) ? '' : 'none'; `,
        `}); `,
      `})()">`,
  `</div>`
]);

dv.paragraph(`**Total de tags:** ${totalTags} | **Tags exibidas:** ${top60.length}${topTag ? ` | **Tag mais usada:** ${topTag[0]} (${topTag[1].count} vezes)` : ""}`);

const links = top60.map(([tag, data]) => {
  const cleanTag = tag.replace("#", "");
  const size = getFontSize(data.count);
  const color = getColor(data.firstSeen);
  const rot = getRotation();
  const dateStr = formatDate(data.firstSeen);
  return `<a href="${tag}" style="display: inline-block; font-size: ${size.toFixed(2)}em; color: ${color}; text-decoration: none; transform: rotate(${rot}deg); padding: 4px 8px; margin: 2px; border-radius: 4px; transition: transform 0.2s, background 0.2s; background: transparent; cursor: pointer; white-space: nowrap;" onmouseover="this.style.transform='rotate(0deg) scale(1.15)'; this.style.background='var(--background-modifier-hover)';" onmouseout="this.style.transform='rotate(${rot}deg) scale(1)'; this.style.background='transparent';" title="#${cleanTag} — ${data.count} ocorrência${data.count !== 1 ? 's' : ''} | Primeira aparição: ${dateStr}">#${cleanTag}</a>`;
});

dv.span([
  `<div id="${cloudId}" style="display: flex; flex-wrap: wrap; gap: 4px 6px; padding: 16px; align-items: center; justify-content: center; line-height: 1.6;">`,
    ...links,
  `</div>`
]);

dv.paragraph("---");

if (top60.length > 0) {
  dv.paragraph("### 🏆 Top 10 Tags");

  dv.table(
    ["Rank", "Tag", "Frequência", "Primeira aparição"],
    top60.slice(0, 10).map(([tag, data], i) => [
      `#${i + 1}`,
      tag,
      `${data.count} vez${data.count !== 1 ? "es" : ""}`,
      formatDate(data.firstSeen)
    ])
  );
}
```
