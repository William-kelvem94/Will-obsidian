---
type: deep-dive
category: Low-Level OS
tags: [scheduling, cpu, optimization]
link: "[[02-Engenharia-de-Software/INDEX.md]]"
---

# Process Scheduling and CPU Optimization

## Scheduling Algorithms

### CFS (Completely Fair Scheduler)
The default Linux scheduler. It aims to maximize fairness by giving each process a "proportion" of the CPU's power.
- **Virtual Runtime (vruntime)**: Tracks the amount of time a process has spent on the CPU. The process with the lowest `vruntime` is scheduled next.
- **Red-Black Tree**: Used to store processes sorted by `vruntime` for $O(\log n)$ lookup and insertion.

### Real-time Scheduling
Used for deterministic response times (Hard vs Soft RTOS).
- **Fixed-Priority Preemptive Scheduling**: Highest priority task always runs.
- **Earliest Deadline First (EDF)**: Priorities are dynamically assigned based on the proximity of the deadline.

## Execution Overhead

### Context Switching
The process of saving the state (registers, program counter, stack pointer) of a running process and loading the state of another.
- **Cost**: CPU cycles for state saving, TLB flushes, and cache pollution (cold caches).

## Hardware-Aware Optimization

### CPU Affinity
Binding a process or thread to a specific CPU core to maximize cache hits (L1/L2) and reduce migration overhead.

### NUMA (Non-Uniform Memory Access)
In multi-socket systems, memory is partitioned. A CPU accesses local memory faster than remote memory (memory attached to another CPU).
- **NUMA Policy**: The kernel attempts to allocate memory on the node closest to the CPU executing the process to minimize latency.
