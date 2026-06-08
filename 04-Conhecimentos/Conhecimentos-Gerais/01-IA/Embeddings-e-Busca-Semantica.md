---
title: "Embeddings e Busca Semantica"
date: 2026-06-07
updated: 2026-06-07
type: concept
status: active
tags: [conhecimento-geral, ia, embeddings, busca-semantica, rag]
related: [[Modelos-de-Linguagem-LLMs]], [[RAG-e-Memoria-para-Agentes]], [[Avaliacao-de-RAG-e-Qualidade-de-Contexto]], [[../05-Dados/Taxonomia-Metadados-e-Ontologia]]
summary: "Nota canônica sobre embeddings, vetores, similaridade semântica, busca vetorial e uso em RAG."
---

# Embeddings e Busca Semântica

Embeddings são representações numéricas de texto, imagem, áudio ou outros dados. Em IA, eles permitem comparar significado aproximado em vez de comparar apenas palavras exatas.

## Ideia central

Um texto é transformado em vetor. Vetores próximos tendem a representar conteúdos semanticamente parecidos.

Exemplo:

- "erro no Docker ao subir banco" pode ficar próximo de "container Postgres não inicia".
- Mesmo sem palavras iguais, a busca pode encontrar relação.

## Conceitos

| Conceito | Explicação |
|---|---|
| vetor | lista de números que representa um conteúdo |
| embedding | vetor gerado por modelo específico |
| similaridade | medida de proximidade entre vetores |
| busca vetorial | busca por significado aproximado |
| chunk | pedaço de documento indexado |
| top-k | quantidade de resultados retornados |
| reranking | reordenação dos resultados por relevância |

## Por que isso importa

Busca tradicional encontra palavras. Busca semântica encontra intenção. Para o vault, isso significa recuperar notas úteis mesmo quando o usuário não lembra o nome exato do arquivo.

## Pipeline

1. Ler documentos Markdown.
2. Dividir em chunks.
3. Gerar embeddings.
4. Salvar vetores e metadados.
5. Receber pergunta.
6. Gerar embedding da pergunta.
7. Buscar vetores próximos.
8. Montar contexto para o LLM.

## Qualidade dos embeddings

A qualidade depende de:

- modelo usado;
- idioma dos textos;
- tamanho dos chunks;
- clareza dos títulos;
- qualidade dos metadados;
- remoção de ruído;
- atualização do índice.

## Problemas comuns

| Problema | Causa | Correção |
|---|---|---|
| resultado irrelevante | chunks ruins | dividir por cabeçalho |
| duplicação | notas repetidas | criar nota canônica |
| contexto fraco | texto sem resumo | adicionar `summary` |
| busca ampla demais | pergunta vaga | expandir consulta com termos específicos |
| resultado antigo | índice desatualizado | reindexar após mudanças |

## Chunking para Obsidian

Estratégia recomendada:

- preservar YAML;
- usar `#`, `##` e `###` como divisores;
- manter tabelas inteiras;
- manter listas de checklist juntas;
- incluir caminho do arquivo como metadado;
- incluir tags e links internos no chunk.

## Metadados úteis

```yaml
source_path: Conhecimentos-Gerais/01-IA/Embeddings-e-Busca-Semantica.md
title: Embeddings e Busca Semantica
type: concept
tags: [ia, embeddings, rag]
updated: 2026-06-07
```

## Como avaliar busca semântica

Perguntar:

- o resultado responde à pergunta?
- a nota retornada é atual?
- há nota mais específica?
- os chunks vieram com contexto suficiente?
- o modelo misturou documentos sem perceber?

## Resumo para IA

Embeddings são a ponte entre o vault e busca semântica. Eles não garantem verdade, apenas proximidade de significado. A resposta final depende de bons chunks, bons metadados e avaliação do contexto recuperado.

## Links internos

- [[Modelos-de-Linguagem-LLMs]]
- [[RAG-e-Memoria-para-Agentes]]
- [[Avaliacao-de-RAG-e-Qualidade-de-Contexto]]
- [[../05-Dados/Taxonomia-Metadados-e-Ontologia]]
