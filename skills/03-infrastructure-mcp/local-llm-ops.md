---
tags: [infrastructure, llm, local-ai, skills-mcp]
updated: 2026-05-03
title: "Local LLM Operations (LLMOps)"
date: 2026-04-27
---

# Local LLM Operations (LLMOps)

Strategies for running, optimizing, and scaling Large Language Models on local hardware.

## Optimization Stack
- **Quantization**: Using GGUF/EXL2 formats to fit larger models in VRAM (4-bit, 5-bit, 6-bit tradeoffs).
- **KV Cache Quantization**: Reducing memory usage during long context windows.
- **Context Management**: Strategies for handling 32k+ context without performance degradation.

## Tools & Servers
- **LM Studio**: GUI-based management and local API serving.
- **Ollama**: Minimalist CLI and easy model management.
- **vLLM / TGI**: High-throughput serving for local automation pipelines.

## Configuration Best Practices
1. **Temperature Tuning**:
   - `0.0 - 0.2`: Code generation & Hard logic.
   - `0.7 - 0.9`: Creative writing & Brainstorming.
2. **System Prompts**: Crafting consistent "Personalities" for local agents.
3. **GPU Offloading**: Maximizing VRAM usage while keeping the OS responsive.

## Local Benchmarking
- Tracking Token/s (TPS) across different models (DeepSeek-V3, Llama-3, etc.).
- Testing reasoning capabilities for complex coding tasks vs simple text manipulation.
