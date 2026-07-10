---
title: "Inventário Atual e Governança do Vault"
date: 2026-06-07
updated: 2026-07-10
type: inventory
status: active
tags: [vault-ops, inventario, governanca, canonico, migracao]
summary: "Inventário operacional da estrutura canônica atual do WILL-OBSIDIAN após a migração física."
---

# Inventário Atual e Governança do Vault

## Estado atual

A estrutura numerada foi criada e os principais blocos foram migrados para caminhos canônicos. A partir de agora, a organização deve tratar as áreas numeradas como fonte oficial. Pastas legadas permanecem apenas para compatibilidade, auditoria ou preservação histórica.

## Áreas canônicas

| Área | Função | Indexação padrão |
|---|---|---:|
| `00-Inbox/` | captura e triagem | não |
| `01-Hubs/` | navegação e mapas | sim |
| `02-JARVIS/` | identidade, memória, agentes e aprendizado | sim, seletiva |
| `03-Projetos/` | execução, decisões e portfólio | sim, seletiva |
| `04-Conhecimentos/` | conhecimento curado e reutilizável | sim |
| `05-Skills/` | capacidades, workflows e playbooks | sim |
| `06-Will-Pessoal/` | contexto pessoal e sensível | não por padrão |
| `07-Operacoes-do-Vault/` | governança, auditoria e manutenção | sim |
| `08-Arquivo/` | legado e histórico | não |
| `09-Sistema/` | schemas, agentes, scripts e testes | seletiva |
| `10-Interfaces/` | dashboards, canvases e painéis | seletiva |
| `11-Dados-Brutos/` | fontes e material sem curadoria | não por padrão |
| `99-Templates/` | modelos reutilizáveis | não |

## Regras de organização

1. Conteúdo novo entra somente em caminho canônico.
2. Conhecimento curado fica em `04-Conhecimentos/`.
3. Fontes originais ficam em `11-Dados-Brutos/`.
4. Skills ficam em `05-Skills/`; mirrors em `.agents/05-Skills/` e `.continue/05-Skills/` exigem controle de drift.
5. Regras, schemas e configurações ficam em `09-Sistema/`.
6. Legado não deve ser duplicado nem indexado como conhecimento atual.
7. Conteúdo pessoal permanece restrito por padrão.
8. Cada nota importante deve declarar status, privacidade, indexação e origem quando aplicável.

## Pendências de auditoria

- validar links internos e notas órfãs;
- comparar hubs com a árvore física real;
- identificar duplicatas entre áreas legadas e canônicas;
- verificar drift entre skills canônicas e mirrors;
- revisar frontmatter em lotes;
- atualizar dashboards e consultas Dataview para os caminhos atuais;
- registrar cada lote de expansão no Registro de Expansão de Conhecimentos Gerais.

## Fonte técnica

- [[Mapa-de-Migracao-Fisica-do-Vault]]
- [[Status-da-Migracao-Fisica]]
- [[../09-Sistema/schema/Politica-de-Privacidade-e-Indexacao]]
- [[../09-Sistema/config/indexer_config.json]]
