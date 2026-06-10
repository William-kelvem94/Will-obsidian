---
type: deep-dive
category: Astrophysics
tags: [general-relativity, black-holes, hawking-radiation, gravitational-waves]
links: ["[[03-Sistemas-Formais-e-Exatas]]"]
---

# General Relativity and Black Holes

## The Schwarzschild Metric
A non-rotating, spherically symmetric black hole is described by the Schwarzschild metric in coordinates $(t, r, \theta, \phi)$:
$$ds^2 = -\left(1 - \frac{2GM}{c^2 r}\right)c^2 dt^2 + \left(1 - \frac{2GM}{c^2 r}\right)^{-1} dr^2 + r^2(d\theta^2 + \sin^2\theta d\phi^2)$$
The event horizon occurs at the Schwarzschild radius $r_s = \frac{2GM}{c^2}$.

## Event Horizons and Singularity
At $r = r_s$, the coordinate $t$ and $r$ swap signatures, meaning all future-directed paths lead inevitably toward the singularity at $r = 0$. The singularity is a region of infinite spacetime curvature.

## Hawking Radiation
Quantum field theory in curved spacetime predicts that black holes emit thermal radiation. Near the event horizon, virtual particle-antiparticle pairs are created; if one falls in and the other escapes, the black hole loses mass. The Hawking temperature is:
$$T_H = \frac{\hbar c^3}{8\pi G M k_B}$$
This implies that black holes eventually evaporate.

## Gravitational Waves
Perturbations in the spacetime metric $g_{\mu\nu} = \eta_{\mu\nu} + h_{\mu\nu}$ propagate as waves at the speed of light. For a binary system, the luminosity of gravitational radiation is:
$$L_{GW} = \frac{32}{5}\frac{G^4}{c^5}\frac{M_1^2 M_2^2 (M_1+M_2)}{a^5}$$
where $a$ is the semi-major axis.
