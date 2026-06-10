---
tags: [neuro-symbolic, ai, knowledge-graphs, reasoning]
status: complete
created: 2026-06-10
---

# Neural-Symbolic Integration

## 1. The Core Dichotomy
AI has historically been split into two paradigms:
- **Connectionist (Neural Networks):** Sub-symbolic, distributed representations, excellent at pattern recognition, intuitive "System 1" thinking (fast, automatic).
- **Symbolic (Logic-based):** Explicit symbols, formal rules, excellent at structured reasoning and transparency, "System 2" thinking (slow, deliberate).

**Neural-Symbolic (NeSy) Integration** aims to combine the learning power of NNs with the reasoning and interpretability of symbolic logic.

## 2. Integration Architectures

### Symbolic-on-Neural (Deep Logic)
Using NNs to extract symbols from raw data, which are then processed by a symbolic engine.
- **Example:** An object detection model (Neural) identifies "Apple" and "Table", and a logic engine (Symbolic) reasons that "Apple is on the Table".

### Neural-on-Symbolic (Differentiable Logic)
Representing symbolic logic as differentiable operations so that they can be trained via gradient descent.
- **T-Norms:** Replacing boolean AND/OR with continuous functions (e.g., product or min/max) to allow gradients to flow.
- **Logic Tensor Networks (LTN):** Mapping logical constants to tensors and predicates to functions, allowing the model to optimize for "satisfiability" of a set of logical constraints.

## 3. Knowledge Graphs (KG) and Embeddings
KGs provide a structured symbolic representation of the world.

- **Knowledge Graph Embeddings (KGE):** Techniques like **TransE**, **RotatE**, or **ComplEx** map entities and relations into a continuous vector space while preserving the symbolic structure (e.g., $h + r \approx t$).
- **Graph Neural Networks (GNNs):** Use message passing to aggregate neighborhood information, combining the topology of the KG with the learning capabilities of NNs.

## 4. Neuro-symbolic Reasoning Workflows
The hybrid approach typically follows one of these patterns:

1. **Neural Perception $\rightarrow$ Symbolic Reasoning $\rightarrow$ Neural Actuation.**
2. **Learning the Logic:** Using a neural network to "induce" symbolic rules from data (Inductive Logic Programming).
3. **Constraint-Guided Learning:** Using symbolic rules as loss functions (regularizers) to force a neural network to obey certain physical or logical laws.

## 5. Key Advantages
- **Interpretability:** The symbolic component provides a trace of "why" a decision was made.
- **Data Efficiency:** Symbolic rules act as a strong prior, reducing the amount of data needed to learn a task.
- **Generalization:** Symbolic logic generalizes perfectly to unseen cases that follow the same rules, unlike NNs which may hallucinate.

---
**Related Notes:**
- [[Model-Context-Protocol-MCP]]
- [[RAG-e-Memoria-para-Agentes]]
- [[Embeddings-e-Busca-Semantica]]
