---
title: "Arquiteturas de Agentes Cooperativos"
description: "Padrões práticos para coordenar múltiplos agentes no JARVIS sem duplicar trabalho, estourar contexto ou comprometer arquivos do vault."
tags: [multiagente, agentes, orquestracao, engenharia, jarvis, vault, jarvis-engenharia]
date: 2026-05-20
updated: 2026-06-13
---

# Arquiteturas de Agentes Cooperativos

Esta nota complementa [[Arquitetura-Agente]]: em vez de explicar um único agente cognitivo, ela descreve como coordenar vários agentes especializados trabalhando sobre o mesmo vault.

## Quando usar múltiplos agentes

Use arquitetura cooperativa quando a tarefa tiver separação natural de responsabilidades:

- um agente lê conteúdo conceitual;
- outro revisa scripts, automações e integrações;
- outro verifica segurança, duplicidade e impacto no Git;
- um coordenador consolida os resultados e decide o próximo passo.

Evite múltiplos agentes para tarefas lineares, pequenas ou com alto risco de conflito de escrita. Mais agentes aumentam custo de contexto, complexidade de coordenação e chance de duplicação.

## Papéis essenciais

| Papel | Responsabilidade | Pode escrever? |
|---|---|---|
| Coordenador | Define escopo, divide tarefas, consolida decisões e aprova escrita | Sim |
| Explorador | Lê arquivos, mapeia padrões, encontra duplicações | Não |
| Especialista | Produz proposta técnica ou conteúdo de domínio | Preferencialmente não direto |
| Verificador | Confere qualidade, segurança, escopo e regressões | Não |
| Executor | Aplica mudanças aprovadas em arquivos específicos | Sim, com escopo fechado |

A regra prática é simples: **quanto mais autônomo o agente, menor deve ser o escopo de escrita dele**.

## Padrões de coordenação

### 1. Coordenador + especialistas

O coordenador envia subtarefas específicas e recebe relatórios curtos. É o melhor padrão para o vault, porque evita que cada agente carregue o projeto inteiro no contexto.

Fluxo:

```text
pedido do usuário → coordenador → exploradores/especialistas → síntese → edição controlada → verificação
```

### 2. Blackboard / quadro compartilhado

Os agentes não conversam diretamente entre si; todos registram achados em um artefato comum, como uma nota temporária, checklist ou relatório.

Use quando:

- há muitos achados independentes;
- a tarefa exige auditoria posterior;
- você quer rastrear decisões.

Cuidado: o quadro compartilhado não deve virar um `transcript` gigante. Registre apenas decisões e evidências úteis.

### 3. Event-bus local

Um event-bus é uma fila de eventos: `arquivo_lido`, `duplicidade_encontrada`, `mudança_aplicada`, `verificação_falhou`.

No contexto do JARVIS, isso pode ser implementado de forma simples com:

- arquivos JSONL locais;
- fila em memória;
- SQLite;
- Redis local, se houver necessidade real.

Use event-bus quando scripts ou agentes precisam reagir a eventos sem acoplamento direto.

### 4. Revisão adversarial

Depois da execução, um verificador independente tenta provar que a mudança está errada: duplicada, rasa, insegura, fora do escopo ou mal organizada.

Esse padrão é importante para mudanças em várias notas, automações ou dados sensíveis.

## Contrato mínimo entre agentes

Todo agente deve receber:

1. objetivo claro;
2. arquivos permitidos;
3. arquivos proibidos;
4. se pode ou não editar;
5. formato de resposta esperado;
6. limite de profundidade;
7. critério de conclusão.

Exemplo:

```text
Analise somente leitura os arquivos em 04-Conhecimentos/07-Humanidades/Saude.
Não edite nada.
Retorne duplicações, notas relacionadas e recomendação de merge/linkagem.
Limite: 300 palavras.
```

## Controle de custo e contexto

O erro clássico é pedir para vários agentes lerem o vault inteiro. Isso multiplica contexto e pode estourar cota rapidamente.

Boas práticas:

- dividir por pasta ou tema;
- pedir relatórios curtos;
- evitar que agentes leiam logs/transcrições grandes;
- preferir `grep`/busca direcionada antes de leitura completa;
- só carregar arquivos relacionados à decisão atual;
- executar escrita em um único ponto, não em todos os agentes.

## Escrita segura no vault

Para evitar conflitos:

- um único agente deve editar cada arquivo por vez;
- notas novas devem ser criadas apenas após busca por equivalentes;
- arquivos de índice devem ser atualizados conscientemente;
- mudanças em Git devem ser staged por path específico, nunca com `git add .`.

## Aplicação no JARVIS

Padrão recomendado para expansões futuras:

1. Explorador de conteúdo identifica notas existentes e lacunas.
2. Explorador técnico identifica scripts, MCP, RAG e automações relacionadas.
3. Coordenador decide se o melhor é criar nota nova, transformar em índice ou expandir nota existente.
4. Executor edita apenas os arquivos aprovados.
5. Verificador revisa duplicação, links e escopo de commit.

## Links relacionados

- [[Arquitetura-Agente]]
- [[RAG-Local-Guide]]
- [[MCP-Client-Examples]]
- [[Ecossistema-e-Protocolos-MCP]]
- [[Seguranca-e-Governanca-LocalFirst]]
