---
title: "Arquiteturas Orientadas a Eventos (EDA)"
date: 2026-06-09
area: "Programação e Engenharia de Software"
tags: [eda, event-driven, sagas, outbox-pattern, event-sourcing]
aliases: ["Event-Driven Architecture", "EDA"]
related: ["04-Conhecimentos/02-Engenharia-de-Software/INDEX", "04-Conhecimentos/02-Engenharia-de-Software/Arquitetura-de-Software", "04-Conhecimentos/02-Engenharia-de-Software/APIs-e-Integracoes"]
---

# Arquiteturas Orientadas a Eventos (EDA)

Event-Driven Architectures (EDA) são padrões de design onde o fluxo do sistema é determinado por eventos (mudanças de estado). Em vez de chamadas síncronas (Request-Response), os componentes comunicam-se de forma assíncrona através de mediadores (brokers).

## Padrões de Implementação

### Event Sourcing
Diferente da persistência tradicional (onde apenas o estado atual é salvo), o Event Sourcing armazena todas as mudanças de estado como uma sequência imutável de eventos.
- **Vantagens**: Auditoria completa, capacidade de "viagem no tempo" (reconstruir estado em qualquer ponto), e separação clara entre comando e consulta.
- **Desafio**: Complexidade na leitura do estado atual, exigindo a criação de *Projections* ou *Snapshots*.

### Outbox Pattern
Resolve o problema da consistência atômica entre atualizar um banco de dados e publicar um evento em um broker (evitando que um falhe enquanto o outro sucede).
- **Funcionamento**: O sistema escreve o evento em uma tabela `Outbox` na mesma transação do negócio. Um processo separado (*Relay*) lê essa tabela e publica os eventos no broker.
- **Garantia**: Garante a entrega *at-least-once* do evento.

### Sagas
Padrão para gerenciar transações distribuídas em microsserviços, onde não é possível utilizar transações ACID globais (2PC - Two Phase Commit).
- **Saga Baseada em Coreografia**: Cada serviço publica um evento que desencadeia a próxima ação em outro serviço. Descentralizada.
- **Saga Baseada em Orquestração**: Um orquestrador central comanda a sequência de passos e decide a próxima ação.
- **Compensação**: Se um passo falha, a Saga executa "transações compensatórias" para reverter os efeitos dos passos anteriores.

## Trade-offs de EDA

| Critério | Síncrono (REST/gRPC) | Assíncrono (EDA) |
|----------|----------------------|------------------|
| **Acoplamento** | Forte (dependência de endpoint/disponibilidade). | Fraco (dependência apenas do contrato do evento). |
| **Latência** | Baixa para resposta imediata. | Maior (processamento eventual). |
| **Complexidade** | Simples de rastrear (stack trace linear). | Alta (exige rastreamento distribuído/Correlation IDs). |
| **Escalabilidade** | Limitada por bloqueios de thread/IOWait. | Alta (consumidores escalam independentemente). |

## Links Relacionados
- [[04-Conhecimentos/02-Engenharia-de-Software/INDEX]]
- [[04-Conhecimentos/02-Engenharia-de-Software/Arquitetura-de-Software]]
- [[04-Conhecimentos/02-Engenharia-de-Software/APIs-e-Integracoes]]
