---
title: "Seguranca vs Utilidade (Tradeoffs)"
area: "Conhecimento-Geral/Etica"
tags: ["ethics","security","agents","tradeoffs","guardrails"]
created: "2026-05-08"
status: "draft"
---

# Seguranca vs Utilidade (Tradeoffs)

Em agentes de programacao, a tensao classica e: quanto mais autonomia, mais utilidade imediata; quanto mais guardrails, mais seguranca e previsibilidade. O objetivo nao e "maxima seguranca" abstrata, mas um equilibrio que preserve o controle humano e reduza risco sistemico.

## Um modelo pratico: risco x reversibilidade

Classifique a acao por:

- Impacto: baixa/medio/alto
- Reversibilidade: facil/dificil
- Evidencia: forte/fraca

Regra: quanto maior impacto e menor reversibilidade, maior o nivel de confirmacao humana e evidencias exigidas.

## Padroes de controle (escalonados)

1. Read-only: agente so observa, mapeia, sugere.
2. Write-safe: agente escreve apenas em areas "sandbox" (notas novas, logs separados).
3. Change-with-check: agente altera codigo/infra mas com verificacoes e testes definidos.
4. Autonomia parcial: agente executa mudancas repetiveis com limites, kill switch e auditoria.

## Guardrails que preservam utilidade

- "Probes seguros": pequenas verificacoes que reduzem incerteza (ex.: `git status`, `rg`, `py_compile`).
- "Planos executaveis": passos curtos, verificaveis, com criterio de parada.
- "Fallback claro": se falhar, reverte ou para e pede confirmacao.

## Anti-padroes

- "Auto-fix sem evidencia": mudar coisas por intuicao quando a evidencia esta fraca.
- "Logs infinitos": guardar tudo para compensar falta de processo.
- "Autonomia sem auditoria": agente faz, ninguem entende depois.

## Relacionado

- [[Sinais-de-Incerteza-e-Quando-Parar]]
- [[Transparencia-de-Decisao-e-Rastreabilidade]]
- [[Limites-de-Automacao-e-Consentimento]]

