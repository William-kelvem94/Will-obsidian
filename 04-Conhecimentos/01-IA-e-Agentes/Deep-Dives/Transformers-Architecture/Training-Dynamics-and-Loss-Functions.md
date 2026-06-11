---
type: technical-deep-dive
category: Transformers Architecture
tags: [training, loss-functions, learning-rate, optimization]
links: [04-Conhecimentos/01-IA-e-Agentes/README.md]
---

# Training Dynamics and Loss Functions

## Cross-Entropy Loss and Label Smoothing

The standard objective for LLMs is the minimization of the cross-entropy loss over the sequence:
$$\mathcal{L} = -\sum_{i=1}^N \log P(y_i | x_{<i})$$

### Label Smoothing
To prevent the model from becoming overconfident (which leads to overfitting and calibration issues), label smoothing is applied. Instead of a hard one-hot target $[0, 1, 0]$, the target becomes $[\epsilon/K, 1-\epsilon, \epsilon/K]$.
This encourages the model to maintain a degree of uncertainty and improves generalization.

## Learning Rate Schedulers

The choice of learning rate (LR) is critical for convergence in high-dimensional spaces.

### Cosine Decay
Modern training uses a linear warm-up followed by a cosine decay:
$$\eta_t = \eta_{min} + \frac{1}{2}(\eta_{max} - \eta_{min})\left(1 + \cos\left(\frac{t}{T_{max}}\pi\right)\right)$$
- **Warm-up**: Prevents divergence in the early stages when gradients are volatile.
- **Decay**: Gradually reduces the LR to allow the model to settle into a sharper local minimum in the loss landscape.

## Weight Decay and AdamW

Transformers typically use **AdamW**, which decouples weight decay from the gradient update. Standard Adam applies weight decay to the moving average of the gradients; AdamW applies it directly to the weights, ensuring that the regularization is consistent regardless of the adaptive learning rate.
