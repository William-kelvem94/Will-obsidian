---
title: Multivariable Calculus and Optimization
tags:
  - mathematics
  - optimization
  - deep-learning
created: 2026-06-09
updated: 2026-06-09
status: active
---

# Multivariable Calculus and Optimization

## 1. The Gradient ($\nabla$)
For a scalar field $f(\mathbf{x})$, the gradient is the vector of partial derivatives:
$$\nabla f(\mathbf{x}) = \left[ \frac{\partial f}{\partial x_1}, \frac{\partial f}{\partial x_2}, \dots, \frac{\partial f}{\partial x_n} \right]^T$$
The gradient points in the direction of steepest ascent.

### Application: Gradient Descent
Weights $\mathbf{w}$ are updated iteratively to minimize a loss function $L$:
$$\mathbf{w}_{t+1} = \mathbf{w}_t - \eta \nabla L(\mathbf{w}_t)$$
where $\eta$ is the learning rate.

## 2. The Jacobian Matrix ($\mathbf{J}$)
For a vector-valued function $f: \mathbb{R}^n \to \mathbb{R}^m$, the Jacobian is the matrix of all first-order partial derivatives:
$$\mathbf{J} = \frac{\partial f}{\partial \mathbf{x}} = \begin{bmatrix} \frac{\partial f_1}{\partial x_1} & \dots & \frac{\partial f_1}{\partial x_n} \\ \vdots & \ddots & \vdots \\ \frac{\partial f_m}{\partial x_1} & \dots & \frac{\partial f_m}{\partial x_n} \end{bmatrix}$$

### Role in Backpropagation
In neural networks, the error is propagated backward using the chain rule, which manifests as a sequence of Jacobian-vector products.

## 3. The Hessian Matrix ($\mathbf{H}$)
The Hessian is the square matrix of second-order partial derivatives of a scalar function $f$:
$$\mathbf{H}_{ij} = \frac{\partial^2 f}{\partial x_i \partial x_j}$$

### Application: Second-Order Optimization
- **Curvature:** The Hessian describes the local curvature of the loss landscape.
- **Newton's Method:** Uses the inverse Hessian to find the minimum more efficiently:
$$\mathbf{w}_{t+1} = \mathbf{w}_t - \mathbf{H}^{-1} \nabla L(\mathbf{w}_t)$$

## 4. Backpropagation Mathematics
Backpropagation is an application of the chain rule to compute $\nabla L$ with respect to all weights. For a loss $L$ and weight $w_{ij}^{(l)}$ in layer $l$:
$$\frac{\partial L}{\partial w_{ij}^{(l)}} = \frac{\partial L}{\partial a_i^{(l)}} \cdot \frac{\partial a_i^{(l)}}{\partial z_i^{(l)}} \cdot \frac{\partial z_i^{(l)}}{\partial w_{ij}^{(l)}}$$
where $z$ is the pre-activation and $a$ is the activation.

---
See also: [[Linear-Algebra-for-AI]]
