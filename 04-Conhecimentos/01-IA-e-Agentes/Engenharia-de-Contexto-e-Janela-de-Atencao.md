---
title: Engenharia de Contexto e Janela de Atenção
tags:
  - transformers
  - attention-mechanism
  - information-density
created: 2026-06-09
updated: 2026-06-09
status: active
---

# Context Engineering e Attention Window

A context window não é apenas um token limit, mas um recurso finito de "attention" onde a information density determina a qualidade da saída.

## Attention Mechanisms (Self-Attention)

Os Transformers utilizam o mecanismo de *scaled dot-product attention* para ponderar a importância de cada token em relação a todos os outros na sequência. 

### Attention Dilution Problem
À medida que a janela de contexto aumenta, a "massa" de atenção é distribuída por mais tokens. Se o contexto for preenchido com ruído, a probabilidade de o modelo ignorar instruções cruciais aumenta.
- **Information Density:** A relação entre tokens úteis e padding tokens. Quanto maior a densidade, maior a precisão do modelo.

## Context Optimization Strategies

### 1. Context Compression (Context Distillation)
Remover redundâncias e converter descrições longas em representações densas (ex: usar JSON em vez de prosa para dados estruturados).
- **Exemplo:** Substituir *"O usuário informou que seu nome é João e ele mora em São Paulo"* por `{"user": "João", "loc": "SP"}`.

### 2. Hierarchical Structuring
Organizar o contexto de forma que a IA possa navegar logicamente.
- **Aplicação:** Utilizar delimitadores claros (`### Instruções`, `### Contexto`, `### Saída Esperada`) para ajudar o mecanismo de atenção a segmentar as partes do prompt.

### 3. RAG (Retrieval-Augmented Generation) vs. Long Context
Embora janelas de 1M+ tokens existam, o RAG continua sendo superior para a maioria dos casos devido à redução do ruído e custo computacional.
- **RAG:** Seleciona apenas os fragmentos mais relevantes $\rightarrow$ Alta densidade.
- **Long Context:** Insere todo o documento $\rightarrow$ Risco de diluição.

## Impact Summary

| Variável | Impact on Output | Recomendação |
| :--- | :--- | :--- |
| **Low Density** | Hallucinations, loss of instructions | Limpar o prompt, usar RAG |
| **High Density** | Respostas precisas, concisas | Uso de schemas (JSON/Markdown) |
| **Context Overflow** | "Lost in the Middle" effect | Colocar info crítica nas extremidades |

---
Links: [[01-IA-e-Agentes/INDEX]]
