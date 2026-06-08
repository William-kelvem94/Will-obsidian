---
title: "Vault Ops — Manutenção do Cofre"
description: "Guia operacional completo para manter o vault organizado, automatizado, saudável e alinhado com o Projeto JARVIS. Inclui scripts, rotinas, métricas e boas práticas."
tags: [vault, manutencao, automacao, ops, hub, second-brain]
updated: 2026-05-02
---

# Vault Ops — Manutenção do Cofre

Este é o **manual vivo** do Neural Hub. Aqui está registrado tudo que preciso fazer para manter o vault organizado, indexado, automatizado e pronto para uso humano + agentes de IA.

O objetivo final é ter um Second Brain que **cresce sozinho**, com mínima intervenção manual, mas com máxima qualidade e consistência.

---

## 🎯 Objetivo Geral

- Manter todos os hubs centrais atualizados (`Bem-vindo.md`, `Cerebro-Will.md`, `Projetos.md`, `JARVIS/README.md`).
- Garantir que a estrutura de pastas reflita a arquitetura de 5 tiers.
- Usar metadados padronizados em **todas** as notas importantes (frontmatter YAML).
- Executar automações regularmente para limpeza, indexação RAG e sincronização.
- Manter o vault **RAG-friendly** (notas atômicas, bem linkadas, com bom conteúdo).

---

## 📋 Principais Pontos de Manutenção

- **HUBS**: Atualizar sempre que houver mudança significativa em projetos ou skills.
- **Estrutura de Pastas**: Manter clara a separação entre `Projetos/01-Ativos/`, `Privados/`, `EstudosFocados/`, `EstudosPesquisas/`, `Will-Pessoal/` e `JARVIS/`.
- **Frontmatter Padrão** (obrigatório em notas importantes):
  ```yaml
  ---
  title: "..."
  description: "Resumo claro de 1-2 linhas"
  tags: [tag1, tag2, #hub]
  updated: YYYY-MM-DD
  status: active | archived | draft
  source: "link ou origem"
  ---
  ```
- **Limpeza**: Rodar `vault_cleanup.py` após criar ou mover muitas notas.

---

## 🛠️ Scripts Disponíveis (Documentação Completa)

### 1. `vault_cleanup.py`
**Objetivo**: Normalizar frontmatter, corrigir tags, adicionar `updated` e tags de contexto.  
**Quando rodar**: Sempre após grande edição ou importação.  
**Uso**:
```powershell
cd .\scripts
python vault_cleanup.py
```
**O que ele faz**:
- Valida YAML
- Converte tags para array
- Adiciona tags automáticas baseadas na pasta (#projetos, #jarvis, etc.)
- Gera relatório em `vault_cleanup_report.md`

### 2. `github_sync.py`
**Objetivo**: Manter atualizado o inventário dos 67 repositórios.  
**Benefício**: Saber exatamente quais repos tenho localmente e quais precisam de análise.  
**Uso**: Semanal.

### 3. `vault_merge.ps1`
**Objetivo**: Mesclar vaults de diferentes máquinas mantendo a versão mais recente.  
**Recursos**: Comparação MD5, backup automático, relatório JSON.  
**Uso recomendado**:
- Sempre use `-DryRun` primeiro.

### 4. `daily_logger.py`
**Objetivo**: Gerar log diário automático a partir do histórico git.  
**Saída**: Nota em `JARVIS/03-Memory/Logs/`.

### 5. `project_health_checker.py`
**Objetivo**: Dar nota 0-100 para cada projeto ativo.  
**Critérios principais**: README, testes, Docker, documentação, dependências.

### 6. `knowledge_indexer.py`
**Objetivo**: Manter o índice vetorial RAG atualizado (o mais importante para IA).  
**Modos**:
- `--build` (completo)
- `--update` (incremental)
- `--watch` (monitoramento contínuo)

### 7. `mcp-vault-server/index.js`
**Objetivo**: Expor o vault inteiro como ferramenta para agentes externos (Claude, etc.).  
**Comando**:
```powershell
cd .scripts\mcp-vault-server
node index.js
```

---

## 🔄 Rotina Recomendada

### Diária (5-10 min)
- Rodar `daily_logger.py`
- Atualizar `Plano-de-Acao.md` com o que foi feito

### Semanal
1. `github_sync.py`
2. `project_health_checker.py`
3. `knowledge_indexer.py --update`
4. Revisar notas órfãs

### Mensal
1. `knowledge_indexer.py --build`
2. Arquivar projetos concluídos
3. Revisão geral dos OKRs
4. Limpeza de backups antigos

---

## 📊 Monitoramento de Saúde do Vault

**Métricas chave**:
- Total de notas
- % de notas órfãs (< 5% é meta)
- Cobertura RAG (> 90%)
- Média de health score dos projetos (> 75)
- Commits recentes

**Metas de Excelência**:
- Zero notas sem tags ou frontmatter
- Graph limpo e denso de conexões
- Todos os projetos ativos com análise completa

---

## Fluxo para Novos Projetos (Passo a Passo)

1. Criar nota no local correto (`Projetos/` ou `Privados/`).
2. Preencher frontmatter completo.
3. Adicionar ao hub correspondente.
4. Rodar `vault_cleanup.py`.
5. Atualizar `Plano-de-Acao.md` e `Projetos.md`.
6. Se for privado importante → criar nota de análise técnica detalhada.

---

## Boas Práticas Gerais

- Prefira notas atômicas (uma ideia por nota).
- Sempre linke para hubs e glossário.
- Use Dataview para dashboards dinâmicos.
- Mantenha o `Master-Glossary` atualizado.
- Faça backup antes de merges grandes.

**Últimas Operações Registradas**:
- 2026-04-23: Merge de 97 arquivos
- 2026-04-23: Expansão inicial do vault

---

**Este documento é vivo.** Atualize sempre que criar um novo script ou mudar um fluxo.

[[Bem-vindo]] | [[Cerebro-Will]] | [[03-Projetos/Projetos]] | [[Vault-Hierarchy-Map]]
