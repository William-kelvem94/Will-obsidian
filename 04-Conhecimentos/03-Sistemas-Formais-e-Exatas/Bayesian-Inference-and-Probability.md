---
title: Bayesian Inference and Probability
tags:
  - mathematics
  - probability
  - statistics
created: 2026-06-09
updated: 2026-06-09
status: active
---

# Bayesian Inference and Probability

## 1. Bayes' Theorem
Bayesian inference updates the probability for a hypothesis $H$ as more evidence $E$ becomes available:
$$P(H|E) = \frac{P(E|H) P(H)}{P(E)}$$

- **Prior $P(H)$:** Initial belief about the hypothesis before observing evidence.
- **Likelihood $P(E|H)$:** Probability of observing evidence $E$ given that $H$ is true.
- **Posterior $P(H|E)$:** Updated belief after observing evidence.
- **Evidence $P(E)$:** Marginal probability of the evidence: $P(E) = \sum_{H'} P(E|H')P(H')$.

## 2. Markov Chains
A Markov Chain is a stochastic process where the next state depends only on the current state, not the sequence of events that preceded it:
$$P(X_{n+1} = x | X_1, X_2, \dots, X_n = x_n) = P(X_{n+1} = x | X_n = x_n)$$

### Stationary Distribution
A distribution $\pi$ is stationary if:
$$\pi \mathbf{P} = \pi$$
where $\mathbf{P}$ is the transition matrix.

## 3. Monte Carlo Methods
Monte Carlo methods use repeated random sampling to obtain numerical results for complex integrals or probability distributions.

### Markov Chain Monte Carlo (MCMC)
MCMC allows sampling from a distribution $P(H|E)$ when the evidence $P(E)$ is computationally intractable.

- **Metropolis-Hastings Algorithm:**
  1. Propose a new state $H'$ from $g(H'|H)$.
  2. Calculate the acceptance ratio: $\alpha = \min\left(1, \frac{P(E|H')P(H')g(H|H')}{P(E|H)P(H)g(H'|H)}\right)$.
  3. Accept $H'$ with probability $\alpha$.

- **Gibbs Sampling:** A special case of Metropolis-Hastings where each variable is sampled from its conditional distribution given all others.

---
See also: [[Multivariable-Calculus-and-Optimization]]
