---
title: Calibracao de Confianca em Agentes
tags:
  - ia-para-programacao
  - psicologia
  - confianca
  - verificacao
type: knowledge_note
created: 2026-05-08
source: internal
---

# Calibracao de Confianca em Agentes

Problema: agentes podem soar certos quando estao errados. Calibracao e alinhar "quao certo parece" com "quao provavel e estar certo".

## O que calibrar

- Confianca no entendimento do requisito.
- Confianca na mudanca proposta (impacto e efeitos colaterais).
- Confianca na verificacao (testes, reproducoes, evidencias).

## Sinais de superconfianca (red flags)

- Nao cita condicoes, casos limite, ou riscos.
- Da resposta final sem "provas" (teste, leitura de codigo, reproducao).
- Confunde termos do dominio ou nomes de arquivos.
- Pula de sintomas para solucao sem diagnostico.

## Sinais de boa calibracao (green flags)

- Faz inferencias com rotulo: "supondo X", "se Y for verdade".
- Propone verificacoes baratas antes de mudanças caras.
- Explicita trade-offs e alternativas.
- Descreve limites: "nao consigo confirmar sem rodar X".

## Escala pratica (3 niveis)

- Baixa: falta evidencia direta; precisa checagem local.
- Media: evidencia parcial (leitura de codigo + coerencia); ainda precisa teste.
- Alta: evidencia direta (teste passa, repro confirma, output observado).

## Protocolos simples

### Antes de agir
- Pergunta: "Qual a menor verificacao que aumenta a confianca?"
- Se a tarefa for destrutiva, pedir confirmacao humana.

### Depois de agir
- Resumir: o que mudou, como foi verificado, e o que ficou pendente.
- Registrar um aprendizado reutilizavel em memoria/skills quando aplicavel.

## Heuristica para decidir "posso aplicar patch?"

Aplicar patch so quando:
- o requisito esta claro; e
- a area afetada esta isolada; e
- existe um teste ou reproducao simples; ou
- o patch e reversivel e baixo risco.

Relacionados:
- [[Conhecimento-Geral/IA-para-Programacao/Engenharia-de-Contexto]]
- [[Conhecimento-Geral/IA-para-Programacao/Avaliacao-de-Respostas-de-IA]]


[[Conhecimento-Geral/IA-para-Programacao/INDEX|← Voltar ao índice de IA para Programação]]
