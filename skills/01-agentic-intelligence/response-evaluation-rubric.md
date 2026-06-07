---
title: "Response Evaluation Rubric"
category: "ai"
level: 3
description: "Rubrica para avaliar respostas de IA por correcao, aderencia, utilidade e risco."
projects: []
related_skills: [best-practices, advanced-reasoning-patterns]
resources: []
updated: 2026-06-07
date: 2026-06-01
tags: [skills-ai]
---

# Response Evaluation Rubric

Response evaluation rubric e um quadro simples para revisar saidas de IA antes de confiar nelas. A skill e util em code review, documentacao, suporte tecnico e pesquisa assistida por modelo.

## Dimensoes

| Dimensao | Pergunta | Peso |
| --- | --- | --- |
| Correcao | A resposta e verdadeira ou verificavel? | Alto |
| Aderencia | Ela segue o pedido e as restricoes? | Alto |
| Utilidade | Ela ajuda o usuario a agir? | Medio |
| Clareza | Ela e compreensivel sem contexto extra? | Medio |
| Seguranca | Ela evita dano, vazamento ou excesso de permissao? | Alto |
| Humildade | Ela marca incerteza e limites? | Medio |

## Escala

- `0`: falhou.
- `1`: parcialmente adequado.
- `2`: adequado.

Se qualquer dimensao de peso alto receber `0`, a resposta precisa de revisao antes de uso.

## Aplicacao Rapida

1. Releia o pedido original.
2. Marque restricoes explicitas.
3. Compare a resposta com evidencias disponiveis.
4. Procure acao concreta ou decisao clara.
5. Registre riscos e lacunas.

## Relacionado

- [[Conhecimento-Geral/IA-para-Programacao/Avaliacao-de-Respostas-de-IA]]
- [[skills/01-agentic-intelligence/best-practices]]
- [[skills/01-agentic-intelligence/advanced-reasoning-patterns]]

