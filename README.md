# 🧠 Will Vault - Obsidian Neural Hub

Este repositório é o vault principal do Obsidian do Will. Ele organiza conhecimento, projetos, JARVIS, skills, vida pessoal, operações do vault e suporte técnico para uso com IA, RAG e automações.

Para navegação humana dentro do Obsidian, comece por:

- [[Bem-vindo|Neural Hub]]
- [[INDEX|INDEX global]]
- [[01-Hubs/README|Hubs Centrais do Vault]]

## 🚀 Estrutura física principal

```txt
Will-obsidian/
├── 00-Inbox/             <- Entrada e rascunhos rápidos
├── 01-Hubs/              <- Navegação superior, dashboards e canvases
├── 02-JARVIS/            <- IA, agentes, memória e arquitetura do JARVIS
├── 03-Projetos/          <- Projetos ativos, execução e histórico
├── 04-Conhecimentos/     <- Base de conhecimentos estruturada (ontologia técnica)
├── 05-Skills/            <- Habilidades, MCPs e capacidades
├── 06-Will-Pessoal/      <- Dados pessoais, hábitos e visão
├── 07-Operacoes-do-Vault/ <- Manutenção, inventários e status do vault
├── 08-Arquivo/           <- Legado preservado fora do fluxo ativo
├── 09-Sistema/           <- Configurações, scripts e infraestrutura técnica
├── 11-Dados-Brutos/      <- Fontes externas, bases e clippings
└── 99-Templates/         <- Modelos reutilizáveis
```

## 🧭 Função das áreas

| Área | Função |
|---|---|
| `00-Inbox/` | entrada temporária para ideias, capturas e rascunhos |
| `01-Hubs/` | navegação superior, painéis visuais (dashboards) e canvases |
| `02-JARVIS/` | IA, agentes, memória e identidade operacional do JARVIS |
| `03-Projetos/` | projetos ativos, execução, portfólio e histórico |
| `04-Conhecimentos/` | base estruturada por ontologia (IA, Engenharia, Dados, Humanidades, etc.) |
| `05-Skills/` | habilidades técnicas e capacidades do vault |
| `06-Will-Pessoal/` | contexto pessoal, rotina, saúde e finanças |
| `07-Operacoes-do-Vault/` | manutenção, inventários e governança |
| `08-Arquivo/` | legado e notas arquivadas fora do fluxo ativo |
| `09-Sistema/` | configurações, scripts, instruções técnicas, testes e schemas |
| `11-Dados-Brutos/` | bases de dados brutos e clippings de páginas web |
| `99-Templates/` | modelos globais reutilizáveis |

## 📚 Consolidação do Vault

A reestruturação física e a consolidação de conhecimentos foram concluídas com sucesso. Todas as bases legadas (`Conhecimentos-Gerais`, `Knowledge-Base`, `wiki`, `JARVIS antigo`, `Projetos antigo`, `skills antigo` e `Will-Pessoal antigo`) foram totalmente migradas para os novos destinos numerados planos. Os links internos de todo o vault foram atualizados de forma automática para evitar referências quebradas.

## 🛠️ Sistema técnico

Arquivos técnicos ficam localizados em `09-Sistema/`:

- `09-Sistema/agents/` — instruções para agentes e modelos.
- `09-Sistema/config/` — configurações do vault e integradores.
- `09-Sistema/scripts/` — scripts Python de automação e reestruturação.
- `09-Sistema/schema/` — regras e validações técnicas.
- `09-Sistema/simuladores/` — simuladores interativos e quizzes.

Alguns arquivos continuam na raiz porque ferramentas esperam encontrá-los ali, como `.gitignore`, `.env.example`, `.mcp.json`, `.pre-commit-config.yaml`, `requirements.txt` e arquivos de lock.

## 🔎 Governança e Status

A governança do vault e logs operacionais são mantidos em:

- [[07-Operacoes-do-Vault/Reestruturacao-Geral-do-Vault]]
- [[07-Operacoes-do-Vault/Inventario-Inicial-do-Vault]]
- [[07-Operacoes-do-Vault/Status-da-Migracao-Fisica]]

## 📦 Como clonar e usar

```bash
git clone https://github.com/William-kelvem94/Will-obsidian.git
cd Will-obsidian
pip install -r requirements.txt
```

Depois, abra a pasta no Obsidian.

## ☁️ Backup e segurança

- Git mantém histórico de alterações.
- Recomenda-se backup externo ou pasta sincronizada.
- Dados pessoais devem ser tratados com cuidado antes de indexação por IA/RAG.
- Arquivos sensíveis não devem ser expostos em notas públicas ou automações sem revisão.

---

Gerenciado por William Kelvem.
