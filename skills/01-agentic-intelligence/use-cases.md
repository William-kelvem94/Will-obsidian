---
tags: [skills, skills-ai, use-cases, examples]
updated: 2026-05-16
title: "Casos de Uso — Inteligencia Agentica"
---

# Casos de Uso — Inteligencia Agentica

Este arquivo apresenta casos de uso reais com configuracoes, fluxos passo a passo, resultados esperados e variacoes. Cada caso pode ser adaptado para diferentes projetos.

## 1. Refatoracao de Codigo Existente

**Cenario**: Melhorar legibilidade e manutencao de um componente React.

**Configuracao**:
```yaml
agente: programador.agent
ferramentas: [search_files, read_file, edit_file, execute_command]
validacao: pnpm lint && pnpm test
```

**Fluxo**:
1. `search_files("src/components/LoginForm.tsx")` — localizar o arquivo.
2. `read_file("src/components/LoginForm.tsx")` — entender o comportamento.
3. Planejar: extrair logica de formulario para hook `useLoginForm`.
4. `edit_file` — aplicar extracao de hook.
5. `execute_command("pnpm test")` — validar.

**Resultado esperado**: Componente 40% menor, logica testavel isoladamente, testes existentes passando.

**Variacao**: React para Vue, extrair composable `useLoginForm`.

## 2. Correcao de Bug com Explicacao

**Cenario**: Login falha quando usuario nao tem token.

**Configuracao**:
```yaml
agente: programador-pesquisador.agent
abordagem: ReAct + Reflexion
ferramentas: [search_files, read_file, edit_file, execute_command]
```

**Fluxo**:
1. Pesquisar: "Onde o token e verificado em auth.py?"
2. `grep_search("token")` em `backend/auth.py`.
3. `read_file` — identificar que a verificacao ocorre depois do uso.
4. `edit_file` — mover verificacao para antes do uso.
5. `execute_command("pytest tests/test_auth.py")` — validar.

**Resultado esperado**: Bug corrigido, teste de regressao adicionado, documentacao da causa raiz.

**Variacao**: Bug de permissao em API REST, usar `grep_search` para encontrar middleware.

## 3. Implementacao de Pipeline RAG

**Cenario**: Adicionar busca semantica ao JARVIS usando FAISS.

**Configuracao**:
```yaml
agente: programador-pesquisador.agent
referencias: [memory-architectures, project-jarvis-prompts]
ferramentas: [create_file, edit_file, execute_command]
```

**Fluxo**:
1. Ler [[memory-architectures]] para schema FAISS.
2. `create_file("backend/memory/vector_store.py")` — implementar classe `SemanticMemory`.
3. `edit_file("backend/app.py")` — adicionar rota `/api/search`.
4. `execute_command("pytest tests/test_memory.py")` — validar pipeline.

**Resultado esperado**: API com busca semantica funcional, 3 endpoints (inserir, buscar, deletar).

## 4. Cricao de Template de Prompt

**Cenario**: Criar template para revisao de PR.

**Configuracao**:
```yaml
agente: direto (direct-agent-prompts)
template_base: templates.md
saida: skills/01-agentic-intelligence/prompts.md
```

**Fluxo**:
1. Identificar padrao: revisoes de PR sempre pedem seguranca + performance + estilo.
2. Criar template com placeholders: `{arquivo}`, `{foco}`.
3. Adicionar a [[prompts]] na secao de revisao.
4. Testar com PR real.

**Template gerado**:
```
"Revise o codigo em {arquivo} com foco em {foco}.
Liste: (1) problemas de seguranca, (2) oportunidades de performance,
(3) sugestoes de estilo. Para cada item, inclua linha e sugestao."
```

## 5. Orquestracao Multi-Agente para Feature Complexa

**Cenario**: Implementar nova feature fullstack (API + Frontend + Testes).

**Configuracao**:
```yaml
orquestrador: multi-agent-orchestration
agentes:
  - pesquisador: pesquisa requisitos e documentacao
  - programador: implementa backend e frontend
  - revisor: revisa e sugere melhorias
  - testador: cria e executa testes
```

**Fluxo**:
1. Diretor divide: `Pesquisador -> Programador -> Revisor -> Testador`.
2. Cada agente recebe contexto comprimido do anterior.
3. Monitor valida saida final contra requisitos.

**Resultado esperado**: Feature completa em 4 iteracoes, cada agente focando em sua especialidade.

## 6. Consenso entre Agentes para Decisao de Arquitetura

**Cenario**: Escolher entre SQL e NoSQL para novo modulo.

**Configuracao**:
```yaml
metodo: votacao ponderada
agentes:
  - Arquiteto A: defende SQL (peso 1.0)
  - Arquiteto B: defende NoSQL (peso 1.0)
  - Arquiteto C: juiz (peso 1.5)
```
**Fluxo**: Debate -> Votacao ponderada -> Decisao documentada.

## 7. Automacao de Documentacao

**Cenario**: Gerar README automatico para projeto existente.

**Fluxo**: `read_file` da estrutura -> `llm_call` para resumo -> `create_file` README.md.

## 8. Configuracao de Ambiente Dev

**Cenario**: Preparar ambiente Windows para desenvolvimento JARVIS.

**Fluxo**: Docker compose -> variaveis de ambiente -> validacao com `curl`.

## 9. Pipeline de Memoria Episodica

**Cenario**: Agente aprende com erros passados via Reflexion.

**Fluxo**: Executar -> Falhar -> Refletir -> Registrar -> Repetir com contexto.

## 10. Deploy com Docker

**Cenario**: Subir fullstack com Docker.

**Fluxo**: `read_file` docker-compose.yml -> `edit_file` para servicos -> `execute_command` docker compose up.

## Referencias

- [[mcp-operators]] — Operadores para execucao dos casos.
- [[advanced-workflows]] — Fluxos mais complexos.
- [[multi-agent-orchestration]] — Orquestracao multi-agente.
- [[project-jarvis-prompts]] — Prompts especificos para JARVIS.
