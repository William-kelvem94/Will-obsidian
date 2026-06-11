---
type: deep-dive
topic: Quantitative Finance
domain: Finance
links: ["[[03-Sistemas-Formais-e-Exatas]]"]
tags: [stochastic-calculus, black-scholes, option-pricing]
---

# Black-Scholes and Option Pricing

## Stochastic Calculus and Itô's Lemma
The price of an underlying asset $S_t$ is modeled by a Geometric Brownian Motion (GBM):
$$dS_t = \mu S_t dt + \sigma S_t dW_t$$
where $W_t$ is a standard Wiener process. For a twice-differentiable function $f(t, S_t)$, **Itô's Lemma** provides:
$$df = \left( \frac{\partial f}{\partial t} + \mu S_t \frac{\partial f}{\partial S} + \frac{1}{2} \sigma^2 S_t^2 \frac{\partial^2 f}{\partial S^2} \right) dt + \sigma S_t \frac{\partial f}{\partial S} dW_t$$

## The Black-Scholes PDE
By constructing a risk-neutral portfolio consisting of the option and the underlying asset, we derive the Black-Scholes Partial Differential Equation (PDE):
$$\frac{\partial V}{\partial t} + r S \frac{\partial V}{\partial S} + \frac{1}{2} \sigma^2 S^2 \frac{\partial^2 V}{\partial S^2} - rV = 0$$
This is a parabolic PDE closely related to the **heat equation**.

## Option Pricing Formula
For a European Call option $C(S, t)$ with strike $K$ and maturity $T$:
$$C(S, t) = S_t N(d_1) - K e^{-r(T-t)} N(d_2)$$
where $N(\cdot)$ is the CDF of the standard normal distribution, and:
$$d_1 = \frac{\ln(S_t/K) + (r + \sigma^2/2)(T-t)}{\sigma \sqrt{T-t}}, \quad d_2 = d_1 - \sigma \sqrt{T-t}$$

## The Greeks
The Greeks measure the sensitivity of the option price to its parameters:
- **Delta ($\Delta$):** $\frac{\partial V}{\partial S} = N(d_1)$ (for calls)
- **Gamma ($\Gamma$):** $\frac{\partial^2 V}{\partial S^2} = \frac{N'(d_1)}{S \sigma \sqrt{T-t}}$
- **Vega ($\nu$):** $\frac{\partial V}{\partial \sigma} = S \sqrt{T-t} N'(d_1)$
- **Theta ($\Theta$):** $\frac{\partial V}{\partial t}$
- **Rho ($\rho$):** $\frac{\partial V}{\partial r}$
