---
type: technical-deep-dive
category: Transformers Architecture
tags: [layer-norm, residuals, gelu, gradients]
links: [04-Conhecimentos/01-IA-e-Agentes/README.md]
---

# Layer Normalization and Residuals

## Residual Connections

Residual connections (Skip-connections) address the vanishing gradient problem in deep networks by allowing gradients to flow through the network without being attenuated by non-linearities.
$$\text{Output} = x + \text{Sublayer}(x)$$

In Transformers, this ensures that the identity mapping is preserved, enabling the training of models with hundreds of layers.

## Layer Normalization (LayerNorm)

LayerNorm stabilizes training by normalizing the activations across the feature dimension for each training example independently.

### Post-Norm vs. Pre-Norm
1. **Post-Norm (Original Transformer)**: 
   $$\text{LayerNorm}(x + \text{Sublayer}(x))$$
   - Leads to higher instability at initialization; often requires a "warm-up" learning rate phase.
2. **Pre-Norm (Modern Standard)**: 
   $$x + \text{Sublayer}(\text{LayerNorm}(x))$$
   - More stable gradients; allows for higher learning rates and faster convergence. Standard in GPT-3, Llama, etc.

### RMSNorm (Root Mean Square Layer Normalization)
A variant used in Llama that simplifies LayerNorm by removing the mean centering and only scaling by the root mean square:
$$\bar{a}_i = \frac{a_i}{\sqrt{\frac{1}{d} \sum_{j=1}^d a_j^2}} \cdot \gamma_i$$

## GELU Activation Function

The Gaussian Error Linear Unit (GELU) is used instead of ReLU to avoid the "dying ReLU" problem.
$$\text{GELU}(x) = x P(X \le x) = x \cdot \Phi(x)$$
Where $\Phi(x)$ is the standard Gaussian cumulative distribution function. This provides a smoother transition and allows a small amount of negative gradient, aiding optimization.
