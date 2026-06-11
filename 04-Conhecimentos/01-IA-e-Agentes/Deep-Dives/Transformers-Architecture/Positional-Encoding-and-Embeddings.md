---
type: technical-deep-dive
category: Transformers Architecture
tags: [embeddings, positional-encoding, rope, alibi]
links: [04-Conhecimentos/01-IA-e-Agentes/README.md]
---

# Positional Encoding and Embeddings

Since Transformers lack recurrence or convolution, they have no inherent sense of the order of tokens. Positional information must be explicitly injected.

## Sinusoidal Positional Encodings

The original Transformer (Vaswani et al.) used fixed sinusoidal functions:
$$PE_{(pos, 2i)} = \sin(pos / 10000^{2i/d_{model}})$$
$$PE_{(pos, 2i+1)} = \cos(pos / 10000^{2i/d_{model}})$$

- **Properties**: This allows the model to learn to attend by relative positions, since for any fixed offset $k$, $PE_{pos+k}$ can be represented as a linear function of $PE_{pos}$.
- **Limitation**: Poor extrapolation to sequence lengths beyond those seen during training.

## Rotary Positional Embeddings (RoPE)

RoPE encodes absolute positional information using a rotation matrix, effectively implementing a relative position mechanism.

### Mechanism
RoPE rotates the $Q$ and $K$ vectors in 2D planes. For a vector $x$ at position $m$:
$$\text{RoPE}(x, m) = R_m x$$
Where $R_m$ is an orthogonal rotation matrix. The dot product of two rotated vectors depends only on their relative distance $m-n$:
$$\langle R_m q, R_n k \rangle = \langle q, R_{n-m} k \rangle$$

- **Benefit**: Better extrapolation and theoretical foundation for relative distance.
- **Usage**: Standard in Llama and most modern LLMs.

## ALiBi (Attention with Linear Biases)

ALiBi removes positional embeddings entirely and instead adds a static bias to the attention scores.

### Formulation
The attention score between token $i$ and $j$ is modified:
$$\text{Score}(i, j) = Q_i K_j^T - m \cdot |i - j|$$
Where $m$ is a head-specific slope.

- **Extrapolation**: ALiBi allows models to generalize to significantly longer sequences than those seen during training without the "out-of-distribution" failures typical of absolute embeddings.
- **Efficiency**: Zero overhead for embedding lookups.
