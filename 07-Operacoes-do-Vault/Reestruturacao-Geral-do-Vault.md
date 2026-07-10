---
title: "Reestruturação Geral do Vault"
date: 2026-06-07
updated: 2026-06-07
type: roadmap
status: active
tags: [vault-ops, reestruturacao, organizacao, migracao]
related: [[../01-Hubs/README]], [[../01-Hubs/Hub-Operacoes-do-Vault]], [[../Bem-vindo]], [[../Vault-Hierarchy-Map]]
summary: "Plano seguro para reorganizar a estrutura geral do Obsidian sem perda de conteúdo e sem quebrar links de forma descontrolada."
---

# Reestruturação Geral do Vault

Esta nota define como reorganizar o Obsidian com segurança. O objetivo é melhorar a arquitetura sem perder conteúdo, sem quebrar links em massa e sem transformar o vault em um labirinto.

## Diagnóstico

O vault tem uma base forte, mas cresceu de forma orgânica. Existem bons pilares, porém alguns nomes e fronteiras podem gerar confusão.

## Problemas principais

| Problema | Impacto | Correção proposta |
|---|---|---|
| `Conhecimentos-Gerais` e `Conhecimento-Geral` parecem duplicados | confusão de navegação | consolidar em hub e migrar depois |
| hubs antigos e novos coexistem | entrada dispersa | usar `01-Hubs` como camada superior |
| templates espalhados | difícil reutilizar | centralizar navegação em Hub de Templates |
| projetos e estudos se misturam | perda de foco | separar conhecimento estável de execução |
| dados pessoais podem se misturar com RAG | risco de contexto sensível | criar política de sensibilidade |

## Estrutura atual preservada

Por enquanto, estas áreas continuam existindo:

```txt
02-JARVIS/
Projetos/
05-Skills/
04-Conhecimentos/
04-Conhecimentos/07-Humanidades/
Will-Pessoal/
Vault-Ops
Master-Glossary
Graph-Legenda
Vault-Hierarchy-Map
```

## Estrutura de navegação criada

A nova navegação fica em:

```txt
01-Hubs/
├── README.md
├── Hub-Conhecimentos.md
├── Hub-JARVIS.md
├── Hub-Projetos.md
├── Hub-Skills.md
├── Hub-Will-Pessoal.md
├── Hub-Operacoes-do-Vault.md
└── Hub-Templates.md
```

## Estrutura-alvo futura

A reorganização física ideal pode seguir este desenho:

```txt
00-Inbox/
01-Hubs/
02-JARVIS/
03-Projetos/
04-Conhecimentos/
05-Skills/
06-Will-Pessoal/
07-Operacoes-do-Vault/
08-Arquivo/
99-Templates/
```

## Estrutura futura de conhecimentos

```txt
04-Conhecimentos/
├── 00-Mapas-e-Ontologia/
├── 01-IA-e-Agentes/
├── 02-Engenharia-de-Software/
├── 03-Dados-e-Analytics/
├── 04-Seguranca-e-Redes/
├── 05-Produto-UX-e-Carreira/
├── 06-Estudos-e-Aprendizagem/
├── 07-Humanidades/
├── 08-Vida-Pratica/
└── 99-Templates/
```

## Estratégia de migração segura

### Fase 1 - Hubs

Status: iniciada.

- criar `01-Hubs`;
- atualizar `Bem-vindo.md`;
- criar hubs por domínio;
- não mover conteúdo ainda.

### Fase 2 - Inventário

Criar inventário das pastas atuais:

- caminho;
- função;
- manter, mover, arquivar ou revisar;
- links críticos;
- risco de sensibilidade;
- prioridade.

### Fase 3 - Migração por blocos

Mover apenas um domínio por vez:

1. conhecimentos técnicos;
2. humanidades;
3. templates;
4. operações;
5. projetos;
6. JARVIS;
7. Will-Pessoal.

### Fase 4 - Atualização de links

Depois de cada bloco:

- atualizar hubs;
- atualizar README e INDEX;
- revisar links internos;
- criar nota redirect se necessário;
- verificar grafo.

### Fase 5 - Arquivamento

Apenas depois da validação:

- mover duplicados para `08-Arquivo`;
- preservar histórico;
- documentar decisão;
- nunca apagar sem motivo claro.

## Regras de migração

- Não mover em massa sem inventário.
- Não apagar conteúdo útil.
- Não renomear sem atualizar links.
- Não misturar conhecimento técnico com memória pessoal.
- Não indexar dados sensíveis sem revisão.
- Todo commit deve ser em PT-BR e detalhado.
- Cada etapa precisa deixar o vault utilizável.

## Checklist antes de mover arquivos

- [ ] O destino está claro?
- [ ] Os links de origem foram mapeados?
- [ ] O conteúdo tem sensibilidade?
- [ ] Existe hub apontando para o novo local?
- [ ] Há risco de duplicidade?
- [ ] O commit descreve a mudança em PT-BR?

## Decisão atual

A decisão atual é **organizar primeiro por hubs**, preservar a estrutura física existente e mover conteúdo apenas depois de inventário. Essa abordagem reduz risco e evita perda de conteúdo.

## Próxima ação recomendada

Criar `Inventario-do-Vault.md` listando todas as pastas principais, função, destino futuro e prioridade de migração.
