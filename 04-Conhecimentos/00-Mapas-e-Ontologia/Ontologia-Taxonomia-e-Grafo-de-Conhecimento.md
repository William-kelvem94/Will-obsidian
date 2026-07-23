---
title: "Ontologia, Taxonomia e Grafo de Conhecimento"
updated: 2026-07-10
type: concept
status: active
tags: [ontologia, taxonomia, grafo, graphrag, modelagem]
indexavel: true
uso_ia: livre
related: [[Engenharia-de-Conhecimento-para-Segundo-Cerebro]], [[Ontologia-de-Conhecimento-para-IA]]
---

# Três camadas de estrutura

**Taxonomia** organiza classes em hierarquia: IA → agentes → memória. **Ontologia** define classes, propriedades, restrições e significado. **Grafo de conhecimento** instancia entidades e relações com evidência: uma nota implementa uma skill, uma fonte sustenta uma afirmação, uma decisão supersede outra.

## Relações recomendadas

`is_a`, `part_of`, `instance_of`, `supports`, `contradicts`, `depends_on`, `causes`, `measured_by`, `implemented_by`, `related_to`, `supersedes`, `derived_from`.

## Exemplo

```yaml
subject: RAG
predicate: measured_by
object: answer_faithfulness
evidence: [[Avaliacao-de-RAG-e-Qualidade-de-Contexto]]
confidence: medium
```

## Regras

- Relações devem ter direção e significado explícitos.
- “Relacionado” é fallback, não substituto para uma relação específica.
- Toda relação factual relevante deve apontar para uma fonte ou nota derivada.
- Não confundir hierarquia de pastas com verdade ontológica.
- Quando duas notas discordarem, preservar ambas e registrar a condição de validade.

## Uso no WILL-OBSIDIAN

Pastas oferecem navegação humana; frontmatter oferece filtragem; wikilinks oferecem grafo; índices oferecem entrada; fontes oferecem rastreabilidade. A resposta de IA deve recuperar o menor subgrafo suficiente para responder.

## Referência

[GraphRAG da Microsoft](https://microsoft.github.io/graphrag/) e [métodos GraphRAG](https://microsoft.github.io/graphrag/index/methods/).
