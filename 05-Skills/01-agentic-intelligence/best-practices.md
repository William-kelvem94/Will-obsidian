---
tags: [skills, skills-ai, best-practices, guidelines, review]
updated: 2026-06-13
title: "Boas Praticas — Inteligencia Agentica"
date: 2026-06-01
---

# Boas Praticas — Inteligencia Agentica

Este guia reune boas praticas para usar IA no desenvolvimento e manter a organizacao do vault. Inclui catalogo de anti-padroes, checklist de revisao e convencoes de nomenclatura.

## Estrutura de Trabalho

- Use `skills/01-agentic-intelligence/README.md` como hub principal.
- Separe prompts, workflows e templates em arquivos diferentes.
- Mantenha anotacoes do projeto em `skills/` e nao misture com codigo de producao.
- Use tags como `#agentic`, `#mcp`, `#skill`, `#memory` para localizacao rapida.
- Prefixo de pastas numerico para ordenacao: `01-agentic-intelligence/`, `02-fullstack/`.

## Como Perguntar ao Agente

| Pratica | Exemplo Ruim | Exemplo Bom |
|---------|-------------|-------------|
| Seja especifico | "Corrija o codigo" | "Corrija o bug de validacao em `auth.py` linha 42" |
| Forneca contexto | "Refatore isso" | "Refatore `src/services/user.py` separando logging da logica de negocios" |
| Pasos numerados | "Melhore o projeto" | "1. Leia o arquivo, 2. Identifique problemas, 3. Corrija, 4. Teste" |
| Defina formato | "Me de o resultado" | "Retorne JSON com: `status`, `changes`, `validation`" |

## Anti-Padroes (O que NAO fazer)

| Anti-Padrao | Problema | Solucao |
|-------------|----------|---------|
| Editar sem ler | Quebra codigo sem entender contexto | Sempre `read_file` antes de `edit_file` |
| Mudancas massivas | Difcil reverter, alto risco de erro | Dividir em commits menores, 1 arquivo por vez |
| Prompt generico | Resposta superficial, precisa de iteracoes | Incluir arquivo, funcao, objetivo e formato |
| Ignorar validacao | Bug passa despercebido | Rodar `pytest` / `pnpm lint` apos cada mudanca |
| Nao documentar | Perde contexto da decisao | Criar nota de processo ou resumo apos mudanca |
| Confiar cegamente | IA pode alucinar caminhos de arquivo | Verificar `path_exists` antes de editar |
| Loop sem condicao de parada | Consome tokens infinitamente | Definir `max_iterations` ou `is_complete` |
| Misturar responsabilidades | Agente confunde papeis | Usar agente especifico para cada tarefa |

## Checklist de Revisao de Codigo

### Antes de Editar
- [ ] Leu o arquivo completo com `read_file`?
- [ ] Entendeu o contexto e dependencias?
- [ ] Verificou se ha testes existentes para o modulo?
- [ ] Planejou as mudancas em texto?

### Durante a Edicao
- [ ] Mudancas sao atomicas (1 arquivo por vez)?
- [ ] Preservou estilo e comentarios existentes?
- [ ] Adicionou tratamento de erro basico?
- [ ] Manteve compatibilidade com codigo existente?

### Apos a Edicao
- [ ] Executou `execute_command` para validar?
- [ ] Testes existentes continuam passando?
- [ ] Criou resumo das alteracoes?
- [ ] Atualizou documentacao relacionada?

## Convencoes de Nomenclatura

```
# Arquivos de agente
<nome-do-agente>.agent.md

# Arquivos de skill
<nome-da-skill>.md

# Pastas numeradas
01-<categoria>/
02-<categoria>/

# Tags
#agentic    -> inteligencia agentica
#mcp        -> model context protocol
#memory     -> arquiteturas de memoria
#reasoning  -> padroes de raciocinio
#skill      -> skill generica
#agent      -> definicao de agente
#reference  -> referencia rapida
```

## Fluxo Ideal de IA

```python
class IdealWorkflow:
    def execute(self, task: str) -> dict:
        # 1. Localizar contexto
        files = search_files(task)

        # 2. Entender arquivos
        contexts = [read_file(f) for f in files]

        # 3. Planejar
        plan = self.plan(task, contexts)

        # 4. Executar mudancas
        changes = []
        for step in plan:
            result = edit_file(step["file"], step["old"], step["new"])
            changes.append(result)

        # 5. Validar
        validation = execute_command("pytest")

        # 6. Documentar
        summary = self.summarize(task, changes, validation)
        return {"changes": changes, "validation": validation, "summary": summary}
```

## Integracao com o Projeto

- Relacione cada skill ao projeto em `Projetos/` ou `Will-Pessoal/`.
- Use [[project-jarvis-prompts]] para tarefas especificas do ecossistema JARVIS.
- Crie notas de processo em `Will-Pessoal/Conhecimento/Leituras.md` se o aprendizado for valioso.
- Registre decisoes importantes em `JARVIS/Decisoes/` com data e contexto.

## Atualizacao Continua

- Revise e melhore estes arquivos a cada nova experiencia.
- Adicione novos templates quando identificar tarefas recorrentes.
- Atualize [[README]] com novas referencias e links.
- Mantenha [[INDEX]] sincronizado com a estrutura atual.

## Referencias

- [[mcp-operators]] — Operadores para execucao segura.
- [[quick-reference]] — Cheat sheet de comandos.
- [[skills-categories]] — Categorizacao de skills por dominio.
- [[use-cases]] — Casos de uso praticos com exemplos.
