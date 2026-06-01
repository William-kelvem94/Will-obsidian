---
title: "Benchmark IA Local"
description: "Plano de benchmark para avaliar Ollama, Whisper, Piper, RAG e desempenho do vault em hardware local." 
tags: [ia, benchmark, local, pesquisa, projetos]
updated: 2026-06-01
date: 2026-04-27
---

# Benchmark IA Local

## Objetivo
Executar um conjunto prático de testes para medir desempenho de IA local no vault e gerar dados reais que guiem decisões de arquitetura.

## Escopo
- inferência de LLM local (`Ollama`, `llama3.2`, `qwen2.5-coder`)
- speech-to-text local (`Whisper`, `faster-whisper`)
- text-to-speech PT-BR (`Piper`, `Coqui`)
- indexação/memória local (`FAISS`, `sentence-transformers`)
- visão leve (`MediaPipe`, `YOLOv8 nano`)

## O que medir
- latência de inferência por token / prompt
- throughput de texto e voz por segundo
- uso de CPU/RAM durante cada teste
- tamanho do modelo e tempo de carregamento
- qualidade de saída mínima aceitável

## Ambiente de teste
1. Abra o vault em VS Code.
2. Crie virtualenv se ainda não houver:
   ```powershell
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1
   python -m pip install --upgrade pip
   ```
3. Instale dependências de benchmark:
   ```powershell
   pip install ollama openai-whisper faster-whisper TTS sentence-transformers faiss-cpu mediapipe
   ```
4. Prepare um conjunto simples de prompts e áudios de teste.

## Testes de LLM local

### 1. Inferência básica com Ollama
- Instale e rode Ollama:
  ```powershell
  curl -fsSL https://ollama.com/install.sh | sh
  ollama pull llama3.2
  ```
- Execute um prompt simples e meça o tempo:
  ```powershell
  Measure-Command { ollama run llama3.2 --prompt "Explique em 3 frases como funciona RAG." }
  ```
- Registre:
  - latência total
  - tamanho do modelo
  - CPU/RAM usados

### 2. Comparar modelos de Ollama
- `llama3.2`
- `qwen2.5-coder`
- `gpt4o-mini`
- `mistral` (se disponível localmente)

### 3. Prompt de código
- Teste um prompt de análise de código para ver desempenho em `openclaude-wk` ou `Projetos/Privados/openclaude-wk.md`.

## Testes de voz

### 1. Whisper local
- Execute:
  ```powershell
  python -m whisper transcribe --model tiny sample_audio.wav
  ```
- Meça tempo e acurácia.
- Compare com `base` e `small`.

### 2. faster-whisper
- Instale e execute um mesmo arquivo com `faster-whisper`.
- Compare latência e acurácia.

### 3. Piper / Coqui TTS PT-BR
- Exemplo de uso Piper:
  ```powershell
  python -c "from TTS.utils.manage import ModelManager; manager = ModelManager(); model_path = manager.download_model('tts_models/pt/br/piper'); print(model_path)"
  ```
- Meça o tempo para converter texto em áudio.

## Testes de memória RAG

### 1. Indexar notas do vault
- Selecione 50 notas do vault como dataset.
- Execute um script de indexação com `sentence-transformers` e `faiss-cpu`.
- Verifique tempo de inserção e busca.

### 2. Consulta de similaridade
- Faça buscas por 3 perguntas de exemplo.
- Meça tempo de resposta e qualidade dos resultados.

## Testes de visão

### 1. MediaPipe
- Execute um script simples de detecção de rosto/gesto.
- Verifique latência por frame e taxa de detecção.

### 2. YOLOv8 nano
- Se houver ambiente de visão, teste um modelo leve para detecção de objetos.

## Exemplo de métricas registradas
| Teste | Modelo / Ferramenta | Latência | CPU | RAM | Observação |
|---|---|---|---|---|---|
| LLM inferência | Ollama llama3.2 | 2.3s | 45% | 4.2GB | prompt geral |
| Whisper tiny | Speech2Text | 1.8s | 35% | 2.1GB | boa acurácia |
| Piper TTS | TTS PT-BR | 0.9s | 25% | 1.8GB | voz natural |

## Resultado esperado
- Um relatório simples com números paginados.
- Decisão sobre modelo local viável para Jarvis.
- Indicação clara do ponto de ruptura entre desempenho e custo.

## Próximo passo
- Salvar resultados em `Projetos/EstudosFocados/Workspace-Study/Benchmark-IA-Local.md`.
- Comparar com `Projetos/EstudosFocados/IA-LOCAL.md` e `openclaude-wk`.
- Atualizar `Workspace-Analysis` com conclusões reais.
