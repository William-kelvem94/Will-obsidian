---
title: "Orquestração e Consenso Multi-Agentes"
description: "Como arquitetar sistemas onde múltiplos agentes especializados colaboram, debatem e chegam a um consenso para resolver tarefas complexas."
tags: [multi-agent, orchestration, consensus, swarm, skills-ai]
date: 2026-04-27
updated: 2026-04-27
---

# 🤖 Orquestração e Consenso Multi-Agentes

Quando a complexidade de um sistema escala, um único "Super Agente" falha (por confusão de papéis ou diluição do contexto do prompt). A solução é dividir o problema entre **Agentes Especializados** que interagem em rede (ex: LangChain LangGraph, AutoGen, CrewAI).

## Padrões de Orquestração

### 1. Hierárquico (Manager-Worker)
O padrão corporativo mais comum.
- **Agente Gerente (Router/Planner):** Recebe o prompt do usuário, divide o problema em subtarefas e delega.
- **Agentes Trabalhadores:** Têm prompts restritos e ferramentas específicas. Ex:
  - *Agente Coder:* Apenas escreve código Python.
  - *Agente Reviewer:* Apenas lê e critica código.
  - *Agente Executor:* Tem acesso ao bash para rodar testes.
- O Gerente agrega as respostas e finaliza.

### 2. Rede Sequencial (Pipeline)
Os dados fluem de um agente para outro em uma esteira de montagem.
- `Pesquisador` -> `Redator` -> `Revisor` -> `Publicador`.
- Bom para processos bem definidos, mas falha em problemas onde é necessário voltar passos (backtracking).

### 3. Swarm / Rede de Pares (Peer-to-Peer)
Agentes conversam ativamente em uma "sala de chat" compartilhada, intervindo quando seu conhecimento é necessário. Requer regras de engajamento rígidas.

## Mecanismos de Consenso e Crítica

Como garantir que a resposta final de um grupo de agentes está correta?

### Debater (Adversarial Setup)
Cria-se agentes com visões conflitantes de propósito:
- Agente A propõe uma arquitetura com SQL.
- Agente B é explicitamente instruído (via System Prompt) a criticar o Agente A defendendo NoSQL.
- Agente C (Juiz) lê o debate, sintetiza os pontos fortes de ambos e toma a decisão final baseada nas restrições reais do usuário.

### Self-Critique & Peer-Review
Antes de um resultado ser enviado ao usuário, o artefato obrigatoriamente passa por um agente Avaliador.
Se o Avaliador pontuar abaixo de 8/10 (ou encontrar bugs), o artefato volta para o Criador com o feedback.

## Desafios Técnicos na Implementação
1. **Loop Infinito de Acordo:** Agentes concordando demais ("Isso é ótimo!" "Obrigado!") e desperdiçando tokens. *Solução*: Forçar formatos de saída estruturados (JSON) com campos `is_complete` e proibir cortesia (politeness) nos prompts.
2. **Context Bleed:** Agentes esquecendo seu papel especializado. *Solução*: Reforço constante do System Prompt ("Você é estritamente o revisor de segurança").
3. **Roteamento de Estado:** Uso de State Machines (ex: LangGraph) onde o estado do sistema dita qual nó/agente deve ser ativado em seguida.
