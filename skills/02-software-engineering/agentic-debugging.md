---
title: "Agentic Debugging"
description: "Skill: usar agentes para diagnosticar e corrigir bugs com evidencias e validacao."
tags: [skill, software-engineering, debug, agents, skills-eng]
updated: 2026-06-01
status: active
date: 2026-06-01
---

# Agentic Debugging

## Objetivo

Transformar o agente em um investigador: ele reduz hipoteses e valida com probes baratos.

## Procedimento

1. Fixar reproducao e criterio de sucesso.
2. Delimitar camada e boundary (UI, API, db, integra).
3. Formular hipoteses pequenas.
4. Provar ou refutar com logs/testes minimos.
5. Aplicar fix pequeno e validar.
6. Registrar aprendizado reutilizavel.

## Saidas Esperadas

- uma explicacao causal curta (por que aconteceu);
- um patch minimal;
- um teste ou validacao repetivel;
- uma nota de aprendizado quando aplicavel.

