---
title: "Operacoes do Vault"
date: 2026-06-08
updated: 2026-06-08
type: moc
status: active
tags: [vault, operacoes, migracao, auditoria, governanca]
summary: "Ponto canonico para inventarios, migracao fisica, auditoria, manutencao e saude do vault."
---

# Operacoes do Vault

Esta pasta concentra a governanca operacional do vault. Aqui vivem os mapas de migracao, inventarios, status e registros de manutencao que ajudam a manter a estrutura numerada coerente.

## O que fica aqui

- inventarios iniciais e inventarios por dominio;
- mapa de migracao fisica;
- status da migracao;
- planos de reorganizacao;
- auditorias de links e notas orfas;
- runbooks de manutencao;
- checklists de saude do vault;
- registros de decisoes de organizacao.

## Documentos centrais

- [[Reestruturacao-Geral-do-Vault]]
- [[Inventario-Inicial-do-Vault]]
- [[Mapa-de-Migracao-Fisica-do-Vault]]
- [[Status-da-Migracao-Fisica]]

## Relacao com os hubs

- [[../01-Hubs/Hub-Operacoes-do-Vault|Hub de Operacoes]]
- [[../01-Hubs/README|Hubs Centrais]]
- [[../Bem-vindo|Neural Hub]]

## Camadas de conteudo

| Camada | Papel | Onde mora |
|---|---|---|
| Evidencia bruta | fonte original, recorte, captura | `11-Dados-Brutos/` |
| Sintese curada | conhecimento organizado e notas canonicas | `04-Conhecimentos/` |
| Regra e sistema | contratos, esquemas, agentes e automacoes | `09-Sistema/` |

## Regra operacional

1. Mapear antes de mover.
2. Migrar em blocos pequenos.
3. Preservar links antigos ate a reconciliacao.
4. Validar navegacao no Obsidian depois de cada bloco.
5. Arquivar legado somente depois de confirmar o novo caminho canonico.

## Itens de manutencao recomendados

- criar auditoria de links quebrados;
- criar relatorio de notas orfas;
- criar mapa visual dos dominios;
- registrar decisoes importantes em ADRs ou notas de operacao;
- revisar periodicamente o equilibrio entre raw, wiki e schema.
