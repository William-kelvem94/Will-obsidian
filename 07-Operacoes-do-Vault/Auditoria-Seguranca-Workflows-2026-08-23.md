---
title: Auditoria de segurança dos workflows GitHub Actions
type: auditoria-github-security
status: atual
updated: 2026-08-23
classe_privacidade: operacional
indexavel: true
uso_ia: permitido
---

# Auditoria de workflows e riscos estáticos

- Repositórios auditados: 85
- Repositórios com workflows: 23
- Arquivos encontrados: 90
- Workflows executáveis: 89
- Arquivo inerte: 1 — `AppFlowy-Will/.github/workflows/android_ci.yaml.bak`
- Execuções retornadas: 0
- Falhas runtime confirmadas: nenhuma

## Achados

- 13 arquivos em 8 repositórios contêm valores sensíveis literais ou fixtures que exigem revisão.
- 4 workflows usam `pull_request_target`.
- 16 arquivos em 8 repositórios têm permissões de escrita.
- 72 arquivos usam ações externas não fixadas por SHA.
- 251 referências externas usam tags como `@v4`, `@v5`, `@master` ou `@stable`.
- `persist-credentials: true` foi encontrado em workflows do `Domni` e `Gerenciador_Financeiro-7.0`.
- Dois workflows `workflow_run` foram encontrados no `ruflo`.
- Nenhum padrão `curl | bash` ou `wget | bash` foi identificado.

## Repositórios prioritários para revisão

`Domni`, `Gerenciador_Financeiro-7.0`, `Gerenciador_Financeiro-5.0`, `AFFiNE-Will`, `demandas-organizadas-v2-legacy`, `Criador_de_audios`, `MEU_NECTAR_JARVIS`, `TRANSCRITOR`, `ruflo` e `pixel-agents`.

## Limitação

O conector não retornou IDs de execuções para jobs/logs. Portanto, não é possível confirmar sucesso ou falha runtime apenas com esta sessão.
