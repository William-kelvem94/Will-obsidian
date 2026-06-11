---
type: deep-dive
topic: Mathematics for AI
subject: Probability Theory and Bayesian Networks
tags: [probability, bayesian, gp, mcmc, variational-inference]
links: [[03-Sistemas-Formais-e-Exatas/INDEX|Index]]
---

# Probability Theory and Bayesian Networks

## 1. Gaussian Processes (GP)
A GP is a collection of random variables, any finite number of which have a joint Gaussian distribution. A GP is completely specified by its mean function $m(x)$ and covariance function $k(x, x')$:
$$ f(x) \sim \mathcal{GP}(m(x), k(x, x')) $$
For a set of inputs $\mathbf{X}$ and targets $\mathbf{y}$, the predictive distribution for $f_*$ at $x_*$ is:
$$ P(f_* | \mathbf{X}, \mathbf{y}, x_*) = \mathcal{N}(\bar{f}_*, \text{cov}(f_*)) $$
where $\bar{f}_* = K(x_*, \mathbf{X}) [K(\mathbf{X}, \mathbf{X}) + \sigma_n^2 I]^{-1} \mathbf{y}$.

## 2. Variational Inference (VI)
VI transforms the problem of posterior inference into an optimization problem. We seek to approximate the true posterior $P(z | x)$ with a simpler distribution $q(z)$ from a family $\mathcal{Q}$ by minimizing the KL divergence:
$$ q^*(z) = \arg \min_{q \in \mathcal{Q}} D_{KL}(q(z) || P(z|x)) $$
This is equivalent to maximizing the Evidence Lower Bound (ELBO):
$$ \text{ELBO}(q) = \mathbb{E}_{q(z)} [\log P(x, z)] - \mathbb{E}_{q(z)} [\log q(z)] $$

## 3. Markov Chain Monte Carlo (MCMC)
MCMC samples from a distribution $P(x)$ by constructing a Markov Chain whose stationary distribution is $P(x)$.

### Metropolis-Hastings Algorithm
1. Propose $x'$ from $Q(x' | x)$.
2. Calculate acceptance probability: $\alpha = \min\left(1, \frac{P(x')Q(x | x')}{P(x)Q(x' | x)}\right)$.
3. Accept $x'$ with probability $\alpha$, else stay at $x$.

## 4. Belief Propagation (BP)
BP is a message-passing algorithm for performing inference on graphical models (Bayesian Networks or Markov Random Fields). For a factor graph, the message from variable $x_i$ to factor $f_j$ is:
$$ \mu_{x_i \to f_j}(x_i) = \prod_{k \in \text{nb}(i) \setminus \{j\}} \mu_{f_k \to x_i}(x_i) $$
The message from factor $f_j$ to variable $x_i$ is:
$$ \mu_{f_j \to x_i}(x_i) = \sum_{x_{\sim i}} f_j(x_i, x_{\sim i}) \prod_{k \in \text{nb}(j) \setminus \{i\}} \mu_{x_k \to f_j}(x_k) $$
