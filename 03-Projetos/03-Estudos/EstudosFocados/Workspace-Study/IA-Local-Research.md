---
title: "IA Local Research"
description: "Pesquisa de IA local para Jarvis, incluindo voz, visão, RAG, Ollama e arquitetura offline." 
tags: [ia, jarvis, pesquisa, local, projetos]
updated: 2026-06-10
date: 2026-04-27
---

# IA Local Research

## Objetivo
Documentar o estado da pesquisa de IA local no vault e sugerir prioridades de estudo para Jarvis, IA-LOCAL e DEEP-LEARNING.

## Componentes chave

- `Projetos/EstudosFocados/IA-LOCAL.md`
  - Visão do assistente local com voz, memória e automação de PC.
  - Prioriza privacidade offline e modularidade segura.

- `Projetos/EstudosPesquisas/AI-Local-Gratuita.md`
  - Ferramentas e stack sugeridas: Ollama, Whisper, Piper / Coqui, FAISS, MediaPipe.
  - Enfoque em soluções gratuitas e modelos locais.

- `Projetos/EstudosFocados/DEEP-LEARNING.md`
  - Caso de uso de RAG e fine-tuning PT-BR como base para Jarvis e automações.

## Tecnologias e prioridades

1. **LLM local**
   - Ollama como prioridade.
   - Modelos `llama3.2` e `qwen2.5-coder` para general e código.

2. **Speech2Text local**
   - Whisper offline com modelos tiny/base/small.
   - Validação de latência e acurácia.

3. **Text2Speech PT-BR**
   - Piper e Coqui para voz local de baixa latência.

4. **Memória RAG**
   - FAISS + sentence-transformers para indexação local.
   - Usar RAG para histórico de sessões e contexto de notas.

5. **Visão leve**
   - MediaPipe para face/gesture.
   - Avaliar YOLOv8 nano para reconhecimento de objetos.

## Gaps identificados

- Dependência de LLMs externos em `IA-LOCAL` e `PROJECT_JARVIS_5.0`.
- Pipeline de voz não consolidado: Whisper → faster-whisper → Piper.
- Falta de documentações de segurança e auditoria de automações de PC.
- Ausência de benchmark de latência para modelos em hardware alvo.

## Próximas perguntas de pesquisa

- Qual é o mínimo de hardware para rodar `llama3.2` e Piper com latência aceitável?
- Como segmentar dados sensíveis dentro de logs e memória RAG?
- Qual é a arquitetura ideal para separar comando de voz e automação segura?
- Em que momento a visão adiciona valor real vs custo de complexidade?

## Próximas ações sugeridas

- Testar Ollama local e registrar tempo de inferência.
- Executar benchmark de Whisper tiny/base/small na máquina atual.
- Criar protótipo de memória RAG com FAISS e um conjunto de notas do vault.
- Documentar um fluxo de automação PC com controles reversíveis.
- Definir critério de aceitação para o MVP IA local.

## Guia prático de execução

1. Abra `Projetos/EstudosFocados/IA-LOCAL.md` e `Projetos/EstudosPesquisas/AI-Local-Gratuita.md`.
2. Crie um script de benchmark local em `Workspace-Study/Benchmark-IA-Local.md`.
3. Liste as métricas mínimas: latência, uso de CPU/RAM, qualidade da voz e estabilidade da memória.
4. Rode os testes em um hardware alvo e registre os resultados em uma tabela.
5. Extraia conclusões sobre a viabilidade do Jarvis offline.

## Links de referência
- [[03-Projetos/03-Estudos/EstudosFocados/IA-LOCAL|IA-LOCAL (Estudos Focados)]]
- [[03-Projetos/03-Estudos/EstudosPesquisas/AI-Local-Gratuita|AI Local Gratuita]]
- [[03-Projetos/03-Estudos/EstudosFocados/DEEP-LEARNING|DEEP-LEARNING]]
