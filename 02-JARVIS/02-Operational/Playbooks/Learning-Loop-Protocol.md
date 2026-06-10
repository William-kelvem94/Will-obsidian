---
tags: [playbook, jarvis, learning, optimization, jarvis-operacao]
title: "Learning Loop Protocol (LLP)"
date: 2026-06-09
updated: 2026-06-10
---

# Learning Loop Protocol (LLP)

O LLP é o mecanismo de "estômago" do vault: ele digere a experiência bruta de projetos e a transforma em conhecimento estruturado.

## 🔄 O Ciclo de Feedback

### Fase 1: Captura de Incidente/Sucesso (03-Projetos)
Ao finalizar uma task ou resolver um bug crítico:
1. Registrar o evento em `03-Projetos/01-Ativos/` no formato:
   - **O que aconteceu?** (Sintoma/Resultado)
   - **Por que aconteceu?** (Causa Raiz)
   - **Como foi resolvido?** (Ação)
   - **Qual a lição atemporal?** (Insight)

### Fase 2: Destilação (02-JARVIS)
O agente JARVIS deve processar a nota de projeto e perguntar:
- *"Esta lição se aplica a outros projetos?"* $\to$ Se sim, mover para **04-Conhecimentos**.
- *"Esta lição requer uma nova habilidade?"* $\to$ Se sim, atualizar **05-Skills**.

### Fase 3: Injeção (04-Conhecimentos / 05-Skills)
O insight é movido para a nota atômica correspondente.
- **Exemplo:** Um erro de concorrência no Projeto X torna-se uma regra de ouro em `04-Conhecimentos/02-Engenharia-de-Software/Concorrencia-e-Paralelismo.md`.

## 🛠️ Gatilhos de Execução
- **Semanalmente:** Revisão de `02-JARVIS/02-Operational/Challenges/` para extrair padrões.
- **Post-Mortem:** Sempre que um projeto for movido para `08-Arquivo`.

## 📈 Métrica de Sucesso
O vault é considerado "inteligente" quando a solução para um problema novo é encontrada via link de um problema antigo, sem necessidade de nova pesquisa externa.
