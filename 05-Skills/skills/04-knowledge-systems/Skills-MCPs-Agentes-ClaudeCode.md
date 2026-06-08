---
tags: [skills, mcp, agentes, automacao, firecrawl, claudecode, poweruser, advanced, skills-knowledge]
title: "Skills, MCPs e Agentes - Claude Code, Firecrawl e Stack Padrão"
date: 2026-05-24
updated: 2026-06-07
---

# Skills, MCPs, Agentes e Fluxos de Automação — Power User Claude Code

## 1. SKILLS (AUTOMAÇÕES INTERNAS, SLASH COMMANDS)

Skills são comandos internos do Claude Code, invocáveis via /nome-da-skill ou de forma automática por contexto. 
Toda skill pode receber argumentos. Usuário avançado pode customizar chamadas.

### Skills nativas do Claude Code

| Skill        | Descrição Técnica                                                                 | Exemplo de Uso                 |
|--------------|-----------------------------------------------------------------------------------|--------------------------------|
| /commit      | Cria commit, sugere mensagem, adiciona arquivos, não faz push                     | /commit -m "Nova feature de login" |
| /review-pr   | Analisa e revisa PRs (gh cli) — sumariza, sugere, aprova, comenta                 | /review-pr 123                 |
| /pdf         | Processa PDFs locais: sumariza, extrai tabelas/dados, busca páginas, split        | /pdf ./relatorio.pdf           |
| /help        | Lista e explica comandos e funções                                               | /help                         |
| /clear       | Limpa contexto e memória de sessão                                                | /clear                        |
| /settings    | Mostra/configura env vars, hooks, statusline, preferências, modelo                | /settings                     |
| /plan        | Modo planejamento: quebra tarefas, aprova fluxo antes de executar                 | /plan "Refatorar autenticação" |
| /tasks       | Kanban interno: lista/cria/edita/marca tarefas                                   | /tasks list                   |
| /fast        | Respostas ultra-rápidas (Opus 4.x, decoding acelerado)                           | /fast                         |
| /agents      | Lista/spawna agentes especializados                                               | /agents                       |
| /mcp         | Lista e detalha Model Connected Plugins ativos                                    | /mcp                          |

Extra: Skills podem ser expandidas com plugins/scripts internos, integrações ou orquestradores customizados.

---

## 2. MCPs (Model Connected Plugins — Plugins & Integrações Avançadas)

MCPs conectam o Claude Code a APIs e engines externas (web, CI/CD, scraping, bancos e automações corporativas).

- **FIRECRAWL**: Suite para automação web/scraping/monitoração/extratos estruturados/browser automation.
    - firecrawl_agent / firecrawl_scrape / firecrawl_map / firecrawl_crawl / firecrawl_extract / firecrawl_parse / firecrawl_monitor_create,run,check,list,get,update,delete / firecrawl_interact/stop / firecrawl_search/search_feedback
- Plugins variáveis: cloud, bancos, Notion, Jira, Github, Slack, Linear (ativação depende de config local).

---

## 3. AGENTES (ROBÔS/AUTOMAÇÕES INTELIGENTES)

| Nome               | O que faz                                                                                  |
|--------------------|------------------------------------------------------------------------------------------|
| claude-code-guide  | Dúvidas sobre Claude Code, comandos, integrações, settings, fluxos e atalhos.             |
| statusline-setup   | Configura statusline e indicadores na shell/editor.                                       |
| general-purpose    | Pesquisa multi-etapas, buscas complexas, fluxos longos, automações open-context.          |

---

## 4. WORKFLOWS, TOOLS E CAPACIDADES INTERNAS

- **Glob:** Busca arquivos por padrão/wildcard/regex.
- **Grep:** Busca textual/regex em todo vault/código.
- **Read/Write/Edit:** Leitura/escrita incremental segura em qualquer arquivo.
- **Bash:** Executa comandos shell (git, npm, python, scripts, etc).
- **TaskCreate/List/Update:** Kanban/tasks internos via script.
- **Memory:** Memória persistente para fatos, regras e preferências.
- **Plan Mode:** Planejamento granular com aprovação prévia.

---

## 5. EXEMPLOS DE USO AVANÇADO

- Commit em massa: `/commit -m "Atualização dos scripts para LGPD e novos testes automáticos."`
- Busca + scrape na web: `/pdf ./docs/relatorio.pdf` — `/plan "Reestruturar glossário cruzando incidentes reais"`
- Criação de tarefas: `/tasks create "Refatorar ingestion pipeline do projeto X"`
- Monitoramento de página crítica: `functions.mcp__firecrawl-mcp__firecrawl_monitor_create`

---

## 6. EXTENSIBILIDADE

- **Hooks customizados**: Scripts shell/python disparados por eventos (push, commit, etc).
- **Custom MCPs**: Admin pode ativar endpoints REST/GraphQL customizados conforme demanda.

--- 

*Este arquivo resume e traduz para uso imediato as skills, MCPs, agentes e workflows avançados utilizáveis e customizáveis neste ambiente. Veja também:
- [[05-Skills/skills/04-knowledge-systems/obsidian-neural-vault]]
- [[02-JARVIS/JARVIS/Main]]
*