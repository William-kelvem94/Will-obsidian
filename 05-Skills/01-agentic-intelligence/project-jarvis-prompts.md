---
tags: [skills, skills-ai, jarvis, prompts, agent]
updated: 2026-06-10
title: "Prompts para PROJECT_JARVIS_5.0"
date: 2026-06-01
---

# Prompts para PROJECT_JARVIS_5.0

Este arquivo contem prompts focados no projeto `PROJECT_JARVIS_5.0`, com enfase em IA local, RAG, memoria e integracao de sistemas. Cada secao inclui templates de system prompt, exemplos few-shot e definicoes de persona.

## Persona JARVIS — System Prompt Base

```
Voce e JARVIS, um assistente de IA autonomo especializado em desenvolvimento de software.
- Seu ambiente: Windows 11, VS Code, Python 3.12, Node.js 20.
- Sua base de conhecimento: vault Obsidian com documentos, decisoes e memorias.
- Seu estilo: tecnico, direto, objetivos. Responda em portugues brasileiro.
- Ferramentas disponiveis: MCP tools (search_files, read_file, edit_file, create_file, execute_command).
- Regra principal: SEMPRE leia o contexto antes de editar. SEMPRE valide apos alterar.
```

## Templates de System Prompt por Contexto

### Prompt de Arquitetura e Visao
```
Descreva a arquitetura ideal de PROJECT_JARVIS_5.0 considerando:
- Backend: Python com FastAPI
- Frontend: Next.js 14 com TypeScript
- Memoria local: Obsidian Vault com embeddings FAISS
- Modelo local: Ollama (Mistral ou Llama 3)
- Voz: Whisper local para STT e TTS
- Visao: Moondream ou LLaVA para analise de imagens

Formato de saida: diagrama ASCII + lista de componentes + fluxo de dados.
```

### Prompt de Pipeline de Memoria
```
Explique um pipeline de ingestao para o Vault Obsidian:
1. Leitura de notas markdown do vault
2. Chunking semantico (por cabecalho ou por tamanho)
3. Geracao de embeddings com modelo local (ex: all-MiniLM-L6-v2)
4. Armazenamento em banco vetorial FAISS com metadados
5. Indice de busca hibrida (vetorial + BM25)

Inclua codigo Python para cada etapa.
```

### Prompt de Desenvolvimento Backend
```
Crie um endpoint FastAPI que:
- Receba texto do usuario via POST /api/chat
- Gere embeddings com sentence-transformers
- Execute busca semantica no FAISS
- Retorne os top-3 documentos relevantes
- Inclua tratamento de erro e logging

Exemplo de resposta esperada:
{
  "query": "como funciona a memoria do jarvis?",
  "results": [
    {"document": "memory-architectures.md", "score": 0.92, "snippet": "A memoria episodica..."},
    ...
  ]
}
```

### Prompt de Frontend
```
Projete um componente de chat em Next.js que:
- Exiba historico de conversa com bolhas de mensagem
- Suporte entradas de texto e voz (microfone)
- Mostre indicador de carregamento durante processamento
- Exiba fontes dos resultados de busca semantica
- Lide com erros de conexao graciosamente

Use Tailwind CSS para estilizacao e TypeScript para tipagem.
```

### Prompt de Testes e Validacao
```
Gere casos de teste para o pipeline de memoria do Jarvis:
- Teste de insercao: adicionar documento, verificar se embedding foi gerado
- Teste de busca: consultar por termo similar, verificar relevancia
- Teste de integracao: enviar pergunta via API, verificar resposta com contexto
- Teste de erro: enviar payload invalido, verificar status 422

Use pytest com fixtures para simular documentos do Obsidian.
```

### Prompt de Documentacao
```
Crie uma secao "Como funciona" para o README de PROJECT_JARVIS_5.0:
1. Fluxo de entrada: voz ou texto -> API -> agente
2. Processamento: analise de intencao -> selecao de skill -> execucao
3. Memoria: busca semantica no vault -> injecao no contexto
4. Saida: geracao de resposta -> formatacao -> exibicao

Inclua diagrama ASCII do fluxo completo.
```

### Prompt de Melhoria Continua
```
Sugira 5 melhorias de curto prazo para tornar o Jarvis mais confiavel:
1. Cache de embeddings para reducao de latencia
2. Circuit breaker para chamadas de API externas
3. Logging estruturado com JSON para debugging
4. Testes de ponta a ponta para o fluxo critico
5. Monitoramento de uso de tokens e limites de contexto

Para cada melhoria, estime esforco (horas) e impacto (alto/medio/baixo).
```

## Exemplos Few-Shot para JARVIS

### Exemplo 1: Diagnostico de Projeto
```
Usuario: "Analise a estrutura do projeto e identifique problemas."
JARVIS: {
  "analise": {
    "componentes_principais": ["backend FastAPI", "frontend Next.js", "memoria FAISS"],
    "arquivos_criticos": ["app/main.py", "components/Chat.tsx", "memory/vector_store.py"],
    "riscos": [
      "Falta de tratamento de erro no pipeline de embedding",
      "Ausencia de testes de integracao no fluxo de voz"
    ]
  },
  "acoes_recomendadas": ["Adicionar try/except em vault_memory.py", "Criar test_chat_pipeline.py"]
}
```

### Exemplo 2: Correcao de Bug
```
Usuario: "O endpoint /api/chat esta retornando 500."
JARVIS: "1. Lendo arquivo app/routes/chat.py... 2. Identificando erro na linha 42: variavel 'query' nao definida quando o corpo da requisicao esta vazio. 3. Corrigindo com validacao previa. 4. Testando com pytest."
```

## Referencias

- [[direct-agent-prompts]] — Prompts prontos para copiar no chat.
- [[memory-architectures]] — Arquiteturas de memoria para agentes.
- [[programador.agent]] — Agente especializado em desenvolvimento.
- [[prompts]] — Biblioteca de templates de prompt.
