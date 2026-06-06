---
title: "Ollama GPU Issues — Troubleshooting"
description: "Fix GPU detection and performance issues with Ollama"
tags: [troubleshooting, ollama, gpu, nvidia, llm, playbook, jarvis-engenharia]
updated: 2026-06-05
date: 2026-04-27
---

# 🎮 Ollama GPU Issues

Troubleshooting GPU detection and performance in Ollama.

---

## 🔍 Quick Diagnosis

```bash
# Check if Ollama is running
curl http://localhost:11434/api/tags

# Check GPU status
nvidia-smi  # NVIDIA
rocm-smi    # AMD

# Run model and check GPU usage
ollama run llama3.1:8b
# Open another terminal:
nvidia-smi  # Should show GPU usage
```

---

## ❌ Problem 1: GPU Not Detected

### Symptoms
- Ollama runs on CPU only (slow)
- No GPU usage in `nvidia-smi` while running
- Message: "CUDA not available"

### Diagnosis
```bash
# Check NVIDIA driver
nvidia-smi
# Should show driver version and GPU

# Check CUDA availability
python3 -c "import torch; print(torch.cuda.is_available())"

# Check Ollama GPU support
ollama show llama3.1:8b | grep -i gpu
```

### Solution (Windows)
1. **Install/Update NVIDIA Drivers:**
   - Download from https://www.nvidia.com/Download/index.aspx
   - Minimum driver version: 450.xx+

2. **Verify CUDA:**
   ```powershell
   # Check if CUDA is installed
   nvidia-smi
   # Look for "CUDA Version: XX.X"
   ```

3. **Reinstall Ollama:**
   - Download latest from https://ollama.ai/download
   - Ollama bundles CUDA libraries

### Solution (Linux)
```bash
# Install NVIDIA driver
sudo ubuntu-drivers autoinstall

# Or manual:
sudo apt install nvidia-driver-535

# Install CUDA toolkit (optional, Ollama bundles it)
sudo apt install nvidia-cuda-toolkit

# Reboot
sudo reboot

# Verify
nvidia-smi
```

---

## ❌ Problem 2: Out of Memory (OOM)

### Symptoms
- `RuntimeError: CUDA out of memory`
- Model loads then crashes
- GPU shows 100% memory usage

### Solution

**Option 1: Reduce GPU layers**
```bash
# Set number of GPU layers (lower = less VRAM)
ollama run llama3.1:8b --gpu-layers 20

# Or set in Modelfile
FROM llama3.1:8b
PARAMETER num_gpu 20
```

**Option 2: Use smaller model**
```bash
# 8B model requires ~6GB VRAM
# 3B model requires ~3GB VRAM
# 1B model requires ~2GB VRAM

ollama pull llama3.1:3b  # Smaller, faster
ollama run llama3.1:3b
```

**Option 3: Increase context offloading**
```bash
# Offload more to CPU
export OLLAMA_NUM_GPU=25  # Lower number
ollama serve
```

---

## ❌ Problem 3: Slow Performance Despite GPU

### Symptoms
- GPU is detected but model is slow
- GPU utilization is low (<50%)

### Solution

**1. Check GPU layers:**
```bash
# Increase GPU layers
export OLLAMA_NUM_GPU=35  # or higher (max 99)
ollama serve
```

**2. Optimize batch size:**
```bash
export OLLAMA_NUM_PARALLEL=2  # Parallel requests
export OLLAMA_MAX_LOADED_MODELS=1  # Don't keep multiple models
ollama serve
```

**3. Check thermal throttling:**
```bash
# Monitor GPU temperature
nvidia-smi -l 1  # Update every second

# If temp > 80°C, GPU may throttle
# Solution: Improve cooling, reduce fan curve
```

**4. Check power mode:**
```bash
# Linux: Set performance mode
sudo nvidia-smi -pm 1
sudo nvidia-smi -pl 250  # Set power limit (250W example)
```

---

## ❌ Problem 4: Multiple GPUs, Ollama Uses Wrong One

### Symptoms
- Have multiple GPUs (e.g., integrated + discrete)
- Ollama uses weaker GPU

### Solution
```bash
# Linux/Mac: Set GPU
export CUDA_VISIBLE_DEVICES=0  # Use first GPU
export CUDA_VISIBLE_DEVICES=1  # Use second GPU

# Windows (PowerShell):
$env:CUDA_VISIBLE_DEVICES="0"

# Check which GPU is #0, #1:
nvidia-smi -L
```

---

## ❌ Problem 5: "CUDA Driver Version is Insufficient"

### Symptoms
- Error: `CUDA driver version is insufficient for CUDA runtime version`

### Solution
```bash
# Check CUDA version needed by Ollama
# Usually printed in Ollama startup logs

# Update NVIDIA driver to match
# Driver version must be >= CUDA version

# Quick reference:
# CUDA 11.8 → Driver 450.80+
# CUDA 12.0 → Driver 525.60+
# CUDA 12.1 → Driver 530.30+

# Download and install newer driver:
# https://www.nvidia.com/Download/index.aspx
```

---

## ❌ Problem 6: Ollama Service Won't Start

### Symptoms
- `ollama serve` crashes immediately
- No GPU access from service

### Solution (Linux)
```bash
# Check if running as systemd service
systemctl status ollama

# If using systemd, ensure GPU access
sudo nano /etc/systemd/system/ollama.service

# Add to [Service]:
Environment="OLLAMA_NUM_GPU=35"
Environment="CUDA_VISIBLE_DEVICES=0"

# Reload and restart
sudo systemctl daemon-reload
sudo systemctl restart ollama
```

### Solution (Windows)
```powershell
# Run as admin
# Right-click Terminal → Run as Administrator
ollama serve
```

---

## ❌ Problem 7: Mixed Precision Errors

### Symptoms
- `RuntimeError: CUDA error: an illegal memory access was encountered`
- Random crashes

### Solution
```bash
# Disable FP16 (use FP32 instead)
export OLLAMA_FLASH_ATTENTION=0
ollama serve

# Or in Modelfile:
FROM llama3.1:8b
PARAMETER use_mmap false
```

---

## 🛠️ Optimization Tips

### 1. Optimal GPU Layer Count by VRAM

| VRAM | Recommended Layers | Model Size |
|------|-------------------|------------|
| 4GB  | 15-20            | 3B params  |
| 6GB  | 25-30            | 7-8B params |
| 8GB  | 30-35            | 7-8B params |
| 12GB | 35-40            | 13B params |
| 16GB+ | 40-45           | 20B+ params |

### 2. Environment Variables for Performance
```bash
# ~/.bashrc or ~/.zshrc (Linux/Mac)
# Or set in PowerShell profile (Windows)

export OLLAMA_NUM_GPU=35
export OLLAMA_NUM_THREAD=8
export OLLAMA_MAX_LOADED_MODELS=1
export OLLAMA_KEEP_ALIVE=5m
```

### 3. Model Selection by Use Case

| Use Case | Recommended Model | VRAM | Speed |
|----------|------------------|------|-------|
| Chat     | llama3.1:8b      | 6GB  | Good  |
| Code     | codellama:7b     | 6GB  | Fast  |
| Fast     | phi:3b           | 3GB  | Very Fast |
| Quality  | mixtral:8x7b     | 12GB | Slow  |

---

## 📋 Pre-flight Checklist

Before running Ollama with GPU:

- [ ] NVIDIA driver installed and up to date
- [ ] `nvidia-smi` command works
- [ ] At least 6GB VRAM available
- [ ] Ollama latest version installed
- [ ] Sufficient RAM (2x model size)
- [ ] GPU not being used by other apps

---

## 🔗 Related Resources

- [[skills/03-infrastructure-mcp/local-llm-ops|Local LLM Ops]] — Ollama optimization
- [[JARVIS/02-Operational/Config/ENV-Registry|ENV Registry]] — Environment variables
- [Ollama Documentation](https://github.com/ollama/ollama/blob/main/docs/gpu.md)

---

## 📞 Still Stuck?

1. Check Ollama logs:
   ```bash
   # Linux
   journalctl -u ollama -f
   
   # Windows
   # Check terminal where 'ollama serve' is running
   ```

2. Check GitHub issues: https://github.com/ollama/ollama/issues
3. Test with smallest model: `ollama run phi:3b`
4. Try CPU-only mode to rule out GPU issues:
   ```bash
   export OLLAMA_NUM_GPU=0
   ollama serve
   ```

---

*Keep this updated as you encounter and solve GPU issues*

[[JARVIS/README|← Voltar ao Command Center]]
