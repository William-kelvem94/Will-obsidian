---
type: deep-dive
topic: Mathematics for AI
subject: Linear Algebra, Tensors, and Manifolds
tags: [linear-algebra, tensors, manifolds, svd]
links: [[03-Sistemas-Formais-e-Exatas/INDEX|Index]]
---

# Linear Algebra, Tensors, and Manifolds

## 1. Tensors and Tensor Contractions

A tensor $\mathcal{T}$ is a multi-linear map $\mathcal{T}: V^* \times \dots \times V^* \times V \times \dots \times V \to \mathbb{R}$, where $V$ is a vector space and $V^*$ its dual. In coordinates, a tensor of type $(r, s)$ is represented by a multi-dimensional array $T^{i_1 \dots i_r}_{j_1 \dots j_s}$.

### Tensor Contraction
Contraction is the operation of summing over a pair of indices (one contravariant and one covariant). For a tensor $T^{i \dots}_{j \dots}$, the contraction over indices $i$ and $j$ is:
$$ C^{k_1 \dots k_{r-1}}_{l_1 \dots l_{s-1}} = \sum_{i=1}^{\dim V} T^{i k_1 \dots k_{r-1}}_{i l_1 \dots l_{s-1}} $$
In the context of Deep Learning, the Einstein summation convention is used: $A_{ij} B_{jk} = C_{ik}$, where the repeated index $j$ implies summation.

## 2. Riemannian Manifolds in Latent Space

Modern AI interprets latent spaces $\mathcal{Z}$ not as Euclidean spaces, but as Riemannian manifolds $(\mathcal{M}, g)$. The metric tensor $g_{ij}$ defines the local geometry and distance:
$$ ds^2 = g_{ij} dx^i dx^j $$

### The Pull-back Metric
For a generative model $f: \mathcal{Z} \to \mathcal{X}$, the latent space inherits a metric from the data space $\mathcal{X}$ via the pull-back:
$$ g_{ij}(\mathbf{z}) = \sum_{k} \frac{\partial f^k}{\partial z^i} \frac{\partial f^k}{\partial z^j} $$
This allows for geodesic paths in latent space that correspond to the shortest semantic transitions in the data space.

## 3. Singular Value Decomposition (SVD)

SVD generalizes the eigendecomposition of a square matrix to any $m \times n$ matrix $A$:
$$ A = U \Sigma V^T $$
Where:
- $U \in \mathbb{R}^{m \times m}$ is orthogonal (left singular vectors).
- $\Sigma \in \mathbb{R}^{m \times n}$ is diagonal with non-negative entries $\sigma_i$ (singular values).
- $V \in \mathbb{R}^{n \times n}$ is orthogonal (right singular vectors).

### Dimensionality Reduction via Eckart-Young-Mirsky Theorem
The best rank-$k$ approximation of $A$ in the Frobenius norm is obtained by keeping only the $k$ largest singular values:
$$ A_k = \sum_{i=1}^k \sigma_i u_i v_i^T $$
The error is given by: $\|A - A_k\|_F^2 = \sum_{i=k+1}^{\min(m,n)} \sigma_i^2$.
