---
tags: [infrastructure, llm, local-ai, ollama, docker, quantization, vllm, skills-mcp]
updated: 2026-06-01
title: "Local LLM Operations (LLMOps)"
date: 2026-04-27
---

# Local LLM Operations (LLMOps)

Estratégias para executar, otimizar e escalar Large Language Models em hardware local. Este guia cobre desde a configuração básica do Ollama até arquiteturas de multi-model serving com GPU passthrough.

## 1. Ollama: Setup e Gerenciamento

### Instalação
```powershell
# Windows (via WSL2 é recomendado para performance)
wsl --install -d Ubuntu
# Dentro do WSL2:
curl -fsSL https://ollama.com/install.sh | sh
```

### Comandos Essenciais
```bash
# Listar modelos disponíveis localmente
ollama list

# Pull de modelos
ollama pull llama3.2:3b        # 3B params, rápido para testes
ollama pull llama3.2:1b        # 1B params, ultra-rápido
ollama pull deepseek-r1:7b     # 7B com raciocínio
ollama pull mistral:7b         # 7B generalista
ollama pull nomic-embed-text   # Modelo de embedding (768d)

# Executar modelo interativamente
ollama run deepseek-r1:7b

# Remover modelo
ollama rm llama3.2:1b
```

### API Endpoint Local
O Ollama expõe uma API compatível com OpenAI:

```python
from openai import OpenAI

client = OpenAI(
    base_url="http://localhost:11434/v1",
    api_key="ollama"  # Placeholder, não é validado
)

response = client.chat.completions.create(
    model="deepseek-r1:7b",
    messages=[{"role": "user", "content": "Explique RAG em português"}],
    temperature=0.3,
    max_tokens=2048
)
print(response.choices[0].message.content)
```

### ModFile (Model Files)
Crie modelos customizados com parâmetros fixos:

```dockerfile
FROM llama3.2:3b

# Ajustes de parâmetros
PARAMETER temperature 0.2
PARAMETER top_p 0.9
PARAMETER stop "</s>"

# Sistema prompt fixo
SYSTEM "Você é um assistente especializado em arquitetura de software. Responda em português."

# Template de mensagem customizado
TEMPLATE """{{ if .System }}<|system|>
{{ .System }}
{{ end }}<|user|>
{{ .Prompt }}
<|assistant|>"""
```

```bash
ollama create jarvis-assistant -f ./ModFile
ollama run jarvis-assistant
```

## 2. Docker-Based LLM Deployment

### Ollama em Container
```yaml
# docker-compose.yml
version: "3.8"
services:
  ollama:
    image: ollama/ollama:latest
    container_name: ollama
    ports:
      - "11434:11434"
    volumes:
      - ollama_data:/root/.ollama
    deploy:
      resources:
        reservations:
          devices:
            - driver: nvidia
              count: all
              capabilities: [gpu]
    restart: unless-stopped

  open-webui:
    image: ghcr.io/open-webui/open-webui:main
    container_name: open-webui
    ports:
      - "3000:8080"
    volumes:
      - openwebui_data:/app/backend/data
    environment:
      - OLLAMA_BASE_URL=http://ollama:11434
    depends_on:
      - ollama

volumes:
  ollama_data:
  openwebui_data:
```

```bash
docker compose up -d
# Interface disponível em http://localhost:3000
```

### vLLM para High-Throughput Serving
```bash
docker run --gpus all -p 8000:8000 \
    -v ~/.cache/huggingface:/root/.cache/huggingface \
    vllm/vllm-openai:latest \
    --model mistralai/Mistral-7B-Instruct-v0.3 \
    --dtype auto \
    --max-model-len 8192 \
    --gpu-memory-utilization 0.9
```

### TGI (Text Generation Inference) da Hugging Face
```bash
docker run --gpus all -p 8080:80 \
    ghcr.io/huggingface/text-generation-inference:latest \
    --model-id mistralai/Mistral-7B-Instruct-v0.3
```

## 3. Quantização

### GGUF (GPT-Generated Unified Format)
Formato mais popular para CPUs e GPUs com recursos limitados:

| Tipo | Bits | Tamanho (7B) | Qualidade Relativa | Uso |
|------|------|-------------|-------------------|-----|
| Q2_K | 2-bit | ~2.7 GB | 60% | Extreme compression |
| Q3_K_M | 3-bit | ~3.3 GB | 70% | Bate e volta |
| Q4_K_M | 4-bit | ~4.1 GB | 85% | **Recomendado** |
| Q5_K_M | 5-bit | ~4.8 GB | 92% | Melhor custo-benefício |
| Q6_K | 6-bit | ~5.6 GB | 96% | Alta qualidade |
| Q8_0 | 8-bit | ~6.7 GB | 99% | Quase lossless |
| F16 | 16-bit | ~13.5 GB | 100% | Original |

### AWQ (Activation-Aware Weight Quantization)
Melhor que GPTQ para inferência, com menor perda:

```python
from awq import AutoAWQForCausalLM
from transformers import AutoTokenizer

model_path = "mistralai/Mistral-7B-Instruct-v0.3"
quant_path = "mistral-7b-awq-4bit"

model = AutoAWQForCausalLM.from_pretrained(model_path)
tokenizer = AutoTokenizer.from_pretrained(model_path)

# AWQ quantization (4-bit)
model.quantize(
    tokenizer,
    quant_config={"zero_point": True, "q_group_size": 128, "w_bit": 4}
)
model.save_quantized(quant_path)
```

### GPTQ (Post-Training Quantization)
```python
from auto_gptq import AutoGPTQForCausalLM, BaseQuantizeConfig

quantize_config = BaseQuantizeConfig(
    bits=4,
    group_size=128,
    damp_percent=0.01,
    desc_act=False,
)
model = AutoGPTQForCausalLM.from_pretrained(
    model_path,
    quantize_config=quantize_config,
)
```

## 4. VRAM Requirements by Model Size

| Parâmetros | Precisão | VRAM Aproximada | Exemplos |
|-----------|---------|----------------|----------|
| 1B | Q4_K_M | ~0.8 GB | Llama 3.2 1B, TinyLlama |
| 3B | Q4_K_M | ~2.2 GB | Llama 3.2 3B, Phi-3 Mini |
| 7B | F16 | ~14 GB | Mistral 7B, Llama 2 7B |
| 7B | Q4_K_M | ~4.1 GB | Mesmos modelos quantizados |
| 13B | Q4_K_M | ~7.5 GB | Llama 2 13B, Mixtral 8x7B |
| 34B | Q4_K_M | ~19 GB | Yi-34B, CodeLlama 34B |
| 70B | Q4_K_M | ~40 GB | Llama 3 70B, Qwen 72B |
| 70B | F16 | ~140 GB | Mesmos modelos em full precision |

**Regra prática:** `VRAM ≈ param_count × bytes_per_param × 1.2` (overhead de KV cache).

### Cálculo de KV Cache
```python
def estimate_kv_cache_vram(
    model_params: int,
    context_length: int,
    bits: int = 16,
    num_layers: int = 32,
    num_heads: int = 32,
    hidden_dim: int = 4096
) -> float:
    """Estima VRAM do KV cache em GB"""
    bytes_per_value = bits / 8
    kv_cache_per_token = 2 * num_layers * num_heads * (hidden_dim // num_heads) * bytes_per_value
    total_vram = kv_cache_per_token * context_length / (1024**3)
    return total_vram

# Estimativa para Mistral 7B com 32K contexto:
kv_vram = estimate_kv_cache_vram(7e9, 32768)
print(f"KV Cache VRAM: {kv_vram:.2f} GB")
```

## 5. Multi-Model Serving

### Arquitetura com Roteamento Inteligente
```python
class ModelRouter:
    def __init__(self):
        self.models = {
            "fast": {"endpoint": "http://localhost:11434", "model": "llama3.2:3b"},
            "reasoning": {"endpoint": "http://localhost:11435", "model": "deepseek-r1:7b"},
            "code": {"endpoint": "http://localhost:8000", "model": "codellama:7b"},
            "embedding": {"endpoint": "http://localhost:11434", "model": "nomic-embed-text"},
        }
    
    def route(self, task: str) -> dict:
        if any(k in task for k in ["code", "python", "function"]):
            return self.models["code"]
        if any(k in task for k in ["explain", "think", "reason"]):
            return self.models["reasoning"]
        if len(task) < 50:  # Perguntas curtas = rápidas
            return self.models["fast"]
        return self.models["reasoning"]
```

### Multi-Instance Ollama
```bash
# Instância 1: modelos pequenos (porta 11434)
OLLAMA_HOST=0.0.0.0:11434 ollama serve

# Instância 2: modelos grandes (porta 11435)
OLLAMA_HOST=0.0.0.0:11435 OLLAMA_MODELS=/path/to/large/models ollama serve
```

### Load Balancing com OpenAI Proxy
```python
# proxy.py - Roteia requisições baseado no modelo
from fastapi import FastAPI, Request
import httpx

app = FastAPI()
BACKENDS = {
    "llama3.2:3b": "http://ollama-fast:11434/v1",
    "deepseek-r1:7b": "http://ollama-reasoning:11435/v1",
    "nomic-embed-text": "http://ollama-embed:11436/v1",
}

@app.post("/v1/chat/completions")
async def proxy(request: Request):
    body = await request.json()
    model = body.get("model")
    backend = BACKENDS.get(model)
    
    if not backend:
        return {"error": f"Model {model} not available"}
    
    async with httpx.AsyncClient() as client:
        resp = await client.post(f"{backend}/chat/completions", json=body)
        return resp.json()
```

## 6. GPU Passthrough

### WSL2 + CUDA
```powershell
# 1. Instalar NVIDIA CUDA no Windows
# 2. Instalar WSL2 CUDA driver
wsl --install -d Ubuntu

# Dentro do WSL2:
# Verificar GPU
nvidia-smi

# Instalar CUDA toolkit
sudo apt update && sudo apt install -y nvidia-cuda-toolkit

# Testar com Ollama
ollama pull mistral:7b
ollama run mistral:7b
```

### Docker com GPU
```bash
# Verificar se o NVIDIA Container Toolkit está instalado
nvidia-ctk --version

# Testar GPU no container
docker run --gpus all nvidia/cuda:12.2.0-base nvidia-smi
```

### Verificação de GPU Offloading
```bash
# Verificar quantas camadas estão sendo offloaded para GPU
ollama run mistral:7b --verbose
# Procure por "gpu_layers" na saída
```

## 7. Monitoramento e Métricas

### OpenAI API Compatible Endpoint Metrics
```python
# metrics.py - Coleta métricas de todos os endpoints
import time
import psutil
import GPUtil
from prometheus_client import start_http_server, Gauge, Histogram

# Métricas
LLM_LATENCY = Histogram("llm_request_duration_seconds", "LLM request latency", ["model"])
VRAM_USAGE = Gauge("vram_usage_bytes", "VRAM usage", ["gpu_id"])
TOKENS_PER_SECOND = Gauge("tokens_per_second", "Generation speed", ["model"])

def collect_metrics():
    while True:
        gpus = GPUtil.getGPUs()
        for gpu in gpus:
            VRAM_USAGE.labels(gpu_id=gpu.id).set(gpu.memoryUsed * 1024 * 1024)
        time.sleep(15)
```

### Benchmarking Local
```python
import time
from openai import OpenAI

def benchmark_model(model: str, prompt: str, runs: int = 5):
    client = OpenAI(base_url="http://localhost:11434/v1", api_key="ollama")
    latencies = []
    total_tokens = 0
    
    for _ in range(runs):
        start = time.time()
        response = client.chat.completions.create(
            model=model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=500,
        )
        elapsed = time.time() - start
        tokens = response.usage.completion_tokens
        latencies.append(elapsed)
        total_tokens += tokens
    
    avg_latency = sum(latencies) / len(latencies)
    avg_tps = total_tokens / sum(latencies)
    
    return {
        "model": model,
        "avg_latency_s": round(avg_latency, 2),
        "avg_tokens_per_second": round(avg_tps, 2),
        "p95_latency_s": round(sorted(latencies)[int(runs * 0.95)], 2),
    }

# Resultados típicos (RTX 4090):
# - llama3.2:3b: ~80 t/s
# - deepseek-r1:7b: ~45 t/s
# - mistral:7b: ~50 t/s
```

## 8. Boas Práticas de Produção

### Configuração de Temperature por Tarefa

| Tarefa | Temperature | Top_p | Top_k |
|--------|-------------|-------|-------|
| Geração de código | 0.1 - 0.2 | 0.9 | 40 |
| Raciocínio lógico | 0.2 - 0.4 | 0.9 | 40 |
| Tradução | 0.3 - 0.5 | 0.85 | 40 |
| Escrita criativa | 0.7 - 0.9 | 0.95 | 50 |
| Brainstorming | 0.9 - 1.1 | 1.0 | 100 |

### System Prompts Consistentes
Mantenha system prompts versionados e testados:

```python
SYSTEM_PROMPTS = {
    "coder": "Você é um engenheiro de software sênior. Gere código limpo, \
              com type hints, e sempre explique a lógica em português.",
    "analyst": "Você é um analista de dados. Responda com números, \
                fontes e sempre faça análises críticas.",
    "creative": "Você é um escritor criativo. Use linguagem rica e \
                 estruturas narrativas envolventes.",
}
```

### Health Checks
```python
@app.get("/health")
async def health_check():
    results = {}
    for name, config in MODEL_ROUTER.models.items():
        try:
            client = OpenAI(base_url=config["endpoint"], api_key="ollama")
            response = client.chat.completions.create(
                model=config["model"],
                messages=[{"role": "user", "content": "ping"}],
                max_tokens=5,
            )
            results[name] = {"status": "healthy", "latency_ms": response.usage.total_tokens}
        except Exception as e:
            results[name] = {"status": "unhealthy", "error": str(e)}
    return results
```

---

*Veja também: [[04-knowledge-systems/memory-management]], [[mcp-servers]], [[04-knowledge-systems/advanced-rag-strategies]].*
