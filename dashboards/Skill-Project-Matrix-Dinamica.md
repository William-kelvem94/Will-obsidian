---
title: "Skill-Project Matrix Dinâmica"
description: "Matriz interativa skills × projetos gerada dinamicamente via DataviewJS"
tags: [dashboard, dataviewjs, skills, projetos, matriz, dinâmica]
updated: 2026-05-19
aliases:
  - "Matriz Dinâmica Skills-Projetos"
  - "Skill-Project Matrix Dinâmica"
  - "D2"
---

# 📊 Skill-Project Matrix Dinâmica

> Matriz gerada automaticamente via **DataviewJS** a partir das notas em `skills/` e `Projetos/`. Atualizada sempre que o vault é reindexado.

---

## Sumário

```dataviewjs
// === Sumário: estatísticas gerais da matriz ===
const skillPages = dv.pages('"skills/"')
  .filter(p => !p.file.path.includes('SKILL.md') && !p.file.path.includes('README.md') && !p.file.path.includes('INDEX.md'));
const projectPages = dv.pages('"Projetos/"')
  .filter(p => !p.file.path.includes('README.md') && !p.file.path.includes('INDEX.md'));

const skillsComNivel = skillPages.filter(p => p.level !== undefined || p.nivel);
const projetosVinculados = new Set();

for (const p of projectPages) {
  if (p.file.outlinks) {
    for (const link of p.file.outlinks) {
      if (String(link.path || '').startsWith('skills/')) {
        projetosVinculados.add(p.file.name);
        break;
      }
    }
  }
}
for (const s of skillPages) {
  if (s.file.outlinks) {
    for (const link of s.file.outlinks) {
      if (String(link.path || '').startsWith('Projetos/')) {
        projetosVinculados.add(link.path.replace(/\.md$/,'').split('/').pop());
      }
    }
  }
  if (s.projects && Array.isArray(s.projects)) {
    for (const proj of s.projects) {
      const match = projectPages.find(p => {
        const name = p.file.name.toLowerCase().replace(/^project_/i,'').replace(/[-_]/g,' ');
        const title = (p.title || '').toLowerCase().replace(/\s*\([^)]*\)/g,'');
        return name.includes(String(proj).toLowerCase()) || title.includes(String(proj).toLowerCase());
      });
      if (match) projetosVinculados.add(match.file.name);
    }
  }
}

const totalSkills = skillsComNivel.length;
const totalProjetos = projetosVinculados.size;
const totalCelulas = totalSkills * totalProjetos;
const celulasPreenchidas = totalCelulas; // computed below after we build the matrix

dv.span([
  `**🧠 Total de Skills com nível:** ${totalSkills}  ·  `,
  `**📁 Projetos vinculados:** ${totalProjetos}  ·  `,
  `**📐 Dimensão da matriz:** ${totalSkills} × ${totalProjetos} = ${totalCelulas} células  ·  `,
  `**📊 Densidade:** a calcular abaixo ↓`
].join(''));
```

---

## Legenda

| Emoji | Nível | Descrição |
|:-----:|:-----:|-----------|
| ⬜ | — | Sem relação entre skill e projeto |
| 🔵 | Básico / Iniciante | Skill com nível 1–2 ou iniciante |
| 🟡 | Intermediário | Skill com nível 3 ou intermediário |
| 🟢 | Avançado | Skill com nível 4–5 ou avançado |

---

## Matriz Skills × Projetos

```dataviewjs
// ================================================================
//  MATRIZ SKILLS × PROJETOS — DataviewJS
//  Lê skills/ (frontmatter: level, nivel, projects)
//  e Projetos/ (detecta wiki-links bidirecionais)
// ================================================================

// ---- 1. Coletar páginas ----
const skillPages = dv.pages('"skills/"')
  .filter(p => !p.file.path.includes('SKILL.md') && !p.file.path.includes('README.md') && !p.file.path.includes('INDEX.md'));
const projectPages = dv.pages('"Projetos/"')
  .filter(p => !p.file.path.includes('README.md') && !p.file.path.includes('INDEX.md'));

// ---- 2. Normalizar nível ----
function extrairNivel(p) {
  if (p.level !== undefined) {
    const n = Number(p.level);
    if (!isNaN(n) && n >= 1 && n <= 5) return n;
  }
  if (p.nivel) {
    const mapa = {
      'iniciante': 1, 'básico': 1, 'basico': 1,
      'intermediário': 2, 'intermediario': 2,
      'avançado': 3, 'avancado': 3
    };
    return mapa[String(p.nivel).toLowerCase().trim()] || 0;
  }
  return 0;
}

function nivelParaEmoji(n) {
  if (n >= 4) return '🟢';
  if (n >= 3) return '🟡';
  if (n >= 1) return '🔵';
  return '⬜';
}

function nivelParaTexto(n) {
  if (n >= 4) return 'Avançado';
  if (n >= 3) return 'Intermediário';
  if (n >= 1) return 'Básico';
  return '—';
}

// ---- 3. Indexar projetos por nome/variantes ----
const projectIndex = {};  // lowercase key → page
for (const p of projectPages) {
  const raw = p.file.name.toLowerCase();
  projectIndex[raw] = p;
  const semProject = raw.replace(/^project_/i, '').replace(/[-_]+/g, ' ').trim();
  if (semProject !== raw) projectIndex[semProject] = p;
  if (p.title) {
    const t = String(p.title).toLowerCase().replace(/\s*\([^)]*\)/g, '').trim();
    if (t && !projectIndex[t]) projectIndex[t] = p;
  }
}

// ---- 4. Mapear skill → projetos ----
function projetosDaSkill(s) {
  const linked = new Set();

  // 4a. Outlinks da skill para notas em Projetos/
  if (s.file.outlinks) {
    for (const link of s.file.outlinks) {
      const path = String(link.path || '');
      if (path.startsWith('Projetos/')) {
        const match = path.match(/([^/]+)\.md$/);
        if (match) linked.add(match[1].toLowerCase());
      }
    }
  }

  // 4b. Campo projects no frontmatter
  if (s.projects && Array.isArray(s.projects)) {
    for (const proj of s.projects) {
      const projStr = String(proj).toLowerCase().trim();
      for (const [key, pp] of Object.entries(projectIndex)) {
        if (key.includes(projStr) || projStr.includes(key)) {
          linked.add(pp.file.name.toLowerCase());
        }
      }
    }
  }

  return linked;
}

// ---- 5. Montar lista de skills com nível ----
const skills = [];
for (const s of skillPages) {
  const nivel = extrairNivel(s);
  if (nivel === 0) continue;
  skills.push({
    page: s,
    nivel,
    nivelTexto: nivelParaTexto(nivel),
    nivelEmoji: nivelParaEmoji(nivel),
    nome: s.file.name,
    titulo: s.title || s.file.name,
    pasta: s.file.folder,
    projetos: projetosDaSkill(s)
  });
}

// ---- 6. Montar lista de projetos vinculados ----
const projetosVinculados = new Map();
for (const sk of skills) {
  for (const projName of sk.projetos) {
    if (!projetosVinculados.has(projName)) {
      const pp = projectPages.find(p => p.file.name.toLowerCase() === projName);
      if (pp) projetosVinculados.set(projName, pp);
    }
  }
}
// Também incluir projetos que linkam para skills
for (const p of projectPages) {
  if (p.file.outlinks) {
    for (const link of p.file.outlinks) {
      if (String(link.path || '').startsWith('skills/')) {
        if (!projetosVinculados.has(p.file.name.toLowerCase())) {
          projetosVinculados.set(p.file.name.toLowerCase(), p);
        }
        break;
      }
    }
  }
}

const projetosOrdenados = [...projetosVinculados.entries()]
  .sort((a, b) => (a[1].title || a[1].file.name).localeCompare(b[1].title || b[1].file.name));

// ---- 7. Montar a matriz ----
const headers = ['Skill', 'Nível', ...projetosOrdenados.map(([,p]) => p.title || p.file.name)];
const rows = [];

for (const sk of skills) {
  const row = [
    `[[${sk.page.file.path}|${sk.titulo}]]`,
    `${sk.nivelEmoji} ${sk.nivelTexto}`
  ];
  let preenchidas = 0;
  for (const [, p] of projetosOrdenados) {
    if (sk.projetos.has(p.file.name.toLowerCase())) {
      row.push(sk.nivelEmoji);
      preenchidas++;
    } else {
      row.push('⬜');
    }
  }
  rows.push(row);
}

// ---- 8. Exibir tabela ----
dv.table(headers, rows);

// ---- 9. Atualizar densidade ----
const totalCelulas = skills.length * projetosOrdenados.length;
const totalPreenchidas = rows.reduce((acc, row) => {
  // Count non-⬜ cells (index 2+)
  return acc + row.slice(2).filter(c => c !== '⬜').length;
}, 0);
const densidade = totalCelulas > 0 ? ((totalPreenchidas / totalCelulas) * 100).toFixed(1) : '0.0';

dv.span([
  `\n\n**📊 Densidade da matriz:** ${totalPreenchidas} / ${totalCelulas} células preenchidas (${densidade}%)`
].join(''));

// ---- 10. Rodapé ----
dv.span(`\n\n*Skills sem nível definido foram ignoradas. Gerado em ${new Date().toISOString().split('T')[0]}.*`);
```

---

## Detalhamento por Skill

```dataviewjs
// Lista de todas as skills com seus projetos vinculados
const skillPages2 = dv.pages('"skills/"')
  .filter(p => !p.file.path.includes('SKILL.md') && !p.file.path.includes('README.md') && !p.file.path.includes('INDEX.md'));
const projectPages2 = dv.pages('"Projetos/"')
  .filter(p => !p.file.path.includes('README.md') && !p.file.path.includes('INDEX.md'));

const projectIndex2 = {};
for (const p of projectPages2) {
  const raw = p.file.name.toLowerCase();
  projectIndex2[raw] = p;
  const semProject = raw.replace(/^project_/i, '').replace(/[-_]+/g, ' ').trim();
  if (semProject !== raw) projectIndex2[semProject] = p;
  if (p.title) {
    const t = String(p.title).toLowerCase().replace(/\s*\([^)]*\)/g, '').trim();
    if (t && !projectIndex2[t]) projectIndex2[t] = p;
  }
}

function extrairNivel2(p) {
  if (p.level !== undefined) {
    const n = Number(p.level);
    if (!isNaN(n) && n >= 1 && n <= 5) return n;
  }
  if (p.nivel) {
    const mapa = {
      'iniciante': 1, 'básico': 1, 'basico': 1,
      'intermediário': 2, 'intermediario': 2,
      'avançado': 3, 'avancado': 3
    };
    return mapa[String(p.nivel).toLowerCase().trim()] || 0;
  }
  return 0;
}

function nivelParaEmoji2(n) {
  if (n >= 4) return '🟢';
  if (n >= 3) return '🟡';
  if (n >= 1) return '🔵';
  return '⬜';
}

function projetosDaSkill2(s) {
  const linked = new Set();
  if (s.file.outlinks) {
    for (const link of s.file.outlinks) {
      const path = String(link.path || '');
      if (path.startsWith('Projetos/')) {
        const match = path.match(/([^/]+)\.md$/);
        if (match) linked.add(match[1].toLowerCase());
      }
    }
  }
  if (s.projects && Array.isArray(s.projects)) {
    for (const proj of s.projects) {
      const projStr = String(proj).toLowerCase().trim();
      for (const [key, pp] of Object.entries(projectIndex2)) {
        if (key.includes(projStr) || projStr.includes(key)) {
          linked.add(pp.file.name.toLowerCase());
        }
      }
    }
  }
  return linked;
}

const skills2 = [];
for (const s of skillPages2) {
  const nivel = extrairNivel2(s);
  if (nivel === 0) continue;
  const projs = projetosDaSkill2(s);
  const projLinks = [...projs].map(n => {
    const pp = projectIndex2[n];
    return pp ? `[[${pp.file.path}|${pp.title || pp.file.name}]]` : n;
  });
  skills2.push([
    `[[${s.file.path}|${s.title || s.file.name}]]`,
    `${nivelParaEmoji2(nivel)} ${nivelParaTexto(nivel)}`,
    projLinks.length > 0 ? projLinks.join(', ') : '*(nenhum)*',
    s.file.folder
  ]);
}

dv.table(
  ['Skill', 'Nível', 'Projetos Vinculados', 'Pasta'],
  skills2.sort((a, b) => a[0].localeCompare(b[0]))
);
```

---

*Dashboard gerado com DataviewJS. Atualizado em 2026-05-19.*
