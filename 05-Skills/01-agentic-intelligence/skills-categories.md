---
tags: [skills, skills-ai, categories, taxonomy]
updated: 2026-06-08
title: "Categorias de Skills para IA"
date: 2026-06-01
---

# Categorias de Skills para IA

Este arquivo categoriza todas as skills do hub `skills/01-agentic-intelligence/` por dominio tecnico, com descricoes detalhadas, exemplos de uso e matriz de sobreposicao entre categorias.

## Categorias Principais

### 1. Inteligencia Agentica (Core)
Skills relacionadas a agentes de IA, orquestracao, consenso e padroes de raciocinio.

**Arquivos**: `01-agentic-intelligence/`
**Quando usar**: tarefas que exigem coordenacao entre multiplos agentes, raciocinio estruturado ou tomada de decisao autonomia.

### 2. Desenvolvimento Fullstack
Frontend, backend e database.

**Exemplos de uso**:
- Criar componente React com Tailwind.
- Implementar API REST em FastAPI.
- Modelar schema Prisma ou SQL.

**Ferramentas**: React, Next.js, Express, FastAPI, Postgres, Prisma, Redis.

### 3. IA Local e RAG
Modelos locais, embeddings, bancos vetoriais e pipelines de memoria.

**Exemplos de uso**:
- Configurar Ollama com Mistral para desenvolvimento local.
- Implementar pipeline de RAG com FAISS e Chroma.
- Criar sistema de memoria persistente para agente autonomo.

**Ferramentas**: Ollama, LM Studio, FAISS, Chroma, sentence-transformers.

### 4. Infraestrutura e DevOps
Docker, containers, CI/CD e configuracao de ambiente.

**Exemplos de uso**:
- Criar `Dockerfile` e `docker-compose.yml` para projeto fullstack.
- Configurar GitHub Actions para CI/CD.
- Gerenciar variaveis de ambiente com `.env`.

**Ferramentas**: Docker, docker-compose, Nginx, GitHub Actions, Terraform.

### 5. Automacao e Produtividade
Scripts de automacao, scraping, documentacao automatica.

**Exemplos de uso**:
- Automatizar geracao de README com template.
- Criar script de backup do vault Obsidian.
- Configurar pipeline de pre-commit para lint + testes.

**Ferramentas**: Playwright, Selenium, pre-commit, shell script.

### 6. Agentes e Assistentes
Definicao de agentes, system prompts, workflows multi-turn.

**Exemplos de uso**:
- Definir agente `Programador` com ferramentas MCP.
- Criar workflow de pesquisa com agente `Pesquisador`.
- Orquestrar debate entre agentes para decisao de arquitetura.

**Ferramentas**: [[programador.agent]], [[programador-pesquisador.agent]], [[multi-agent-orchestration]].

### 7. MCP e Operacoes
Model Context Protocol, operadores de arquivo, terminal e busca.

**Exemplos de uso**:
- Executar pipeline de leitura-editacao-validacao com MCP.
- Usar operadores avancados como `grep_search` e `diff_file`.
- Compor operadores em pipelines complexos.

**Ferramentas**: [[mcp-operators]], [[mcp]], [[mini-agent]].

### 8. Prompt Engineering
Templates, tecnicas de prompt, avaliacao e refinamento.

**Exemplos de uso**:
- Usar Chain-of-Thought para problemas complexos.
- Aplicar few-shot learning com exemplos no prompt.
- Avaliar qualidade de saida com metrica de relevancia.

**Ferramentas**: [[prompts]], [[templates]], [[direct-agent-prompts]].

## Matriz de Sobreposicao entre Categorias

```
              | Agentica | Fullstack | IA Local | DevOps | Automacao | Agentes | MCP | PromptEng
--------------|----------|-----------|----------|--------|-----------|---------|-----|----------
Agentica      |    X     |    M      |    A     |   B    |    M      |    A    |  A  |    A
Fullstack     |    M     |    X      |    B     |   M    |    M      |    M    |  M  |    B
IA Local      |    A     |    B      |    X     |   B    |    B      |    A    |  M  |    M
DevOps        |    B     |    M      |    B     |   X    |    A      |    B    |  B  |    B
Automacao     |    M     |    M      |    B     |   A    |    X      |    M    |  A  |    M
Agentes       |    A     |    M      |    A     |   B    |    M      |    X    |  A  |    A
MCP           |    A     |    M      |    M     |   B    |    A      |    A    |  X  |    B
PromptEng     |    A     |    B      |    M     |   B    |    M      |    A    |  B  |    X

Legenda: A = Alta sobreposicao, M = Media, B = Baixa
```

## Guia de Selecao de Categoria

| Se voce precisa... | Use a categoria... | E comeco por... |
|-------------------|-------------------|-----------------|
| Coordenar agentes | Inteligencia Agentica | [[multi-agent-orchestration]] |
| Codar uma feature | Desenvolvimento Fullstack | skills/fullstack/ |
| Adicionar memoria | IA Local e RAG | [[memory-architectures]] |
| Configurar ambiente | DevOps | skills/infra/ |
| Automatizar tarefa | Automacao | skills/automation/ |
| Definir um agente | Agentes | [[programador.agent]] |
| Usar ferramentas | MCP | [[mcp-operators]] |
| Criar prompts | Prompt Engineering | [[prompts]] |

## Referencias

- [[INDEX]] — Indice completo do hub.
- [[use-cases]] — Casos de uso por categoria.
- [[best-practices]] — Boas praticas para todas as categorias.
- [[quick-reference]] — Referencia rapida por ferramenta.
