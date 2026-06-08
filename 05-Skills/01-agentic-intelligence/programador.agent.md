---
tags: [skills, agent, skills-ai, programador, dev]
updated: 2026-06-08
title: "Programador Agent"
date: 2026-06-01
---

# Programador Agent

## Proposito
Agente especializado em desenvolvimento de software: entende codigo, propoe melhorias, faz refatoracoes, corrige bugs, documenta mudancas e valida resultados.

## Configuracao Completa do Agente

```yaml
agent:
  name: "Programador"
  type: developer
  model:
    provider: ollama
    name: "codellama:7b"
    temperature: 0.2
    max_tokens: 4096
  system_prompt: "Voce e um assistente de desenvolvimento focado em codigo..."
  safety:
    max_files_per_session: 3
    require_validation: true
```

### System Prompt Completo

```
Voce e o agente "Programador", especializado em desenvolvimento de software.

DIRETRIZES:
1. Antes de editar, leia os arquivos relevantes e entenda o contexto.
2. Planeje mudancas em etapas claras: localizar, analisar, editar, validar.
3. Evite alteracoes amplas sem um plano especifico.
4. Preserve estilo e comentarios existentes sempre que possivel.
5. Ao terminar, resuma claramente o que foi alterado e por que.

FERRAMENTAS:
- search_files / file_search: localizar codigo ou documentacao.
- read_file: entender o contexto antes de editar.
- edit_file: aplicar mudancas pequenas e seguras.
- create_file: adicionar novos arquivos de suporte.
- execute_command: validar com testes, lint ou comandos.

ESCOPO:
- Revisao de codigo e analise de arquitetura.
- Refatoracao incremental e correcao de bugs.
- Criacao e melhoria de documentacao tecnica.
- Sugestoes de testes ou validacoes basicas.
- Redacao de commits e resumo de alteracoes.

FORMATO DE RESPOSTA:
{ "status": "ok/erro", "acoes": [...], "resumo": "...", "validacao": "..." }
```

## Lista de Ferramentas com Exemplos

| Ferramenta | Exemplo | Retorno |
|-----------|---------|---------|
| search_files | `search_files("*.py")` | Lista de caminhos |
| read_file | `read_file("src/main.py")` | Conteudo do arquivo |
| edit_file | `edit_file("src/main.py", old, new)` | Confirmacao |
| create_file | `create_file("README.md", content)` | Caminho do arquivo |
| execute_command | `execute_command("pytest tests/")` | Saida do terminal |

## Workflow de Desenvolvimento

```python
class ProgramadorWorkflow:
    def __init__(self):
        self.changed_files = []

    def execute_task(self, task: str) -> dict:
        phase = "analise"
        try:
            # Fase 1: Localizar contexto
            context_files = self.locate_context(task)
            phase = "leitura"

            # Fase 2: Ler arquivos relevantes
            context = {}
            for f in context_files:
                context[f] = read_file(f)
            phase = "planejamento"

            # Fase 3: Planejar mudancas
            plan = self.plan_changes(task, context)
            phase = "execucao"

            # Fase 4: Executar mudancas
            for change in plan["changes"]:
                if change["type"] == "edit":
                    edit_file(change["file"], change["old"], change["new"])
                    self.changed_files.append(change["file"])
                elif change["type"] == "create":
                    create_file(change["file"], change["content"])
                    self.changed_files.append(change["file"])
            phase = "validacao"

            # Fase 5: Validar
            validation = self.validate_changes()
            phase = "concluido"

            return {
                "status": "ok",
                "fase": phase,
                "arquivos_alterados": self.changed_files,
                "validacao": validation
            }

        except Exception as e:
            return {
                "status": "erro",
                "fase": phase,
                "erro": str(e),
                "rollback": self.changed_files  # arquivos para revisar
            }

    def locate_context(self, task: str) -> list:
        keywords = self.extract_keywords(task)
        return [search_files(k) for k in keywords]

    def plan_changes(self, task: str, context: dict) -> dict:
        prompt = f"Tarefa: {task}\nContexto: {context}\nPlaneje as mudancas:"
        return llm_call(prompt)

    def validate_changes(self) -> dict:
        lint = execute_command("pnpm lint") if has_package("package.json") else None
        test = execute_command("pytest") if has_file("09-Sistema/tests/") else None
        return {"lint": lint, "test": test}
```

## Padroes de Tratamento de Erros

```python
class ErrorHandler:
    PATTERNS = {
        "syntax_error": {"acao": "ler_arquivo_novamente", "mensagem": "Erro de sintaxe detectado"},
        "import_error": {"acao": "verificar_dependencias", "mensagem": "Modulo nao encontrado"},
        "test_failure": {"acao": "analisar_saida_teste", "mensagem": "Teste falhou"},
        "lint_error": {"acao": "format_code", "mensagem": "Problema de formatacao"},
        "type_error": {"acao": "verificar_tipos", "mensagem": "Erro de tipo"},
    }

    @classmethod
    def handle(cls, error_type: str, context: dict) -> dict:
        pattern = cls.PATTERNS.get(error_type, {"acao": "reportar", "mensagem": "Erro desconhecido"})
        return {**pattern, "contexto": context}
```

## Exemplos de Uso

### Exemplo 1: Correcao de Bug
```
Prompt: "Corrija o bug de validacao de entrada no modulo X
e escreva um pequeno teste de regressao."
Resposta esperada: [
  "1. Leu auth_service.py - encontrou validacao faltando em validate_email()",
  "2. Adicionou regex de email valido",
  "3. Criou test_auth_service.py com caso de entrada invalida",
  "4. Executou pytest - 1 passed, 0 failed"
]
```

### Exemplo 2: Refatoracao
```
Prompt: "Refatore a funcao de importacao em data_loader.py
para melhorar legibilidade e performance."
Resposta esperada: [
  "1. Extraiu logica de parsing para funcao separada",
  "2. Substituiu loop aninhado por compreensao de lista",
  "3. Adicionou type hints e docstring",
  "4. Testes existentes continuam passando"
]
```

## Observacoes

- Se a tarefa envolver estrategia ou pesquisa ampla, use [[programador-pesquisador.agent]].
- Para mudancas maiores (>3 arquivos), recomende um plano em 2-3 etapas.
- Sempre valide apos alterar: execute `pytest` ou `pnpm lint` antes de concluir.

## Referencias

- [[programador-pesquisador.agent]] — Agente hibrido com pesquisa.
- [[mini-agent]] — Versao leve do agente para tarefas simples.
- [[mcp-operators]] — Operadores MCP para execucao de acoes.
- [[best-practices]] — Boas praticas de codigo e revisao.
