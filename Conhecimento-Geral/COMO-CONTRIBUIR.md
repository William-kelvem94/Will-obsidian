---
title: "Como Contribuir para a Base de Conhecimento"
tags: [meta, kb, agente]
---

# 🧠 Diretrizes para Expansão da Knowledge Base

1. Use o template `Templates/Conceito-Conhecimento.md` em `Templates/`.
2. Escolha um conceito que complemente as áreas existentes.
3. Preencha todos os campos YAML.
4. Link para pelo menos 3 outros conceitos ([[link]]).
5. Rode `python .scripts/knowledge_indexer.py` para atualizar os embeddings.
6. Valide a busca semântica usando o servidor MCP.
