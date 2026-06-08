---
title: "Hub de Operacoes do Vault"
date: 2026-06-07
updated: 2026-06-08
type: moc
status: active
tags: [hub, vault-ops, manutencao, organizacao]
summary: "Hub de manutencao, governanca, migracao fisica e operacoes do Obsidian."
---

# Hub de Operacoes do Vault

Este hub reune as notas de manutencao, governanca e reorganizacao fisica do Obsidian.

## Entradas principais

- [[../07-Operacoes-do-Vault/README|Operacoes do Vault]]
- [[../07-Operacoes-do-Vault/Reestruturacao-Geral-do-Vault]]
- [[../07-Operacoes-do-Vault/Inventario-Inicial-do-Vault]]
- [[../07-Operacoes-do-Vault/Mapa-de-Migracao-Fisica-do-Vault]]
- [[../07-Operacoes-do-Vault/Status-da-Migracao-Fisica]]

## Scripts e atalhos

| Arquivo | Uso |
|---|---|
| `reorganizar-vault-simulacao.bat` | simula a migracao sem mover arquivos |
| `reorganizar-vault-aplicar.bat` | aplica a migracao fisica apos confirmacao |
| `09-Sistema/scripts/reorganizar-vault.ps1` | script PowerShell principal |

## Operacoes importantes

- reorganizacao de pastas;
- atualizacao de links internos;
- manutencao de MOCs;
- revisao de notas orfas;
- padronizacao de YAML;
- limpeza de duplicidades;
- preparo para RAG;
- revisao de dados sensiveis.

## Regras de manutencao

1. Nao mover arquivos em massa sem plano.
2. Nao apagar conteudo sem backup ou justificativa.
3. Preferir migracao por blocos.
4. Atualizar hubs depois de mover conteudo.
5. Revisar links internos.
6. Registrar decisoes importantes.
7. Usar commits em PT-BR com descricao detalhada.
8. Rodar simulacao antes de aplicar migracao fisica.

## Checklist de saude do vault

- [ ] Hubs principais estao atualizados?
- [ ] Links criticos funcionam?
- [ ] README e INDEX refletem a estrutura real?
- [ ] Ha notas duplicadas?
- [ ] Ha notas sem YAML?
- [ ] Ha pastas com nomes ambiguos?
- [ ] Dados sensiveis estao separados?
- [ ] Conteudo novo esta linkado?
- [ ] Migracao foi simulada antes de aplicar?

## Proximas melhorias

- Criar auditoria automatica de links.
- Criar relatorio de notas orfas.
- Criar inventarios por pasta.
- Criar politica de dados sensiveis para RAG.
- Atualizar `Vault-Hierarchy-Map` depois da migracao fisica.
