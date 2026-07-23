---
title: "Token Economy: Playbook Operacional"
updated: 2026-07-10
type: playbook
status: active
tags: [tokens, contexto, eficiencia, custo, compressao]
indexavel: true
uso_ia: livre
related: [[TOKEN-ECONOMY]], [[TOKEN-SHORTHAND]], [[../01-IA-e-Agentes/Context-Engineering]], [[../../02-JARVIS/TOKEN-COMPRESSION]]
---

# Economia de tokens

## Ordem de otimização

1. Remover conteúdo irrelevante.
2. Recuperar por hierarquia e links.
3. Deduplicar e normalizar.
4. Comprimir preservando números, condições e exceções.
5. Usar formato compacto e cachear contexto estável.
6. Só então reduzir verbosidade da resposta.

## Orçamento

```yaml
budget:
  system: fixed
  task: explicit
  memory: minimal_sufficient
  evidence: claim_aligned
  output: answer_first
```

## Métricas

Medir custo por tarefa, tokens recuperados, cobertura de evidência, precisão, latência, taxa de repetição e perda semântica após compressão. Otimização sem métrica pode trocar custo por erro.

## Regra de parada

Parar quando a próxima unidade de contexto não alterar decisão, confiança ou capacidade de verificar a resposta.

## Checklist

- [ ] pergunta e formato definidos
- [ ] contexto mínimo recuperado
- [ ] fonte preservada
- [ ] duplicatas removidas
- [ ] incertezas mantidas
- [ ] saída acionável
