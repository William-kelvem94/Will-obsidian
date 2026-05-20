---
title: "Filosofia para Ciência da IA e Tomada de Decisão"
description: "Nota ponte entre epistemologia, ética, lógica e engenharia de agentes para orientar decisões em sistemas inteligentes."
tags: [filosofia, IA, etica, epistemologia, logica, decisao]
date: 2026-05-20
updated: 2026-05-20
---

# Filosofia para Ciência da IA e Tomada de Decisão

Esta nota conecta filosofia aplicada ao desenho de agentes, RAG, automações e decisões técnicas. Ela complementa [[Filosofia-da-Mente]], [[Problema-do-Controle]], [[Logica-e-Pensamento-Critico]] e [[Etica-de-IA-e-Alinhamento]].

## Por que filosofia importa para IA

Sistemas inteligentes não falham apenas por bug técnico. Eles falham por pressupostos ruins: fonte fraca, objetivo mal definido, métrica inadequada, delegação excessiva ou confusão entre correlação e verdade.

A filosofia ajuda a formular perguntas melhores antes da implementação.

## Eixos principais

| Eixo | Pergunta | Aplicação em IA/agentes |
|---|---|---|
| Epistemologia | Como sei que isto é verdadeiro ou confiável? | avaliação de fontes, RAG, incerteza |
| Ética | O que o sistema não deve fazer mesmo se conseguir? | limites, permissões, dados sensíveis |
| Lógica | A conclusão segue das premissas? | validação, inferência, consistência |
| Filosofia da mente | Simulação de raciocínio é raciocínio? | expectativas sobre LLMs |
| Filosofia política | Quem controla sistemas de decisão? | governança, auditoria, poder |

## Aplicação prática no vault

Ao criar um agente, documente:

- objetivo;
- permissões;
- fontes que ele pode usar;
- ações proibidas;
- critérios de confiança;
- quando pedir confirmação humana;
- como registrar evidência.

## Perguntas de decisão

Antes de automatizar:

1. Qual problema real será resolvido?
2. O sistema precisa escrever ou apenas sugerir?
3. O erro é reversível?
4. Há dado sensível envolvido?
5. Como auditar a decisão depois?
6. O usuário entende o trade-off?

## Anti-padrões filosóficos

- Confundir resposta fluente com conhecimento.
- Delegar decisão moral para métrica simples.
- Tratar ausência de evidência como evidência de ausência.
- Otimizar produtividade destruindo autonomia ou privacidade.
- Criar agentes com poder maior que a capacidade de auditoria.

## Links relacionados

- [[Filosofia-da-Mente]]
- [[Problema-do-Controle]]
- [[Etica-de-IA-e-Alinhamento]]
- [[Logica-e-Pensamento-Critico]]
- [[Auditoria-de-Agentes-e-Evidencias]]
- [[Arquiteturas-Cooperativas-de-Agentes]]
