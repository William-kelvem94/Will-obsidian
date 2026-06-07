---
title: "Engenharia de Prompts"
category: "AI"
level: 4
description: "Tecnicas avancadas para projetar prompts que maximizam precisao, relevancia e consistencia de LLMs, com templates, metricas e catalogo de anti-padroes."
projects:
  - "JARVIS Core"
  - "RAG-Local-Guide"
related_skills:
  - "MLOps"
  - "Reinforcement Learning"
  - "Generative Models"
resources:
  - "OpenAI Cookbook"
  - "Anthropic Prompt Engineering Guide"
  - "Papers sobre chain-of-thought e prompt optimization"
date: 2026-04-29
tags: [skills, ai, prompt-engineering]
updated: 2026-06-07
---

# Engenharia de Prompts

Engenharia de prompts e a pratica de criar instrucoes para LLMs que maximizam precisao, relevancia e consistencia. Este documento cobre templates reutilizaveis, metricas de avaliacao, catalogo de anti-padroes e tecnicas avancadas.

## Templates de Prompt

### Template para Geracao de Codigo

```markdown
## Contexto
Projeto: {{projeto}}
Linguagem: {{linguagem}}
Framework: {{framework}}

## Requisitos
{{descricao}}

## Restricoes
- Nao use bibliotecas externas alem de {{bibliotecas}}
- Siga o estilo do codigo existente em {{caminho_referencia}}
- Inclua tipos e docstrings

## Exemplo de saida esperada
{{exemplo}}
```

### Template para Sumarizacao RAG

```
Sistema: Voce e um assistente que resume informacoes tecnicas.
Use APENAS o contexto abaixo para responder.
Se o contexto nao contiver a resposta, diga "Nao encontrado".

Contexto:
{{chunks_relevantes}}

Pergunta: {{pergunta}}
Resposta concisa (max 3 paragrafos):
```

### Template para Classificacao

```
Classifique o sentimento do texto abaixo como:
- POSITIVO
- NEGATIVO
- NEUTRO

Responda APENAS com o rotulo, sem explicacao.

Texto: {{texto}}
Sentimento:
```

## Metricas de Avaliacao

### Precisao de Resposta

```python
def evaluate_response_fidelity(response: str, context: str) -> dict:
    """Avalia fidelidade da resposta ao contexto fornecido."""
    metrics = {
        "hallucination_score": 0.0,
        "context_coverage": 0.0,
        "relevance": 0.0
    }

    # Verifica se a resposta usa termos do contexto
    context_terms = set(context.lower().split())
    response_terms = set(response.lower().split())
    overlap = context_terms & response_terms
    metrics["context_coverage"] = len(overlap) / len(context_terms) if context_terms else 0

    return metrics
```

### Taxa de Alucinacao

```python
def hallucination_rate(responses: list[str], ground_truth: list[str]) -> float:
    """Calcula percentual de respostas que contem informacoes fora do ground truth."""
    hallucinated = 0
    for response, truth in zip(responses, ground_truth):
        response_facts = extract_facts(response)
        truth_facts = extract_facts(truth)
        for fact in response_facts:
            if not any(fact in tf for tf in truth_facts):
                hallucinated += 1
    return hallucinated / sum(len(extract_facts(r)) for r in responses)
```

## Catalogo de Anti-Padroes

| Anti-Padrao | Descricao | Solucao |
|-------------|-----------|---------|
| **Prompt Vago** | "Facil isso" sem contexto | Seja especifico: formato, tom, restricoes |
| **Sobrecarga de Tarefas** | Multiplas tarefas no mesmo prompt | Divida em prompts menores e encadeados |
| **Falta de Exemplos** | Zero-shot para tarefas complexas | Adicione few-shot examples (3-5) |
| **Instrucoes Contraditorias** | "Seja conciso" + "Explique detalhadamente" | Revise consistencia logica |
| **Vies de Posicao** | Informacao importante no meio do prompt | Coloque instrucoes criticas no inicio/fim |
| **Negligenciar System Prompt** | Tudo no user message | Use system para comportamento, user para input |
| **Prompt Injection** | Aceitar input nao sanitizado | Valide e sanitize entradas do usuario |

## Tecnicas Avancadas

### Chain-of-Thought (CoT)

```
Problema: {{problema}}
Resolva passo a passo:
1. Primeiro, identifique os dados relevantes.
2. Em seguida, aplique a formula.
3. Por fim, verifique o resultado.
```

### ReAct (Raciocinio + Acoes)

```markdown
Pensamento: Preciso buscar informacao sobre {{topico}}.
Acao: search_vault(query="{{topico}}", limit=3)
Observacao: {{resultado_busca}}
Pensamento: Com base nos resultados, posso concluir que...
Resposta Final: {{resposta}}
```

### Self-Consistency

```python
def self_consistency(llm, prompt: str, n_samples: int = 5) -> str:
    """Gera multiplas respostas e retorna a mais consistente."""
    responses = []
    for _ in range(n_samples):
        responses.append(llm.generate(prompt, temperature=0.7))

    # Agrupa respostas similares
    clusters = cluster_responses(responses)
    major_cluster = max(clusters, key=len)
    return major_cluster[0]  # resposta representativa
```

### Prompt Chaining

```python
class PromptChain:
    def __init__(self):
        self.steps = []

    def add_step(self, name: str, template: str, parser=None):
        self.steps.append({"name": name, "template": template, "parser": parser})

    async def execute(self, llm, initial_input: str) -> dict:
        context = {"input": initial_input}
        for step in self.steps:
            prompt = step["template"].format(**context)
            response = await llm.generate(prompt)
            if step["parser"]:
                context[step["name"]] = step["parser"](response)
            else:
                context[step["name"]] = response
        return context
```

## Estrategias para JARVIS

- Use system prompt para definir personalidade e regras do agente
- Para RAG, sempre inclua "Se nao souber, diga que nao sabe"
- Para codigo, especifique linguagem, framework e estilo
- Estruture tarefas complexas em sub-prompts com chain-of-thought
- Aplique self-consistency para decisoes criticas

## Referencias

- [[skills/ai/Generative-Models|Generative Models]] — Comportamento de modelos sob diferentes prompts
- [[skills/ai/MLOps|MLOps]] — Avaliacao sistematica de qualidade de prompts
- [[skills/04-knowledge-systems/INDEX|Knowledge Systems]] — RAG e injecao de contexto em prompts
- [[skills/04-knowledge-systems/advanced-rag-strategies|RAG Avancado]] — Query rewriting e decomposicao
