---
title: Psicologia do Prompting
tags:
  - cognitive-psychology
  - prompt-engineering
  - llm-behavior
created: 2026-06-09
updated: 2026-06-09
status: active
---

# Psicologia do Prompting

O desempenho de um LLM não depende apenas da quantidade de dados, mas de como a estrutura linguística do prompt ativa caminhos probabilísticos específicos no espaço latente do modelo.

## Pilares Cognitivos do Prompting

### 1. Estrutura Linguística e Primazia/Recência
A posição da informação no contexto afeta a atenção do modelo (*Lost in the Middle*). 
- **Insight:** Instruções críticas devem ser posicionadas no início (Primazia) ou no final (Recência) do prompt.

### 2. Role-Playing (Atribuição de Persona)
A atribuição de um papel não é meramente cosmética; ela altera a distribuição de probabilidade dos tokens subsequentes, filtrando o "ruído" de personas irrelevantes.
- **Análise:** Ao definir "Você é um Engenheiro de Software Sênior com foco em segurança", o modelo prioriza tokens associados a rigor técnico e vulnerabilidades em detrimento de explicações genéricas.
- **Exemplo:** *"Atue como um revisor de código crítico e pessimista. Seu objetivo é encontrar falhas de segurança que um desenvolvedor júnior ignoraria."*

### 3. Chain-of-Thought (CoT) e Carga Cognitiva
A técnica de "pense passo a passo" funciona como uma memória de trabalho externa (*scratchpad*), permitindo que o modelo processe etapas intermediárias antes de convergir para a resposta final.
- **Perspectiva Cognitiva:** Reduz a pressão de prever o token final corretamente em um único salto probabilístico, distribuindo a complexidade ao longo de vários passos.
- **Exemplo:** *"Analise o problema. Primeiro, extraia as variáveis. Segundo, valide as premissas. Terceiro, execute o cálculo. Finalmente, apresente o resultado."*

## Comparativo de Técnicas

| Técnica | Gatilho Psicológico | Efeito no LLM |
| :--- | :--- | :--- |
| **Few-Shot** | Reconhecimento de Padrão | Alinhamento de formato e tom |
| **Persona** | Especialização de Domínio | Filtragem de espaço latente |
| **CoT** | Sequenciamento Lógico | Redução de erros de raciocínio |

---
Links: [[01-IA-e-Agentes/INDEX]]
