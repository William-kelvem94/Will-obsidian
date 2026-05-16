---
tags: [skills, skills-ai, mcp, operators, pipeline]
updated: 2026-05-16
title: "Operadores MCP para Inteligencia Agentica"
---

# Operadores MCP para Inteligencia Agentica

Este arquivo descreve operadores de acao do Model Context Protocol (MCP) para agentes que executam tarefas de codigo. Inclui definicoes, padroes de composicao, pipelines e tratamento de erros.

## Operadores Basicos

| Operador | Sintaxe | Descricao | Retorno |
|----------|---------|-----------|---------|
| read_file | `read_file(path)` | Le conteudo de um arquivo | string ou null |
| search_files | `search_files(pattern)` | Busca arquivos por nome | list |
| edit_file | `edit_file(path, old, new)` | Substitui texto exato em arquivo | bool |
| create_file | `create_file(path, content)` | Cria novo arquivo com conteudo | bool |
| append_file | `append_file(path, content)` | Adiciona ao final de arquivo | bool |
| delete_file | `delete_file(path)` | Remove arquivo | bool |
| rename_file | `rename_file(old, new)` | Renomeia ou move arquivo | bool |
| execute_command | `execute_command(cmd)` | Executa comando no terminal | string |
| path_exists | `path_exists(path)` | Verifica existencia | bool |
| diff_file | `diff_file(p1, p2)` | Compara versoes | string |

## Operadores Auxiliares

```python
def list_dir(path: str) -> list:
    """Lista arquivos e pastas em um diretorio."""
    import os
    return os.listdir(path)

def get_file_stats(path: str) -> dict:
    """Retorna tamanho, data de modificacao e existencia."""
    import os
    from datetime import datetime
    if not os.path.exists(path):
        return {"exists": False}
    stat = os.stat(path)
    return {
        "exists": True,
        "size": stat.st_size,
        "modified": datetime.fromtimestamp(stat.st_mtime).isoformat(),
        "is_dir": os.path.isdir(path)
    }

def read_yaml(path: str) -> dict:
    """Le dados estruturados de YAML."""
    import yaml
    with open(path) as f:
        return yaml.safe_load(f)

def write_yaml(path: str, data: dict) -> bool:
    """Grava dados estruturados em YAML."""
    import yaml
    with open(path, "w") as f:
        yaml.dump(data, f)
    return True
```

## Operadores de Inspecao Avancada

```python
def grep_search(query: str, is_regex: bool = False,
                include_pattern: str = None, max_results: int = 50) -> list:
    """Busca padroes de texto ou regex no codigo."""
    import subprocess
    cmd = ["rg", "--line-number"]
    if is_regex:
        cmd.append("--regexp")
    if include_pattern:
        cmd.extend(["--glob", include_pattern])
    cmd.extend([query, "."])
    result = subprocess.run(cmd, capture_output=True, text=True)
    lines = result.stdout.strip().split("\n")[:max_results]
    return lines

def get_changed_files(repo_path: str = ".") -> list:
    """Mostra arquivos alterados no repositorio."""
    import subprocess
    result = subprocess.run(
        ["git", "diff", "--name-only"],
        capture_output=True, text=True, cwd=repo_path
    )
    return result.stdout.strip().split("\n") if result.stdout.strip() else []

def multi_replace_string_in_file(replacements: list) -> list:
    """Aplica varias substituicoes atomicas em um ou mais arquivos.

    replacements = [
        {"file": "src/main.py", "old": "foo", "new": "bar"},
        {"file": "src/utils.py", "old": "baz", "new": "qux"},
    ]
    """
    results = []
    for r in replacements:
        success = edit_file(r["file"], r["old"], r["new"])
        results.append({"file": r["file"], "success": success})
    return results
```

## Padroes de Composicao

### Pipeline Sequencial

```python
def pipeline_sequencial(task: str) -> dict:
    """Executa operadores em sequencia, passando resultado ao proximo."""
    files = search_files(task)           # Step 1
    if not files:
        return {"error": "Nenhum arquivo encontrado"}
    content = read_file(files[0])         # Step 2
    if content is None:
        return {"error": "Falha ao ler arquivo"}
    success = edit_file(files[0], ...)    # Step 3
    if not success:
        return {"error": "Falha ao editar"}
    test_result = execute_command("pytest")  # Step 4
    return {"success": True, "test": test_result}
```

### Pipeline com Condicoes

```python
def pipeline_condicional(task: str) -> dict:
    """Executa operadores com base em condicoes."""
    if not path_exists(task["target"]):
        create_file(task["target"], task["template"])
        return {"status": "created"}

    content = read_file(task["target"])
    if "TODO" in content:
        edit_file(task["target"], "TODO", task["replacement"])
        return {"status": "updated"}

    return {"status": "no_changes"}
```

### Pipeline com Tolerancia a Falhas

```python
def pipeline_resiliente(steps: list) -> list:
    """Executa pipeline com tolerancia a falhas."""
    results = []
    for step in steps:
        try:
            result = step["fn"](**step["params"])
            results.append({"step": step["name"], "status": "ok", "result": result})
        except Exception as e:
            results.append({"step": step["name"], "status": "erro", "error": str(e)})
            if step.get("critical", False):
                break
    return results
```

## Tratamento de Erros por Operador

| Operator | Erro Comum | Tratamento |
|----------|-----------|------------|
| read_file | FileNotFoundError | Retornar None, tentar search_files |
| edit_file | oldString nao encontrado | Reler arquivo, verificar conteudo atual |
| create_file | PermissionError | Verificar permissoes do diretorio |
| execute_command | TimeoutExpired | Aumentar timeout ou dividir comando |
| delete_file | FileNotFoundError | Verificar path_exists primeiro |
| rename_file | FileExistsError | Usar nome alternativo ou sobrescrever |
| grep_search | Nenhum resultado | Expandir query ou usar search_files |

## Exemplo de Pipeline Completo

```python
def fluxo_refatoracao(arquivo_alvo: str) -> dict:
    pipeline = [
        {"name": "localizar", "fn": search_files, "params": {"pattern": arquivo_alvo}},
        {"name": "ler", "fn": read_file, "params": {"path": arquivo_alvo}},
        {"name": "editar", "fn": edit_file, "params": {
            "path": arquivo_alvo,
            "old": "funcao_antiga",
            "new": "funcao_nova"
        }, "critical": True},
        {"name": "formatar", "fn": lambda p: format_code(p), "params": {"path": arquivo_alvo}},
        {"name": "testar", "fn": execute_command, "params": {"command": "pytest"}},
        {"name": "comparar", "fn": diff_file, "params": {"oldPath": arquivo_alvo + ".bak", "newPath": arquivo_alvo}},
    ]
    return pipeline_resiliente(pipeline)
```

## Regras de Seguranca

1. Nao execute `delete_file` sem confirmar backup ou ausencia de dependencia.
2. Nao altere grandes blocos sem um plano e validacao.
3. Para mudancas criticas, crie nota de revisao em `skills/`.
4. Evite edicoes multiplas sem `diff_file` e resumo final.
5. Use `path_exists` antes de `read_file` ou `delete_file`.
6. Prefira `edit_file` com substituicao exata em vez de reescrita completa.

## Boas Praticas de Uso

- Use `read_file` com trecho se o arquivo for grande.
- Use `search_files` com termos especificos em vez de adivinhar caminho.
- Prefira `append_file` para adicionar exemplos, docs ou casos de teste.
- Use `grep_search` para encontrar rapidamente padroes no codigo.
- Combine `execute_command` com `pytest` ou `pnpm lint` para validacao.

## Referencias

- [[mcp]] — Visao geral do Model Context Protocol.
- [[mini-agent]] — Implementacao de agente usando estes operadores.
- [[quick-reference]] — Cheat sheet de operadores.
- [[best-practices]] — Boas praticas de uso de operadores.
- [[advanced-workflows]] — Workflows complexos com composicao.
