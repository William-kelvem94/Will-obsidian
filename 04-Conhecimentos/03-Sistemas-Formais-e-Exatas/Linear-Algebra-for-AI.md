---
title: Linear Algebra for AI
tags:
  - mathematics
  - artificial-intelligence
  - linear-algebra
created: 2026-06-09
updated: 2026-06-09
status: active
---

# Linear Algebra for AI

## 1. Tensors
A tensor is a generalization of scalars, vectors, and matrices to higher dimensions. In the context of deep learning, a tensor is a multi-dimensional array of numbers.

- **Scalar (0-order tensor):** A single number $x \in \mathbb{R}$.
- **Vector (1st-order tensor):** An array of numbers $\mathbf{v} \in \mathbb{R}^n$.
- **Matrix (2nd-order tensor):** A 2D array $\mathbf{M} \in \mathbb{R}^{m \times n}$.
- **Higher-Order Tensors:** Arrays with 3 or more dimensions (e.g., image data $\mathbb{R}^{H \times W \times C}$).

### Role in Neural Networks
Neural network weights are stored as tensors. A fully connected layer performs a tensor contraction:
$$\mathbf{y} = \sigma(\mathbf{W}\mathbf{x} + \mathbf{b})$$
where $\mathbf{W}$ is the weight matrix and $\mathbf{x}$ is the input vector.

## 2. Eigenvalues and Eigenvectors
For a square matrix $\mathbf{A}$, a non-zero vector $\mathbf{v}$ is an eigenvector if:
$$\mathbf{A}\mathbf{v} = \lambda\mathbf{v}$$
where $\lambda$ is the eigenvalue.

### Significance in AI
- **Stability:** In Recurrent Neural Networks (RNNs), the spectral radius (largest absolute eigenvalue) of the hidden-state weight matrix $\mathbf{W}_h$ determines if the gradients vanish or explode.
- **Dimensionality Reduction:** Principal Component Analysis (PCA) uses eigenvectors of the covariance matrix to find the directions of maximum variance.

## 3. Singular Value Decomposition (SVD)
SVD generalizes eigendecomposition to any $m \times n$ matrix $\mathbf{A}$:
$$\mathbf{A} = \mathbf{U}\mathbf{\Sigma}\mathbf{V}^T$$
- $\mathbf{U}$: Orthogonal matrix of left singular vectors.
- $\mathbf{\Sigma}$: Diagonal matrix of singular values $\sigma_1 \ge \sigma_2 \ge \dots \ge \sigma_k \ge 0$.
- $\mathbf{V}^T$: Orthogonal matrix of right singular vectors.

### Role in Neural Network Weights
- **Weight Compression:** Low-rank approximation via SVD allows compressing large weight matrices by keeping only the top $k$ singular values: $\mathbf{A} \approx \mathbf{U}_k \mathbf{\Sigma}_k \mathbf{V}_k^T$.
- **Regularization:** SVD can identify and prune near-zero singular values to prevent overfitting.

---
See also: [[Multivariable-Calculus-and-Optimization]]
