# 🧠 Will Vault - Obsidian Neural Hub

Este repositório é o vault principal do Obsidian do Will. Ele organiza conhecimento, projetos, JARVIS, skills, vida pessoal, operações do vault e suporte técnico para uso com IA, RAG e automações.

Para navegação humana dentro do Obsidian, comece por:

- [[Bem-vindo|Neural Hub]]
- [[INDEX|INDEX global]]
- [[01-Hubs/README|Hubs Centrais do Vault]]

## 🚀 Estrutura física principal

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

## 🧭 Função das áreas

| Área | Função |
|---|---|
| `00-Inbox/` | entrada temporária para ideias, capturas e rascunhos |
| `01-Hubs/` | navegação superior do vault |
| `02-JARVIS/` | IA, agentes, memória e arquitetura do JARVIS |
| `03-Projetos/` | projetos, objetivos, execução e portfólio |
| `04-Conhecimentos/` | base consolidada de conhecimento técnico, estudos e vida prática |
| `05-Skills/` | habilidades técnicas e capacidades reutilizáveis |
| `06-Will-Pessoal/` | contexto pessoal e dados sensíveis |
| `07-Operacoes-do-Vault/` | manutenção, inventários, migração e governança |
| `08-Arquivo/` | legado preservado e conteúdos fora do fluxo ativo |
| `09-Sistema/` | configurações, scripts, instruções técnicas, testes e schemas |
| `10-Interfaces/` | painéis, dashboards, canvases e web-ui |
| `11-Dados-Brutos/` | dados brutos, clippings e bases importadas |
| `99-Templates/` | modelos reutilizáveis globais |

## 📚 Bases ainda em migração

Durante a reorganização, algumas pastas antigas ainda existem e serão migradas por blocos:

- `Conhecimentos-Gerais/`
- `Conhecimento-Geral/`
- `Knowledge-Base/`
- `JARVIS/`
- `Projetos/`
- `skills/`
- `Will-Pessoal/`
- `dashboards/`
- `raw/`
- `wiki/`

A nova estrutura já está sendo usada como destino oficial, mas a migração completa deve preservar links e conteúdo.

## 🛠️ Sistema técnico

Arquivos técnicos agora ficam principalmente em `09-Sistema/`:

- `09-Sistema/agents/` — instruções para agentes e modelos.
- `09-Sistema/config/` — configurações técnicas.
- `09-Sistema/scripts/` — scripts e atalhos de reorganização.
- `09-Sistema/schema/` — estrutura e contratos técnicos, quando migrado.
- `09-Sistema/tests/` — testes, quando migrado.

Alguns arquivos continuam na raiz porque ferramentas esperam encontrá-los ali, como `.gitignore`, `.env.example`, `.mcp.json`, `.pre-commit-config.yaml`, `requirements.txt` e arquivos de lock.

## 🔎 Reorganização do vault

A migração física é guiada por:

- [[07-Operacoes-do-Vault/Reestruturacao-Geral-do-Vault]]
- [[07-Operacoes-do-Vault/Inventario-Inicial-do-Vault]]
- [[07-Operacoes-do-Vault/Mapa-de-Migracao-Fisica-do-Vault]]

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
