---
tags: [skills, skills-ai, agentic, workflow, react, multi-agent, human-in-the-loop]
updated: 2026-06-13
title: "Autonomous Agent Workflows (AAW)"
date: 2026-04-27
---

# Autonomous Agent Workflows (AAW)

## Visão Geral

Este workflow define como um agente autônomo (como [[02-JARVIS/Main|JARVIS]] ou Antigravity) deve interagir com o vault e executar tarefas complexas de forma autônoma. Abrange desde loops básicos de raciocínio até arquiteturas multi-agente com supervisão humana.

## 1. Agent Loops: Padrões Fundamentais

### ReAct (Reasoning + Acting)
O padrão mais difundido para agentes autônomos. O agente alterna entre raciocínio e ação em um loop contínuo:

```python
class ReActAgent:
    def __init__(self, tools: dict):
        self.tools = tools
        self.memory = []
    
    def run(self, task: str, max_steps: int = 10) -> str:
        self.memory.append({"role": "user", "content": task})
        
        for step in range(max_steps):
            # 1. THOUGHT: Raciocina sobre o que fazer
            thought = self.llm_call(
                system="Pense passo a passo. Decida qual ferramenta usar.",
                messages=self.memory
            )
            self.memory.append({"role": "assistant", "content": thought})
            
            # 2. ACTION: Executa uma ferramenta
            action = self.parse_action(thought)
            if action["type"] == "final_answer":
                return action["content"]
            
            result = self.execute_tool(action)
            self.memory.append({
                "role": "tool",
                "content": f"({action['name']}): {result[:500]}"
            })
        
        return "Max steps reached."
    
    def parse_action(self, thought: str) -> dict:
        # Ex: <tool>read_file<param>path</param></tool>
        import re
        match = re.search(r"<tool>(\w+)</tool>\s*<param>(.*?)</param>", thought)
        if match:
            return {"type": "tool", "name": match.group(1), "param": match.group(2)}
        return {"type": "final_answer", "content": thought}
```

### Plan-and-Execute
Separa o planejamento da execução:

```python
class PlanAndExecute:
    def __init__(self, planner_llm, executor_llm, tools):
        self.planner = planner_llm
        self.executor = executor_llm
        self.tools = tools
    
    def run(self, task: str) -> str:
        # Fase 1: Planejamento
        plan = self.planner.generate(f"""Crie um plano detalhado para:
        {task}
        
        Formato:
        1. Ação: descrição | Ferramenta: nome | Parâmetros: ...
        2. Ação: ...
        """)
        
        steps = self.parse_plan(plan)
        results = []
        
        # Fase 2: Execução
        for step in steps:
            result = self.execute_step(step, context=results)
            results.append(result)
            
            # Re-planejamento se necessário
            if self.needs_replan(result, step):
                plan = self.planner.generate(
                    f"Re-planeje a partir do passo {step['number']} \
                     com base em: {result}"
                )
                steps = self.parse_plan(plan)
        
        # Fase 3: Síntese
        return self.executor.generate(
            f"Sintetize os resultados em resposta a: {task}\n\n{results}"
        )
```

## 2. Tool Use e Function Calling

### Definindo Ferramentas para o Agente
```python
from pydantic import BaseModel, Field
from typing import Callable

class Tool(BaseModel):
    name: str
    description: str
    parameters: dict
    function: Callable
    
    def to_openai_format(self) -> dict:
        return {
            "type": "function",
            "function": {
                "name": self.name,
                "description": self.description,
                "parameters": {
                    "type": "object",
                    "properties": self.parameters,
                    "required": list(self.parameters.keys()),
                }
            }
        }

# Ferramentas do JARVIS
tools = [
    Tool(
        name="search_vault",
        description="Busca notas no vault do Obsidian por similaridade semântica",
        parameters={
            "query": {"type": "string", "description": "O termo de busca"},
            "limit": {"type": "integer", "description": "Nº máx. de resultados"}
        },
        function=lambda query, limit=5: vault_search(query, limit)
    ),
    Tool(
        name="write_note",
        description="Cria ou atualiza uma nota no vault",
        parameters={
            "path": {"type": "string"},
            "content": {"type": "string"}
        },
        function=lambda path, content: vault_write(path, content)
    ),
    Tool(
        name="execute_python",
        description="Executa código Python em sandbox isolado",
        parameters={
            "code": {"type": "string", "description": "Código Python"}
        },
        function=lambda code: sandbox_execute(code)
    ),
]

agent = ReActAgent(tools={t.name: t for t in tools})
```

### Function Calling com OpenAI / Compatível
```python
def agent_with_function_calling(task: str) -> str:
    messages = [{"role": "user", "content": task}]
    tool_defs = [t.to_openai_format() for t in tools]
    
    for _ in range(10):
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=messages,
            tools=tool_defs,
            tool_choice="auto",
        )
        
        msg = response.choices[0].message
        
        if not msg.tool_calls:
            return msg.content  # Resposta final
        
        # Executa cada ferramenta chamada
        for tool_call in msg.tool_calls:
            fn_name = tool_call.function.name
            fn_args = json.loads(tool_call.function.arguments)
            tool_map = {t.name: t for t in tools}
            result = tool_map[fn_name].function(**fn_args)
            
            messages.append(msg)
            messages.append({
                "role": "tool",
                "tool_call_id": tool_call.id,
                "content": str(result)
            })
```

## 3. Memória em Agentes

### Memória de Curto Prazo (Buffer de Conversa)
```python
from collections import deque

class ConversationBuffer:
    def __init__(self, max_messages: int = 20):
        self.buffer = deque(maxlen=max_messages)
    
    def add(self, role: str, content: str):
        self.buffer.append({"role": role, "content": content})
    
    def get_context(self) -> list[dict]:
        return list(self.buffer)
    
    def summarize_if_needed(self, llm):
        if len(self.buffer) >= self.buffer.maxlen:
            summary = llm(f"Summarize: {self.buffer}")
            self.buffer.clear()
            self.buffer.append({"role": "system", "content": f"History: {summary}"})
```

### Memória de Longo Prazo (Persistente)
Veja [[04-knowledge-systems/memory-management]] para implementação completa.

```python
class LongTermMemory:
    def __init__(self, vector_db):
        self.db = vector_db
    
    def store(self, agent_id: str, experience: dict):
        embedding = generate_embedding(experience["summary"])
        self.db.add(
            embeddings=[embedding],
            documents=[json.dumps(experience)],
            metadatas=[{"agent_id": agent_id, "type": experience["type"]}]
        )
    
    def recall(self, agent_id: str, query: str, n: int = 5) -> list[dict]:
        results = self.db.query(query, where={"agent_id": agent_id}, n_results=n)
        return [json.loads(doc) for doc in results["documents"]]
```

## 4. Multi-Agent Systems

### Orquestrador com Times de Agentes
```python
class AgentTeam:
    def __init__(self):
        self.agents = {
            "researcher": ResearchAgent(),
            "coder": CodeAgent(),
            "reviewer": ReviewAgent(),
            "writer": DocumentationAgent(),
        }
    
    def execute(self, task: str) -> str:
        # 1. Pesquisa
        research = self.agents["researcher"].run(task)
        
        # 2. Codifica solução
        solution = self.agents["coder"].run(
            f"Contexto: {research}\nTarefa: {task}"
        )
        
        # 3. Revisa
        review = self.agents["reviewer"].run(solution)
        if review["approved"]:
            # 4. Documenta
            docs = self.agents["writer"].run(solution)
            return docs
        else:
            # Loop de correção
            return self._iterate(task, research, solution, review["feedback"])
```

### Comunicação entre Agentes
```python
class MessageBus:
    """Barramento de mensagens assíncrono para agentes"""
    def __init__(self):
        self.topics = defaultdict(list)
    
    def subscribe(self, agent, topic: str):
        self.topics[topic].append(agent)
    
    def publish(self, topic: str, message: dict):
        for agent in self.topics[topic]:
            agent.receive(topic, message)

# Exemplo: Agente de código publica resultado
bus = MessageBus()
bus.subscribe(review_agent, "code_complete")
bus.subscribe(doc_agent, "code_complete")

code_agent.on_complete = lambda result: bus.publish(
    "code_complete", {"author": "coder", "result": result}
)
```

### Consenso entre Agentes (Multi-Agent Debate)
Veja [[multi-agent-consensus]] para padrões de votação e consenso:

```python
def debate_consensus(question: str, agents: list[Agent], rounds: int = 3):
    opinions = [agent.answer(question) for agent in agents]
    
    for round_num in range(rounds):
        for i, agent in enumerate(agents):
            # Cada agente vê as opiniões dos outros
            feedback = opinions[:i] + opinions[i+1:]
            new_opinion = agent.revise(question, opinions[i], feedback)
            opinions[i] = new_opinion
        
        # Verifica convergência
        if all_similar(opinions):
            break
    
    return aggregate_opinions(opinions)
```

## 5. Error Recovery e Retry Logic

### Retry com Backoff Exponencial
```python
import time
import random

def with_retry(func, max_retries: int = 3, base_delay: float = 1.0):
    for attempt in range(max_retries):
        try:
            return func()
        except Exception as e:
            if attempt == max_retries - 1:
                raise
            
            delay = base_delay * (2 ** attempt) + random.uniform(0, 0.5)
            log(f"Attempt {attempt + 1} failed: {e}. Retrying in {delay:.1f}s")
            time.sleep(delay)
```

### Graceful Degradation
```python
class DegradationStrategy:
    def __init__(self):
        self.tier = 0  # 0 = full, 1 = reduced, 2 = fallback
    
    def execute(self, task: str) -> str:
        strategies = [
            self._full_capability,
            self._reduced_capability,
            self._fallback
        ]
        
        for strategy in strategies:
            try:
                return strategy(task)
            except Exception as e:
                self.tier += 1
                log(f"DEGRADATION: {e}. Moving to tier {self.tier}")
        
        return "Não foi possível completar a tarefa."
    
    def _full_capability(self, task: str) -> str:
        return agent_with_all_tools(task)
    
    def _reduced_capability(self, task: str) -> str:
        return agent_with_core_tools(task)
    
    def _fallback(self, task: str) -> str:
        return llm_direct_response(task)
```

### Checkpointing
```python
class WorkflowCheckpointer:
    def save_state(self, workflow_id: str, step: int, state: dict):
        # Salva estado intermediário para recovery
        db.execute(
            "INSERT INTO checkpoints (workflow_id, step, state) \
             VALUES (?, ?, ?) ON CONFLICT(workflow_id, step) DO UPDATE SET state = ?",
            (workflow_id, step, json.dumps(state), json.dumps(state))
        )
    
    def load_checkpoint(self, workflow_id: str) -> int | None:
        row = db.execute(
            "SELECT MAX(step) FROM checkpoints WHERE workflow_id = ?",
            (workflow_id,)
        ).fetchone()
        return row[0] if row else None
    
    def resume(self, workflow_id: str, workflow_func):
        last_step = self.load_checkpoint(workflow_id)
        start_step = last_step + 1 if last_step else 0
        return workflow_func(start_step=start_step)
```

## 6. Human-in-the-Loop Patterns

### Aprovação Humana para Ações Críticas
```python
class HumanInTheLoop:
    def __init__(self, approval_channel: str = "telegram"):
        self.pending_actions = Queue()
        self.approval_channel = approval_channel
    
    async def request_approval(self, action: dict) -> bool:
        """Pausa o fluxo e espera aprovação humana"""
        
        # Envia notificação
        await self.send_notification(
            channel=self.approval_channel,
            message=f"⚠️ Aprovação necessária:\n"
                    f"Ação: {action['type']}\n"
                    f"Parâmetros: {action['params']}\n"
                    f"Risco: {action['risk_level']}"
        )
        
        # Aguarda resposta (timeout de 5 minutos)
        try:
            response = await self.wait_for_response(timeout=300)
            return response["approved"]
        except TimeoutError:
            log("Aprovação humana expirou. Pulando ação.")
            return False
    
    async def run_with_approval(self, task: str):
        agent = ReActAgent(tools=self.tools)
        
        for step in agent.plan(task):
            if step["risk_level"] == "high":
                approved = await self.request_approval({
                    "type": step["type"],
                    "params": step["params"],
                    "risk_level": step["risk_level"]
                })
                if not approved:
                    continue
            
            agent.execute(step)
```

### Modos de Autonomia
```python
class AutonomyMode:
    FULL = "full"       # Executa tudo autônomo
    SUPERVISED = "supervised"  # Executa, reporta, aguarda OK
    CONFIRMATION = "confirmation"  # Pergunta antes de cada ação
    MANUAL = "manual"   # Apenas sugere, aguarda comando

class AutonomousAgent:
    def __init__(self, mode: str = "supervised"):
        self.mode = mode
        self.loop = HumanInTheLoop()
    
    async def execute(self, task: str):
        if self.mode == AutonomyMode.FULL:
            return self._execute_autonomous(task)
        elif self.mode == AutonomyMode.SUPERVISED:
            result = self._execute_with_logging(task)
            await self.loop.send_report(result)
            return result
        elif self.mode == AutonomyMode.CONFIRMATION:
            return await self._execute_step_by_step(task)
        elif self.mode == AutonomyMode.MANUAL:
            return await self._suggest_and_wait(task)
```

## 7. Protocolo de Atuação no Vault

### S.S.O. (Scan, Sync, Optimize)
Conforme definido no vault:

1. **Scan:** Escaneie o diretório e os arquivos de contexto.
2. **Sync:** Garanta que os links internos e MOCs estão atualizados.
3. **Optimize:** Melhore a legibilidade e a estética da nota gerada.

### Regras de Integridade
- Respeitar tags do [[01-agentic-intelligence/skills-categories|Graph-Legenda]]
- Registrar memórias em `02-JARVIS/Memorias/Episodicas/`
- Documentar decisões em `02-JARVIS/Decisoes/`

## Ferramentas MCP Recomendadas

- `search_vault(query)` — Busca semântica no Obsidian.
- `create_note(path, content)` — Cria/atualiza notas.
- `execute_python(code)` — Sandbox de execução.
- `request_human_approval(action)` — Pausa para aprovação.
- `store_memory(type, content)` — Persiste memória de longa duração.
- `checkpoint_save(workflow_id, state)` — Salva progresso.

---

*Consulte também: [[multi-agent-orchestration]], [[04-knowledge-systems/memory-management]], [[best-practices]], [[mcp]].*
