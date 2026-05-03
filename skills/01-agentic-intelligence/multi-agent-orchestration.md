---
tags: [agentic, intelligence, orchestration, skills-ai]
updated: 2026-05-03
title: "Multi-Agent Orchestration & Subagent Pipelines"
date: 2026-04-27
---

# Multi-Agent Orchestration & Subagent Pipelines

This skill covers the coordination of multiple AI agents to solve complex tasks, specifically focusing on the "Subagent-per-Task" architecture used in high-end systems like Hermes and Project Jarvis.

## 核心 (Core) Principles
1. **Separation of Concerns**: Each agent has a specific role (e.g., Researcher, Coder, Reviewer).
2. **Context Compression**: Summarize previous agent steps before passing to the next to save tokens.
3. **Recursive Decomposition**: Break large tasks into sub-tasks that can be handled by specialized "micro-agents".

## Jarvis 5.0 Workflow
### 1. The Director (Routing)
- Receives USER request.
- Analyzes intent and selects relevant skills.
- Dispatches sub-tasks to specialized workers.

### 2. The Worker (Execution)
- Executes specific MCP tools.
- Maintains local state within the task scope.
- Reports back with a structured artifact or result.

### 3. The Monitor (Validation)
- Checks the output against initial requirements.
- Triggers retry loops if expectations aren't met.

## Implementation Patterns
- **Memory Handover**: How to pass state between agents without context bloat.
- **Dynamic Skill Loading**: Injecting only the necessary tools for the current sub-task.
- **Feedback Loops**: Allowing the 'Critic' agent to suggest improvements to the 'Worker' agent.

## Tools of Choice
- **MCP Servers**: For bridging the LLM to the filesystem and external APIs.
- **LM Studio / Ollama**: Orchestrating local model pools with varied architectures (e.g., Llama-3 for logic, Phi-3 for simple tasks).
