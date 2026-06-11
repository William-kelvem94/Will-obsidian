---
title: Heuristicas de Triagem de Issues
tags:
  - ia-para-programacao
  - psicologia
  - triagem
  - priorizacao
type: knowledge_note
created: 2026-05-08
source: internal
---

# Heuristicas de Triagem de Issues

Objetivo: decidir rapido "o que fazer agora" sem cair em vieses (urgencia falsa, favoritismo, perfeccionismo).

## Grade rapida (5 perguntas)

1. Impacto: quem sofre e quanto (perda, risco, bloqueio)?
2. Frequencia: acontece sempre, as vezes, ou raro?
3. Detectabilidade: falha silenciosa ou barulhenta?
4. Reversibilidade: da pra desfazer rapido?
5. Evidencia: existe log, repro, teste, ou so relato?

## Classificacao sugerida (classes)

- P0: perda de dados, seguranca, pagamentos, indisponibilidade geral.
- P1: fluxo principal quebrado para muitos usuarios.
- P2: bug com workaround ou baixa frequencia.
- P3: melhoria, refactor, polish.

## Vieses comuns na triagem

- Disponibilidade: prioriza o que aconteceu ontem, nao o que e mais caro.
- Aversao a ambiguidade: escolhe tarefas faceis e deixa as dificeis eternas.
- Escalada de compromisso: insiste numa solucao antiga porque ja investiu tempo.

Contramedidas:
- Definir "proxima acao minima" para reduzir ambiguidade (ex.: criar repro).
- Timebox de investigacao antes de implementar.
- Registrar decisao e criterio (para revisitar com dados).

## Proxima acao minima (playbook)

- Sem reproducao: primeiro criar repro ou coletar logs.
- Com reproducao: escrever teste que falha.
- Com teste falhando: implementar a menor correção que faz passar.
- Sem teste possivel: adicionar guardrails (validacao, fallback, observabilidade).

Relacionados:
- [[04-Conhecimentos/07-Humanidades/Psicologia/Vieses-Cognitivos]]
- [[04-Conhecimentos/07-Humanidades/IA-para-Programacao/Debug-com-Agentes]]


[[04-Conhecimentos/07-Humanidades/IA-para-Programacao/INDEX|← Voltar ao índice de IA para Programação]]
