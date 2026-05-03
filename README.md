# 🧠 Will Vault - Obsidian Personal Knowledge Management

Repositório central do meu Cérebro Digital (Vault do Obsidian). Este projeto organiza conhecimento, projetos, logs diários e automações para gerenciamento de informações.

## 🚀 Estrutura do Vault

- **`.scripts/`**: Automações em Python e PowerShell para manutenção e geração de logs.
- **`JARVIS/`**: Núcleo operacional, memória e logs do sistema.
- **`Projetos/`**: Gerenciamento de projetos ativos, parados e arquivados.
- **`Templates/`**: Modelos para notas, reuniões e logs.
- **`skills/`**: Base de conhecimento técnico e sistemas de IA (RAG).

## 🛠️ Automações (Scripts)

| Script | Propósito | Execução |
| :--- | :--- | :--- |
| `daily_logger.py` | Gera um resumo diário de atividades (Git, arquivos modificados). | `python .scripts/daily_logger.py` |
| `github_sync.py` | Sincroniza a lista de repositórios do GitHub no vault. | `python .scripts/github_sync.py` |
| `knowledge_indexer.py` | Gera embeddings para o sistema de busca semântica (RAG). | `python .scripts/knowledge_indexer.py --update` |
| `project_health_checker.py` | Analisa a saúde dos projetos e links quebrados. | `python .scripts/project_health_checker.py` |
| `vault_cleanup.py` | Remove arquivos órfãos e organiza anexos. | `python .scripts/vault_cleanup.py` |

## 🔌 Configuração do Obsidian

### Plugins Essenciais (Comunitários)
- **[Dataview](https://github.com/blacksmithgu/obsidian-dataview)**: Transforma o vault em um banco de dados consultável. Usado para dashboards e listas automáticas.
- **[Templater](https://github.com/SilentVoid13/Templater)**: Permite o uso de lógica (JS) na criação de notas.

### Snippets CSS
- **`vault-theme.css`**: 
  - **Coloração de Tags**: Atribui cores específicas para tags como `#jarvis`, `#projetos`, `#skills/ai`, etc.
  - **Dashboard Design**: Melhora visual de tabelas e cabeçalhos `H1` para um aspecto mais profissional e "operacional".

## 🖥️ Dashboards Operacionais

O vault conta com dashboards dinâmicos para visualização de estado:
- **[[JARVIS/05-System/Vault-Health-Dashboard|Vault Health Dashboard]]**: Visão geral da saúde do vault, notas recentes e projetos ativos.
- **[[Projetos/Projetos|Painel de Projetos]]**: Listagem automática de projetos por status e prioridade.

## 📦 Como Clonar e Usar

1. Clone o repositório:
   ```bash
   git clone https://github.com/William-kelvem94/Will-obsidian.git
   ```
2. Instale as dependências dos scripts:
   ```bash
   pip install -r requirements.txt
   ```
3. Configure o arquivo `.env`:
   - Copie `.env.example` para `.env` e preencha as variáveis.
4. Abra a pasta no Obsidian e habilite os plugins comunitários.

## ☁️ Backup e Segurança

A resiliência de dados é mantida em três níveis:
1. **Versionamento (Git)**: Histórico completo de alterações via commits.
2. **Sincronização Cloud**: Recomendado manter o vault em uma pasta sincronizada (Google Drive, Dropbox ou iCloud) para backup em tempo real e acesso mobile.
3. **GitHub Actions**: Automações semanais garantem que dados externos (como lista de repositórios) estejam sempre atualizados.

---
*Gerenciado por [William-kelvem94](https://github.com/William-kelvem94)*
