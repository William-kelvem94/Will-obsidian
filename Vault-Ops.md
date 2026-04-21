---
title: "Vault Ops — Manutenção do Cofre"
description: "Guia de manutenção, scripts e boas práticas para organizar e expandir o vault Obsidian."
tags:
  - vault
  - manutencao
  - automacao
  - ops
  - hub
updated: 2026-04-15
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

Uso:

```powershell
Set-Location 'c:\Users\willi\Documents\GitHub\Will-obsidian\.scripts'
python .\github_sync.py
```

Isso ajuda a manter o inventário atualizado com os últimos commits e o status dos repositórios mapeados.

### `.scripts/mcp-vault-server/index.js`

Servidor local MCP para expor o vault como recurso e ferramenta estruturada.

Uso:

```powershell
Set-Location 'c:\Users\willi\Documents\GitHub\Will-obsidian\.scripts\mcp-vault-server'
node .\index.js
```

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

- `Bem-vindo.md` → porta de entrada principal do vault.
- `Projetos.md` → MOC de projetos públicos por categoria.
- `Projetos/README.md` → hub de projetos mapeados por linguagem.
- `Projetos/Plano-de-Acao.md` → lista de ações e prioridades do vault.
- `Projetos/Privados/README.md` → hub dos clones locais em análise.
- `Will-Pessoal/README.md` → hub pessoal para perfil, vida e objetivos.
- `JARVIS/README.md` → hub do segundo cérebro e memória ativa.

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
