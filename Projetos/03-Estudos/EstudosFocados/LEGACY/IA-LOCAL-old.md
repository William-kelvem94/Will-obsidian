---
title: "Estudos Focado: IA-LOCAL (JARVIS)"
description: "Documento estratégico para IA-LOCAL: visão Jarvis, trade-offs offline/online, voz, visão e automação PC." 
tags:
  - jarvis
  - projetos
  - analise
  - estrategia
  - voz
  - vision
date: 2026-04-27
updated: 2026-06-05
---

# Estudos Focado: IA-LOCAL [[README]] [[Privados/IA-LOCAL]]

**Quartel-General da Estratégia**
- Esta nota define a visão Jarvis local antes de migrar para implementação.
- Esta pasta responde: qual é o Jarvis mínimo viável e onde ele adiciona valor hoje.
- Pesquisa técnica: [[../EstudosPesquisas/README|Estudos e Pesquisas]].

## Missão do projeto
Construir um assistente pessoal local que entenda voz, mantenha memória e possa executar ações no PC com segurança.

## Proposta de valor
- Para usuários individuais: ter um Jarvis local que possa administrar tarefas, notas e automações sem depender inteiramente de nuvem.
- Para o vault: criar um template de assistente offline que pode ser replicado em outros projetos.

## Público e casos de uso
**Usuário primário**
- usuário power user que quer automações de PC e notas com voz.

**Casos de uso**
- ditado de notas e comandos de ação.
- busca de lembretes e histórico de sessões.
- execução de macros ou automações simples no desktop.

## Métricas de sucesso
- Tempo para converter speech-to-text < 3s.
- Taxa de reconhecimento de comando > 85%.
- Máximo de 5 falhas de automação por fluxo de 10 minutos.
- Capacidade de rodar offline em hardware de laptop médio.

## Hipóteses estratégicas
- Usuários aceitam menos recursos mas preferem privacidade/offline.
- Um motor local Ollama ou LLaMA 3.2:3b é viável para o MVP.
- Voice + memory são mais valiosos que visão inicialmente.
- A automação de PC deve ser modular e segura.

## Situação atual
- Core existente com FAISS, Whisper, pyautogui e OpenRouter.
- Problema: dependência de LLM externo e performance de Whisper.
- Gap: visão e multi-modalidade não consolidados.

## Arquitetura estratégica
- `core/` = gerenciamento de memória e agente.
- `interfaces/` = voz, comando e PC control.
- `models/` = configuração de LLM local ou remota.
- `security/` = limites de automação e logs.

## Roadmap estratégico
### Fase 1 — Jarvis offline minimal (4 semanas)
- Substituir OpenRouter por Ollama local ou modelo compatível.
- Mudar Whisper para faster-whisper e Piper TTS PT-BR.
- Testar comandos básicos e logs de auditoria.

### Fase 2 — Visão e OCR leve (8 semanas)
- Implementar MediaPipe face/gesture e OCR de tela.
- Adicionar detecção de contexto de tela para comandos mais inteligentes.
- Criar feedback visual de ações.

### Fase 3 — Autonomia segura (16 semanas)
- Integrar LangGraph ou agentes multi-step.
- Tornar automações de PC seguras e reversíveis.
- Adicionar política de consentimento e logs de segurança.

## Dependências e decisões
- LLM offline: Ollama vs outros formatos.
- TTS: Piper é prioridade para PT-BR.
- Visão: MediaPipe versus visão embarcada leve.
- Automação PC: pyautogui vs pydirectinput.

## Riscos
- Comandos de PC podem causar ações indesejadas.
- Whisper CPU lento impacta usabilidade.
- Offline LLM pode ser pesado para laptops fracos.
- Visão adiciona complexidade de teste e performance.

## Decisões pendentes
- Focar voice+memory primeiro ou lançar visão paralela?
- Usar modelo local grande ou modelo menor quantizado?
- Como separar claramente dados pessoais e logs de comando?

## Diário de Bordo
- 09/04/2026 10:56:40 — nota criada com visão de Jarvis local.
- 09/04/2026 10:56:43 — roadmap de fases montado.

## Próximas ações imediatas
- Testar inferência local do modelo escolhido e medir latência.
- Atualizar o pipeline de voz para faster-whisper e Piper.
- Projetar um fluxo seguro de automação de PC.
- Criar um documento de segurança para automações.

## Referências
- [[../EstudosPesquisas/IA-LOCAL|Pesquisa IA-LOCAL]]
- [[../EstudosPesquisas/AI-Local-Gratuita|AI Local Gratuita]]
- [[../Plano-de-Acao|Plano de Ação]]
