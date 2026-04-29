---
title: "Arquitetura de Memória para Agentes: Episódica, Semântica e Trabalho"
description: "Guia profundo sobre como estruturar a memória de longo e curto prazo para que agentes IA mantenham consistência de identidade e contexto."
tags: [agentic, memory, rag, context, arquitetura, skills-ai]
date: 2026-04-27
updated: 2026-04-29
---

# 🧠 Arquitetura de Memória para Agentes Autônomos

A memória é o que diferencia um "chatbot de sessão única" de um "agente autônomo contínuo" como o JARVIS. A arquitetura correta simula a cognição humana através de três pilares: Memória de Trabalho, Memória Semântica e Memória Episódica.

## 1. Memória de Trabalho (Working Memory / Curto Prazo)

A memória de trabalho é o **Context Window** (Janela de Contexto) atual da LLM.

- **Definição:** Tudo o que está imediatamente acessível ao modelo durante a interação (histórico de chat recente, o prompt do sistema ativo, variáveis de ambiente lidas recentemente).
- **Desafios:** Limitação de tokens (ex: 128k para Claude 3, 8k/32k para modelos locais como Llama 3).
- **Gerenciamento:**
  - **Summarization:** Quando o contexto fica longo, um sub-agente resume a conversa antiga e a injeta como um bloco condensado.
  - **Context Pruning:** Remoção ativa de logs de erro ou saídas de ferramentas gigantes após sua utilidade passar.

## 2. Memória Semântica (Conhecimento Factual)

A memória semântica armazena "fatos do mundo" e conhecimentos aprendidos ao longo do tempo. É o núcleo do RAG (Retrieval-Augmented Generation).

- **Definição:** Fatos, conceitos, arquiteturas de projeto, regras de negócio e documentações (como os arquivos deste repositório `Vault`).
- **Implementação Técnica:**
  - Banco de Dados Vetorial (ChromaDB, FAISS, Pinecone).
  - *Embeddings*: Textos divididos em chunks (blocos) e convertidos em vetores matemáticos para busca semântica (`text-embedding-3-small` ou embeddings locais `all-MiniLM-L6-v2`).
- **Busca Híbrida:** Uso de Vector Search (para similaridade semântica) + BM25/Keyword Search (para encontrar nomes exatos de variáveis e arquivos).
- **No JARVIS:** O `KnowledgeBase` inteiro é a memória semântica dele.

## 3. Memória Episódica (Experiência e Autobiografia)

A memória episódica registra *eventos* no tempo. É o que permite que o agente se lembre de *como* resolveu um problema no passado ou das interações anteriores com o usuário.

- **Definição:** O "diário" do agente. Sequências de eventos (Timestamp, Contexto, Ação, Resultado).
- **Uso Crítico:** Evitar repetição de erros (Reflexion). Ex: "Na semana passada tentei instalar o pacote X no Ubuntu 22.04 e falhou por causa do Python 3.12, então eu devo usar Python 3.10."
- **Implementação Técnica:**
  - Logs estruturados (JSON) de interações e sessões.
  - Extração de *Insights*: Periodicamente (ex: no final do dia), um agente offline lê os logs da sessão, extrai "lições aprendidas" e as insere na memória semântica ou no perfil do usuário.

## Fluxo Cognitivo Integrado

1. **Gatilho:** Usuário faz uma requisição.
2. **Retrieval (Recall):**
   - Agente busca na *Memória Semântica* por fatos relacionados.
   - Agente busca na *Memória Episódica* por experiências passadas parecidas.
3. **Injeção:** Esses dados são formatados e injetados na *Memória de Trabalho* (Prompt).
4. **Geração:** O LLM responde ou age.
5. **Consolidação:** Após a tarefa, as novas lições são gravadas nas memórias de longo prazo.
