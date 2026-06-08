---
title: "💰 Token Economy — Guia Definitivo de Otimização de Tokens para IAs"
tags: [token-economy, otimizacao, contexto, eficiencia, prompt-engineering, cost-efficiency, RAG, compression]
date: 2026-06-01
updated: 2026-06-01
category: knowledge-domain
aliases: ["Economia de Tokens", "Token Optimization", "Context Window Economy"]
related: ["04-Conhecimentos/Knowledge-Base/TOKEN-SHORTHAND", "02-JARVIS/JARVIS/TOKEN-COMPRESSION", "99-Templates/Legado/Template-Prompt-Otimizado"]
---

# 💰 Token Economy — Maximizar Qualidade, Minimizar Tokens

Estratégias sistematizadas para reduzir consumo de tokens sem perder riqueza semântica, complexidade ou precisão. Projetado para LLMs, sistemas RAG e agentes autônomos.

---

## 📊 Princípio Fundamental

```
Qualidade_da_Resposta ∝ (Informacao_Relevante / Tokens_Consumidos)
```

Cada token deve carregar **máxima densidade informacional**. Remover ruído é tão importante quanto adicionar contexto.

---

## 🔢 1. Anatomia do Custo de Tokens

| Componente | % Típica | Estratégia de Redução |
|-----------|----------|----------------------|
| System Prompt | 10-25% | Enxuto, modular, referências externas |
| Histórico/Contexto | 30-50% | Sumarização, sliding window, RAG seletivo |
| Instrução/Pergunta | 5-15% | Direta, sem rodeios, template mínimo |
| Output esperado (formato) | 5-10% | Schema enxuto, sem boilerplate |
| Dados de entrada | 15-40% | Pré-filtragem, chunking inteligente, hash |

---

## 🎯 2. Estratégias Core

### 2.1 Poda Estrutural

| Técnica | Redução | Impacto na Qualidade |
|---------|---------|---------------------|
| Remover saudações/cortesia | 2-5% | Nulo |
| Eliminar redundância intra-prompt | 10-20% | Positivo |
| Substituir prosa por schemas (JSON/YAML) | 30-50% | Neutro a positivo |
| Remover adj. e adv. desnecessários | 5-10% | Neutro |
| Usar abbreviations padronizadas | 10-20% | Neutro (com glossário) |
| Comprimir listas em ranges/regras | 15-30% | Neutro |

### 2.2 Hierarquia de Inclusão Contextual

```
Priority 1 (SEMPRE incluir)
├── Identidade do agente + Objetivo atual
├── Comando/instrução central
├── Schema de output esperado
└── Dados essenciais (mínimo viável)

Priority 2 (Incluir se relevante)
├── Histórico recente (últimas N interações)
├── Contexto de projeto ativo
└── Restrições/regras de negócio

Priority 3 (Incluir sob demanda)
├── Tutoriais/documentação
├── Exemplos extensos
├── Dados históricos completos
└── Glossários completos (referenciar, não embutir)
```

### 2.3 Compressão Semântica (Lossy Controlada)

| Nível | Compressão | Uso |
|-------|-----------|-----|
| **Lossless** | 1:1 | Instruções críticas, schemas, comandos |
| **Light** | 2:1 ~ 3:1 | Contexto geral, descrições de projeto |
| **Medium** | 5:1 ~ 10:1 | Histórico, logs, memorias antigas |
| **Heavy** | 10:1 ~ 30:1 | Dados brutos, documentos longos (RAG) |
| **Ultra** | 30:1+ | Embeddings + retrieval (não usar no prompt) |

---

## 🧩 3. Técnicas por Componente

### 3.1 System Prompt Enxuto

**❌ Ruim (~200 tokens):**
```
Você é um assistente de IA especializado em análise de dados que deve ajudar o usuário a interpretar métricas de desempenho de vendas... (continua)
```

**✅ Otimizado (~60 tokens):**
```yaml
role: data-analyst
expertise: [sales-analytics, kpi-interpretation]
constraints:
  - use_plain_language
  - cite_numbers_raw
  - max_3_recommendations
tone: direct
```

### 3.2 Few-Shot Comprimido

**❌ Ruim:**
```json
// Exemplo 1 de classificação de sentimento
Input: "Eu amei o produto, funcionou perfeitamente!"
Output: Positivo
```

**✅ Otimizado:**
```
SENT->LABEL:
"amei o produto perfeito"->POS
"odiei o suporte horrivel"->NEG
"ate que funciona normal"->NEU
```

### 3.3 Chain-of-Thought Compressed

**❌ Ruim:**
```
Let's think step by step. First, we need to analyze the problem. 
Then we consider the options. After that, we evaluate each one...
```

**✅ Otimizado:**
```
REASON: [step1 -> step2 -> step3 -> conclusion]
```

### 3.4 RAG Chunk Otimizado

```
Chunk size ideal: 256-512 tokens (vs 1000+ comum)
Overlap: 10-15% (vs 20-25% comum)
Formato: [TITLE]\n[KEYWORDS]\n[BODY - max 300t]
Pré-filtragem: Similarity threshold > 0.7
Max chunks: 3-5 por consulta
```

---

## 🔤 4. Shorthand & Abbreviações Padrão

→ Ver [[04-Conhecimentos/Knowledge-Base/TOKEN-SHORTHAND]] (lista completa de abreviações padronizadas)

### Amostra Rápida

| Escrita Normal | Shorthand | Economia |
|---------------|-----------|----------|
| with respect to | w.r.t. | 75% |
| as soon as possible | ASAP | 70% |
| in other words | i.e. | 65% |
| for example | e.g. | 60% |
| based on | b/o | 60% |
| does not | dont | 30% |
| regarding | re: | 60% |
| implementation | impl | 50% |
| configuration | cfg | 60% |
| documentation | docs | 60% |
| development | dev | 55% |
| production | prod | 55% |
| repository | repo | 55% |
| technology | tech | 50% |
| management | mgmt | 50% |

---

## 📐 5. Formatos de Alta Densidade

### 5.1 YAML > JSON > Prosa
```
Prosa: 120 tokens
JSON: 80 tokens  (33% menos)
YAML: 50 tokens  (58% menos)
```

### 5.2 Tabelas Markdown Compactas
```
| Item | Qtd | Status |
|------|-----|--------|
| Alpha | 12 | ok |
| Beta | 5 | wip |
vs.
Items: Alpha(12,ok), Beta(5,wip)  ← 40% menos tokens
```

### 5.3 Named Entity Shorthand
```
Sistema de siglas para entidades frequentes:
- WJ = Will JARVIS (agente)
- WK = William Kelvem (humano)
- VO = Vault Obsidian
- PS = Problem Statement
- AC = Acceptance Criteria
- TSK = Task
- PRJ = Project
- SPR = Sprint
- EP = Epic
- US = User Story
```

---

## ⚙️ 6. Estratégias para Context Window

### 6.1 Sliding Window Inteligente
```
Window: 8K tokens
├── System (500t) — fixo
├── Current Task (1000t) — variável
├── Recent History (3000t) — sliding (últimas N interações)
├── Retrieved Context (2500t) — RAG dinâmico
└── Buffer (1000t) — output + margem
```

### 6.2 Sumarização Recursiva
```
raw_text (5000t)
  → summary_v1 (800t)
    → summary_v2 (200t)
      → bullet_points (50t)
```
Usar para: logs extensos, históricos de conversa, relatórios longos.

### 6.3 Cache de Contexto
```
Cache Layer:
  Session: instruções do projeto atual
  Day: histórico do dia + decisões recentes
  Week: metas semanais + blockers
  Project: escopo, arquitetura, stakeholders
```
Reidratar apenas o nível necessário.

---

## 🤖 7. Para Interações com LLMs Locais

Contexto local (7B-13B) exige ainda mais disciplina:

| Modelo | Context Max | Recomendado | Taxa Compressão |
|--------|------------|-------------|-----------------|
| Llama 3.1 8B | 128K | <8K efetivo | 16:1 |
| Mistral 7B | 32K | <4K efetivo | 8:1 |
| Qwen 2.5 7B | 128K | <8K efetivo | 16:1 |
| DeepSeek Coder | 16K | <4K efetivo | 4:1 |
| Phi-4 | 16K | <4K efetivo | 4:1 |

---

## 📋 8. Checklist de Pré-Envio

Antes de enviar um prompt, verificar:

- [ ] Remover cortesia/saudação
- [ ] Substituir prosa por schema (YAML >> JSON >> texto)
- [ ] Aplicar abbreviations do glossário
- [ ] Comprimir exemplos few-shot (mínimo viável)
- [ ] Filtragem RAG: relevância > 0.7, max 5 chunks
- [ ] Histórico sumarizado (não cru)
- [ ] Output format mais enxuto possível
- [ ] Instrução única, sem repetições
- [ ] Remover contexto não essencial
- [ ] Preferir links internos a explicações inline

---

## 📈 9. Métricas de Acompanhamento

| Métrica | Fórmula | Alvo |
|---------|---------|------|
| Densidade Informacional | chars_relevantes / tokens_totais | > 2.5 |
| Taxa de Compressão | tokens_brutos / tokens_finais | > 4:1 |
| Custo por Consulta | tokens_total * $/1K tokens | < $0.001 |
| Eficiência RAG | chunks_usados / chunks_retornados | > 80% |
| Precisão Semântica | output_relevante / output_total | > 90% |

---

## 🔗 10. Crosslinks

- [[04-Conhecimentos/Knowledge-Base/TOKEN-SHORTHAND]] — Abreviações padronizadas
- [[02-JARVIS/JARVIS/TOKEN-COMPRESSION]] — Compressão de contexto para o JARVIS
- [[99-Templates/Legado/Template-Prompt-Otimizado]] — Template de prompt otimizado
- [[04-Conhecimentos/Knowledge-Base/IA-APLICADA]] — Hub de IA Aplicada
- [[INDEX]]
