---
type: technical-deep-dive
category: Transformers Architecture
tags: [inference, kv-cache, paged-attention, quantization]
links: [04-Conhecimentos/01-IA-e-Agentes/README.md]
---

# Inference Optimization and KV Caching

## KV Caching

In autoregressive generation, the model computes the next token based on all previous tokens. Without caching, the $Q, K, V$ projections for the entire prefix are recomputed at every step.

### The KV Cache
By storing the Key ($K$) and Value ($V$) tensors of previous tokens in memory, the model only needs to compute the $Q, K, V$ for the *single* new token. 
- **Complexity**: Reduces the per-token generation cost from $O(n^2)$ to $O(n)$.
- **Bottleneck**: Inference becomes memory-bandwidth bound rather than compute-bound.

## PagedAttention

PagedAttention (vLLM) addresses the memory fragmentation caused by KV caches.
- **Problem**: Traditional KV caches require contiguous memory, leading to internal fragmentation.
- **Solution**: KV caches are partitioned into "blocks" (pages). A page table maps logical blocks to physical memory, allowing non-contiguous storage and efficient sharing of blocks (e.g., for parallel sampling/beam search).

## Speculative Decoding

To mitigate the bottleneck of autoregressive generation, speculative decoding uses a small "draft" model to predict multiple future tokens quickly.
1. The draft model generates $k$ tokens.
2. The large "target" model verifies these tokens in a single forward pass.
3. Accepted tokens are kept; rejected tokens are discarded and replaced by the target model's correction.

## Quantization

Quantization reduces the precision of weights and activations to decrease memory footprint and increase throughput.

- **INT8**: 8-bit integer quantization. Often uses symmetric or asymmetric scaling.
- **FP8**: 8-bit floating point (E4M3 or E5M2), maintaining a dynamic range better than INT8.
- **NF4 (NormalFloat 4)**: A non-linear quantization specifically optimized for normally distributed weights (used in QLoRA), providing near-FP16 precision with 4 bits.
