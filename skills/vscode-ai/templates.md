# Templates de Prompt — VS Code AI

Use estes modelos como base para criar prompts consistentes e reutilizáveis.

## Template de refatoração
"Você é um assistente de desenvolvimento. Aqui está o arquivo: [caminho].
Meu objetivo é: [objetivo].
Por favor:
1. Identifique problemas.
2. Sugira melhorias.
3. Aplique mudanças no arquivo.
4. Explique o que mudou e por quê."

## Template de correção de bug
"Você é um analista de código. O arquivo `path/to/file` tem o seguinte problema: [descrição do erro].
Por favor:
- localize a raiz do problema,
- corrija o código,
- explique a correção e quais testes precisam ser adicionados."

## Template de documentação
"Você é um gerador de documentação técnica.
- Projeto: [nome do projeto]
- Arquivo/função: [contexto]
- Objetivo: [descrever função, uso, deploy, arquitetura]
Crie uma seção clara para README com exemplos de uso e comandos principais."

## Template de criação de testes
"Você é um criador de testes.
- Função/rota: [nome]
- Cenários: [validação de entradas inválidas, autenticação, erros esperados]
Gere testes unitários e integração suficientes para cobrir os casos principais."

## Template de arquitetura de IA local
"Você é um arquiteto de IA.
- Projeto: [nome do projeto]
- Requisitos: [voz, visão, RAG, memória]
Descreva uma arquitetura modular, incluindo componentes de ingestão, embeddings, busca semântica e memória persistente."

## Template de fluxo MCP
"Use este fluxo:
1. `search_files` para encontrar [arquivo ou pasta].
2. `read_file` para entender o contexto.
3. `edit_file` para fazer a mudança.
4. `execute_command` para validar.
5. `summarize` as alterações."
}