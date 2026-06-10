---
type: deep-dive
topic: Mathematics for AI
subject: Information Theory and KL Divergence
tags: [information-theory, entropy, kl-divergence, mutual-information]
links: [[03-Sistemas-Formais-e-Exatas/INDEX|Index]]
---

# Information Theory and KL Divergence

## 1. Shannon Entropy
Entropy $H(X)$ measures the average uncertainty of a random variable $X$ with probability mass function $P(X)$:
$$ H(X) = -\sum_{x \in \mathcal{X}} P(x) \log P(x) $$
It represents the lower bound on the average number of bits needed to encode samples from $X$.

## 2. Cross-Entropy
Cross-entropy $H(P, Q)$ measures the average number of bits needed to identify an event from a set of events with distribution $P$ when using a code based on distribution $Q$:
$$ H(P, Q) = -\sum_{x \in \mathcal{X}} P(x) \log Q(x) $$
In neural networks, we minimize cross-entropy between the ground truth distribution $P$ (often one-hot) and the predicted distribution $Q$.

## 3. Kullback-Leibler (KL) Divergence
KL divergence $D_{KL}(P || Q)$ quantifies the "distance" (relative entropy) between two probability distributions:
$$ D_{KL}(P || Q) = \sum_{x \in \mathcal{X}} P(x) \log \frac{P(x)}{Q(x)} = H(P, Q) - H(P) $$
Properties:
- $D_{KL}(P || Q) \geq 0$ (Gibbs' Inequality).
- Non-symmetric: $D_{KL}(P || Q) \neq D_{KL}(Q || P)$.

## 4. Mutual Information (MI)
MI $I(X; Y)$ measures the amount of information obtained about $X$ through $Y$:
$$ I(X; Y) = \sum_{x,y} P(x,y) \log \frac{P(x,y)}{P(x)P(y)} $$
Equivalently:
$$ I(X; Y) = H(X) - H(X | Y) = D_{KL}(P(X,Y) || P(X)P(Y)) $$
In AI, MI is used to quantify the dependence between latent representations and targets (e.g., in InfoGAN).
