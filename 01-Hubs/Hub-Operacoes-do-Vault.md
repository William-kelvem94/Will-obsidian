---
title: "Hub de Operações do Vault"
date: 2026-06-07
updated: 2026-06-07
type: moc
status: active
tags: [hub, vault-ops, manutencao, organizacao]
summary: "Hub de manutenção, governança, migração física e operações do Obsidian."
---

# Hub de Operações do Vault

Este hub reúne as notas de manutenção, governança e reorganização física do Obsidian.

## Entradas principais

- [[../Vault-Ops|Vault Operations]]
- [[../Vault-Hierarchy-Map|Mapa de Hierarquia do Vault]]
- [[../Master-Glossary|Glossário Mestre]]
- [[../Graph-Legenda|Legenda do Grafo]]
- [[../07-Operacoes-do-Vault/Reestruturacao-Geral-do-Vault]]
- [[../07-Operacoes-do-Vault/Inventario-Inicial-do-Vault]]
- [[../07-Operacoes-do-Vault/Mapa-de-Migracao-Fisica-do-Vault]]

## Scripts e atalhos

| Arquivo | Uso |
|---|---|
| `reorganizar-vault-simulacao.bat` | simula a migração sem mover arquivos |
| `reorganizar-vault-aplicar.bat` | aplica a migração física após confirmação |
| `09-Sistema/scripts/reorganizar-vault.ps1` | script PowerShell principal |

## Operações importantes

- reorganização de pastas;
- atualização de links internos;
- manutenção de MOCs;
- revisão de notas órfãs;
- padronização de YAML;
- limpeza de duplicidades;
- preparo para RAG;
- revisão de dados sensíveis.

## Regras de manutenção

1. Não mover arquivos em massa sem plano.
2. Não apagar conteúdo sem backup ou justificativa.
3. Preferir migração por blocos.
4. Atualizar hubs depois de mover conteúdo.
5. Revisar links internos.
6. Registrar decisões importantes.
7. Usar commits em PT-BR com descrição detalhada.
8. Rodar simulação antes de aplicar migração física.

## Checklist de saúde do vault

- [ ] Hubs principais estão atualizados?
- [ ] Links críticos funcionam?
- [ ] README e INDEX refletem a estrutura real?
- [ ] Há notas duplicadas?
- [ ] Há notas sem YAML?
- [ ] Há pastas com nomes ambíguos?
- [ ] Dados sensíveis estão separados?
- [ ] Conteúdo novo está linkado?
- [ ] Migração foi simulada antes de aplicar?

## Próximas melhorias

- Criar auditoria automática de links.
- Criar relatório de notas órfãs.
- Criar inventários por pasta.
- Criar política de dados sensíveis para RAG.
- Atualizar `Vault-Hierarchy-Map` depois da migração física.
