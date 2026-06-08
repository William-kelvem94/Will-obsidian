---
title: "Transparencia de Decisao e Rastreabilidade"
area: "04-Conhecimentos/07-Humanidades/Etica"
tags: ["ethics","transparency","agents","audit","traceability"]
created: "2026-05-08"
status: "draft"
---

# Transparencia de Decisao e Rastreabilidade

Transparencia de decisao, para agentes, nao e "explicar tudo". E garantir que um humano consiga responder:

- O que foi decidido?
- Por que foi decidido?
- Com base em que evidencias?
- Quem pode ser impactado?
- Como reverter ou revisar depois?

## O minimo auditavel (template curto)

Registre, em 5 campos:

1. Decisao: frase unica, clara.
2. Evidencia: 1-3 itens (arquivo/linha, erro, comando, resultado).
3. Alternativas: o que foi considerado e por que nao.
4. Risco: impacto e reversibilidade.
5. Proxima revisao: quando reavaliar.

## Rastreabilidade de execucao (para mudancas)

Para mudancas em repositorio/automacao:

- objetivo da mudanca
- lista de arquivos alterados
- comandos executados (sem dados sensiveis)
- resultados de verificacao (build/test)
- como desfazer

## Redacao segura

- Evite incluir payloads inteiros em logs.
- Use placeholders para PII.
- Prefira referenciar arquivos locais em vez de colar conteudo.

## Relacionado

- [[Auditoria-de-Agentes-e-Evidencias]]
- [[Politica-de-Logs-para-Agentes]]


[[04-Conhecimentos/07-Humanidades/Etica/INDEX|← Voltar ao índice de Ética]]
