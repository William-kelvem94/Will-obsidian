---
title: "Arquitetura RAG para Obsidian e JARVIS"
date: 2026-06-07
updated: 2026-06-07
type: guide
status: active
tags: [conhecimento-geral, ia, rag, obsidian, jarvis, arquitetura]
related: [[RAG-e-Memoria-para-Agentes]], [[Embeddings-e-Busca-Semantica]], [[Context-Engineering]], [[Avaliacao-de-RAG-e-Qualidade-de-Contexto]], [[../00-Mapas-e-Ontologia/00-Ontologia-de-Conhecimento-para-IA]]
summary: "Arquitetura prática para usar o Obsidian como base RAG do JARVIS, com ingestão, chunking, embeddings, recuperação, resposta e memória."
---

# Arquitetura RAG para Obsidian e JARVIS

Esta nota descreve uma arquitetura prática para transformar o Obsidian em uma base consultável por IA. O objetivo é permitir que o JARVIS ou qualquer agente leia conhecimento curado, recupere contexto relevante e responda com menos improviso.

## Objetivo

Criar um fluxo onde:

1. o Obsidian guarda conhecimento humano em Markdown;
2. um pipeline transforma notas em chunks;
3. os chunks viram embeddings;
4. uma busca semântica recupera contexto;
5. o agente monta uma resposta baseada em fontes internas;
6. aprendizados novos voltam para o vault como notas ou logs.

## Camadas da arquitetura

| Camada | Função | Exemplo |
|---|---|---|
| Fonte | arquivos Markdown do vault | `Conhecimentos-Gerais/` |
| Ingestão | leitura e normalização | script Python/Node |
| Chunking | divisão por sentido | cabeçalhos Markdown |
| Embeddings | representação vetorial | modelo local ou API |
| Vector store | armazenamento semântico | ChromaDB, Qdrant, FAISS |
| Retriever | busca de contexto | top-k por similaridade |
| Context builder | montagem de contexto final | notas + resumo + metadados |
| LLM | geração de resposta | local ou remoto |
| Avaliador | revisão da resposta | regras, testes, checklist |
| Memória | registro do aprendizado | Obsidian/JARVIS |

## Fluxo de ingestão

```txt
Obsidian Markdown
  ↓
Leitor de arquivos
  ↓
Parser de YAML + conteúdo
  ↓
Chunking por cabeçalhos
  ↓
Geração de embeddings
  ↓
Banco vetorial
  ↓
Índice consultável pelo agente
```

## O que indexar

Indexar primeiro:

- `Conhecimentos-Gerais/`;
- `skills/`;
- documentação técnica dos projetos;
- decisões arquiteturais;
- runbooks;
- mapas e índices.

Indexar com cuidado:

- notas pessoais sensíveis;
- saúde;
- finanças;
- relacionamento;
- logs brutos;
- arquivos com tokens, senhas ou dados privados.

## Metadados mínimos do chunk

Cada chunk deve guardar:

```yaml
source_path: caminho/do/arquivo.md
title: titulo_da_nota
heading: cabecalho_do_trecho
tags: [lista, de, tags]
type: guide | concept | runbook | decision | template
updated: YYYY-MM-DD
sensitivity: public | internal | private
```

## Estratégia de chunking

Para Obsidian, o melhor chunk geralmente é semântico, não apenas por tamanho.

Regras:

- não separar definição de exemplo;
- não quebrar tabela ao meio;
- preservar YAML;
- preservar links internos;
- manter título do arquivo em todo chunk;
- gerar chunk menor para checklists;
- gerar chunk maior para guias conceituais.

## Recuperação

A recuperação deve combinar:

1. busca semântica;
2. filtros por pasta;
3. filtros por tipo;
4. data de atualização;
5. prioridade de notas canônicas;
6. reranking quando necessário.

## Montagem de contexto

Contexto final ideal:

```txt
Pergunta do usuário
Objetivo da tarefa
Notas recuperadas
Trechos relevantes
Metadados das fontes
Lacunas conhecidas
Instrução de resposta
```

## Resposta do agente

Uma resposta boa deve:

- responder diretamente;
- mencionar notas usadas quando útil;
- separar fato, hipótese e sugestão;
- apontar lacunas;
- sugerir próxima ação;
- evitar afirmar o que não está no vault.

## Memória de volta ao vault

Depois de uma tarefa, o agente pode criar:

- nota de decisão;
- nota de aprendizado;
- atualização de roadmap;
- registro de erro e solução;
- runbook;
- template;
- resumo de reunião.

## Riscos arquiteturais

| Risco | Impacto | Mitigação |
|---|---|---|
| indexar dados sensíveis | vazamento ou uso indevido | classificação de sensibilidade |
| chunk ruim | contexto incompleto | chunking por cabeçalho e sentido |
| busca ampla demais | resposta genérica | filtros por pasta e tipo |
| nota duplicada | respostas conflitantes | nota canônica + MOC |
| índice desatualizado | resposta antiga | reindexar após mudanças |
| agente escreve demais | bagunça no vault | fila de revisão humana |

## Critérios de qualidade

- a busca retorna nota específica antes da genérica;
- o contexto final é menor que o necessário, não maior;
- a resposta consegue dizer quando falta informação;
- o agente não cria links inexistentes sem avisar;
- memórias pessoais não são misturadas com conhecimento geral;
- decisões importantes viram ADR ou nota própria.

## Checklist de implementação

- [ ] Separar pastas por sensibilidade.
- [ ] Criar parser de YAML.
- [ ] Preservar caminho do arquivo em cada chunk.
- [ ] Indexar título, tags e tipo.
- [ ] Criar testes com perguntas conhecidas.
- [ ] Medir se a nota correta aparece no top-k.
- [ ] Criar rotina de reindexação.
- [ ] Criar regra para novas memórias.

## Resumo para IA

Ao usar Obsidian como base RAG, trate cada nota como fonte curada. Recupere notas específicas, preserve metadados, monte contexto curto e registre novos aprendizados como notas estruturadas, não como texto solto.

## Links internos

- [[RAG-e-Memoria-para-Agentes]]
- [[Embeddings-e-Busca-Semantica]]
- [[Context-Engineering]]
- [[Avaliacao-de-RAG-e-Qualidade-de-Contexto]]
- [[../00-Mapas-e-Ontologia/00-Ontologia-de-Conhecimento-para-IA]]
