---
title: Modelos Mentais e Heurísticas de Decisão no Prompting
tags:
  - prompt-engineering
  - mental-models
  - cognitive-architecture
created: 2026-06-09
updated: 2026-06-09
status: active
---

# Modelos Mentais e Heurísticas de Decisão

A aplicação de modelos mentais na estruturação de *system prompts* transforma a IA de um simples gerador de texto em um agente de raciocínio estruturado. Ao instilar heurísticas específicas, reduz-se a alucinação e aumenta-se a precisão lógica.

## Modelos Mentais Principais

### 1. First Principles (Primeiros Princípios)
Consiste em decompor complexidades em suas verdades fundamentais e reconstruir a solução a partir do zero.
- **Aplicação no Prompt:** Instruir a IA a ignorar analogias comuns e derivar a solução a partir de axiomas básicos.
- **Exemplo:** *"Para resolver este problema de arquitetura, não utilize padrões preexistentes. Decomponha a necessidade em requisitos fundamentais de dados e latência, e construa a solução a partir dessas premissas."*

### 2. Navalha de Occam (Occam's Razor)
A explicação mais simples é geralmente a correta. Reduz o sobreajuste (*overfitting*) cognitivo da IA.
- **Aplicação no Prompt:** Forçar a IA a priorizar a simplicidade e eliminar redundâncias.
- **Exemplo:** *"Analise a causa raiz deste erro. Entre múltiplas hipóteses, priorize a que requer o menor número de suposições adicionais."*

### 3. Inversão (Inversion)
Em vez de pensar em como alcançar o sucesso, pense em como evitar a falha.
- **Aplicação no Prompt:** Definir "guardrails" negativos e cenários de falha para evitar comportamentos indesejados.
- **Exemplo:** *"Antes de propor a solução, liste três maneiras pelas quais esta implementação poderia falhar catastroficamente e ajuste a proposta para mitigar esses riscos."*

## Tabela de Heurísticas para System Prompts

| Modelo Mental | Objetivo | Comando Chave |
| :--- | :--- | :--- |
| **First Principles** | Inovação/Rigor | "Decomponha em verdades fundamentais" |
| **Occam's Razor** | Simplicidade | "Priorize a explicação mais simples" |
| **Inversão** | Robustez | "Como evitar o pior cenário possível?" |
| **Círculo de Competência** | Precisão | "Identifique onde termina seu conhecimento factual" |

---
Links: [[01-IA-e-Agentes/INDEX]]
