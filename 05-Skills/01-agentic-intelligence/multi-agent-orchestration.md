---
tags: [agentic, intelligence, orchestration, skills-ai, multi-agent]
updated: 2026-06-13
title: "Orquestracao Multi-Agente e Pipelines de Subagentes"
date: 2026-06-01
---

# Orquestracao Multi-Agente e Pipelines de Subagentes

Este documento cobre a coordenacao de multiplos agentes de IA para resolver tarefas complexas, com foco na arquitetura "Subagente-por-Tarefa" usada em sistemas como Hermes e Project JARVIS.

## Principios Fundamentais

1. **Separacao de Responsabilidades**: Cada agente tem um papel especifico (Pesquisador, Programador, Revisor).
2. **Compressao de Contexto**: Resumir passos de agentes anteriores antes de passar ao proximo para economizar tokens.
3. **Decomposicao Recursiva**: Dividir tarefas grandes em sub-tarefas trataveis por "micro-agentes" especializados.

## Roles especializados para expansao de conteudo

Quando o vault usa subagentes para crescer, o objetivo nao e repetir a mesma analise em oito nomes diferentes. A funcao e distribuir tipos distintos de conhecimento para manter o grafo limpo e escalavel.

| Papel | Foco de conteudo | Saida principal |
|---|---|---|
| Boole | validacao e conformidade | frontmatter, checklists e gates |
| Poincare | mapa e navegacao | hubs, rotas e relacoes hierarquicas |
| Peirce | decisao e inferencia | notas de decisao, evidencia e tradeoff |
| Avicenna | sintese e curadoria | conceitos densos, glossarios e notas canonicas |
| Lorentz | estabilidade e invariancia | regras de migracao, compatibilidade e preservacao |
| McClintock | auditoria e reconciliacao | inventario, orfaos, duplicatas e ponte legado |
| Aquinas | taxonomia e principios | classificacao estavel e doutrina do vault |
| Euler | relacoes e visao sistêmica | indices, dashboards e resumos de sistema |

### Fluxo prático

1. Validar a base com Boole.
2. Mapear o dominio com Poincare e Euler.
3. Consolidar conhecimento com Avicenna e Aquinas.
4. Registrar o raciocinio com Peirce.
5. Auditar o legado com McClintock.
6. Endurecer a mudanca com Lorentz.

### Aplicacao no vault

- Boole fortalece frontmatter, qualidade e aceitacao em `09-Sistema/`.
- Poincare fortalece hubs e trilhas em `01-Hubs/` e `02-JARVIS/`.
- Peirce alimenta decisoes em `02-JARVIS/02-Operational/Decisions/`.
- Avicenna e Aquinas elevam densidade conceitual em `04-Conhecimentos/`.
- Lorentz e McClintock protegem migracoes, legado e limpeza em `07-Operacoes-do-Vault/`.
- Euler sustenta indices, glossarios e visoes panoramicas em todo o grafo.

## Arquitetura do JARVIS 5.0

```
Usuario -> [Diretor] -> [Pesquisador] -> [Programador] -> [Revisor] -> [Monitor] -> Resposta
                |              |               |              |            |
           Roteamento     Busca dados      Implementa     Valida      Garante qualidade
```

### 1. Diretor (Roteamento)
- Recebe a requisicao do usuario.
- Analisa intencao e seleciona skills relevantes.
- Dispara sub-tarefas para trabalhadores especializados.

```python
class DirectorAgent:
    def route_task(self, user_request: str) -> TaskPlan:
        intent = self.analyze_intent(user_request)
        skills = self.select_skills(intent)
        plan = TaskPlan(
            subtasks=[
                Subtask("pesquisar", skills=["search_files", "read_file"]),
                Subtask("implementar", skills=["edit_file", "create_file"]),
                Subtask("revisar", skills=["execute_command", "read_file"]),
            ],
            fallback_strategy="retry_once",
        )
        return plan
```

### 2. Trabalhador (Execucao)
- Executa ferramentas MCP especificas.
- Mantem estado local dentro do escopo da tarefa.
- Reporta com artefato estruturado ou resultado.

### 3. Monitor (Validacao)
- Verifica a saida contra requisitos iniciais.
- Aciona loops de repeticao se expectativas nao forem atendidas.

```python
def validate_output(output, requirements: dict) -> ValidationResult:
    score = 0
    for req, value in requirements.items():
        if req in output:
            score += 1
    if score / len(requirements) < 0.8:
        return ValidationResult(passed=False, retry=True, score=score)
    return ValidationResult(passed=True, retry=False, score=score)
```

## Protocolos de Comunicacao entre Subagentes

### Handoff com Contexto Comprimido
Cada subagente recebe apenas o resumo do agente anterior, nao o historico completo:

```python
def handoff(previous_summary: str, current_agent_prompt: str) -> str:
    return f"""
    [Resumo do agente anterior]: {previous_summary}
    [Sua tarefa]: {current_agent_prompt}
    [Regras]: Nao repita o que ja foi feito. Apenas execute sua parte.
    """
```

### Contrato de Entrada/Saida
Cada agente segue um contrato estrito definido por JSON Schema:

```json
{
  "input_schema": {
    "type": "object",
    "properties": {
      "task": {"type": "string"},
      "context": {"type": "string"},
      "files": {"type": "array", "items": {"type": "string"}}
    }
  },
  "output_schema": {
    "type": "object",
    "properties": {
      "result": {"type": "string"},
      "changed_files": {"type": "array"},
      "confidence": {"type": "number"}
    },
    "required": ["result"]
  }
}
```

## Estrategias de Gerenciamento de Estado

| Estrategia | Descricao | Quando Usar |
|-----------|-----------|-------------|
| State Machine | Maquina de estados explicita (LangGraph) | Workflows complexos com multiplos caminhos |
| Memoria Compartilhada | Banco vetorial para estado global | Multiplos agentes precisam de contexto comum |
| Passagem de Mensagens | Cada agente envia/recebe mensagens | Sistemas peer-to-peer descentralizados |

### Exemplo com LangGraph (State Machine)

```python
from langgraph.graph import StateGraph, END

class AgentState(TypedDict):
    messages: list
    current_agent: str
    artifacts: dict

def router(state: AgentState) -> str:
    if state["current_agent"] == "diretor":
        return "pesquisador"
    elif state["current_agent"] == "pesquisador":
        return "programador"
    elif state["current_agent"] == "programador":
        return "revisor"
    return END

graph = StateGraph(AgentState)
graph.add_node("diretor", diretor_node)
graph.add_node("pesquisador", pesquisador_node)
graph.add_node("programador", programador_node)
graph.add_node("revisor", revisor_node)
graph.add_conditional_edges("diretor", router)
```

## Ferramentas Recomendadas

- **MCP Servers**: Ponte entre o LLM e o sistema de arquivos / APIs externas.
- **LM Studio / Ollama**: Orquestracao de pools de modelos locais com arquiteturas variadas.
- **LangGraph**: Framework para workflows com estado e maquina de estados.
- **CrewAI**: Orquestracao de agentes com papeis definidos e delegacao.

## Padroes Avancados

- **Memory Handover**: Passagem de estado entre agentes sem inchaco de contexto — use sumarizacao automatica.
- **Dynamic Skill Loading**: Injetar apenas ferramentas necessarias para a sub-tarefa atual.
- **Feedback Loops**: Agente "Critico" sugere melhorias ao agente "Trabalhador".
- **Circuit Breaker**: Interromper pipeline se um agente retornar erro critico.

## Referencias

- [[multi-agent-consensus]] — Mecanismos de consenso entre agentes.
- [[mcp-operators]] — Operadores MCP para execucao de ferramentas.
- [[advanced-reasoning-patterns]] — Padroes de raciocinio como ReAct e Reflexion.
- [[project-jarvis-prompts]] — Prompts especificos para o ecossistema JARVIS.
