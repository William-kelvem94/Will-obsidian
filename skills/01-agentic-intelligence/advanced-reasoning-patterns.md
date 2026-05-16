---
title: "Advanced Reasoning Patterns: ReAct, ToT, CoT e Reflexion"
description: "Analise profunda dos padroes de raciocinio avancado utilizados por agentes LLM para tomada de decisao e resolucao de problemas complexos."
tags: [agentic, reasoning, react, tot, cot, reflexion, skills-ai]
updated: 2026-05-16
---

# Padroes de Raciocinio Avancado para Agentes de IA

Para que agentes como o JARVIS superem respostas genericas e atinjam o nivel de resolucao de problemas de um engenheiro senior, e essencial a implementacao de padroes estruturados de raciocinio.

## Tabela Comparativa

| Padrao | Mecanismo | Quando Usar | Custo de Tokens |
|--------|-----------|-------------|-----------------|
| CoT | Cadeia linear de pensamento | Problemas que exigem passo a passo | Baixo |
| ReAct | Intercala pensamento e acao | Tarefas que exigem ferramentas | Medio |
| ToT | Arvore de multiplos caminhos | Problemas complexos com backtracking | Alto |
| Reflexion | Aprendizado com erros passados | Depuracao e melhoria iterativa | Medio |

## 1. Chain-of-Thought (CoT)

Cadeia linear de raciocinio que guia o modelo passo a passo.

### Prompt Template de CoT

```
Pergunta: {pergunta}
Vamos pensar passo a passo:
1. Primeiro, vou analisar o que esta sendo pedido.
2. Depois, vou identificar os componentes envolvidos.
3. Entao, vou aplicar a logica necessaria.
4. Por fim, vou verificar se a resposta faz sentido.
Resposta:
```

### Exemplo Practico

```
Pergunta: "Quantos arquivos .md existem em skills/01-agentic-intelligence/"
Raciocinio:
1. Preciso listar o diretorio skills/01-agentic-intelligence/
2. Filtrar apenas arquivos com extensao .md
3. Contar o numero de resultados
4. Verificar se ha subdiretorios com .md

Acao: search_files("skills/01-agentic-intelligence/*.md")
Observacao: 18 arquivos encontrados
Resposta: Existem 18 arquivos .md no diretorio.
```

## 2. ReAct (Reasoning + Acting)

Framework que intercala raciocinio com acoes concretas no ambiente.

### Loop ReAct

```
Thought: Preciso entender a estrutura do projeto
Action: search_files("src/**/*.py")
Observation: [lista de arquivos]

Thought: Agora preciso ler o arquivo principal
Action: read_file("src/main.py")
Observation: [conteudo do arquivo]

Thought: Identifiquei o problema. Vou corrigir.
Action: edit_file("src/main.py", "...")
Observation: Arquivo atualizado

Thought: Preciso validar a correcao
Action: execute_command("pytest")
Observation: Testes passaram

Final Answer: Bug corrigido em src/main.py.
```

### Implementacao em Python

```python
class ReActAgent:
    def __init__(self, tools: dict):
        self.tools = tools
        self.history = []

    def step(self, thought: str) -> str:
        action = self.choose_action(thought)
        result = self.tools[action["tool"]](**action["params"])
        self.history.append({"thought": thought, "action": action, "result": result})
        return result

    def choose_action(self, thought: str) -> dict:
        prompt = f"""
        Com base nesse pensamento: "{thought}"
        Escolha a proxima acao entre: {list(self.tools.keys())}
        Responda em JSON: {{"tool": "nome", "params": {{}}}}
        """
        response = llm_call(prompt)
        return json.loads(response)

    def run(self, task: str) -> str:
        while not self.is_complete():
            thought = self.generate_thought(task)
            if thought == "COMPLETE":
                return self.final_answer()
            self.step(thought)
```

## 3. Tree of Thoughts (ToT)

Expande CoT permitindo explorar multiplos caminhos em paralelo.

### Funcionamento

```
Problema: "Qual arquitetura escolher para o backend?"

[Raiz] Como projetar o backend?
    |
    |-- No 1: FastAPI monolitico
    |   |-- Pro: Simples, rapido de desenvolver
    |   |-- Contra: Escalabilidade limitada
    |
    |-- No 2: FastAPI + microservicos
    |   |-- Pro: Escalavel, desacoplado
    |   |-- Contra: Complexidade operacional
    |
    |-- No 3: GraphQL + Lambda
        |-- Pro: Serverless, consultas flexiveis
        |-- Contra: Cold starts, vendor lock-in

[Heuristica] Pontuacao: No 2 = 8/10, No 1 = 6/10, No 3 = 5/10
[Backtrack] No 3 pontuou baixo -> podar
[Expansao] No 2 -> detalhar implementacao
[Decisao] FastAPI + microservicos
```

### Implementacao Simplificada

```python
class ToTNode:
    def __init__(self, content: str, parent=None):
        self.content = content
        self.parent = parent
        self.children = []
        self.score = 0.0

class TreeOfThoughts:
    def __init__(self, max_depth: int = 3, beam_width: int = 3):
        self.max_depth = max_depth
        self.beam_width = beam_width

    def solve(self, problem: str) -> ToTNode:
        root = ToTNode(problem)
        frontier = [root]
        for depth in range(self.max_depth):
            candidates = []
            for node in frontier:
                branches = self.generate_branches(node)
                for branch in branches:
                    branch.score = self.evaluate(branch)
                    candidates.append(branch)
            candidates.sort(key=lambda n: n.score, reverse=True)
            frontier = candidates[:self.beam_width]
        return max(frontier, key=lambda n: n.score)

    def generate_branches(self, node: ToTNode) -> list:
        prompt = f"Problema: {node.content}\nGere 3 abordagens diferentes:"
        responses = llm_call(prompt, n=3)
        return [ToTNode(r, parent=node) for r in responses]

    def evaluate(self, node: ToTNode) -> float:
        prompt = f"Avalie esta abordagem de 0 a 10: {node.content}"
        score = float(llm_call(prompt))
        return score / 10.0
```

## 4. Reflexion

Aprendizado com erros sem retreinamento de pesos.

### Loop de Reflexao

```python
class ReflexionAgent:
    def __init__(self):
        self.memory = []

    def attempt(self, task: str) -> dict:
        result = self.execute(task)
        if not result["success"]:
            reflection = self.reflect(task, result)
            self.memory.append(reflection)
            result = self.execute_with_context(task)
        return result

    def reflect(self, task: str, failed_result: dict) -> str:
        prompt = f"""
        Tarefa: {task}
        Resultado: {failed_result['output']}
        Erro: {failed_result['error']}
        Analise porque falhou e o que deveria ser feito diferente:
        """
        return llm_call(prompt)

    def execute_with_context(self, task: str) -> dict:
        context = "\n".join(self.memory[-3:])
        prompt = f"""
        Licoes aprendidas anteriormente: {context}
        Tarefa atual: {task}
        Evite os erros do passado.
        """
        return execute_with_prompt(prompt)
```

### Exemplo
1. Tentativa: codigo nao compila (erro de tipo).
2. Reflexao: "Usei `int` onde deveria ser `float`."
3. Proxima tentativa: insere conversao explicita.
4. Memoria: registrada para evitar repeticoes.

## Integracao no JARVIS

Combinar ToT para planejamento inicial, ReAct para execucao e Reflexion para debug autonomo:

```python
class JarvisReasoningEngine:
    def __init__(self):
        self.planner = TreeOfThoughts()
        self.executor = ReActAgent(tools=MCP_TOOLS)
        self.learner = ReflexionAgent()

    def solve(self, task: str):
        plan = self.planner.solve(task)
        result = self.executor.run(plan.content)
        result = self.learner.attempt(task)
        return result
```

## Referencias

- [[multi-agent-orchestration]] — Orquestracao de agentes com ReAct.
- [[multi-agent-consensus]] — Consenso entre agentes com votacao.
- [[memory-architectures]] — Memoria episodica para Reflexion.
- [[project-jarvis-prompts]] — Prompts para JARVIS com ReAct.
