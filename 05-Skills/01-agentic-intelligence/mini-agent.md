---
tags: [skills, skills-ai, mini-agent, implementation]
updated: 2026-06-10
title: "Mini-Agent de IA para VS Code"
date: 2026-06-01
---

# Mini-Agent de IA para VS Code

Este mini-agent e uma implementacao leve de agente para usar IA no VS Code com leitura, edicao e validacao de codigo. Inclui codigo completo, configuracao e exemplos de uso.

## Objetivo

Criar um agente leve que:
- Entenda o contexto do codigo.
- Faca mudancas seguras.
- Valide com testes.
- Produza um resumo final.

## Implementacao Completa em Python

### Classe Principal do Mini-Agent

```python
import json
import subprocess
from typing import Callable, Dict, List, Optional

class MiniAgent:
    def __init__(self, config: dict):
        self.config = config
        self.history = []
        self.max_steps = config.get("max_steps", 10)
        self.tools = self._register_tools()

    def _register_tools(self) -> Dict[str, Callable]:
        return {
            "search_files": self._search_files,
            "read_file": self._read_file,
            "edit_file": self._edit_file,
            "create_file": self._create_file,
            "execute_command": self._execute_command,
            "path_exists": self._path_exists,
        }

    def _search_files(self, pattern: str) -> List[str]:
        import glob
        return glob.glob(pattern, recursive=True)

    def _read_file(self, path: str) -> Optional[str]:
        try:
            with open(path, "r", encoding="utf-8") as f:
                return f.read()
        except FileNotFoundError:
            return None

    def _edit_file(self, path: str, old: str, new: str) -> bool:
        content = self._read_file(path)
        if content is None:
            return False
        if old not in content:
            return False
        with open(path, "w", encoding="utf-8") as f:
            f.write(content.replace(old, new, 1))
        return True

    def _create_file(self, path: str, content: str) -> bool:
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)
        return True

    def _execute_command(self, command: str) -> str:
        try:
            result = subprocess.run(
                command, shell=True, capture_output=True, text=True, timeout=30
            )
            return result.stdout + result.stderr
        except subprocess.TimeoutExpired:
            return "TIMEOUT: comando excedeu 30s"

    def _path_exists(self, path: str) -> bool:
        import os
        return os.path.exists(path)

    def run(self, task: str) -> dict:
        self.history = []
        for step in range(self.max_steps):
            action = self._decide_next_action(task)
            if action["type"] == "complete":
                return self._summarize()
            result = self._execute_action(action)
            self.history.append({"step": step, "action": action, "result": result})
        return {"status": "max_steps_atingido", "history": self.history}

    def _decide_next_action(self, task: str) -> dict:
        # Logica de decisao baseada no estado atual
        if not self.history:
            return {"type": "tool", "tool": "search_files", "params": {"pattern": "**/*.py"}}
        last_result = self.history[-1]["result"]
        if last_result and "error" not in str(last_result).lower():
            return {"type": "tool", "tool": "read_file", "params": {"path": last_result[0]}}
        return {"type": "complete"}

    def _execute_action(self, action: dict) -> any:
        if action["type"] == "tool":
            tool = self.tools.get(action["tool"])
            if tool:
                return tool(**action["params"])
        return None

    def _summarize(self) -> dict:
        return {
            "status": "concluido",
            "steps": len(self.history),
            "history": [
                {"tool": h["action"]["tool"], "result": str(h["result"])[:200]}
                for h in self.history
            ],
        }
```

### Configuracao YAML

```yaml
mini_agent:
  name: "mini-agent-jarvis"
  max_steps: 10
  model:
    provider: ollama
    name: "mistral:7b"
    temperature: 0.3
  tools:
    - search_files
    - read_file
    - edit_file
    - create_file
    - execute_command
    - path_exists
  safety:
    max_files_per_session: 3
    require_validation: true
    backup_before_edit: false
```

## Fluxo do Mini-Agent

```
[Entrada]: Tarefa do usuario
     |
[Step 1]: Entender o contexto
  -> search_files para localizar arquivos
  -> read_file para ler conteudo
     |
[Step 2]: Planejar a mudanca
  -> Definir objetivo em 2-3 frases
  -> Listar arquivos, mudancas e validacoes
     |
[Step 3]: Executar
  -> edit_file para alterar
  -> create_file para novos arquivos
     |
[Step 4]: Validar
  -> execute_command para testes/lint
  -> Verificar se nao ha regression
     |
[Step 5]: Resumir
  -> Listar arquivos alterados
  -> Listar comandos executados
  -> Resumo do resultado
```

## Exemplo de Prompt do Agente

```
Voce e um assistente de desenvolvimento. Meu objetivo e {objetivo}.
Use search_files para encontrar arquivos relevantes, depois read_file
para entender o contexto. Planeje as mudancas, aplique-as com edit_file
e valide com execute_command. No final, escreva um resumo curto.
```

## Exemplo de Caso Real

```python
# Objetivo: corrigir bug no backend de voz
agent = MiniAgent({
    "max_steps": 10,
    "tools": ["search_files", "read_file", "edit_file", "execute_command"]
})

task = """
1. search_files por 'voice' e 'audio' em PROJECT_JARVIS_5.0
2. read_file do modulo de captura de voz
3. edit_file para melhorar tratamento de entrada
4. execute_command para rodar teste de integracao
"""

result = agent.run(task)
print(json.dumps(result, indent=2))
```

## Regras do Mini-Agent

1. Antes de editar, SEMPRE leia o arquivo completo relevante.
2. Nao faca mudancas amplas em mais de tres arquivos sem plano.
3. Se o projeto tiver testes, execute-os apos cada alteracao.
4. Preserve comentarios e estilo existentes sempre que possivel.
5. Se uma ferramenta falhar, tente 1 vez com abordagem alternativa.
6. Ao final, forneca um resumo executivo do que foi feito.

## Tratamento de Erros

```python
class MiniAgentError(Exception):
    pass

class ToolExecutionError(MiniAgentError):
    def __init__(self, tool: str, params: dict, reason: str):
        self.tool = tool
        self.params = params
        self.reason = reason
        super().__init__(f"Falha em {tool}: {reason}")

class MaxStepsError(MiniAgentError):
    def __init__(self, steps: int):
        super().__init__(f"Maximo de {steps} steps atingido sem conclusao")
```

## Integracao com VS Code

```json
{
  "key": "ctrl+shift+m",
  "command": "workbench.action.terminal.sendSequence",
  "args": { "text": "python -c \"from mini_agent import MiniAgent; agent = MiniAgent({}); agent.run('${selectedText}')\"\n" }
}
```

## Sugestoes de Metas

- Adicionar novo endpoint de RAG.
- Melhorar documentacao de `PROJECT_JARVIS_5.0`.
- Criar testes para a memoria persistente.
- Refatorar modulo de autenticacao.

## Referencias

- [[programador.agent]] — Agente completo para desenvolvimento.
- [[mcp-operators]] — Operadores MCP para acoes.
- [[direct-agent-prompts]] — Prompts prontos para o agente.
- [[best-practices]] — Boas praticas de uso.
