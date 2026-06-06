---
title: "Sistemas de RAG Avançado no Vault"
description: "Playbook para melhorar precisão, manutenção e avaliação do RAG local do JARVIS sem duplicar o guia básico."
tags: [rag, embeddings, busca-semantica, engenharia, jarvis, playbook, jarvis-engenharia]
date: 2026-05-20
updated: 2026-06-05
---

# Sistemas de RAG Avançado no Vault

Esta nota complementa [[RAG-Local-Guide]]. O guia local explica o mínimo: FAISS, `all-MiniLM-L6-v2`, índice e metadados. Este playbook trata do que melhora qualidade: preparação das notas, chunking, reranking, avaliação, manutenção e governança.

## Objetivo

Um RAG bom não é apenas “buscar top-k embeddings”. Ele precisa responder com contexto suficiente, sem trazer ruído e sem indexar informação sensível indevidamente.

Critérios de qualidade:

- recuperar notas certas para perguntas reais;
- preservar fonte e caminho do arquivo;
- evitar chunks quebrados no meio de ideias;
- priorizar notas atuais e bem estruturadas;
- permitir reindexação segura;
- respeitar privacidade e frontmatter sensível.

## Pipeline recomendado

```text
nota Markdown → normalização → chunking semântico → embeddings → índice vetorial → busca → reranking → montagem de contexto → resposta com fontes
```

### 1. Normalização

Antes de gerar embeddings:

- remover blocos vazios, metadados irrelevantes e ruído de template;
- preservar títulos, subtítulos e backlinks importantes;
- manter o caminho do arquivo como metadado;
- respeitar campos como `sensivel: true` quando existirem;
- evitar indexar logs, caches, transcrições longas e arquivos temporários.

## Chunking por estrutura Markdown

Evite dividir tudo em blocos fixos. O vault é Markdown, então a estrutura já carrega significado.

Estratégia prática:

1. separar por `#`, `##` e `###`;
2. manter o título da nota e o caminho em todos os chunks;
3. juntar seções pequenas demais;
4. quebrar seções enormes por parágrafo ou lista;
5. nunca separar tabela do título que explica a tabela;
6. preservar backlinks próximos do trecho.

Exemplo de metadado por chunk:

```json
{
  "file": "Conhecimento-Geral/Saude/Sono-e-Ritmo-Circadiano.md",
  "heading": "Ciclo Circadiano",
  "tags": ["saude", "sono"],
  "updated": "2026-05-20",
  "sensitive": false
}
```

## Reranking

A busca vetorial encontra candidatos; o reranking escolhe o que realmente entra no contexto.

Sinais úteis:

- similaridade vetorial;
- presença literal de termos da consulta;
- proximidade com notas hub ou índices;
- data de atualização;
- densidade de conteúdo útil;
- penalização de notas duplicadas;
- prioridade para notas do domínio correto.

Modelo simples:

```text
score_final = score_vetorial + boost_termo + boost_dominio + boost_recencia - penalidade_ruido
```

Não precisa começar com reranker neural. Um reranking híbrido lexical + semântico já melhora muito.

## Índices por domínio

Para um vault grande, um único índice pode misturar assuntos demais. Considere índices ou filtros por domínio:

- `Conhecimento-Geral/Saude`
- `Conhecimento-Geral/IA-para-Programacao`
- `JARVIS/04-Engineering`
- `Projetos`
- `Will-Pessoal` com regras de privacidade mais rígidas

O índice pode continuar fisicamente único, desde que os metadados permitam filtros por pasta, tag e sensibilidade.

## Avaliação contínua

Crie um conjunto pequeno de perguntas recorrentes e confira se o RAG recupera as notas esperadas.

Exemplos:

| Pergunta | Notas esperadas |
|---|---|
| Como consultar o cérebro local? | [[RAG-Local-Guide]] |
| Como evitar duplicidade ao criar notas? | notas de organização e higiene de repo |
| Como melhorar sono e foco? | [[Sono-e-Ritmo-Circadiano]], [[Higiene-do-Sono-e-Recuperacao]] |
| Como usar MCP para ler arquivos? | [[MCP-Client-Examples]] |

Métricas simples:

- acerto no top-3;
- acerto no top-5;
- quantidade de ruído;
- resposta cita fonte correta?;
- resposta usou nota desatualizada?.

## Manutenção do índice

Checklist:

- [ ] reindexar após mudanças grandes no vault;
- [ ] remover chunks de arquivos deletados;
- [ ] validar se `metadata.json` aponta para arquivos existentes;
- [ ] excluir arquivos sensíveis ou temporários;
- [ ] registrar versão do modelo de embedding;
- [ ] manter backup do índice anterior antes de upgrade.

## RAG-friendly no Obsidian

Para melhorar recuperação:

- use títulos descritivos;
- mantenha notas atômicas;
- inclua sinônimos importantes no texto;
- linke notas ponte e notas conceituais;
- evite parágrafos gigantes;
- escreva resumos no início de notas longas;
- use tags consistentes.

## Anti-padrões

- Indexar tudo sem filtro.
- Confiar apenas em top-1.
- Misturar logs/transcrições com conhecimento curado.
- Não registrar a fonte usada na resposta.
- Atualizar notas sem reindexar.
- Criar várias notas quase iguais em vez de linkar uma nota base.

## Links relacionados

- [[RAG-Local-Guide]]
- [[Arquitetura-Agente]]
- [[Ecossistema-e-Protocolos-MCP]]
- [[Seguranca-e-Governanca-LocalFirst]]
- [[Notas-RAG-Friendly]]
- [[Minimizacao-de-Dados-para-RAG-e-Agentes]]
