---
title: "Sistemas de Consenso e Replicação"
date: 2026-06-09
area: "Programação e Engenharia de Software"
tags: [sistemas-distribuidos, consenso, replicacao, paxos, raft, consistencia]
aliases: ["Consensus Systems", "Replication Strategies"]
related: ["04-Conhecimentos/02-Engenharia-de-Software/INDEX", "04-Conhecimentos/02-Engenharia-de-Software/Banco-de-Dados"]
---

# Sistemas de Consenso e Replicação

Sistemas de consenso permitem que um conjunto de nós em um sistema distribuído concordem com um valor único, mesmo na presença de falhas de nós ou partições de rede, garantindo a linearizabilidade e a consistência do estado global.

## Algoritmos de Consenso

### Paxos
O Paxos é a base teórica para a maioria dos algoritmos de consenso. Ele opera através de instâncias de consenso onde os nós assumem papéis de *Proposers*, *Acceptors* e *Learners*.
- **Funcionamento**: Baseia-se em duas fases: *Prepare* (promessa de não aceitar propostas com números menores) e *Accept* (aceitação do valor se a promessa for mantida).
- **Complexidade**: Notório por ser difícil de implementar e entender, levando à criação de variantes como Multi-Paxos.

### Raft
O Raft foi projetado como uma alternativa mais compreensível ao Paxos, focando na decomposição do problema em três subproblemas principais:
1. **Eleição de Líder**: Garante que haja apenas um líder ativo por termo.
2. **Replicação de Log**: O líder aceita comandos do cliente, anexa-os ao log e replica-os nos seguidores.
3. **Segurança**: Garante que se um log entry foi commitada, ela estará presente em todos os líderes subsequentes.

## Consistência: Strong vs. Eventual

A escolha do modelo de consistência impacta diretamente a disponibilidade e a latência do sistema, conforme descrito pelo Teorema CAP.

| Atributo | Strong Consistency (Consistência Forte) | Eventual Consistency (Consistência Eventual) |
|-----------|-----------------------------------------|-------------------------------------------|
| **Definição** | Após uma atualização, qualquer leitura subsequente retorna o valor mais recente. | Eventualmente, todos os nós convergirão para o mesmo valor, se não houver novas atualizações. |
| **Latência** | Alta (exige coordenação entre nós). | Baixa (leituras/escritas locais). |
| **Disponibilidade** | Menor (pode bloquear leituras durante partições). | Alta (sempre disponível para leitura/escrita). |
| **Exemplos** | ZooKeeper, etcd (via Raft), Bancos SQL ACID. | Cassandra, DynamoDB, DNS, S3. |
| **Trade-off** | Privilegia Consistência (C) sobre Disponibilidade (A). | Privilegia Disponibilidade (A) sobre Consistência (C). |

## Links Relacionados
- [[04-Conhecimentos/02-Engenharia-de-Software/INDEX]]
- [[04-Conhecimentos/02-Engenharia-de-Software/Banco-de-Dados]]
