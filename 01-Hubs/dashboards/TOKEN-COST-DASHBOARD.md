---
title: "💰 Token Cost Dashboard — Monitoramento de Custos de Tokens"
tags: [dashboard, token-economy, cost, monitoring, dataview]
date: 2026-06-01
updated: 2026-06-01
category: dashboard
aliases: ["Token Cost Monitor", "Painel de Custos de Tokens"]
related: ["04-Conhecimentos/DATA-TOKEN-GOVERNANCE", "04-Conhecimentos/TOKEN-ECONOMY"]
---

# 💰 Token Cost Dashboard — Monitoramento de Custos

> Painel para rastrear, analisar e otimizar gastos com tokens em interações com IAs.

---

## 📊 1. Resumo Rápido

```dataviewjs
// Resumo de custos (placeholder - preencher com dados reais)
const costs = {
  today: { tokens: 0, cost: 0, sessions: 0 },
  week: { tokens: 0, cost: 0, sessions: 0 },
  month: { tokens: 0, cost: 0, sessions: 0 },
  budget: { monthly: 100, daily: 5 }
};

dv.span(`### Hoje: **${costs.today.cost}** (${costs.today.tokens} tokens, ${costs.today.sessions} sessões)`);
dv.span(`\n### Semana: **${costs.week.cost}** (${costs.week.tokens} tokens, ${costs.week.sessions} sessões)`);
dv.span(`\n### Mês: **${costs.month.cost}** (${costs.month.tokens} tokens, ${costs.month.sessions} sessões)`);
dv.span(`\n### Budget: \`\${costs.budget.monthly}/mês\` | Restante: \`${costs.budget.monthly - costs.month.cost}\``);
```

---

## ⚡ 2. Tabela de Preços por Provedor

| Provedor | Modelo | Input/1M tok | Output/1M tok | Ctx Window | Ideal para |
|----------|--------|-------------|--------------|------------|------------|
| **OpenAI** | GPT-4o | $2.50 | $10.00 | 128K | Pesquisa complexa, código |
| **OpenAI** | GPT-4o-mini | $0.15 | $0.60 | 128K | Rapid tasks, simple analysis |
| **Anthropic** | Claude 3.5 Sonnet | $3.00 | $15.00 | 200K | Análise profunda, long docs |
| **Anthropic** | Claude 3.5 Haiku | $0.80 | $4.00 | 200K | Classificação, extração |
| **Google** | Gemini 2.0 Flash | $0.10 | $0.40 | 1M | High volume, simple |
| **Google** | Gemini 2.0 Pro | $2.00 | $8.00 | 2M | Complex reasoning |
| **Local** | Llama 3.1 70B | $0 (GPU) | $0 (GPU) | 128K | Privacy, high volume |
| **Local** | DeepSeek Coder V2 | $0 (GPU) | $0 (GPU) | 128K | Code, self-hosted |

---

## 💡 3. Calculadora de Economia

| Estratégia | Antes | Depois | Economia |
|-----------|-------|--------|----------|
| Prompt em YAML vs prosa | 500 tok | 180 tok | **64%** |
| Shorthand (abreviações) | 300 tok | 210 tok | **30%** |
| Sumarização de histórico | 2000 tok | 400 tok | **80%** |
| RAG com threshold 0.75 | 2500 tok | 750 tok | **70%** |
| Model routing (task certa) | GPT-4o toda task | Mini + 4o | **40-80%** |
| Cache de contexto | Sem cache | Com cache | **50-70%** |

---

## 📈 4. Últimas Sessões (Log)

```dataview
TABLE 
  date as "Data",
  tokens_in as "Tok In",
  tokens_out as "Tok Out",
  total_tokens as "Total",
  cost as "Custo",
  model as "Modelo",
  duration_ms as "Duração"
FROM "logs/token_cost"
SORT date DESC
LIMIT 20
```

> Logs salvos em `logs/token_cost/` — formato JSON estruturado.

---

## 🚨 5. Alertas e Limites Ativos

| Tipo | Limite | Ação | Status |
|------|--------|------|--------|
| Custo diário | $5.00 | Reduzir ctx 50% | ✅ Ativo |
| Custo mensal | $100.00 | Bloquear tasks não-críticas | ✅ Ativo |
| Tokens/sessão | 8K | Sumarizar + arquivar | ✅ Ativo |
| Eficiência mínima | 2:1 | Revisar prompt | ✅ Ativo |
| Sessões longas | > 30min | Sugerir pausa | 🔲 Inativo |

---

## ⚙️ 6. Configuração de Budget

```yaml
budget_config:
  provider_limits:
    openai:
      max_daily: "$3.00"
      max_monthly: "$60.00"
    anthropic:
      max_daily: "$2.00"
      max_monthly: "$40.00"
    local:
      max_daily: "$0 (electricity)"
      max_monthly: "$0 (electricity)"

  task_allocation:
    analysis: 30%
    code: 35%
    research: 20%
    operational: 10%
    buffer: 5%

  auto_routing:
    - if_complexity_simple: "gpt-4o-mini"
    - if_complexity_medium: "gpt-4o"
    - if_complexity_complex: "claude-sonnet"
    - if_privacy_required: "local-llama"
```

---

## 🔗 Crosslinks

- [[04-Conhecimentos/03-Dados-e-Analytics/DATA-TOKEN-GOVERNANCE]] — Governança de dados e tokens
- [[04-Conhecimentos/03-Dados-e-Analytics/TOKEN-ECONOMY]] — Estratégias de otimização
- [[04-Conhecimentos/03-Dados-e-Analytics/TOKEN-SHORTHAND]] — Abreviações padronizadas
- [[01-Hubs/dashboards/INDEX]] — Central de dashboards
- [[INDEX]]
