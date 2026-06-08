---
title: "Sistemas Sensoriais e Percepção — JARVIS 5.0"
description: "Detalhamento técnico de como o Jarvis vê, ouve e sente o ambiente através de hardware local."
tags: [jarvis, percepcao, visão, voz, biometria, engenharia, jarvis-engenharia]
updated: 2026-06-07
date: 2026-04-27
---

# Sistemas Sensoriais e Percepção 🧠👁️🎙️

O JARVIS 5.0 não é apenas um chatbot; ele é uma entidade **multimodal local**. Esta nota detalha o funcionamento técnico dos seus "sentidos".

## 1. O Sistema Nervoso: `PerceptionManager`
Toda a percepção é centralizada no `backend/app/perception/perception_manager.py`. Ele orquestra três motores principais em threads separadas para garantir latência zero na interação.

### 🧵 Gerenciamento de Threads
- **Thread de Câmera**: Captura frames (padronizado em 640x480, ~1 FPS para economia de CPU).
- **Thread de Voz**: Escuta constante via `sounddevice` para o Wake Word offline.
- **Thread de Eventos**: Notifica o agente quando algo relevante acontece (ex: Will entrou na sala).

---

## 2. Visão Computacional (`face_engine` & `gesture_engine`)
A visão é processada via **OpenCV** e **MediaPipe**.

### 👤 Identidade e Emoção
- **Reconhecimento Facial**: Utiliza `DeepFace` ou `Face_Recognition` local para identificar o @kelvem94.
- **Análise de Sentimentos**: Detecta 7 estados emocionais (Raiva, Nojo, Medo, Felicidade, Tristeza, Surpresa, Neutro).
- **Uso**: O Jarvis ajusta o tom da resposta baseado no humor detectado. Se você estiver frustrado, ele será mais direto e técnico.

### ✋ Gestos e Controle
- **Gestos de Mão**: `fist`, `open_palm`, `point`, `thumbs_up`, `thumbs_down`.
- **Ações Proativas**:
    - `Thumbs Up`: Pode confirmar uma ação sugerida sem precisar de comando de voz.
    - `Point`: Indica ao Jarvis para qual monitor ou janela ele deve olhar.

---

## 3. Audição e Biometria Vocal (`voice_engine`)
O sistema de áudio é otimizado para o hardware do **Book2 360**.

### 🎙️ Processamento de Áudio
- **Wake Word**: `Hey Jarvis` processado via `OpenWakeWord` (16kHz).
- **VAD (Voice Activity Detection)**: Ignora ruídos de fundo e só processa quando há fala humana real.
- **Biometria Vocal**: Identifica o usuário pelo timbre de voz, mesmo que ele esteja de costas para a câmera.

---

## 4. Integração de Contexto (Contexto Sensorial)
A cada mensagem enviada ao LLM, o Jarvis injeta um **Snapshot de Percepção**:

```json
{
  "falante": "William",
  "confianca_voz": 0.98,
  "emocao": "Focado/Neutro",
  "face_presente": true,
  "gesto": "pointing",
  "timestamp": "2026-04-14T14:55:00"
}
```

Isso permite que o Jarvis responda coisas como: *"Entendido, Will. Estou vendo que você está apontando para o terminal, vou analisar o erro para você."*

---

## 5. Limitações e Safe-Guards
- **Privacidade**: Todo o processamento visual e auditivo é **100% Offline**. Nada é enviado para a nuvem.
- **Performance**: O FPS da câmera é ajustado dinamicamente via `JARVIS_PERCEPTION_FPS`. Se a CPU esquentar, o Jarvis "pisca" mais devagar.

[[02-JARVIS/JARVIS/README|← Voltar ao Command Center]]
