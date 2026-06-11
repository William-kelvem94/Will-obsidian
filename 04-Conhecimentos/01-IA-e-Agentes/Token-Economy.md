---
title: "Token Economy"
date: 2026-06-07
updated: 2026-06-07
type: guide
status: active
tags: [conhecimento-geral, ia, token-economy, contexto, rag]
related: [[Prompt-Engineering]], [[RAG-e-Memoria-para-Agentes]], [[../00-Mapas-e-Ontologia/00-Como-usar-este-vault-com-IA]]
summary: "Estratégias para reduzir tokens, melhorar contexto e tornar interações com IA mais baratas, rápidas e precisas."
---

# Token Economy

Token economy é a prática de gastar menos contexto para obter respostas melhores. Em IA, mais texto nem sempre significa mais precisão. Contexto demais pode gerar ruído.

## Objetivo

Reduzir repetição, custo, lentidão, perda de foco e confusão causada por excesso de informações.

Aumentar precisão, reuso de conhecimento, velocidade de resposta e consistência entre sessões.

## Técnicas principais

### 1. Resumos canônicos

Criar uma nota curta que represente um assunto complexo. Outras notas linkam para ela.

Exemplo: em vez de explicar RAG em toda nota, linkar para [[RAG-e-Memoria-para-Agentes]].

### 2. Contexto em camadas

Enviar primeiro o resumo. Só enviar detalhes quando necessário.

Camadas úteis:

1. resumo de poucas linhas;
2. nota principal;
3. anexos técnicos;
4. logs completos.

### 3. Notas atômicas

Cada nota deve conter um conceito ou procedimento. Isso facilita recuperar só o necessário.

### 4. Índices MOC

MOCs funcionam como mapas. Eles ajudam humanos e IA a navegar sem ler tudo.

### 5. Tabelas de decisão

Tabelas comprimem critérios e reduzem explicações longas.

### 6. Vocabulário consistente

Usar sempre os mesmos nomes: `RAG`, `memória episódica`, `playbook`, `MOC`, `chunk`, `vault`. Isso melhora busca semântica.

## Resumo para IA

Toda nota importante pode ter uma seção com:

- tema;
- objetivo;
- conceitos principais;
- decisões;
- riscos;
- links essenciais.

## Como evitar desperdício de tokens

| Problema | Sinal | Correção |
|---|---|---|
| contexto duplicado | mesma explicação em várias notas | criar nota canônica |
| contexto antigo | decisões conflitantes | registrar `updated` e status |
| contexto longo | resposta perde foco | usar MOC primeiro |
| contexto vago | resposta genérica | adicionar objetivo e critérios |
| contexto misturado | resposta confusa | separar pessoal, técnico e projeto |

## Notas boas para economia

Uma nota econômica tem título descritivo, YAML preenchido, resumo curto, cabeçalhos claros, exemplos mínimos, links para aprofundamento, decisões explícitas e pouca repetição.

## Exemplo de compressão

Versão longa: o sistema deve usar Docker porque evita instalar pacotes no Windows, isola ambientes, facilita reprodução e reduz erro de dependência.

Versão compacta: decisão: preferir Docker para desenvolvimento local no Windows. Motivo: isolamento, reprodutibilidade e menor conflito de dependências.

## Regra 80/20

Para a maioria das tarefas, a IA precisa de pouco histórico e muita clareza sobre objetivo, restrições e estado atual.

## Links internos

- [[Prompt-Engineering]]
- [[RAG-e-Memoria-para-Agentes]]
- [[../03-Dados-e-Analytics/Taxonomia-Metadados-e-Ontologia]]
- [[../99-Templates/Template-Nota-Atomica]]
