---
title: "🧠 Token Compression — Estratégias de Compressão de Contexto para o JARVIS"
tags: [jarvis, token-compression, contexto, memoria, eficiencia, JARVIS]
date: 2026-06-01
updated: 2026-06-05
category: system
aliases: ["Compressão de Contexto", "JARVIS Token Strategy", "Context Compression"]
related: ["Knowledge-Base/TOKEN-ECONOMY", "Knowledge-Base/TOKEN-SHORTHAND", "JARVIS/05-System/AGENT-CONTRACT"]
---

# 🧠 JARVIS Token Compression — Protocolo de Contexto Enxuto

Manual de operação para minimizar consumo de tokens do JARVIS sem perder capacidade analítica ou continuidade de memória.

---

## 🔄 1. Pipeline de Compressão

```
Entrada Bruta (ex: 8K tokens)
  │
  ├─ Stage 1: Filtragem (remove ruído, duplicatas, irrelevância)
  │     loss: 0% / redução: 20-40%
  │
  ├─ Stage 2: Sumarização (resume blocos grandes)
  │     loss: 10-20% / redução: 60-80%
  │
  ├─ Stage 3: Shorthand (aplica glossário de abreviações)
  │     loss: 0% / redução: 15-30%
  │
  ├─ Stage 4: Estruturação (converte prosa → YAML/schema)
  │     loss: 0-5% / redução: 30-50%
  │
  └─ Output Final (ex: 800 tokens — compressão ~10:1)
```

---

## ⚡ 2. Prioridades de Contexto por Camada (Tiered Recall)

### Tier 1 — Sempre Ativo (alocado fixo: 500t)
```
- Agent identity: "JARVIS, assistente de WK"
- Session goal: task atual + deadline
- Project active: nome + status + próximo passo
- User state: energia WK (low/med/high)
```

### Tier 2 — Sessão Atual (alocado: 1K-2K)
```
- Histórico: últimas 3-5 interações (sumarizadas)
- Decision tree: caminho atual de raciocínio
- Current file/note being edited
- Recent changes (git diff sumarizado)
```

### Tier 3 — Memória Operacional (alocado: 1K-3K)
```
- Estado.md (versão comprimida)
- Project.md do projeto ativo (só seção ACTIVE)
- Learned patterns relevantes ao contexto atual
- Mini-glossário de projeto (abreviações custom)
```

### Tier 4 — Pesquisa RAG (alocado: 1K-3K, sob demanda)
```
- Query → retriever → top 3 chunks (250t cada)
- Similarity threshold > 0.75
- Formato: [NOTE] section::line @score
```

---

## 📦 3. Formatos de Memória Compacta

### 3.1 Estado.md (comprimido)
```yaml
WK_state:
  energy: med
  focus: desenv
  context: PRJ-ActivityTracker
JA_state:
  session: 45min
  steps_done: [2/5]
  current_step: "db-schema"
blockers:
  - "awaiting WK approval on model"
next: "define user fields"
```

### 3.2 Histórico de Decisões
```yaml
decisions:
  - id: DEC-042
    what: "escolhido PostgreSQL sobre MongoDB"
    why: "dados relacionais, time pequeno"
    when: "2026-05-28"
    tags: [arch, db]
```

### 3.3 Diário Comprimido
```yaml
log_2026-06-01:
  tasks: [review, code, meet, docs]
  highlights: ["deploy feito em prod", "bug #42 resolvido"]
  energy_curve: [7, 5, 3, 6]
  blockers: ["dep mock lento"]
  decisions: [DEC-043, DEC-044]
```

---

## 🧩 4. Técnicas por Tipo de Conteúdo

### 4.1 Logs Técnicos
```
RAW → 3000t
  ├── UNIQUE: apenas linhas com erro/warn
  ├── COUNT: "ERROR x12, WARN x5, INFO x200"
  └── PATTERN: "3 occorrencias de timeout >30s em svc-auth"
COMPRESSED → 80t (37x)
```

### 4.2 Reuniões
```
RAW → 5000t (ata completa)
  ├── DECISIONS: "Decidido usar FastAPI"
  ├── ACTIONS: "@WK criar schema, @JA gerar migration"
  └── KEY: "troca de BD aprovada, prazo 15d"
COMPRESSED → 60t (83x)
```

### 4.3 Código
```
RAW → diff completo
  ├── STATS: "+150 -30 em 5 arquivos"
  ├── SIGNATURE: "feat(auth): add JWT refresh"
  └── HOTSPOT: fn validate_token() alterada
COMPRESSED → 25t + signatures
```

### 4.4 Pesquisa/Leitura
```
RAW → artigo 10K tokens
  ├── CLAIM: "o paper prova que MoE reduz custo 40%"
  ├── METHOD: "experimento com 8 experts, top-2 routing"
  └── RELEVANCE: "aplicavel ao projeto atual? → sim (otimizacao custo)"
COMPRESSED → 50t (200x)
```

---

## 📊 5. Métricas de Performance do JARVIS

| Métrica | Atual | Alvo | Fórmula |
|---------|-------|------|---------|
| Ctx por sessão | ~6K tokens | <3K | tokens médios por interação |
| Precisão decisão | 85% | >92% | dec_acertadas / dec_totais |
| Continuidade | 70% | >85% | ctx_retomado / ctx_perdido |
| Compressão média | 3:1 | >8:1 | input_bruto / input_final |
| Tempo resposta | 8s | <3s | (modelo 7B local) |

---

## 🔧 6. Comandos do JARVIS para Compressão

| Comando | Função | Economia |
|---------|--------|----------|
| `/summarize <range>` | Sumariza notas/blocos | 5-10x |
| `/compact` | Re-escreve nota em formato compacto | 2-3x |
| `/glossary` | Gera glossário de abreviações da sessão | 1.5x |
| `/clean` | Remove notas redundantes do ctx | 1.2x |
| `/status` | Versão comprimida do Estado.md | 5x |
| `/snapshot` | Salva contexto comprimido para retomada | variável |
| `/trim` | Remove histórico não essencial | 2x |

---

## 📋 7. Checklist Diário do JARVIS

- [ ] Iniciar sessão com `/status` (não ler Estado.md bruto)
- [ ] Usar abbreviations do TOKEN-SHORTHAND
- [ ] Sumarizar logs antes de armazenar
- [ ] Preferir YAML a prosa em notas de estado
- [ ] Manter sessão < 3K tokens
- [ ] Usar RAG seletivo (threshold 0.75)
- [ ] Registrar decisoes em formato compacto
- [ ] Fazer `/snapshot` ao finalizar sessão
- [ ] Limpar histórico a cada 10 interações

---

## 🔗 Crosslinks

- [[Knowledge-Base/TOKEN-ECONOMY]]
- [[Knowledge-Base/TOKEN-SHORTHAND]]
- [[Templates/Template-Prompt-Otimizado]]
- [[JARVIS/05-System/AGENT-CONTRACT]]
- [[JARVIS/05-System/ONBOARDING-AGENTE]]
- [[JARVIS/05-System/Comandos-JARVIS]]
- [[INDEX]]
