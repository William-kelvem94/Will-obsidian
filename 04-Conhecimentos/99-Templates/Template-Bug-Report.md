---
title: "Template - Bug Report"
date: 2026-06-07
updated: 2026-06-07
type: template
status: active
tags: [conhecimento-geral, template, bug, debug, qualidade]
related: [[../02-Engenharia-de-Software/Playbook-de-Debug-de-API-e-Backend]], [[../02-Engenharia-de-Software/Testes-e-Qualidade-de-Software]], [[../00-Mapas-e-Ontologia/Documentacao/Documentacao-Tecnica-Runbooks-e-ADRs]]
summary: "Template para registrar bugs com reprodução, contexto, logs, hipótese e correção."
---

# Template - Bug Report

Use este modelo para registrar bugs de forma clara e reutilizável.

```md
---
title: "Bug - título curto"
date: YYYY-MM-DD
updated: YYYY-MM-DD
type: bug-report
status: open | investigating | fixed | closed
tags: [bug]
related: [[]]
summary: "Resumo curto do problema."
---

# Bug - título curto

## Contexto

Onde o problema aconteceu?

## Ambiente

- sistema:
- versão:
- navegador:
- dispositivo:
- branch:
- commit:

## Passos para reproduzir

1. 
2. 
3. 

## Resultado esperado

O que deveria acontecer?

## Resultado obtido

O que aconteceu de fato?

## Evidências

- logs:
- prints:
- payload:
- endpoint:

## Hipótese inicial

Qual camada parece relacionada?

## Causa encontrada

O que causou o bug?

## Correção aplicada

O que foi feito?

## Prevenção

- [ ] teste adicionado
- [ ] documentação atualizada
- [ ] validação criada
- [ ] log melhorado
```

## Checklist

- [ ] O bug é reproduzível?
- [ ] Ambiente foi informado?
- [ ] Existe resultado esperado?
- [ ] Existe resultado obtido?
- [ ] Logs ou evidências foram anexados?
- [ ] A correção foi documentada?

## Resumo para IA

Bug report bom reduz adivinhação. Sempre registrar ambiente, passos, resultado esperado, resultado obtido e evidências.
