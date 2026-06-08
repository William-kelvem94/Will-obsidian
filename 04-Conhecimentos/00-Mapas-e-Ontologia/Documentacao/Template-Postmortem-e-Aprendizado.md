---
title: "Template - Postmortem e Aprendizado"
date: 2026-06-07
updated: 2026-06-07
type: template
status: active
tags: [conhecimento-geral, documentacao, postmortem, aprendizado, template]
related: [[Documentacao-Tecnica-Runbooks-e-ADRs]], [[../../02-Engenharia-de-Software/Observabilidade-Logs-e-Monitoramento]], [[../../08-Vida-Pratica/Produtividade/Decisao-e-Priorizacao]]
summary: "Template para registrar falhas, incidentes e aprendizados de forma madura, prática e reutilizável."
---

# Template - Postmortem e Aprendizado

Use este modelo quando algo importante deu errado, atrasou, falhou ou gerou retrabalho. O objetivo não é procurar culpado. É transformar falha em conhecimento.

## Modelo

```md
---
title: "Postmortem - nome do evento"
date: YYYY-MM-DD
updated: YYYY-MM-DD
type: postmortem
status: active
tags: [postmortem, aprendizado]
related: [[]]
summary: "Resumo curto do evento e do aprendizado."
---

# Postmortem - nome do evento

## Resumo

O que aconteceu em poucas linhas?

## Linha do tempo

- HH:mm - evento 1
- HH:mm - evento 2
- HH:mm - evento 3

## Impacto

Quem ou o que foi afetado?

## Causa principal

Qual foi a causa mais provável?

## Causas contribuintes

- 

## O que funcionou

- 

## O que não funcionou

- 

## Aprendizados

- 

## Ações preventivas

- [ ] Ação 1
- [ ] Ação 2

## Links relacionados

- [[]]
```

## Quando usar

- bug recorrente;
- incidente de produção;
- falha de processo;
- decisão que deu ruim;
- problema de comunicação;
- atraso relevante;
- automação que gerou ruído;
- deploy problemático.

## Checklist de qualidade

- [ ] O texto separa fato de interpretação?
- [ ] A causa foi investigada?
- [ ] Há ação preventiva?
- [ ] O aprendizado pode ser reutilizado?
- [ ] Links internos foram adicionados?

## Resumo para IA

Postmortem deve transformar erro em melhoria. Ao criar um postmortem, preservar linha do tempo, impacto, causa, aprendizados e ações preventivas.
