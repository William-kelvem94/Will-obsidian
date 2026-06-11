---
title: "Resiliência e Tolerância a Faltas"
date: 2026-06-09
area: "Programação e Engenharia de Software"
tags: [resiliencia, fault-tolerance, circuit-breaker, bulkheads, chaos-engineering]
aliases: ["Resilience Engineering", "Tolerance to Faults"]
related: ["04-Conhecimentos/02-Engenharia-de-Software/INDEX", "04-Conhecimentos/02-Engenharia-de-Software/Performance-e-Otimizacao"]
---

# Resilience and Fault Tolerance

Sistemas resilientes são projetados para absorver falhas, degradar graciosamente e recuperar-se automaticamente, evitando que a falha de um componente cause um cascading failure em todo o ecossistema.

## Resilience Patterns

### Circuit Breaker (Disjuntor)
Evita que o sistema tente realizar chamadas a um serviço que já está falhando, poupando recursos e permitindo que o serviço dependente se recupere.
- **Estados**:
    - **Closed**: Fluxo normal; as chamadas passam.
    - **Open**: Falha detectada; as chamadas são rejeitadas imediatamente (Fast Fail).
    - **Half-Open**: Período de teste; algumas chamadas são permitidas para verificar se o serviço voltou ao normal.

### Bulkheads (Compartmentalization)
Inspirado na engenharia naval, este padrão isola recursos para que a falha em uma parte do sistema não consuma todos os recursos globais.
- **Implementation**: Segregar thread pools ou connection pools por serviço ou cliente. Se o "Serviço A" travar e consumir todas as suas threads alocadas, o "Serviço B" continua operando com seu próprio pool.

### Chaos Engineering (Engenharia do Caos)
Disciplina de experimentar em produção para garantir que o sistema pode suportar condições inesperadas.
- **Metodologia**:
    1. Definir o "Steady State" (estado estável) via métricas.
    2. Introduzir uma hipótese (ex: "se o banco de dados de cache cair, a latência aumentará, mas o sistema não cairá").
    3. Injetar a falha (ex: matar instâncias de Redis, injetar latência de rede).
    4. Observar e validar a hipótese.
    5. Corrigir fraquezas descobertas.

## Recovery Strategy Matrix

| Pattern | Main Objective | When to Use | Effect on User Experience |
|---------|-------------------|-------------------|-------------------------------------------|
| **Circuit Breaker** | Prevenir cascading failure | Unstable external dependencies | Fast fail or fallback response |
| **Bulkheads** | Fault isolation | Systems with multiple critical flows | Apenas a funcionalidade afetada fica lenta/indisponível |
| **Retries** | Corrigir transient failures | Temporary network errors (503, Timeout) | Aumento na latência da requisição |
| **Timeouts** | Evitar infinite blocks | Synchronous calls to third parties | Controlled timeout error |

## Links Relacionados
- [[04-Conhecimentos/02-Engenharia-de-Software/INDEX]]
- [[04-Conhecimentos/02-Engenharia-de-Software/Performance-e-Otimizacao]]
