---
type: deep-dive
topic: Mathematics for AI
subject: Optimization Theory and Convergence
tags: [optimization, sgd, adam, kkt]
links: [[03-Sistemas-Formais-e-Exatas/INDEX|Index]]
---

# Optimization Theory and Convergence

## 1. First-Order Optimization Methods

### Stochastic Gradient Descent (SGD)
The update rule for a parameter $\theta$ is:
$$ \theta_{t+1} = \theta_t - \eta \nabla \mathcal{L}(\theta_t; \xi_t) $$
where $\xi_t$ is a random mini-batch. Convergence is guaranteed for convex functions if the learning rate $\eta_t$ satisfies the Robbins-Monro conditions: $\sum \eta_t = \infty, \sum \eta_t^2 < \infty$.

### Adam (Adaptive Moment Estimation)
Adam maintains estimates of the first moment $\hat{m}_t$ and second moment $\hat{v}_t$:
$$ m_t = \beta_1 m_{t-1} + (1-\beta_1) \nabla \mathcal{L}_t, \quad v_t = \beta_2 v_{t-1} + (1-\beta_2) (\nabla \mathcal{L}_t)^2 $$
Correcting for bias:
$$ \hat{m}_t = \frac{m_t}{1-\beta_1^t}, \quad \hat{v}_t = \frac{v_t}{1-\beta_2^t} $$
Update: $\theta_{t+1} = \theta_t - \frac{\eta}{\sqrt{\hat{v}_t} + \epsilon} \hat{m}_t$.

### RMSProp
A precursor to Adam that scales the gradient by the square root of the exponential moving average of squared gradients:
$$ v_t = \gamma v_{t-1} + (1-\gamma) (\nabla \mathcal{L}_t)^2 \implies \theta_{t+1} = \theta_t - \frac{\eta}{\sqrt{v_t + \epsilon}} \nabla \mathcal{L}_t $$

## 2. Convex vs Non-Convex Optimization

A function $f$ is convex if $\forall x, y \in \text{dom}(f), \forall \lambda \in [0,1]$:
$$ f(\lambda x + (1-\lambda)y) \leq \lambda f(x) + (1-\lambda)f(y) $$
In convex optimization, any local minimum is a global minimum. In non-convex landscapes (like Deep Neural Networks), the presence of saddle points is more prevalent than local minima.

## 3. Constrained Optimization

### Lagrange Multipliers
To minimize $f(x)$ subject to $g(x) = 0$, we define the Lagrangian:
$$ \mathcal{L}(x, \lambda) = f(x) + \lambda g(x) $$
The optimality condition requires $\nabla \mathcal{L} = 0$.

### Karush-Kuhn-Tucker (KKT) Conditions
For inequality constraints $h_i(x) \leq 0$, the KKT conditions for optimality are:
1. **Stationarity**: $\nabla f(x^*) + \sum \mu_i \nabla h_i(x^*) = 0$
2. **Primal Feasibility**: $h_i(x^*) \leq 0$
3. **Dual Feasibility**: $\mu_i \geq 0$
4. **Complementary Slackness**: $\mu_i h_i(x^*) = 0$
