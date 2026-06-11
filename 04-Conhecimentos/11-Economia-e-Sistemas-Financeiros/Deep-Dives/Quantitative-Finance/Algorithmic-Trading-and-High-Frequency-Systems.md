---
type: deep-dive
topic: Quantitative Finance
domain: Finance
links: ["[[03-Sistemas-Formais-e-Exatas]]"]
tags: [hft, algorithmic-trading, order-book, machine-learning]
---

# Algorithmic Trading and High-Frequency Systems

## Limit Order Book (LOB) Dynamics
The LOB is a collection of limit orders $L = \{(p, q, t)_i\}$, where $p$ is price, $q$ is quantity, and $t$ is time.
- **Order Flow Imbalance (OFI):** Measures the net difference between buy and sell pressure.
$$\text{OFI}_t = \sum_{i \in \text{events}} \text{sgn}(\text{side}_i) \cdot \Delta q_i$$
- **Price Impact:** The correlation between the volume of a trade and the subsequent change in mid-price $P_{mid} = \frac{P_{ask} + P_{bid}}{2}$.

## Latency Arbitrage and Market Making
Latency arbitrage exploits the time differential in price updates across different exchanges. A high-frequency trader (HFT) detects a price change on Exchange A and executes on Exchange B before the update arrives.
The **Avellaneda-Stoikov model** for market making optimizes the spread $s$ to manage inventory risk $q$:
$$\max \mathbb{E} \left[ -\exp(-\gamma X_T) \right]$$
where $X_T$ is the terminal wealth and $\gamma$ is the risk aversion coefficient.

## Quantitative Alpha Generation with ML
Alpha $\alpha$ is the excess return relative to a benchmark. Modern systems use:
- **Feature Engineering:** Signal extraction from microstructure data (e.g., VPIN - Volume Synchronized Probability of Informed Trading).
- **Reinforcement Learning (RL):** Using Q-learning or PPO to optimize execution strategies (minimizing slippage).
- **Stationarity:** Applying Fractional Differencing to maintain memory while achieving stationarity for time-series models:
$$(1-L)^d y_t = \sum_{k=0}^\infty \binom{d}{k} (-1)^k y_{t-k}$$
where $L$ is the lag operator and $d \in (0, 1)$.
