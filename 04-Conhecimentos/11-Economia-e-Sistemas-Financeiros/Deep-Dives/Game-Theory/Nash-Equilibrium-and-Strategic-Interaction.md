---
type: deep-dive
topic: Game Theory
domain: Economics
links: ["[[03-Sistemas-Formais-e-Exatas]]"]
tags: [mathematics, nash-equilibrium, strategic-interaction]
---

# Nash Equilibrium and Strategic Interaction

## Non-Cooperative Games
A non-cooperative game is defined as a triplet $G = \langle N, S, u \rangle$, where:
- $N = \{1, \dots, n\}$ is the set of players.
- $S = S_1 \times \dots \times S_n$ is the strategy space, with $S_i$ being the set of strategies available to player $i$.
- $u = (u_1, \dots, u_n)$ is the utility function, where $u_i: S \to \mathbb{R}$ assigns a payoff to player $i$ for every strategy profile $s \in S$.

## The Mathematics of Nash Equilibrium
A strategy profile $s^* = (s_1^*, \dots, s_n^*) \in S$ is a **Pure Strategy Nash Equilibrium (PSNE)** if for every player $i \in N$:
$$u_i(s_i^*, s_{-i}^*) \geq u_i(s_i, s_{-i}^*), \quad \forall s_i \in S_i$$
where $s_{-i}^*$ denotes the strategy profile of all players except $i$.

### Mixed Strategy Nash Equilibrium (MSNE)
When pure strategies do not exist, we consider probability distributions $\sigma_i$ over $S_i$. The expected utility for player $i$ is:
$$U_i(\sigma) = \sum_{s \in S} \left( \prod_{j=1}^n \sigma_j(s_j) \right) u_i(s)$$
A profile $\sigma^*$ is a Mixed Strategy Nash Equilibrium if:
$$U_i(\sigma_i^*, \sigma_{-i}^*) \geq U_i(\sigma_i, \sigma_{-i}^*), \quad \forall \sigma_i \in \Delta(S_i)$$

## Pareto Optimality vs. Nash Equilibrium
A strategy profile $s$ is **Pareto Optimal** if there exists no other profile $s' \in S$ such that:
$$u_i(s') \geq u_i(s) \quad \forall i \in N, \text{ and } \exists j \in N : u_j(s') > u_j(s)$$
The tension between PSNE and Pareto Optimality is most evident in the Prisoner's Dilemma, where the unique Nash Equilibrium is strictly Pareto-dominated by a cooperative outcome.

## Best Response Dynamics
The best response correspondence $B_i: S_{-i} \rightrightarrows S_i$ is defined as:
$$B_i(s_{-i}) = \{ s_i \in S_i : u_i(s_i, s_{-i}) \geq u_i(s_i', s_{-i}), \forall s_i' \in S_i \}$$
A Nash Equilibrium is a fixed point of the joint best response correspondence:
$$s^* \in B(s^*)$$
