---
title: "Mapa de Migração Física do Vault"
date: 2026-06-07
updated: 2026-06-07
type: roadmap
status: active
tags: [vault-ops, migracao, pastas, organizacao]
related: [[Reestruturacao-Geral-do-Vault]], [[Inventario-Inicial-do-Vault]], [[../01-Hubs/README]], [[../Bem-vindo]]
summary: "Mapa de destino para reorganizar fisicamente as pastas do Will-obsidian sem perda de conteúdo."
---

# Mapa de Migração Física do Vault

Este documento define como reorganizar fisicamente as pastas do `Will-obsidian`.

A regra principal é: **mover, não apagar**. Tudo que for reorganizado deve preservar conteúdo, histórico e possibilidade de revisão.

## Estrutura física final recomendada

```txt
Will-obsidian/
├── 00-Inbox/
├── 01-Hubs/
├── 02-JARVIS/
├── 03-Projetos/
├── 04-Conhecimentos/
├── 05-Skills/
├── 06-Will-Pessoal/
├── 07-Operacoes-do-Vault/
├── 08-Arquivo/
├── 09-Sistema/
├── 10-Interfaces/
├── 11-Dados-Brutos/
└── 99-Templates/
```

## Função de cada pasta

| Pasta final | Função |
|---|---|
| `00-Inbox/` | entrada temporária para notas soltas, capturas e triagem |
| `01-Hubs/` | navegação superior e mapas centrais |
| `02-JARVIS/` | IA, agentes, memória e identidade operacional do JARVIS |
| `03-Projetos/` | projetos ativos, estudos ligados a projetos, objetivos e execução |
| `04-Conhecimentos/` | conhecimento estável, estudos, IA, engenharia, dados, humanidades e vida prática |
| `05-Skills/` | habilidades técnicas, pipelines, MCPs e capacidades reutilizáveis |
| `06-Will-Pessoal/` | contexto pessoal, rotina, saúde, finanças e reflexões sensíveis |
| `07-Operacoes-do-Vault/` | manutenção, governança, inventários, mapas e reestruturação |
| `08-Arquivo/` | legado, notas antigas, duplicidades e conteúdos preservados fora do fluxo ativo |
| `09-Sistema/` | configurações, scripts, schemas, testes, benchmarks e arquivos técnicos do repositório |
| `10-Interfaces/` | dashboards, painéis, canvases e web-ui |
| `11-Dados-Brutos/` | raw, bases, clippings e fontes importadas |
| `99-Templates/` | templates globais reutilizáveis |

## Mapeamento das pastas atuais

| Pasta atual | Destino recomendado | Motivo |
|---|---|---|
| `01-Hubs/` | `01-Hubs/` | já é a camada nova de navegação |
| `07-Operacoes-do-Vault/` | `07-Operacoes-do-Vault/` | já é a camada nova de operações |
| `Bases/` | `11-Dados-Brutos/Bases/` | base importada ou fonte de dados |
| `benchmarks/` | `09-Sistema/benchmarks/` | artefatos técnicos de avaliação |
| `Canvases/` | `10-Interfaces/Canvases/` | recursos visuais do Obsidian |
| `Clippings/` | `11-Dados-Brutos/Clippings/` | capturas e conteúdos importados |
| `Conhecimento-Geral/` | `04-Conhecimentos/07-Humanidades/` | humanidades e conhecimento cultural |
| `Conhecimentos-Gerais/` | `04-Conhecimentos/` | conhecimento técnico, IA, dados e vida prática |
| `dashboards/` | `10-Interfaces/dashboards/` | painéis e visualizações |
| `flashcards/` | `04-Conhecimentos/06-Estudos-e-Aprendizagem/flashcards/` | estudo e revisão |
| `Ideias/` | `00-Inbox/Ideias/` | ideias precisam triagem antes de virar projeto ou conhecimento |
| `JARVIS/` | `02-JARVIS/` | área própria de IA e memória |
| `Knowledge-Base/` | `04-Conhecimentos/Knowledge-Base/` | base de conhecimento legada ou complementar |
| `Projetos/` | `03-Projetos/` | execução e portfólio |
| `raw/` | `11-Dados-Brutos/raw/` | dados brutos |
| `schema/` | `09-Sistema/schema/` | estrutura técnica e configuração |
| `scripts/` | `09-Sistema/scripts/` | scripts do repositório |
| `simuladores/` | `09-Sistema/simuladores/` | ferramentas técnicas e testes práticos |
| `skills/` | `05-Skills/` | habilidades e capacidades |
| `Templates/` | `99-Templates/Legado/` | templates antigos preservados |
| `tests/` | `09-Sistema/tests/` | testes técnicos |
| `web-ui/` | `10-Interfaces/web-ui/` | interface web |
| `wiki/` | `04-Conhecimentos/wiki/` | documentação e conhecimento enciclopédico |
| `Will-Pessoal/` | `06-Will-Pessoal/` | contexto pessoal e sensível |

## Mapeamento de arquivos raiz

| Arquivo raiz | Destino recomendado | Observação |
|---|---|---|
| `Bem-vindo.md` | manter na raiz | entrada principal do Obsidian |
| `README.md` | manter na raiz | entrada do repositório GitHub |
| `INDEX.md` | manter na raiz ou redirecionar para hubs | índice global |
| `Painel-Cockpit.md` | `10-Interfaces/Painel-Cockpit.md` | painel visual/operacional |
| `Projetos.md` | `03-Projetos/Projetos.md` | índice legado de projetos |
| `AGENTS.md` | `09-Sistema/agents/AGENTS.md` | instruções de agentes |
| `CLAUDE.md` | `09-Sistema/agents/CLAUDE.md` | instruções de agente/modelo |
| `GEMINI.md` | `09-Sistema/agents/GEMINI.md` | instruções de agente/modelo |
| `CLI-BOOTSTRAP.md` | `09-Sistema/CLI-BOOTSTRAP.md` | bootstrap técnico |
| `claude_desktop_config.json` | `09-Sistema/config/claude_desktop_config.json` | configuração técnica |
| `indexer_config.json` | `09-Sistema/config/indexer_config.json` | configuração de indexação |
| `.mcp.json` | manter na raiz | configuração esperada por ferramenta |
| `.env.example` | manter na raiz | padrão comum de projeto |
| `.gitignore` | manter na raiz | Git exige na raiz |
| `.pre-commit-config.yaml` | manter na raiz | ferramenta espera na raiz |
| `requirements*.txt` | manter na raiz | dependências Python do repo |
| `requirements.in` | manter na raiz | fonte de dependências Python |
| `skills-lock.json` | manter na raiz | lock técnico atual |
| `start-web-ui.bat` | manter na raiz | atalho local de execução |
| `gitleaks.toml` | manter na raiz | ferramenta pode esperar na raiz |

## Pastas ocultas e técnicas

| Pasta | Destino recomendado | Observação |
|---|---|---|
| `.git/` | manter na raiz | obrigatório |
| `.github/` | manter na raiz | GitHub espera na raiz |
| `.obsidian/` | manter na raiz | Obsidian espera na raiz |
| `.cursor/` | manter na raiz | ferramenta espera na raiz |
| `.continue/` | manter na raiz | ferramenta espera na raiz |
| `.openclaude/` | manter na raiz | ferramenta espera na raiz |
| `.agents/` | manter na raiz ou revisar | pode ser esperado por ferramenta |
| `.scripts/` | manter ou migrar depois | revisar antes de mover |
| `.logs/` | `09-Sistema/logs/` ou ignorar no Git | revisar sensibilidade |

## Estratégia recomendada

A migração deve acontecer em etapas:

1. Criar as pastas finais.
2. Fazer backup local.
3. Rodar script em modo simulação.
4. Validar destinos.
5. Rodar migração real.
6. Abrir Obsidian e revisar links.
7. Atualizar hubs e índices.
8. Fazer commit detalhado em PT-BR.

## Regra de segurança

Antes de mover, executar:

```powershell
git status
```

Só prosseguir se o estado estiver entendido. Se houver alterações locais importantes, criar backup ou commit antes.

## Próxima ação

Usar o script [[../../09-Sistema/scripts/reorganizar-vault.ps1]] quando ele estiver disponível no repositório local.
