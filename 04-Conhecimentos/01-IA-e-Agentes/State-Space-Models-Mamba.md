---
title: State-Space Models and Mamba
tags: [ai, llm, architecture, state-space-models]
date: 2026-06-09
---

# State-Space Models (SSM) and Mamba

This note examines the transition from the Attention mechanism (Transformer) to State-Space Models (SSMs), specifically the Mamba architecture, aimed at solving the quadratic complexity of the context window.

## 1. The Transformer Bottleneck: $\mathcal{O}(L^2)$
Transformers use **Attention**, where every token in a sequence of length $L$ attends to every other token. This leads to:
- **Quadratic Time Complexity**: $O(L^2)$.
- **Quadratic Memory Complexity**: $O(L^2)$ to store the K-V cache.
This makes processing very long sequences (e.g., entire books or codebases) computationally prohibitive.

## 2. Introduction to State-Space Models (SSM)
SSMs are based on classical control theory. They describe a system where a hidden state $h(t)$ evolves over time based on an input $x(t)$.

### Linear Recurrence
A continuous-time SSM is defined as:
1. $\dot{h}(t) = \mathbf{A}h(t) + \mathbf{B}x(t)$
2. $y(t) = \mathbf{C}h(t)$

Where:
- $\mathbf{A}$ is the state transition matrix.
- $\mathbf{B}$ is the input-to-state matrix.
- $\mathbf{C}$ is the state-to-output matrix.

By discretizing this system, we get a **Recurrent Neural Network (RNN)** like structure:
$h_t = \bar{\mathbf{A}}h_{t-1} + \bar{\mathbf{B}}x_t$
$y_t = \mathbf{C}h_t$

This allows for **Linear Complexity** $O(L)$ during inference.

## 3. The Mamba Architecture: Selective SSMs
Traditional SSMs are **Time-Invariant** (the matrices $\mathbf{A, B, C}$ do not change based on the input). This makes them poor at remembering specific tokens (like "not" in a long sentence).

### Selective Mechanism
Mamba introduces **Selection**, where $\mathbf{B}, \mathbf{C},$ and the discretization parameter $\Delta$ are functions of the input $x_t$:
- $\mathbf{B}_t = \text{Linear}_B(x_t)$
- $\mathbf{C}_t = \text{Linear}_C(x_t)$
- $\Delta_t = \text{Linear}_\Delta(x_t)$

This allows the model to selectively "forget" irrelevant information and "remember" critical tokens, essentially acting as a data-dependent filter.

### Hardware-Aware Implementation
To maintain the efficiency of a convolution while having the flexibility of a recurrence, Mamba uses a **Selective Scan** algorithm.
- Instead of materializing the full state in HBM (High Bandwidth Memory), it performs the scan in the fast **SRAM** of the GPU.
- This avoids the memory bottleneck and allows Mamba to train and infer significantly faster than Transformers.

## 4. Comparative Analysis: Mamba vs Transformer

| Feature | Transformer (Attention) | Mamba (Selective SSM) |
| :--- | :--- | :--- |
| **Complexity** | $\mathcal{O}(L^2)$ | $\mathcal{O}(L)$ |
| **Inference Speed** | Slows down as $L$ increases | Constant speed per token |
| **Context Memory** | Perfect (Exact retrieval) | Compressed (Lossy) |
| **Training** | Highly Parallel | Parallel via Selective Scan |

## 5. Implications for AI Agents
Mamba's linear scaling allows agents to:
- Process massive documentation sets in a single pass.
- Maintain much longer active memories without crashing via OOM (Out of Memory).
- Execute on edge devices where VRAM is limited.

## References
- *Mamba: Linear-Time Sequence Models Selective State Spaces* (Gu & Dao)
- *S4: Structured State Spaces for Sequence Modeling* (Albert Gu)
