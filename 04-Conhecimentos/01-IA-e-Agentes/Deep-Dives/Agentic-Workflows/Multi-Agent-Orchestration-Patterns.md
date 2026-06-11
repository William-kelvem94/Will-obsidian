---
type: technical-deep-dive
category: agentic-workflows
tags: [orchestration, multi-agent, swarms, consensus]
links: 
  - "[[01-IA-e-Agentes/README]]"
  - "[[02-Engenharia-de-Software]]"
---

# Multi-Agent Orchestration Patterns

## 1. Hierarchical Orchestration (Manager-Worker)
In hierarchical patterns, a central "Manager" agent decomposes a high-level goal into sub-tasks and assigns them to specialized "Worker" agents.

### Architecture
- **Delegation**: The Manager maintains the state of the global goal and determines which specialist is best suited for a task.
- **Verification**: Workers return results to the Manager, who validates the output against the original requirements.
- **Control Flow**: Strictly top-down. Workers do not communicate with each other unless explicitly permitted by the Manager.

### Pros/Cons
- **Pros**: High control, reduced noise, clear accountability.
- **Cons**: Single point of failure (Manager bottleneck), limited emergent behavior.

## 2. Sequential Orchestration (Pipeline/Chain)
Agents are arranged in a linear pipeline where the output of agent $n$ becomes the input for agent $n+1$.

### Architecture
- **Linear Flow**: Task $\rightarrow$ Agent A $\rightarrow$ Output A $\rightarrow$ Agent B $\rightarrow$ Output B.
- **Refinement Loops**: Integration of "Critic" agents that can trigger a re-run of a previous step if the quality threshold is not met.

### Pros/Cons
- **Pros**: Predictable, easy to debug, high throughput for standardized processes.
- **Cons**: Rigid, lack of flexibility for non-linear problems.

## 3. Joint-Venture Orchestration (Peer-to-Peer Swarms)
Agents operate in a decentralized network, collaborating based on shared goals and capability-based triggers.

### Architecture
- **Dynamic Discovery**: Agents broadcast their capabilities; other agents request help based on these broadcasts.
- **Blackboard System**: A shared memory space where agents post partial solutions and refine them collectively.

### Conflict Resolution and Consensus Mechanisms
In decentralized swarms, conflict arises when agents propose divergent solutions.

#### Consensus Algorithms
- **Voting/Quorum**: A majority of agents must agree on a state transition before it is committed.
- **Weighted Authority**: Influence is weighted by the agent's proven success rate in specific domains.
- **Argumentation Frameworks**: Agents must provide a logic-based justification for their proposal; a "Mediator" agent evaluates the strength of the evidence.

#### Conflict Resolution Strategies
- **Precedence Rules**: Defined priority levels for agents.
- **Iterative Convergence**: Agents refine their proposals through multiple rounds of feedback until the delta between solutions falls below a specific threshold.
