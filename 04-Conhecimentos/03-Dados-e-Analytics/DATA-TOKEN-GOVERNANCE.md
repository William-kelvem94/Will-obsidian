---
title: "📊 Data & Token Governance — Eficácia, Eficiência, Controle e Gerência"
tags: [data-governance, token-governance, eficacia, eficiencia, controle, gerencia, data-management, cost-control]
date: 2026-06-01
updated: 2026-06-01
category: knowledge-domain
aliases: ["Governança de Dados e Tokens", "Data Token Control", "Eficácia e Eficiência"]
related: ["04-Conhecimentos/TOKEN-ECONOMY", "04-Conhecimentos/TOKEN-SHORTHAND", "02-JARVIS/TOKEN-COMPRESSION", "05-Skills/04-knowledge-systems/INDEX"]
---

# 📊 Data & Token Governance — Eficácia, Eficiência, Controle e Gerência

Sistema unificado de governança para maximizar eficácia e eficiência de dados + tokens em operações com IA. Cobre controle granular, gerência de ciclo de vida, métricas de performance e auditoria contínua.

---

## 🎯 1. Eficácia vs Eficiência — Definições Operacionais

| Conceito | Definição | Aplicação em IA | Métrica Chave |
|----------|-----------|-----------------|---------------|
| **Eficácia** | Fazer a coisa certa. Resultado atende ao objetivo. | Resposta da IA resolve o problema do usuário | Taxa de acerto, relevância semântica |
| **Eficiência** | Fazer certo. Mínimo recurso para máximo resultado. | Menos tokens/dados para mesma qualidade | Tokens por resposta, custo por query |
| **Controle** | Visibilidade e governança sobre o sistema. | Monitoramento, alertas, limites, versionamento | Cobertura de monitoria, tempo de detecção |
| **Gerência** | Ciclo de vida, planejamento e alocação. | Budgeting, priorização, retenção, evolução | Custo total, tempo de retenção, ROI |

```
Equilíbrio Ideal:
  Eficácia ≥ 90% (qualidade aceitável)
  Eficiência ≥ 4:1 (compressão)
  Controle ≥ 95% (cobertura de monitoria)
  Gerência = ciclo contínuo (planejar → executar → medir → ajustar)
```

---

## 💾 2. Governança de Dados — Eficácia e Controle

### 2.1 Dimensões da Qualidade de Dados (Data Efficacy)

| Dimensão | Definição | Métrica | Verificação |
|----------|-----------|---------|-------------|
| **Acurácia** | Dados refletem a realidade | % de registros corretos | Amostragem + validação cruzada |
| **Completude** | Todos os campos necessários preenchidos | % de campos não-nulos | `df.isnull().sum() / len(df)` |
| **Consistência** | Dados coerentes entre fontes | % de registros consistentes | Regras de integridade referencial |
| **Atualidade** | Dados refletem o momento correto | Idade média dos dados | `NOW() - updated_at` |
| **Relevância** | Dados são pertinentes ao problema | % útil para a tarefa | Feedback loop do modelo |
| **Unicidade** | Sem duplicatas | % de duplicatas | Hash-based dedup |
| **Validade** | Dados respeitam regras de negócio | % dentro do domínio | Schema validation |

### 2.2 Pipeline de Qualidade (Data Quality Gates)

```
Source → Gate 1: Schema Validation → Gate 2: Completeness Check
  → Gate 3: Uniqueness Check → Gate 4: Consistency Check
    → Gate 5: Freshness Check → Storage/Use
      ↓ Reprovado em qualquer gate → Dead Letter Queue + Alerta
```

### 2.3 Data Lineage — Rastreabilidade

```
Rastrear: Origem → Transformação → Consumo → Arquivamento/Exclusão

Ferramentas:
  - manual: YAML manifesto em cada dataset
  - automático: Great Expectations + dbt docs + DataHub

Formato Mínimo de Lineage:
  dataset: nome
  source: "origem (db, api, file)"
  transformations:
    - step: "descrição"
      date: YYYY-MM-DD
      by: "pessoa/agente"
  consumers: ["pipeline_X", "modelo_Y", "dashboard_Z"]
  retention_days: 90
  sensitivity: low|medium|high
```

### 2.4 Data Contracts

```
Contrato entre produtor e consumidor de dados:

dataset:
  name: nome_do_dataset
  owner: "time/agente responsável"
  schema:
    campo: { type: string, nullable: false, description: "..." }
  slas:
    freshness: < 1h (tempo máximo desde última atualização)
    completeness: > 99%
    accuracy: > 95%
  notification:
    on_breach: slack/channel/email
    on_schema_change: block + notify
```

---

## 🔢 3. Governança de Tokens — Eficiência e Controle

### 3.1 Token Budgeting — Alocação por Camada

```
Token Budget Total (ex: 100K tokens/dia)
│
├─ System Prompts: 10% (10K/dia)
│   ├── Agent Identity: 500t x 5 sessões = 2.5K
│   └── Project Context: 1.5K x 5 sessões = 7.5K
│
├─ Queries/Inferência: 50% (50K/dia)
│   ├── Análise: 30% (15K)
│   ├── Geração Código: 40% (20K)
│   ├── Pesquisa: 20% (10K)
│   └── Outros: 10% (5K)
│
├─ RAG Retrieval: 20% (20K/dia)
│   ├── Chunks: 15K
│   └── Re-ranking context: 5K
│
├─ Memória/Histórico: 15% (15K/dia)
│   ├── Sessão atual: 8K
│   └── Histórico recente: 7K
│
└─ Buffer/SLA: 5% (5K/dia)
```

### 3.2 Token Cost Monitoring

```yaml
monitoring:
  metrics:
    - tokens_por_sessao
    - tokens_por_task_type
    - custo_por_modelo
    - eficiencia: output_tokens / input_tokens
    - taxa_compressao: raw_tokens / final_tokens
  alerts:
    - threshold: custo_diario > limite
      action: "reduzir ctx, trocar modelo, notificar"
    - threshold: tokens_sessao > ctx_window * 0.8
      action: "sumarizar histórico, iniciar nova sessão"
    - threshold: eficiencia < 2:1
      action: "revisar prompt, aplicar compressão"
  logging:
    - formato: JSON estruturado
    - campos: timestamp, model, task, tokens_in, tokens_out, cost, latency
    - retenção: 90 dias
    - storage: logs/token_cost/
```

### 3.3 Cost-Benefit por Modelo

| Provedor | Modelo | Custo Input/1M tokens | Custo Output/1M tokens | Eficácia | Ideal para |
|----------|--------|----------------------|-----------------------|----------|------------|
| OpenAI | GPT-4o | $2.50 | $10.00 | 95% | Pesquisa complexa, código crítico |
| OpenAI | GPT-4o-mini | $0.15 | $0.60 | 85% | Análise rápida, tarefas simples |
| Anthropic | Claude 3.5 Sonnet | $3.00 | $15.00 | 94% | Análise profunda, documentos longos |
| Anthropic | Claude 3.5 Haiku | $0.80 | $4.00 | 82% | Classificação, extração rápida |
| Google | Gemini 2.0 Flash | $0.10 | $0.40 | 80% | Volume alto, tarefas simples |
| Google | Gemini 2.0 Pro | $2.00 | $8.00 | 90% | Raciocínio complexo |
| Local | Llama 3.1 70B | $0 (GPU) | $0 (GPU) | 78% | Privacidade, volume alto |
| Local | Mistral 7B | $0 (CPU) | $0 (CPU) | 65% | Testes, tarefas offline |

### 3.4 Estratégia Híbrida (Custo × Eficácia)

```
Casca de decisão para roteamento inteligente:

Task Complexity?
├── Simple (classificação, extração, formatação)
│   └── → Modelo barato: GPT-4o-mini / Gemini Flash / Haiku
│
├── Medium (análise, geração código simples)
│   ├── Budget OK → GPT-4o / Sonnet
│   └── Budget tight → GPT-4o-mini + CoT
│
├── Complex (arquitetura, pesquisa profunda, código crítico)
│   ├── Prioridade qualidade → GPT-4o / Sonnet / Gemini Pro
│   └── Prioridade privacidade → Llama 70B local
│
└── Batch (grande volume, sem urgência)
    └── → Modelo local + fila assíncrona
```

---

## ⚙️ 4. Sistema de Controle

### 4.1 Controles de Qualidade (Efficacy Gates)

```
Antes da execução:
  [ ] Input validation: dados de entrada dentro do schema esperado
  [ ] Context check: contexto suficiente para resposta adequada
  [ ] Model routing: modelo correto para a complexidade da task

Durante a execução:
  [ ] Token budget monitor: não estourou limite da sessão
  [ ] Latency check: resposta dentro do SLA
  [ ] Intermediate validation: outputs parciais coerentes

Após a execução:
  [ ] Output validation: formato respeita schema
  [ ] Semantic check: resposta relevante ao input
  [ ] Cost log: registrar custo real
  [ ] Feedback loop: usuário confirmou/ajustou?
```

### 4.2 Controles de Custo (Efficiency Gates)

```yaml
cost_controls:
  hard_limits:
    max_tokens_por_sessao: 8000
    max_tokens_por_dia: 100000
    max_custo_por_dia: $5.00
    max_custo_por_mes: $100.00
  
  soft_limits:
    alerta_80pct_diario: true
    sugerir_modelo_mais_barato: true
    comprimir_ctx_automatico: true
  
  auto_actions:
    ao_atingir_80pct_diario: "reduzir ctx em 50%"
    ao_atingir_100pct_diario: "bloquear tarefas não-críticas"
    ao_atingir_limite_sessao: "sumarizar + arquivar + nova sessão"
```

### 4.3 Auditoria e Compliance

```
Registro de Auditoria (imutável):

session_id: "UUID"
timestamp: ISO-8601
agent: "JARVIS | WK"
task_type: "analise | codigo | pesquisa | config"
model: "gpt-4o | sonnet | local"
tokens: { input: N, output: N, total: N }
cost: $X.XXXX
duration_ms: N
quality_score: 0-100 (auto + human feedback)
violations: []
artifacts: ["path/to/output"]
```

---

## 📋 5. Gerência de Ciclo de Vida

### 5.1 Data Lifecycle

```
[1] INGEST → [2] VALIDATE → [3] PROCESS → [4] STORE → [5] USE → [6] ARCHIVE → [7] DELETE
    │            │              │            │         │         │            │
    ├─ Coleta    ├─ Schema      ├─ Clean     ├─ Hot    ├─ Query   ├─ Cold     ├─ Purge
    ├─ Recebe    ├─ Quality     ├─ Transform ├─ Warm   ├─ Train   ├─ Compress ├─ GDPR
    └─ Capture   └─ Dedup       └─ Enrich    └─ Cold   └─ Infer   └─ Glacier  └─ Retention
```

**Política de Retenção:**
| Tipo | Hot (rápido) | Warm (acesso ocasional) | Cold (arquivo) | Delete |
|------|-------------|------------------------|----------------|--------|
| Dados de treino | 30 dias | 90 dias | 1 ano | 2 anos |
| Logs de inferência | 7 dias | 30 dias | 90 dias | 1 ano |
| Memórias de agente | 7 dias | 30 dias | 180 dias | 1 ano |
| Documentos | 90 dias | 1 ano | 5 anos | Never* |
| Código | Forever | - | - | - |

### 5.2 Token Budget Lifecycle (Mensal)

```
Semana 1: Alocar budget mensal por categoria
  ├── Análise: 30%
  ├── Código: 35%
  ├── Pesquisa: 20%
  ├── Operacional: 10%
  └── Buffer: 5%

Semana 2: Revisar consumo parcial
  ├── Categorias dentro do budget → continuar
  └── Categorias acima → reduzir frequência ou trocar modelo

Semana 3: Ajustes finos
  ├── Identificar tarefas de baixo retorno
  └── Migrar para modelo mais barato ou batch local

Semana 4: Fechamento + Aprendizado
  ├── Relatório de consumo real vs planejado
  ├── Ajustar alocação para o próximo mês
  └── Atualizar métricas de eficiência
```

---

## 📊 6. Métricas Compostas (Eficácia × Eficiência)

### 6.1 Scorecard Unificado

```yaml
scorecard:
  data_quality_score:
    formula: "avg(accuracy, completeness, consistency, freshness, relevance)"
    target: "> 0.90"
  
  token_efficiency_score:
    formula: "output_relevant_tokens / total_tokens"
    target: "> 0.40"
  
  cost_effectiveness_score:
    formula: "tasks_completed / total_cost"
    target: "> 50 tasks/$1"
  
  control_coverage:
    formula: "gates_passed / gates_total"
    target: "> 0.95"
  
  governance_maturity:
    levels:
      - 1: "Ad-hoc (sem controle)"
      - 2: "Reativo (monitora após incidente)"
      - 3: "Proativo (alertas e limites)"
      - 4: "Automático (correção autônoma)"
      - 5: "Preditivo (antecipa problemas)"
    target: "Level 4"
```

### 6.2 OKRs de Governança

```
Objetivo: Maximizar eficácia com mínimo consumo de recursos

KR1: Eficácia média ≥ 90% (medido por feedback + autoavaliação)
KR2: Taxa de compressão ≥ 4:1 em todas as interações
KR3: Custo mensal dentro do budget (±10%)
KR4: 100% das sessões com auditoria registrada
KR5: Zero violação de limite sem notificação
KR6: Data quality score ≥ 0.90 para todos os datasets ativos
```

---

## 🔄 7. Ciclo de Melhoria Contínua (Feedback Loop)

```
[Monitor] → [Analyze] → [Plan] → [Act] → [Monitor]...
    │           │          │        │
    ├─ Coleta    ├─ Ident.  ├─ Priori-├─ Implementa
    ├─ Métricas  ├─ Gap     ├─ tizar  ├─ Automatiza
    ├─ Alertas   ├─ Causa   ├─ Budget └─ Documenta
    └─ Logs      └─ Raiz    └─ Timeline

Periodicidade:
  Diário: revisão de custo token + qualidade sessão
  Semanal: análise de tendências + ajuste fino
  Mensal: relatório completo + realocação de budget
  Trimestral: revisão de estratégia + novas ferramentas
```

---

## 🔗 Crosslinks

- [[04-Conhecimentos/03-Dados-e-Analytics/TOKEN-ECONOMY]] — Estratégias de otimização de tokens
- [[04-Conhecimentos/03-Dados-e-Analytics/TOKEN-SHORTHAND]] — Abreviações padronizadas
- [[02-JARVIS/TOKEN-COMPRESSION]] — Compressão de contexto JARVIS
- [[99-Templates/Legado/Template-Prompt-Otimizado]] — Template de prompt enxuto
- [[05-Skills/04-knowledge-systems/INDEX]] — Sistemas de conhecimento e RAG
- [[05-Skills/data-engineering/INDEX]] — Engenharia de dados
- [[05-Skills/devops/FinOps]] — FinOps em nuvem
- [[05-Skills/ai/LLMOps]] — LLMOps e monitoramento
- [[INDEX]]
