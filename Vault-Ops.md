---
title: "Vault Ops — Manutenção do Cofre"
description: "Guia de manutenção, scripts e boas práticas para organizar e expandir o vault Obsidian."
tags:
  - vault
  - manutencao
  - automacao
  - ops
  - hub
updated: 2026-04-23
---

# Vault Ops — Manutenção do Cofre

Este documento é o guia operacional para manter o vault organizado, automatizado e alinhado com o fluxo de trabalho do segundo cérebro.

## Objetivo

Manter os índices, tags e notas principais sempre atualizados, com automação para reduzir trabalho manual.

## Principais pontos de manutenção

- Atualizar os hubs centrais: `Bem-vindo.md`, `Projetos.md`, `Projetos/README.md` e `JARVIS/README.md`.
- Manter a estrutura de pastas clara entre `Projetos/`, `Projetos/Privados/`, `Projetos/EstudosFocados/`, `Projetos/EstudosPesquisas/` e `Will-Pessoal/`.
- Usar metadados padronizados em notas importantes: `title`, `description`, `tags`, `updated`, `source` e `status`.
- Executar limpeza de metadados sempre que uma nova nota for criada ou quando arquivos forem movidos.

## Scripts disponíveis

### `.scripts/vault_cleanup.py`

Roda limpeza e normalização de frontmatter em notas Markdown do vault.

Uso:

```powershell
Set-Location 'c:\Users\willi\Documents\GitHub\Will-obsidian\.scripts'
python .\vault_cleanup.py
```

O script garante que cada nota Markdown tenha:

- blocos de frontmatter YAML válidos
- `tags:` como array ou lista estruturada
- `updated:` com a data da última normalização
- tags de pasta relacionadas, como `#projetos`, `#privados`, `#jarvis` e `#perfil`

O script também gera um relatório em `.scripts/vault_cleanup_report.md` com as ações realizadas.

### `.scripts/github_sync.py`

Usado para sincronizar o inventário de repositórios GitHub com a nota `Projetos/GitHub-Completo.md`.

Agora o script também marca se um repositório tem clone local em `Projetos/Privados/`.

Uso:

```powershell
Set-Location 'c:\Users\willi\Documents\GitHub\Will-obsidian\.scripts'
python .\github_sync.py
```

Isso ajuda a manter o inventário atualizado com os últimos commits, o status de nuvem e quais repositórios já têm análise local.

**Indicadores:**
- 🔒 Clone local existe
- ☁️ Repositório apenas na nuvem

---

### `.scripts/vault_merge.ps1`

Script PowerShell para mesclar vaults externos mantendo as versões mais recentes.

**Recursos:**
- Comparação MD5 para arquivos idênticos
- Resolução de conflitos baseada em timestamp
- Backup automático de arquivos sobrescritos
- Relatório JSON detalhado

Uso:

```powershell
# Análise sem alterações (DRY RUN)
Set-Location 'c:\Users\willi\Documents\GitHub\Will-obsidian\.scripts'
.\vault_merge.ps1 -DryRun:$true -SourcePath "D:\OBSIDIAN\Will"

# Executar merge real
.\vault_merge.ps1 -DryRun:$false -SourcePath "D:\OBSIDIAN\Will"

# Ver relatório detalhado
Get-Content .\vault_merge_report.json | ConvertFrom-Json
```

**Última execução**: 2026-04-23 - 97 arquivos mesclados de D:\OBSIDIAN\Will

---

### `.scripts/daily_logger.py`

Gera logs diários automáticos baseados no histórico git.

Uso:

```powershell
python .scripts/daily_logger.py
# Saída: JARVIS/03-Memory/Logs/YYYY-MM-DD.md
```

**Dados capturados:**
- Commits git com mensagens
- Arquivos modificados/criados/deletados
- Resumo agregado de atividades

---

### `.scripts/project_health_checker.py`

Analisa completude de projetos e gera scores de saúde (0-100).

Uso:

```powershell
python .scripts/project_health_checker.py
# Saída: Projetos/01-Ativos/Privados/[project]/_HEALTH.md
```

**Critérios de pontuação:**
- README.md (20 pts)
- Testes (25 pts)
- Setup Docker (20 pts)
- Dependências (20 pts)
- Documentação (15 pts)

---

### `.scripts/knowledge_indexer.py`

Constrói e mantém índice vetorial RAG para busca semântica.

Uso:

```powershell
# Rebuild completo
python .scripts/knowledge_indexer.py --build

# Update incremental
python .scripts/knowledge_indexer.py --update

# Modo watch (auto-update a cada 5 min)
python .scripts/knowledge_indexer.py --watch

# Verificar integridade
python .scripts/knowledge_indexer.py --verify
```

**Dependências:**
- `skills/04-knowledge-systems/rag-pipeline/embeddings_generator.py`
- `skills/04-knowledge-systems/rag-pipeline/vector_store.py`

---

### `.scripts/mcp-vault-server/index.js`

Servidor local MCP para expor o vault como recurso e ferramenta estruturada.

Uso:

```powershell
Set-Location 'c:\Users\willi\Documents\GitHub\Will-obsidian\.scripts\mcp-vault-server'
node .\index.js
```

---

## 🔄 Tarefas de Manutenção

### Semanais

```powershell
# 1. Atualizar inventário GitHub
python .scripts/github_sync.py

# 2. Verificar saúde dos projetos
python .scripts/project_health_checker.py

# 3. Atualizar índice de conhecimento
python .scripts/knowledge_indexer.py --update

# 4. Revisar notas órfãs
# Verificar: Isolated-Notes-Audit.md
```

### Mensais

```powershell
# 1. Rebuild completo do índice RAG
python .scripts/knowledge_indexer.py --build

# 2. Arquivar projetos concluídos
# Mover de Projetos/01-Ativos/ para Projetos/02-Arquivo/

# 3. Limpar backups antigos (>3 meses)
Get-ChildItem .backups -Directory | Where-Object {
    $_.CreationTime -lt (Get-Date).AddMonths(-3)
} | Remove-Item -Recurse

# 4. Atualizar OKRs
# Editar: Projetos/Objetivos/OKRs.md
```

---

## 📊 Monitoramento de Saúde

### Métricas do Vault

```powershell
# Total de notas
(Get-ChildItem -Recurse -Filter "*.md").Count

# Score de isolamento
Select-String "Isolated notes:" Isolated-Notes-Audit.md

# Cobertura RAG
python .scripts/knowledge_indexer.py --verify

# Status do repositório Git
git status --short
```

### Metas de Saúde
- **Score de isolamento**: <5% de notas órfãs
- **Cobertura RAG**: >90% dos arquivos markdown
- **Saúde de projetos**: >70 média para projetos ativos
- **Logs diários**: Gerados automaticamente

---

## 📅 Operações Recentes

| Data | Operação | Status | Detalhes |
|------|-----------|--------|---------|
| 2026-04-23 | Vault Merge | ✅ Completo | 97 arquivos de D:\OBSIDIAN |
| 2026-04-23 | Expansão Vault | ✅ Completo | Roadmap 30 dias (26 arquivos) |
| 2026-04-23 | GitHub Sync | ✅ Completo | 67 repositórios rastreados |

## Fluxo recomendado para novos projetos

1. Criar a nota pública em `Projetos/` ou `Projetos/Outros/`.
2. Se for um clone local com trabalho ativo, criar nota de análise em `Projetos/Privados/`.
3. Adicionar `source:` e `updated:` no frontmatter da nota.
4. Incluir a nota no hub apropriado: `Projetos.md`, `Projetos/README.md` ou `Projetos/Privados/README.md`.
5. Executar `.scripts/vault_cleanup.py` para normalizar tags e metadados.
6. Atualizar `Projetos/Plano-de-Acao.md` com próxima ação e estado do projeto.

## Boas práticas de organização

- Use `#hub` apenas para notas de índice ou entrada principal.
- Use `#projetos`, `#privados`, `#jarvis`, `#perfil`, `#skills` de forma consistente.
- Separe notas de pesquisa (`EstudosPesquisas`) das notas de execução (`EstudosFocados`).
- Evite nomes de arquivo com espaços em pastas principais sempre que possível.

## Relacionamentos importantes

### Arquivos de Entrada
- [Bem-vindo.md](Bem-vindo.md) → porta de entrada principal do vault
- [Cerebro-Will.md](Cerebro-Will.md) → visão conceitual do segundo cérebro
- [TODO.md](TODO.md) → lista de tarefas globais

### Hubs Principais
- [Projetos.md](Projetos.md) → MOC de projetos públicos por categoria
- [Projetos/README.md](Projetos/README.md) → hub de projetos mapeados por linguagem
- [Projetos/Plano-de-Acao.md](Projetos/Plano-de-Acao.md) → lista de ações e prioridades
- [Projetos/Privados/README.md](Projetos/Privados/README.md) → hub dos clones locais
- [Will-Pessoal/README.md](Will-Pessoal/README.md) → hub pessoal para perfil e objetivos
- [JARVIS/README.md](JARVIS/README.md) → hub do segundo cérebro e memória ativa

### Documentação Técnica
- [JARVIS/00-Architecture/Vault-Architecture-Guide.md](JARVIS/00-Architecture/Vault-Architecture-Guide.md) → guia completo da arquitetura 5-tier
- [JARVIS/01-Identity/Decision-Framework.md](JARVIS/01-Identity/Decision-Framework.md) → templates de decisão
- [JARVIS/01-Identity/Will/Engineering-Principles.md](JARVIS/01-Identity/Will/Engineering-Principles.md) → princípios técnicos
- [JARVIS/02-Operational/Dashboard.md](JARVIS/02-Operational/Dashboard.md) → estado operacional atual
- [skills/README.md](skills/README.md) → índice de habilidades técnicas

### Decisões e Histórico
- [JARVIS/05-System/Decisoes/](JARVIS/05-System/Decisoes/) → registro de decisões importantes
- [JARVIS/03-Memory/Logs/](JARVIS/03-Memory/Logs/) → logs de atividade automáticos
- [JARVIS/03-Memory/Diario/](JARVIS/03-Memory/Diario/) → diários pessoais

## 🏛️ Arquitetura de Camadas (Tiered)

Em 2026-04-21, o vault foi migrado para uma estrutura em camadas para otimizar a performance de agentes de IA:
- **01-Identity/Active**: Core vital.
- **02-Operational/Vision**: Contexto de ação.
- **03-Memory/Learning**: Histórico.
- **04-Engineering/Social**: Conhecimento técnico.
- **05-System/Archive**: Manutenção e histórico legacy.

## 🕵️ Auditoria e Qualidade

As auditorias periódicas (antigo `Isolated-Notes-Audit.md`) focam em:
- **Conectividade**: Garantir que novos hubs não criem orfandade de notas.
- **Normalização**: Aplicar tags e metadados via `.scripts/vault_cleanup.py`.
- **Integridade de Links**: Atualização global após movimentação de pastas (realizada via scripts de S/R).

### Resultados de Auditoria Recente
- Hubs `Bem-vindo.md`, `Projetos.md` e `JARVIS/README.md` totalmente integrados à nova arquitetura.
- Consolidado arquivos de meta-pesquisa em `Projetos/03-Estudos/`.
- Limpeza de scripts e logs temporários concluída.

## 📈 Próximos passos

- [ ] Implementar dashboard via Dataview para o radar de projetos ativos.
- [ ] Criar templates de frontmatter automatizados no VS Code.
- [ ] Expandir o `04-Engineering/Wiki` com a stack de AI Generativa local.
