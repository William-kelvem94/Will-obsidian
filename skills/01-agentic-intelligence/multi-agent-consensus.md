---
title: "Orquestracao e Consenso Multi-Agentes"
description: "Como arquitetar sistemas onde multiplos agentes especializados colaboram, debatem e chegam a um consenso para resolver tarefas complexas."
tags: [multi-agent, orchestration, consensus, swarm, skills-ai, voting]
updated: 2026-05-16
---

# Orquestracao e Consenso Multi-Agentes

Quando a complexidade de um sistema escala, um unico "Super Agente" falha por confusao de papeis ou diluicao do contexto. A solucao e dividir o problema entre **Agentes Especializados** que interagem em rede (ex: LangChain LangGraph, AutoGen, CrewAI).

## Arquitetura Geral

```
Entrada -> [Router] -> Agente A --\
                              -> [Agregador] -> [Juiz] -> Saida
               -> Agente B --/
               -> Agente C --/
```

## Padroes de Orquestracao

### 1. Hierarquico (Manager-Worker)
Padrao corporativo mais comum:
- **Gerente (Router/Planner)**: Recebe o prompt, divide em subtarefas e delega.
- **Trabalhadores**: Prompts restritos e ferramentas especificas.
  - Agente Coder: apenas escreve codigo Python.
  - Agente Reviewer: apenas le e critica codigo.
  - Agente Executor: acesso ao bash para rodar testes.

### 2. Rede Sequencial (Pipeline)
Dados fluem em esteira de montagem: `Pesquisador -> Redator -> Revisor -> Publicador`.
Ideal para processos bem definidos; falha quando backtracking e necessario.

### 3. Swarm / Rede de Pares
Agentes conversam em "sala de chat" compartilhada. Requer regras de engajamento rigidas.

```python
class SwarmCoordinator:
    def __init__(self):
        self.agents = {}
        self.chat_history = []

    def register_agent(self, name: str, agent_fn):
        self.agents[name] = agent_fn

    def debate(self, topic: str, rounds: int = 3):
        for r in range(rounds):
            for name, agent in self.agents.items():
                response = agent(topic, self.chat_history)
                self.chat_history.append({"agent": name, "response": response})
        return self.synthesize()
```

## Algoritmos de Votacao

### Votacao Majoritaria Simples
Cada agente vota e a opcao com mais votos vence.

```python
def majority_vote(votes: list) -> str:
    from collections import Counter
    count = Counter(votes)
    winner = count.most_common(1)[0][0]
    return {"winner": winner, "count": dict(count)}
```

### Votacao Ponderada (Weighted)
Agentes com maior historico de acertos tem peso maior.

```python
def weighted_vote(votes: list, weights: dict) -> str:
    score = {}
    for agent, vote in votes:
        w = weights.get(agent, 1.0)
        score[vote] = score.get(vote, 0) + w
    winner = max(score, key=score.get)
    return {"winner": winner, "scores": score}
```

### Metodo de Borda
Cada agente ranqueia opcoes. Pontos sao atribuidos por posicao.

```python
def borda_count(rankings: list, options: list) -> str:
    scores = {opt: 0 for opt in options}
    n = len(options)
    for ranking in rankings:
        for rank, opt in enumerate(ranking):
            scores[opt] += n - rank
    winner = max(scores, key=scores.get)
    return {"winner": winner, "scores": scores}
```

### Tabela Comparativa

| Metodo | Complexidade | Justica | Caso de Uso |
|--------|-------------|---------|-------------|
| Majoritario | O(n) | Media | Decisoes rapidas, 2-3 opcoes |
| Ponderado | O(n) | Alta | Agentes com confiabilidade variavel |
| Borda | O(n*m) | Muito alta | Multiplas opcoes, ranking completo |
| Consensus | O(n^2) | Maxima | Decisoes criticas, alto custo aceitavel |

## Mecanismos de Consenso e Critica

### Debate Adversarial
Agentes com visoes conflitantes propositais:
- Agente A propoe SQL.
- Agente B defende NoSQL.
- Agente C (Juiz) sintetiza pontos fortes e decide.

```python
def adversarial_debate(proposal: str, agents: dict, judge_fn) -> str:
    arguments = {}
    for name, agent in agents.items():
        arguments[name] = agent.criticize(proposal)
    decision = judge_fn(proposal, arguments)
    return {"decision": decision, "arguments": arguments}
```

### Self-Critique e Peer Review
Artefato passa por agente Avaliador antes de ser enviado ao usuario.

```python
def peer_review(artifact: str, reviewer_fn, threshold: float = 0.8) -> dict:
    review = reviewer_fn(artifact)
    if review["score"] < threshold:
        return {
            "approved": False,
            "feedback": review["feedback"],
            "retry": True
        }
    return {"approved": True, "score": review["score"]}
```

## Estrategias de Agregacao

| Estrategia | Descricao | Exemplo |
|-----------|-----------|---------|
| Media aritmetica | Soma/divisao simples | Scores de relevancia |
| Mediana | Valor central | Rankings com outliers |
| Media ponderada | Pesos por confianca | Votacao com historico |
| Consenso estrito | Unanimidade exigida | Decisoes de seguranca |

## Desafios e Solucoes

| Problema | Sintoma | Solucao |
|----------|---------|---------|
| Loop de acordo | "Otimo!" "Obrigado!" desperdicando tokens | Forcar JSON com `is_complete`, proibir cortesia |
| Context bleed | Agente esquece papel especializado | Reforcar system prompt a cada turno |
| Vies de confirmacao | Agentes concordam com o primeiro a falar | Rotacionar ordem de fala, votacao anonima |
| Custo de tokens | Multiplos agentes = multiplos chamados LLM | Comprimir historico, usar cache de respostas |

## Referencias

- [[multi-agent-orchestration]] — Orquestracao e pipelines de subagentes.
- [[advanced-reasoning-patterns]] — ReAct, ToT, Reflexion para agentes.
- [[memory-architectures]] — Como agentes compartilham memoria.
- [[mcp-operators]] — Ferramentas para execucao de acoes.
