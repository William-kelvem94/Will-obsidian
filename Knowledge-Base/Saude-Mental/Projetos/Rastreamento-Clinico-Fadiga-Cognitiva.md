---
title: "🧠 Projeto - Rastreamento Clínico de Fadiga Cognitiva em Squads de Engenharia"
tags: [saudemental, organizacional, burnout, squads, engenharia, bem-estar]
date: 2026-06-05
updated: 2026-06-05
category: organizational-project
---

# 🧠 Projeto - Rastreamento Clínico de Fadiga Cognitiva & Equilíbrio em Squads de Engenharia

Este projeto documenta o framework de pesquisa, modelagem psicométrica e intervenção ativa desenvolvido para monitorar retrospectiva e prospectivamente o estresse e a exaustão física em equipes de alta performance técnica.

---

## 🎯 1. Modelagem Psicométrica Adotada

Para evitar avaliações de clima corporativo superficiais que ignoram as complexidades da depressão mental e do estresse profissional, o sistema adota instrumentos cientificamente validados adaptados para o desenvolvimento de software:

### 1.1 Maslach Burnout Inventory (MBI) - Dimensão Exaustão Emocional
A exaustão emocional ($EE$) é quantificada usando uma escala Likert de 7 pontos ($0$ a $6$), que mede a frequência dos sintomas experimentados:

$$EE\_Score = \frac{\sum_{i=1}^{9} item_i}{9}$$

Onde escores de média superiores a $3.2$ sinalizam **Exposição de Alto Risco**.

### 1.2 Utrecht Work Engagement Scale (UWES-9)
Utilizado de forma recíproca para medir o vigor, dedicação e absorção focal dos engenheiros durante rituais de desenvolvimento, garantindo que o bem-estar psicológico não seja um mero indicador negativo de fadiga, mas um impulsionador saudável de foco sustentável.

---

## 📅 2. O Pipeline de Feedback: Rituais de Coleta
O pipeline de rastreamento é estruturado para ser invisível ao desenvolvedor, incorporado aos fluxos normais de comunicação:

```
Ritual Semanal 📊 → Feedback Anônimo de 3 Questões Likert (via Slack/Discord Bot)
  └── Processamento dos Indicadores de Sobrecarga (Backlog Ratio)
        └── Gatilho Vermelho 🚨: Alerta automático para o Líder da Squad se Média EE > 3.5
              └── Plano de Ação: Redução de 25% na capacidade da Sprint subsequente (Cooldown)
```

---

## 📈 3. Resultados Práticos e Indicadores Globais

Abaixo estão relatadas as correlações históricas observadas na squad-piloto de infraestrutura durante uma intervenção de 12 semanas de Cooldown Dinâmico:

| Métrica Coletada | Baseline (Semana 1-4) | Pós-Intervenção (Semana 9-12) | Delta Semântico |
|------------------|-----------------------|-------------------------------|-----------------|
| **Índice de Exaustão ($EE$)** | $4.1$ (Alto Risco) | **$2.4$** (Moderado/Saudável)| $-41.4\%$ |
| **Throughput de Entrega** | $23$ Tarefas/Sprint | **$21$** Tarefas/Sprint | $-8.6\%$ (Estável) |
| **Taxa de Bugs Críticos** | $14\%$ em Produção | **$3\%$** em Produção | **$-78.5\%$ (Ganho de Qualidade)** |
| **Segurança Psicológica** | $2.8$ (Insuficiente) | **$4.5$** (Excepcional) | $+60.7\%$ |

### Conclusão e Lição Prática
A redução marginal de $8.6\%$ no volume nominal de entregas gerou uma redução expressiva de **$78.5\%$ na taxa de erros de software**, liberando maior tempo operacional que antes era desperdiçado com correção de incidentes e retrabalho contínuo de DevOps (Firefighting).

---

## 📋 4. Diretrizes de Governança e Links Úteis
- Mapeamento de sintomas corporativos correlatos: [[Knowledge-Base/Saude-Mental/Dicionario/Dicionario-Saude-Mental-Trabalho]]
- Protocolo ativo de intervenção na Sprint: [[Knowledge-Base/Saude-Mental/Checklists/Checklist-Mitigacao-Burnout-Squads]]
- Painel de humor do usuário: [Painel-Health-Mental-Humor.md](Ideias/Painel-Health-Mental-Humor.md)
