---
title: "<% tp.file.title %>"
date: <% tp.date.now("YYYY-MM-DD") %>
tags: [diario, aprendizado]
updated: <% tp.date.now("YYYY-MM-DD HH:mm") %>
---

# Diário de <% tp.date.now("YYYY-MM-DD") %>

## ⚡ Check-in de Energia

- [ ] ⚡ Alta — foco sustentado, ideias fluindo
- [ ] 🔋 Média — distraível mas funcional
- [ ] 🔴 Sobrecarga — preciso desacelerar

## 🎯 Top 3 Prioridades

1.
2.
3.

## 📊 OKRs em Andamento

<%*
let okrOutput = "";
try {
  const okrPath = "Will-Pessoal/02-Visao/Objetivos/README.md";
  const okrFile = app.vault.getAbstractFileByPath(okrPath);
  if (okrFile) {
    const okrContent = await app.vault.read(okrFile);
    const lines = okrContent.split("\n");
    let currentOKR = "";
    for (const line of lines) {
      const headingMatch = line.trim().match(/^###\s+(OKR \d+:.*)/);
      if (headingMatch) {
        currentOKR = headingMatch[1];
        okrOutput += `\n### ${currentOKR}\n\n`;
        continue;
      }
      const itemMatch = line.trim().match(/^- \[([ x])\]\s+(.*)/);
      if (itemMatch && currentOKR) {
        const status = itemMatch[1] === "x" ? "✅" : "⬜";
        okrOutput += `- ${status} ${itemMatch[2]}\n`;
      }
    }
  }
} catch (e) {
  okrOutput = "_Erro ao carregar OKRs._";
}
if (!okrOutput) {
  okrOutput = "_Nenhum OKR ativo encontrado._";
}
tR += okrOutput;
%>

## ✅ Hábitos do Dia

- [ ] Acordei no horário planejado
- [ ] Revisão do dia feita
- [ ] Bloco de foco no projeto principal
- [ ] Movimento físico (≥ 20 min)
- [ ] Telas desligadas 30 min antes de dormir

## 📝 O que aprendi hoje

-

## 📓 Notas

-

## → Ações

-

<% tp.cursor %>
