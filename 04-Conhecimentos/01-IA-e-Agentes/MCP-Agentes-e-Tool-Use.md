---
title: "MCP, Agentes e Uso Seguro de Ferramentas"
updated: 2026-07-10
type: architecture
status: active
tags: [mcp, agentes, ferramentas, seguranca, automacao]
indexavel: true
uso_ia: livre
related: [[Model-Context-Protocol-MCP]], [[../00-Mapas-e-Ontologia/Engenharia-de-Conhecimento-para-Segundo-Cerebro]]
---

# Modelo operacional

MCP padroniza a conexão entre host, cliente e servidores que expõem recursos, prompts e ferramentas. O protocolo resolve interoperabilidade; não resolve autorização, qualidade ou segurança automaticamente.

## Ciclo seguro

`descobrir → inspecionar schema → estimar risco → pedir confirmação quando necessário → executar → validar resultado → registrar proveniência`.

## Classes de ação

| Classe | Exemplo | Política |
|---|---|---|
| leitura | buscar nota | automática se autorizada |
| cálculo | gerar índice | automática e verificável |
| proposta | sugerir alteração | requer revisão |
| escrita reversível | criar nota | confirmar escopo |
| escrita canônica | alterar `main` | confirmação e validação |
| destrutiva | apagar ou publicar | bloqueada por padrão |

## Guardrails

Validar argumentos, limitar escopo, separar dados privados, registrar ferramenta e resultado, tratar conteúdo externo como não confiável e nunca conceder poder maior que o necessário.

## Aplicação

No WILL-OBSIDIAN, pesquisa pode ler fontes e propor notas; publicação deve passar por validação de links, frontmatter, privacidade, diff e commit. O servidor MCP não substitui esse contrato.

## Referências oficiais

- [Introdução ao MCP](https://modelcontextprotocol.io/docs/getting-started/intro)
- [Especificação MCP](https://modelcontextprotocol.io/specification/2025-11-25)
- [Ferramentas MCP](https://modelcontextprotocol.io/specification/2025-11-25/server/tools)
