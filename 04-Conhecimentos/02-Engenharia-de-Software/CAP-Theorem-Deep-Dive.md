---
tags: [distributed-systems, cap-theorem, pacelc, scalability]
status: complete
created: 2026-06-10
---

# CAP Theorem Deep Dive

## 1. The Fundamental Theorem
The CAP Theorem states that in a distributed data store, it is impossible to simultaneously provide more than two out of the following three guarantees:

### Consistency (C)
Every read receives the most recent write or an error. This refers to **Linearizability** (strong consistency), not eventual consistency. 
- *Failure scenario:* If a node returns stale data, Consistency is violated.

### Availability (A)
Every request received by a non-failing node in the system must result in a (non-error) response, without guarantee that it contains the most recent write.
- *Failure scenario:* If the system returns an error or times out because it cannot reach a quorum, Availability is violated.

### Partition Tolerance (P)
The system continues to operate despite an arbitrary number of messages being dropped (or delayed) by the network between nodes.
- *Crucial Note:* Partition Tolerance is **not optional** in distributed systems. Networks fail. Therefore, the real trade-off is between **C** and **A** during a partition.

## 2. The Trade-offs (CP vs AP)

### CP (Consistency + Partition Tolerance)
The system prioritizes data correctness over availability. If a partition occurs, the system shuts down non-quorum nodes to prevent inconsistent writes.
- **Typical Implementations:** MongoDB (with majority read/write), HBase, Etcd.
- **Use Case:** Financial transactions, coordination services.

### AP (Availability + Partition Tolerance)
The system prioritizes responsiveness. Nodes will return the local version of the data, even if it's stale, and resolve conflicts later.
- **Typical Implementations:** Cassandra, DynamoDB, CouchDB.
- **Use Case:** Social media feeds, shopping carts (Eventual Consistency).

## 3. The PACELC Extension
The CAP theorem only describes behavior during a network partition. **PACELC** extends this by describing behavior during normal operation.

**P**artition $\rightarrow$ (choose **A**vailability or **C**onsistency) **E**LSE $\rightarrow$ (choose **L**atency or **C**onsistency).

### The Latency vs Consistency Trade-off
Even without a partition, a system must decide:
- **PC/EL:** Prioritize consistency during partition and consistency (higher latency) during normal operation.
- **PA/EL:** Prioritize availability during partition and latency (lower consistency) during normal operation.

## 4. Practical Implications for Architects
- **Strong Consistency** requires synchronous replication (slowing down writes).
- **Eventual Consistency** allows asynchronous replication (improving throughput and latency).
- **Quorum Systems:** Using $R + W > N$ to achieve a tunable balance between C and A.

---
**Related Notes:**
- [[Sistemas-Distribuidos-e-Escalabilidade]]
- [[Raft-and-Paxos-Implementation-Details]]
- [[Resiliencia-e-Tolerancia-a-Faltas]]
