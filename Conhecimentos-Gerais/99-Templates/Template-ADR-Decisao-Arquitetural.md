---
title: "Template ADR - Decisao Arquitetural"
date: 2026-06-07
updated: 2026-06-07
type: template
status: active
tags: [conhecimento-geral, template, adr, arquitetura, decisao]
related: [[../15-Documentacao/Documentacao-Tecnica-Runbooks-e-ADRs]], [[../04-Produtividade/Decisao-e-Priorizacao]], [[../02-Engenharia-Software/Arquitetura-Web-Moderna]]
summary: "Template para registrar decisões arquiteturais com contexto, alternativas, decisão, consequências e status."
---

# Template ADR - Decisão Arquitetural

Use este modelo para registrar decisões técnicas importantes.

```md
---
title: "ADR - Nome da decisão"
date: YYYY-MM-DD
updated: YYYY-MM-DD
type: decision
status: proposed | accepted | rejected | superseded
tags: [adr, arquitetura]
related: [[]]
summary: "Resumo curto da decisão."
---

# ADR - Nome da decisão

## Status

Proposed | Accepted | Rejected | Superseded

## Contexto

Explique o problema, restrições, cenário e por que a decisão é necessária.

## Opções consideradas

### Opção A

- vantagens:
- desvantagens:
- riscos:

### Opção B

- vantagens:
- desvantagens:
- riscos:

## Decisão

Descreva a escolha feita.

## Motivos

Explique por que essa opção foi escolhida.

## Consequências positivas

- 

## Consequências negativas

- 

## Riscos e mitigação

- risco:
- mitigação:

## Revisão futura

Quando esta decisão deve ser revista?

## Links

- [[]]
```

## Quando criar ADR

Criar ADR quando a decisão:

- afeta arquitetura;
- muda stack;
- cria dependência importante;
- altera modelo de dados;
- muda deploy;
- envolve risco ou custo relevante;
- será difícil lembrar depois.

## Links internos

- [[../15-Documentacao/Documentacao-Tecnica-Runbooks-e-ADRs]]
- [[../04-Produtividade/Decisao-e-Priorizacao]]
- [[../02-Engenharia-Software/Arquitetura-Web-Moderna]]
