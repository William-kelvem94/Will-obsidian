---
title: "Registro de MCPs"
date: 2026-06-10
updated: 2026-06-10
type: analysis
status: active
tags: [mcp, registry, tools, security, automation]
summary: "Catalogo operacional dos MCPs atuais e planejados, com risco, escrita, sensibilidade e contrato."
---

# Registro de MCPs

## MCP atual

| Nome | Proposito | Transporte | Auth | Leitura | Escrita | Sensibilidade | Status |
|---|---|---|---|---|---|---|---|
| `will-obsidian-vault` | operar o vault local | `stdio` | local trusted process | arquivos markdown do vault | sim, com path safety | media | ativo |

## MCPs planejados

| Nome | Proposito | Transporte | Auth | Leitura | Escrita | Sensibilidade | Status |
|---|---|---|---|---|---|---|---|
| `filesystem-mcp` | operar arquivos fora do vault com allowlist | `stdio` ou `http` local | local / token | sim | sim, com allowlist | media-alta | planejado |
| `browser-mcp` | automatizar navegador para tarefas locais | browser bridge | sessao local | sim | sim via UI | media | planejado |
| `github-mcp` | issues, PRs, reviews e repos | connector/API | OAuth/PAT | sim | sim, escopos restritos | media | planejado |
| `analytics-mcp` | consultas, dashboards e reportes | `stdio`/API | token local | sim | sim, com auditoria | media | planejado |
| `docs-mcp` | docx, slides e artefatos documentais | local bridge | local/trusted | sim | sim | media | planejado |
| `search-mcp` | busca lexical e semantica no vault | `stdio`/API | local | sim | opcional | baixa-media | planejado |
| `code-intel-mcp` | mapear simbolos, repos e dependencias | API local | token | sim | opcional | media | planejado |
| `workflow-orchestrator-mcp` | compor fluxos entre tools | `stdio`/API | local + tokens | sim | sim, com logs | alta | planejado |

## Contratos de ferramenta

Cada MCP deve declarar:

- nome e versao;
- transporte;
- politica de autenticacao;
- lista de tools;
- leitura e escrita permitidas;
- allowlist/denylist de caminhos ou recursos;
- nivel de sensibilidade;
- logs e auditoria;
- modo de falha;
- testes de integridade.

## Politica de seguranca

1. Tool com escrita soh entra com limite de escopo.
2. Dados sensiveis nao entram em MCP publico ou geral sem revisao.
3. Tudo que move arquivo precisa de allowlist e rollback possivel.
4. Integracoes externas precisam de logs e separacao de responsabilidade.
5. MCPs de analise e busca devem ser default read-only quando possivel.

## Ordem recomendada de expansao

1. `search-mcp`
2. `analytics-mcp`
3. `github-mcp`
4. `browser-mcp`
5. `docs-mcp`
6. `code-intel-mcp`
7. `workflow-orchestrator-mcp`
8. `filesystem-mcp` ampliado

