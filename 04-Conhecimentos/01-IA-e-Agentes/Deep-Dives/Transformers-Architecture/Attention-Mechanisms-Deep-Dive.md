---
type: technical-deep-dive
category: Transformers Architecture
tags: [attention, mathematics, complexity, transformers]
links: [04-Conhecimentos/01-IA-e-Agentes/README.md]
---

# Attention Mechanisms Deep Dive

## Scaled Dot-Product Attention

The core mechanism of the Transformer is Scaled Dot-Product Attention. It maps a query and a set of key-value pairs to an output.

### Mathematical Formulation
Given input matrices $Q$ (Query), $K$ (Key), and $V$ (Value), attention is computed as:
$$\text{Attention}(Q, K, V) = \text{softmax}\left(\frac{QK^T}{\sqrt{d_k}}\right)V$$

Where:
- $Q, K \in \mathbb{R}^{n \times d_k}$
- $V \in \mathbb{R}^{n \times d_v}$
- $\sqrt{d_k}$ is the scaling factor used to prevent the dot product from growing too large in magnitude, which would push the softmax function into regions with extremely small gradients.

### Complexity Analysis
The computational complexity of a single attention layer is $O(n^2 \cdot d)$, where $n$ is the sequence length and $d$ is the embedding dimension.
- **Matrix Multiplication $QK^T$**: $O(n^2 \cdot d)$.
- **Softmax and Scaling**: $O(n^2)$.
- **Weighting $V$**: $O(n^2 \cdot d)$.
The quadratic dependency on $n$ makes long-context processing computationally expensive and memory-intensive.

## Multi-Head Attention (MHA)

Multi-Head Attention allows the model to jointly attend to information from different representation subspaces at different positions.

### Operation
Instead of performing a single attention function with $d_{model}$-dimensional keys, values, and queries, MHA linearly projects these $h$ times with different, learned linear projections:
$$\text{MultiHead}(Q, K, V) = \text{Concat}(\text{head}_1, \dots, \text{head}_h)W^O$$
$$\text{where } \text{head}_i = \text{Attention}(QW_i^Q, KW_i^K, VW_i^V)$$

### Theoretical Advantage
- **Specialization**: Each head can specialize in different types of linguistic relationships (e.g., one head for syntactic dependencies, another for semantic coreference).
- **Ensemble Effect**: It acts as an ensemble of attention mechanisms, improving the stability and representational capacity of the model.
