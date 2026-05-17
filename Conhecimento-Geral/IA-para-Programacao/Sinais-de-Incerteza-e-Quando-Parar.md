---
title: Sinais de Incerteza e Quando Parar
tags:
  - ia-para-programacao
  - psicologia
  - confianca
  - risco
type: knowledge_note
created: 2026-05-08
source: internal
---

# Sinais de Incerteza e Quando Parar

Objetivo: evitar "seguir no embalo" quando a base de evidencias e fraca, reduzindo bugs introduzidos por pressa.

## Sinais de incerteza tecnica

- Nao existe teste cobrindo o fluxo mudado.
- O codigo depende de estado externo (DB, fila, cache) sem mock.
- Ha concorrencia/retry/idempotencia e voce nao mapeou o contrato.
- A mudanca mexe em autenticacao, permissoes, secrets ou pagamentos.
- O comportamento esperado depende de "como esta em producao".

## Sinais de incerteza cognitiva (do revisor/agente)

- Sensacao de "entendi rapido demais".
- Explicacoes que mudam a cada pergunta.
- Uso de termos vagos: "provavelmente", "deve ser", sem condicao.
- Falta de capacidade de explicar o bug em uma frase precisa.

## Regra de parada (stop rule)

Pare e mude de estrategia quando:
- voce nao consegue escrever um "criterio de aceitacao" testavel; ou
- voce nao consegue descrever um contraexemplo (como falha) sem inventar; ou
- voce precisou de 3 suposicoes grandes para fechar a solucao.

## Alternativas seguras ao inves de mudar codigo

- Criar um teste minimo que falha e descreve o bug.
- Instrumentar logs/metricas para observar a falha.
- Rodar um "safe probe" (entrada controlada, ambiente local).
- Pedir um trecho adicional de contexto (config, schema, logs).

Relacionados:
- [[Conhecimento-Geral/IA-para-Programacao/Debug-com-Agentes]]
- [[Conhecimento-Geral/IA-para-Programacao/Testes-com-Agentes]]

