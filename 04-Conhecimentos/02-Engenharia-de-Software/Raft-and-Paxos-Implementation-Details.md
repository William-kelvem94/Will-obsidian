---
tags: [consensus, raft, paxos, distributed-systems, etcd]
status: complete
created: 2026-06-10
---

# Raft and Paxos Implementation Details

## 1. The Consensus Problem
The goal of a consensus algorithm is to get a group of unreliable nodes to agree on a single value or a sequence of operations (a replicated log), ensuring **Safety** (no two nodes agree on different values) and **Liveness** (the system eventually reaches a decision).

## 2. Paxos: The Foundation
Paxos is the gold standard for consensus but is notoriously difficult to understand and implement.

### The Three Roles
- **Proposers:** Propose values.
- **Acceptors:** Vote on proposals.
- **Learners:** Learn the agreed-upon value.

### The Two-Phase Process
1. **Prepare Phase:** A proposer sends a `Prepare(n)` message. If the acceptor hasn't seen a higher proposal number, it promises not to accept any lower ones.
2. **Accept Phase:** If the proposer gets a majority of promises, it sends `Accept(n, value)`. If the acceptor hasn't promised a higher $n$, it accepts the value.

### Multi-Paxos
To handle a stream of values (a log), Multi-Paxos optimizes by electing a distinguished proposer (leader), skipping the Prepare phase for subsequent entries.

## 3. Raft: Designed for Understandability
Raft decomposes consensus into three sub-problems: Leader Election, Log Replication, and Safety.

### Leader Election
- Nodes are in one of three states: **Follower**, **Candidate**, or **Leader**.
- **Heartbeats:** The leader sends periodic heartbeats to maintain authority.
- **Election Timeout:** If a follower doesn't hear from a leader, it becomes a candidate and starts an election.
- **Term:** A monotonically increasing number that acts as a logical clock to detect stale leaders.

### Log Replication
1. The leader receives a command from a client.
2. The leader appends the command to its log and sends `AppendEntries` RPCs to followers.
3. Once a majority of followers acknowledge the entry, the leader **commits** it and applies it to its state machine.
4. The leader notifies followers that the entry is committed in subsequent heartbeats.

### Safety Properties
- **Election Safety:** At most one leader can be elected in a given term.
- **Leader Completeness:** A leader must possess all committed entries from previous terms. Raft ensures this by only voting for candidates whose logs are "at least as up-to-date" as the voter's.

## 4. Real-World Implementations

### Etcd (Raft)
- Used by Kubernetes for cluster state.
- Implements Raft with a focus on efficiency and linearizable reads.
- Uses **Leases** for distributed locking.

### ZooKeeper (ZAB - ZooKeeper Atomic Broadcast)
- ZAB is similar to Raft/Paxos but specifically designed for ZooKeeper.
- It emphasizes a primary-backup model and strict ordering of transactions.
- Unlike Raft, it separates the "recovery" phase from the "broadcast" phase.

## 5. Comparison Summary
| Feature | Paxos | Raft |
| :--- | :--- | :--- |
| **Complexity** | High (Theoretical) | Medium (Understandable) |
| **Leader** | Weak/Optional | Strong Leader |
| **Log Flow** | Flexible | Strict (Leader $\rightarrow$ Follower) |
| **Election** | Implicit | Explicit (Terms/Timeouts) |

---
**Related Notes:**
- [[Sistemas-Distribuidos-e-Escalabilidade]]
- [[CAP-Theorem-Deep-Dive]]
- [[Resiliencia-e-Tolerancia-a-Faltas]]
