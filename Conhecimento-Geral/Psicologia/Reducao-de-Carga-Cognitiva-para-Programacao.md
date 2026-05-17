---
title: Reducao de Carga Cognitiva para Programacao
tags:
  - psicologia
  - programacao
  - produtividade
  - qualidade
type: knowledge_note
created: 2026-05-08
source: internal
---

# Reducao de Carga Cognitiva para Programacao

Ideia: bugs e decisao ruim aumentam quando a carga cognitiva passa do limite. Reduzir carga melhora qualidade e velocidade.

## Fontes de carga cognitiva no dia a dia

- Context switching (muitos projetos ao mesmo tempo).
- PRs grandes e diffs sem narrativa.
- Falta de naming e contratos claros.
- Dependencia de estado implicito (configs, envs, caches).

## Tecnicas que reduzem carga (alto retorno)

- Escrever "contrato" antes do codigo: entradas, saidas, invariantes.
- Decompor em passos verificaveis (tests first quando possivel).
- Preferir logs e métricas legiveis a adivinhacao.
- Limitar tamanho de PR (unidade revisavel).
- Usar checklists curtos para areas sensiveis (auth, DB, pagamentos).

## Sinais de sobrecarga

- Releitura repetida do mesmo trecho sem progresso.
- Irritacao com detalhes pequenos.
- Aumenta a vontade de "apenas terminar logo".
- Muitas suposicoes nao verificadas.

## Intervencoes rapidas (5-10 min)

- Escrever um resumo do problema em 3 frases.
- Listar 3 hipoteses e um teste para diferenciar.
- Fazer pausa curta e voltar com ordem de leitura (do risco maior ao menor).

Relacionados:
- [[Conhecimento-Geral/Psicologia/Psicologia-Cognitiva]]
- [[Conhecimento-Geral/IA-para-Programacao/Sinais-de-Incerteza-e-Quando-Parar]]

