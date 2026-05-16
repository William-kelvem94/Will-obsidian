---
tags: [skills, skills-ai, prompts, agent, direct]
updated: 2026-05-16
title: "Prompts Prontos para Agente de Chat Local"
---

# Prompts Prontos para Agente de Chat Local

Use estes prompts diretamente no seu agente de chat local (Ollama, LM Studio, Claude, etc). Eles foram formulados para o ecossistema JARVIS e tarefas de desenvolvimento. Cada prompt inclui parametros configuraveis e variacoes por papel do agente.

## Parametros de Configuracao

```yaml
# Configuracao padrao para prompts diretos
model:
  temperature: 0.3
  max_tokens: 4096
  top_p: 0.9
response_format: texto_estruturado
agentes_disponiveis:
  - programador: foco em codigo
  - pesquisador: foco em investigacao
  - revisor: foco em qualidade
  - arquiteto: foco em estrutura
```

## Prompts por Papel do Agente

### Programador (Foco em Codigo)

#### Prompt 1: Diagnostico Rapido de Projeto
```
Voce e um assistente de desenvolvimento. Analise o projeto {projeto} e indique:
1. Quais sao os principais componentes de backend, frontend e memoria?
2. Quais arquivos parecem ser responsaveis pelo fluxo de {funcionalidade}?
3. Quais sao os dois maiores riscos de implementacao deste projeto?

Parametros:
  temperatura: 0.2
  formato: lista numerada com evidencias de cada ponto
```

#### Prompt 2: Corrigir Bug no Backend
```
Encontre e corrija o bug em {arquivo} relacionado a {descricao_erro}.
Explique o problema e o que foi alterado. Ao final, sugira um teste
que valide a correcao.

Passos obrigatorios:
1. search_files para localizar o arquivo
2. read_file para entender o contexto
3. edit_file para corrigir
4. execute_command para validar
```

### Pesquisador (Foco em Investigacao)

#### Prompt 3: Arquitetura de Memoria
```
Sugira uma arquitetura de memoria persistente para {projeto},
usando Obsidian Vault, embeddings e FAISS. Explique passo a passo
onde cada componente deve ser implementado.

Requisitos de saida:
- Diagrama ASCII da arquitetura
- Lista de componentes com responsabilidades
- Fluxo de dados: insercao -> indexacao -> busca -> resposta
- Codigo Python para classe principal
```

#### Prompt 4: Endpoint RAG
```
Crie um endpoint FastAPI para {projeto} que receba texto, gere
embeddings e busque documentos relevantes em FAISS.

Especificacao:
- Rota: POST /api/search
- Body: {"query": "texto", "k": 3}
- Response: {"results": [{"document": "...", "score": 0.95}]}
- Tratamento de erro: 400 para query vazia, 500 para falha interna
```

### Revisor (Foco em Qualidade)

#### Prompt 5: Revisao de Codigo
```
Revise o codigo em {arquivo} e identifique melhorias de:
1. Performance: loops ineficientes, queries N+1, alocacao desnecessaria
2. Seguranca: injecao, vazamento de dados, autenticacao
3. Estilo: convencoes do projeto, legibilidade, comentarios

Para cada item, inclua: linha, problema atual, sugestao de correcao.
Use o formato:
| Linha | Problema | Sugestao |
```

#### Prompt 6: Revisao de PR
```
Revise este Pull Request. Foco em:
- Mudancas que podem quebrar funcionalidades existentes
- Ausencia de testes para novos codigos
- Variaveis de ambiente ou configuracao hardcoded
- Dependencias novas e seu impacto

Score final: aprovado/reprovado/com ressalvas
```

### Arquiteto (Foco em Estrutura)

#### Prompt 7: Melhoria de Arquitetura
```
Analise a arquitetura atual de {projeto} e proponha melhorias.
Considere:
- Separacao de responsabilidades entre modulos
- Fluxo de dados e estado
- Escalabilidade e manutencao
- Integracao com sistemas externos

Saida esperada: estado atual -> problemas -> estado proposto -> beneficios
```

#### Prompt 8: Design de Sistema
```
Projete um sistema para {requisito} considerando:
- Modelo: local (Ollama) ou API (Claude/GPT)
- Memoria: RAG com FAISS + Obsidian Vault
- Interface: chat web + API REST
- Deploy: Docker + Windows

Inclua: diagrama de componentes, fluxo de dados, decisoes tecnicas.
```

## Casos Praticos

### Caso 1: Estudo de IA Local e MCP
```
Voce e Programador e Pesquisador. Realize um estudo pratico usando:
- Projetos/EstudosFocados/IA-LOCAL.md
- skills/01-agentic-intelligence/mcp.md
- Projetos/EstudosFocados/Workspace-Study/Benchmark-IA-Local.md

Documente: passo a passo, benchmark de IA local, decisoes registradas.
```

### Caso 2: Saude do Cerebro (Vault)
```
Avalie a saude do segundo cerebro do Jarvis usando:
- Projetos/EstudosFocados/Workspace-Study/Brain-Health-Dashboard.md
- JARVIS/KnowledgeBase/Brain-Integration.md

Verifique: contexto ativo, ingestao de KB, decisoes recentes, memorias.
Proponha ajustes operacionais com prioridade (alta/media/baixa).
```

### Caso 3: Testes para Pipeline de Memoria
```
Gere casos de teste para o pipeline de memoria do Jarvis:
- Insercao: adicionar documento, verificar embedding gerado
- Busca: consultar termo similar, verificar relevancia ORdenada
- Integracao: enviar pergunta via API, verificar resposta com contexto
- Erro: enviar payload invalido, verificar status 422
```

## Guia de Uso

1. Copie qualquer prompt e cole no chat do agente.
2. Substitua `{variaveis}` pelos valores do seu contexto.
3. Ajuste `temperature` (0.1 para preciso, 0.7 para criativo).
4. Use follow-ups para refinamento: "Explique mais sobre X" ou "Gere codigo para Y".
5. Para tarefas longas, peja um plano primeiro, depois execute passo a passo.

## Referencias

- [[prompts]] — Biblioteca categorizada de templates.
- [[templates]] — Templates reutilizaveis para agentes.
- [[project-jarvis-prompts]] — Prompts focados no JARVIS 5.0.
- [[programador.agent]] — Agente especializado em codigo.
- [[programador-pesquisador.agent]] — Agente hibrido.
