---
title: "Ecossistema e Protocolos MCP"
description: "Guia de arquitetura e governança para expor ferramentas do vault a agentes via MCP/local API com segurança e rastreabilidade."
tags: [mcp, ferramentas, agentes, automacao, engenharia, jarvis, jarvis-engenharia]
date: 2026-05-20
updated: 2026-06-10
---

# Ecossistema e Protocolos MCP

Esta nota organiza a visão de MCP no JARVIS e complementa [[MCP-Client-Examples]]. Os exemplos mostram chamadas; aqui o foco é arquitetura, expansão e governança.

## Papel do MCP no JARVIS

O MCP atua como camada de ferramentas entre agentes/LLMs e o vault. Ele deve reduzir acesso direto e desorganizado aos arquivos, oferecendo operações controladas como:

- ler arquivo permitido;
- buscar notas;
- consultar grafo ou metadados;
- acionar scripts locais;
- validar uma ação antes de escrita.

No desenho geral, ele conversa com [[Arquitetura-Agente]] e com o pipeline de [[RAG-Local-Guide]].

## Princípio central

> Agente não deve ter acesso ilimitado ao vault inteiro quando uma ferramenta específica resolve a tarefa.

Em vez de “deixe o agente abrir tudo”, prefira ferramentas pequenas, auditáveis e com escopo claro.

## Camadas recomendadas

```text
LLM/agente
  ↓
cliente MCP ou adaptador local
  ↓
ferramentas: read/search/graph/write/validate
  ↓
políticas: permissões, paths, sensibilidade, logs
  ↓
vault, scripts e índices
```

## Catálogo mínimo de ferramentas

| Ferramenta | Função | Risco | Controle recomendado |
|---|---|---|---|
| `read_vault_file` | Ler uma nota específica | Baixo/médio | Bloquear paths sensíveis |
| `search_vault` | Buscar notas ou trechos | Médio | Filtrar dados sensíveis |
| `vault_graph_query` | Consultar links e relações | Baixo | Retornar metadados, não conteúdo inteiro |
| `write_vault_file` | Criar/substituir nota | Alto | Exigir confirmação e diff |
| `edit_vault_file` | Alterar trecho | Alto | Exigir arquivo lido, diff pequeno e backup |
| `run_automation` | Acionar scripts | Alto | Allowlist de scripts |

Use nomes reais do servidor quando confirmados; esta tabela é um modelo de governança, não uma garantia de implementação atual.

## Como expandir com segurança

Antes de adicionar uma nova ferramenta:

1. descreva o caso de uso;
2. defina entradas e saídas;
3. limite paths permitidos;
4. defina se pode ler, escrever ou executar;
5. registre erros esperados;
6. adicione exemplo de uso;
7. teste com arquivo não sensível;
8. documente em nota técnica.

## Padrão de resposta das ferramentas

Uma resposta útil para agentes deve conter:

```json
{
  "ok": true,
  "tool": "read_vault_file",
  "path": "02-JARVIS/04-Engineering/RAG-Local-Guide.md",
  "summary": "Guia básico de RAG local com FAISS e all-MiniLM-L6-v2.",
  "content": "...",
  "warnings": []
}
```

Para escrita, inclua:

- arquivo afetado;
- diff ou resumo do diff;
- validações executadas;
- aviso se o arquivo contém frontmatter sensível.

## Logs e auditoria

Nem todo servidor registra automaticamente tudo. A política recomendada é:

- registrar chamadas de escrita;
- registrar acesso a arquivos sensíveis;
- evitar logar conteúdo completo quando houver dado privado;
- rotacionar logs grandes;
- separar log operacional de conhecimento curado.

Logs são evidência operacional, não fonte primária de conhecimento.

## Segurança de paths

Toda ferramenta que recebe caminho deve prevenir:

- `../` para sair do vault;
- leitura de `.env`, tokens e chaves;
- acesso a caches e logs privados;
- escrita acidental em diretórios de configuração;
- sobrescrita de notas sem diff.

## Fluxo recomendado para ações de escrita

```text
search/read → plano → diff proposto → confirmação → escrita → validação → git diff/status
```

Esse fluxo evita perda de informação e combina com [[Seguranca-e-Governanca-LocalFirst]].

## Integração com agentes cooperativos

Em uma arquitetura multiagente:

- exploradores usam apenas leitura/busca;
- executores recebem escopo de escrita por arquivo;
- verificadores usam diff/status e leitura;
- coordenador decide commit/push.

Veja também [[Arquiteturas-Cooperativas-de-Agentes]].

## Links relacionados

- [[MCP-Client-Examples]]
- [[Arquitetura-Agente]]
- [[RAG-Local-Guide]]
- [[RAG-Avancado-Playbook]]
- [[Seguranca-e-Governanca-LocalFirst]]
- [[Privacidade-by-Default-para-Agentes]]
