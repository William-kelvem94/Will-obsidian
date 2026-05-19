---
title: "Onboarding de Agente Externo"
tags: [meta, agente, jarvis, jarvis-sistema]
date: 2026-04-27
updated: 2026-05-08
---

# Como habitar este vault

Este guia e o carregamento minimo para qualquer IA que use o Obsidian como segundo cerebro do JARVIS ou como contexto para programacao.

## Leitura Inicial

1. Leia `JARVIS/README.md` para entender a arquitetura em camadas.
2. Leia `JARVIS/05-System/AGENT-CONTRACT.md` antes de propor ou executar mudancas.
3. Consulte `Graph-Legenda.md` para entender cores e tags.
4. Use os comandos MCP documentados em `JARVIS/05-System/Comandos-JARVIS.md`.
5. Para buscas semanticas, siga `JARVIS/04-Engineering/RAG-Local-Guide.md`.
6. Use `Templates/Template Base.md` para novas notas.
7. Antes de modificar conhecimento canonico, verifique `Conhecimento-Geral/COMO-CONTRIBUIR.md`.

## Regra de Seguranca

Este vault tambem e cerebro para modelos de IA na programacao. Preserve contexto, evite reorganizacoes agressivas e escreva automaticamente apenas nas areas seguras definidas pelo contrato de agentes.

## Antes de Editar

- Verifique se ha mudancas locais no Git.
- Leia o arquivo inteiro antes de alterar.
- Prefira adicionar notas de memoria, decisoes ou improvements em vez de reescrever hubs centrais.
- Quando a mudanca for estrutural, registre a decisao em `JARVIS/02-Operational/Decisions/`.

## Depois de Editar

- Atualize `updated` no frontmatter quando existir.
- Linke a nota nova a pelo menos um hub.
- Rode `python .scripts/vault_cleanup.py --check-only` quando a edicao envolver muitos arquivos.

