---
title: Status operacional GitHub — issues workflows releases
type: auditoria-github
status: atual
updated: 2026-08-22
classe_privacidade: operacional
indexavel: true
uso_ia: permitido
---

# Status operacional GitHub

## Issues abertas

A busca autenticada consolidada nos **85 repositórios** retornou **0 issues abertas** no momento da coleta.

## Workflows

A tentativa de enumerar workflows pela rota pública do conector não retornou uma coleção normalizada. A presença de `.github` na raiz foi registrada no arquivo de branches e estrutura, mas isso não prova a existência ou o estado de workflows. Não foram inventados nomes ou status de CI.

## Releases e tags

As URLs oficiais de releases e tags foram registradas nas fichas técnicas. A listagem individual não foi exposta pela rota pública do conector neste lote; portanto, a ausência de dados aqui não significa que o repositório não tenha releases ou tags.

## Dependências

A coleta de manifestos foi concluída para 55 repositórios, com 105 arquivos detectados na raiz. O conteúdo está em [[11-Dados-Brutos/GitHub/Dependencias-e-Manifestos-2026-08-22]]. Dependências em subpastas e transitivas ainda exigem auditoria recursiva.

## Próxima ação técnica

Para fechar completamente esta camada, é necessário executar uma coleta com acesso recursivo aos endpoints autenticados de Actions, releases, tags, commits e árvore Git. As limitações do conector atual estão registradas para evitar que o vault trate ausência de retorno como ausência de recurso.
