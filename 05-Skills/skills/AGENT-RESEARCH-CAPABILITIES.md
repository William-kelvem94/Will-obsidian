---
title: "🔬 Research Agent Capabilities — Habilidades de Pesquisa para Agentes IA"
tags: [skills, research, agent-capabilities, pesquisa, analise, investigacao, conhecimento]
date: 2026-06-01
updated: 2026-06-07
category: skill
aliases: ["Research Agent Skills", "Agente Pesquisador IA", "Capacidades de Pesquisa"]
related: ["05-Skills/skills/AGENT-FULLSTACK-CAPABILITIES", "05-Skills/skills/01-agentic-intelligence/programador-pesquisador.agent", "05-Skills/skills/04-knowledge-systems/INDEX"]
---

# 🔬 Research Agent Capabilities — Stack Completo de Pesquisa para Agentes IA

Matriz de habilidades de pesquisa que um agente IA deve dominar para conduzir investigações técnicas e científicas completas. Cobre formulação de hipóteses, busca multi-fontes, síntese de conhecimento, validação e aplicação prática.

---

## 🎯 1. Metodologia de Pesquisa

### 1.1 Pipeline de Pesquisa Completo

```
[1] FORMULAR → [2] BUSCAR → [3] ANALISAR → [4] SINTETIZAR → [5] VALIDAR → [6] APLICAR
    │            │            │             │               │            │
    ├─ Hipótese  ├─ Web      ├─ Triagem    ├─ Mapa mental  ├─ Factual   ├─ Implementar
    ├─ Escopo    ├─ Docs     ├─ Profund.   ├─ Resumo est.  ├─ Cross-ref ├─ Documentar
    ├─ Questões  ├─ Papers   ├─ Extrair    ├─ Argumentos   ├─ Gap       └─ Compartilhar
    ├─ Critérios ├─ Código   └─ Relac.     └─ Conclusões   └─ Confiança
    └─ Timeline  └─ People
```

### 1.2 Níveis de Profundidade

| Nível | Tempo | Fontes | Output | Quando Usar |
|-------|-------|--------|--------|-------------|
| **Scan** | 5-15 min | 2-5 fontes | Resumo 1 parágrafo | Contexto rápido, decisão simples |
| **Light** | 15-30 min | 5-10 fontes | Resumo 1 página | Task technique, escolha de lib |
| **Medium** | 1-2h | 10-25 fontes | Análise 2-3 páginas | Arquitetura, comparação de soluções |
| **Deep** | 3-8h | 25-100+ fontes | Artigo 5-10 páginas | Pesquisa original, state of the art |
| **Exhaustive** | 1-4 semanas | 100-500+ fontes | Survey completo | Tese, pesquisa acadêmica, benchmark |

---

## 🌐 2. Fontes de Pesquisa

### 2.1 Mapa de Fontes por Tipo

```yaml
sources:
  technical:
    - tier_1: [docs.oficiais, github_repos, papers_com_peer_review]
    - tier_2: [blog_postagens_tecnicas, stackoverflow, dev.to, medium_tech]
    - tier_3: [videos_tutoriais, cursos, twitter_tech, reddit_dev]
    - tier_4: [fóruns_antigos, posts_sem_data, medium_nontech]

  scientific:
    - tier_1: [arxiv, google_scholar, semantic_scholar, pubmed, ieee]
    - tier_2: [papers_with_code, open_review, conference_proceedings]
    - tier_3: [preprints, blog_de_pesquisadores, phd_theses]

  code:
    - tier_1: [github_source, npm/pypi/crates.io, docs_oficiais]
    - tier_2: [github_issues_discussions, stackoverflow_code, gist]
    - tier_3: [github_wikis, code_examples_de_blog]
```

### 2.2 Critérios de Credibilidade

```yaml
credibility_score:
  official_documentation: 10/10
  peer_reviewed_paper: 9/10
  well_known_author: 8/10
  github_stars_5k+: 7/10
  blog_with_proof: 6/10
  forum_detailed: 4/10
  no_date_no_author: 1/10

cross_validation:
  - "Conferir em 2+ fontes independentes"
  - "Verificar data de publicação (tecnologia muda rápido)"
  - "Checar se código de exemplo realmente funciona"
  - "Validar com documentação oficial antes de implementar"
  - "Procurar por issues conhecidas (known limitations)"
```

---

## 🧠 3. Técnicas de Análise e Síntese

### 3.1 Análise de Argumentos

```
Framework ACE (Analyze, Compare, Evaluate):

1. ANALYZE each source:
   - Claim: O que afima?
   - Evidence: Com que prova?
   - Assumptions: O que assume sem provar?
   - Context: Em que cenário vale?

2. COMPARE across sources:
   - Consensus: Onde concordam?
   - Conflict: Onde discordam?
   - Nuance: Diferenças sutis importantes?

3. EVALUATE:
   - Strength: Argumento mais forte? (mais evidência)
   - Reliability: Fonte mais confiável?
   - Recency: Mais recente vs desatualizado?
   - Relevance: Mais aplicável ao meu contexto?
```

### 3.2 Síntese Estruturada

```yaml
synthesis:
  format: yaml
  schema:
    question: "Pergunta original de pesquisa"
    answer: "Resposta direta (1-2 linhas)"
    confidence: 0-100
    key_findings:
      - finding: ""
        source: ""
        evidence: ""
    consensus:
      agreement: []
      disagreement: []
    gaps:
      - "O que ainda não se sabe"
    practical_implications:
      - "Como aplicar no contexto atual"
    further_research:
      - "Próximas perguntas"
```

### 3.3 Pesquisa Comparativa (Tech Choices)

```
Template para decisão técnica:

TECNOLOGIA A vs B vs C
│
├─ CRITÉRIOS PESADOS
│   ├─ Performance: A > B > C
│   ├─ Maturidade: B > A > C
│   ├─ Comunidade: A > B > C
│   ├─ Curva aprendizado: C > A > B
│   └─ Custo: C > B > A
│
├─ MATRIZ DE PESOS
│   ├─ Performance: 0.30 (crítico)
│   ├─ Maturidade: 0.15
│   ├─ Comunidade: 0.10
│   ├─ Curva: 0.20
│   └─ Custo: 0.25 (budget limitado)
│
├─ SCORE FINAL
│   ├─ A: (0.30*9)+(0.15*7)+(0.10*9)+(0.20*5)+(0.25*3) = 6.15
│   ├─ B: (0.30*7)+(0.15*9)+(0.10*7)+(0.20*8)+(0.25*8) = 7.60 ←
│   └─ C: (0.30*5)+(0.15*3)+(0.10*5)+(0.20*9)+(0.25*9) = 6.20
│
└─ RECOMENDAÇÃO: B (melhor custo-benefício geral)
    Riscos: ecossistema menor que A
    Mitigação: plano de migração para A se necessário
```

---

## ⚡ 4. Pesquisa Técnica para Agentes Fullstack

### 4.1 Estratégia por Tipo de Problema

| Problema | Abordagem de Pesquisa | Fontes Primárias |
|----------|----------------------|-----------------|
| **Bug** | Buscar erro específico (stack trace) → docs + issues + SO | Issues GitHub, StackOverflow, docs |
| **Feature** | Referências de implementação similar → padrões → exemplos | GitHub code search, docs, blogs |
| **Library** | Docs oficiais → exemplos → comparação com alternativas | Docs, npm/pypi, GitHub stars, benchmarks |
| **Arquitetura** | Princípios → case studies → trade-offs → decisão documentada | Papers, blogs de engenharia, arquiteturas conhecidas |
| **Performance** | Profiling → bottleneck → soluções conhecidas → benchmark | Docs de profiling, papers de otimização, benchmarks |
| **Security** | OWASP → CVE database → secure patterns → pentest | OWASP, CVE Mitre, SANS, security blogs |
| **ML/AI** | Papers → implementations → benchmarks → trade-offs | arXiv, PapersWithCode, GitHub, leaderboards |

### 4.2 Pesquisa com Código

```
Pipeline Pesquisa → Código:

1. Research: "melhor forma de implementar cache distribuído em Python"
   ├── Fontes: Redis docs, FastAPI caching patterns, aiocache lib
   ├── Decisão: Redis + aiocache + FastAPI middleware
   └── Output: decision log + architecture sketch

2. Code: implementar baseado na pesquisa
   ├── Seguir patterns identificados na pesquisa
   ├── Adaptar ao contexto específico do projeto
   └── Testar + validar

3. Validate: a implementação funciona como esperado?
   ├── Testes de unidade
   ├── Testes de performance (antes/depois)
   └── Se falhar → voltar ao research com novos dados

4. Document:
   ├── Decision record (por que esta escolha?)
   ├── Trade-offs aceitos
   └── Próximos passos (otimizações futuras)
```

---

## 📐 5. Métricas de Qualidade de Pesquisa

### 5.1 Scorecard de Pesquisa

```yaml
quality_metrics:
  coverage:
    formula: "fontes_relevantes_consultadas / fontes_total_disponiveis"
    target: "> 0.7"
  
  depth:
    formula: "media_de_tiers_explorados_por_topico"  
    target: "> 2.0 (mínimo Tiers 1-2)"
  
  recency:
    formula: "fontes_menos_6_meses / fontes_totais"
    target: "> 0.5 (exceto fundamentos clássicos)"
  
  accuracy:
    formula: "afirmacoes_corretas / afirmacoes_totais"
    target: "> 0.9"
  
  actionability:
    formula: "recomendacoes_implementaveis / recomendacoes_totais"
    target: "> 0.8"
  
  synthesis_quality:
    criteria:
      - "Resposta direta à pergunta?"
      - "Contrasta diferentes visões?"
      - "Identifica gaps?"
      - "Fornece recomendações práticas?"
      - "Pontua nível de confiança?"
    target: "4/5 critérios atendidos"
```

### 5.2 Autoavaliação do Agente

```yaml
post_research_checklist:
  - "Respondi à pergunta original completamente?"
  - "Consultei 2+ fontes independentes?"
  - "Verifiquei datas de publicação?"
  - "Identifiquei viés ou limitações?"
  - "Considerei alternativas?"
  - "Sintetizei de forma clara e acionável?"
  - "Apontei nível de confiança?"
  - "Indiquei direções para pesquisa futura?"
  - "Documentei decisões e trade-offs?"
  - "O output pode ser usado diretamente para ação?"
```

---

## ⚙️ 6. Toolstack do Pesquisador

### 6.1 Ferramentas Essenciais

```yaml
web_search:
  - google: "busca geral"
  - google_scholar: "literatura acadêmica"
  - arxiv: "papers recentes ML/AI"
  - perplexity: "resposta com fontes"
  - stackoverflow: "problemas técnicos"

code_search:
  - github: "busca de código + issues + discussions"
  - sourcegraph: "busca semântica em código"
  - grep: "busca local no vault"

knowledge_management:
  - obsidian: "vault como base de conhecimento"
  - vault_mcp: "ferramentas MCP do vault"
  - web_fetch: "captura de páginas web"

analysis:
  - reading: "leitura + sumarização de documentos"
  - reasoning: "CoT, ToT, raciocínio estruturado"
  - comparison: "comparação multi-fontes sistematizada"
```

### 6.2 Prompt Template de Pesquisa

```yaml
task: research
  - "<research_question>"
depth: <scan|light|medium|deep>
context: |
  Projeto atual: <nome>
  Tecnologias: <stack>
  Objetivo: <goal>
sources:
  tiers: [1, 2]
  max_per_tier: 5
output:
  format: yaml
  schema:
    - answer
    - confidence
    - key_findings
    - sources_used
    - gaps
    - recommendations
constraints:
  - "Priorizar fontes dos últimos 6 meses"
  - "Para cada afirmação, citar fonte"
  - "Identificar claramente o que é certeza vs inferência"
```

---

## 🧩 7. Integração com Outras Capacidades

### 7.1 Research → Fullstack Pipeline

```
PESQUISA → ARQUITETURA → IMPLEMENTAÇÃO → TESTE → DEPLOY → MONITOR

[Research Agent]                    [Fullstack Agent]
     │                                    │
     ├── Descobre melhor stack            ├── Implementa baseado na pesquisa
     ├── Analisa trade-offs               ├── Adapta ao contexto real
     ├── Encontra padrões                 ├── Testa e valida
     └── Documenta decisões               └── Deploy + monitora
           │                                    │
           └─────────── Feedback Loop ───────────┘
                        (O que funcionou? O que não funcionou?)
```

### 7.2 Tipos de Sessão Híbrida

```yaml
hybrid_sessions:
  research_first:
    - "Pesquisar abordagens → decidir → implementar"
    - "Ideal para: features novas, stacks desconhecidas"
  
  code_first:
    - "Implementar MVP → pesquisar otimizações → refatorar"
    - "Ideal para: prototipação rápida, validação de ideia"
  
  parallel:
    - "Pesquisar componente A enquanto implementa B"
    - "Ideal para: tasks independentes no mesmo projeto"
  
  iterative:
    - "Implementar → testar → pesquisar bottleneck → otimizar"
    - "Ideal para: performance, refactoring, debugging complexo"
```

---

## 📚 8. Exemplos de Pesquisa por Domínio

### 8.1 Pesquisa Técnica

```
Problema: "Como implementar autenticação JWT com refresh token em FastAPI?"

Pipeline:
  1. Scan: docs FastAPI Security → 5 min → visão geral
  2. Light: fastapi-jwt-auth vs python-jose vs PyJWT → 20 min → tabela comparativa
  3. Medium: implementação completa com redis blacklist + refresh rotation
     → 1h → PR com código + testes + docs

Output:
  - Decisão: python-jose + redis blacklist (melhor custo-benefício)
  - Código: auth middleware + login/refresh/logout endpoints
  - Testes: unit (token generation) + integration (full flow)
  - Documentação: decision record + setup guide
```

### 8.2 Pesquisa Acadêmica

```
Problema: "Qual o state-of-the-art em fine-tuning eficiente para LLMs?"

Pipeline:
  1. Scan: arxiv search "efficient fine-tuning 2025-2026" → 10 papers → 15 min
  2. Medium: top 3 papers (LoRA, QLoRA, DoRA, MoRA)
     → análise comparativa (performance, custo, facilidade)
     → 2h → relatório completo
  3. Validate: cross-check com PapersWithCode benchmarks
     → confirmar resultados reportados
  4. Apply: recomendar abordagem para o projeto atual

Output:
  - Relatório: comparação LoRA vs QLoRA vs DoRA vs MoRA
  - Recomendação: QLoRA (melhor custo-benefício para hardware local)
  - Roteiro de implementação: passos para fine-tuning com QLoRA
```

### 8.3 Pesquisa de Decisão de Arquitetura

```
Problema: "Monolith vs Microservices para o novo projeto?"

Pipeline:
  1. Medium: pesquisar case studies (Uber, Amazon, Shopify, StackOverflow)
     → 2h → padrões de decisão
  2. Fatos:
     - Monolith: melhor até 10 devs, até ~100K LOC
     - Microservices: necessário quando times independentes, escalas diferentes
  3. Contexto: time < 5 devs, MVP em 3 meses
  4. Decisão: Modular Monolith (estrutura de microserviços em monorepo)
     → fácil migrar se precisar no futuro

Output:
  - Decision record ADR-001
  - Arquitetura: modular monolith
  - Riscos: baixo (se precisar, migração incremental via Strangler Fig)
```

---

## 📊 9. Matriz de Proficiência do Research Agent

| Área | Nível | Critérios |
|------|-------|-----------|
| **Formulação** | Expert | Define perguntas precisas, escopo claro, critérios de sucesso |
| **Busca** | Expert | Encontra fontes relevantes em múltiplos domínios |
| **Triagem** | Avançado | Filtra ruído, identifica fontes de alta qualidade |
| **Análise** | Expert | Extrai argumentos, identifica viés, compara perspectivas |
| **Síntese** | Expert | Constrói answer direta + contexto + recomendações acionáveis |
| **Validação** | Avançado | Cross-check, identifica gaps, pontua confiança |
| **Documentação** | Avançado | Decision records claros, rastreáveis, acionáveis |
| **Aplicação** | Avançado | Traduz pesquisa em código, arquitetura, ação concreta |
| **Deep Research** | Intermediário | Pesquisa acadêmica multi-papers, revisão sistemática |
| **Cross-domain** | Avançado | Conecta conhecimentos de diferentes áreas |

---

## 🔗 Crosslinks

- [[05-Skills/skills/AGENT-FULLSTACK-CAPABILITIES]] — Stack fullstack do agente
- [[05-Skills/skills/01-agentic-intelligence/programador-pesquisador.agent]] — Agent file híbrido
- [[05-Skills/skills/01-agentic-intelligence/README]] — Inteligência agentica
- [[05-Skills/skills/04-knowledge-systems/INDEX]] — Sistemas de conhecimento e RAG
- [[04-Conhecimentos/Knowledge-Base/DATA-TOKEN-GOVERNANCE]] — Governança de dados e tokens
- [[04-Conhecimentos/Knowledge-Base/TOKEN-ECONOMY]] — Estratégias de otimização de tokens
- [[02-JARVIS/JARVIS/05-System/AGENT-CONTRACT]] — Contrato do agente
- [[INDEX]]
