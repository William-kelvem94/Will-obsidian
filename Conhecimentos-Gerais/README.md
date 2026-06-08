---
title: "Conhecimentos Gerais"
date: 2026-06-07
updated: 2026-06-07
type: moc
tags: [conhecimento-geral, moc, ia, estudos, rag, token-economy]
summary: "Hub central de conhecimento reutilizável para estudos, agentes de IA, economia de tokens e expansão do vault."
---

# Conhecimentos Gerais

Este diretório é a camada de **conhecimento amplo, reutilizável e amigável para IA** do vault. Ele existe para reduzir retrabalho, economizar tokens, acelerar estudos futuros e servir como base de consulta para qualquer agente: ChatGPT, Gemini, Claude, modelos locais, JARVIS, pipelines RAG ou scripts próprios.

## Objetivo

Criar uma base de conhecimento que funcione em três níveis:

1. **Humano:** notas claras, estudáveis e fáceis de revisar.
2. **IA:** contexto estruturado para respostas melhores, com menos tokens desperdiçados.
3. **Sistema:** dados em Markdown com YAML, links internos, taxonomia e granularidade adequada para indexação vetorial.

## Como usar

- Para pedir ajuda a uma IA, comece por [[00-Como-usar-este-vault-com-IA]].
- Para melhorar prompts, consulte [[01-IA/Prompt-Engineering]].
- Para RAG, memória e agentes, consulte [[01-IA/RAG-e-Memoria-para-Agentes]].
- Para economizar tokens, consulte [[01-IA/Token-Economy]].
- Para arquitetura de sistemas, consulte [[02-Engenharia-Software/Arquitetura-Web-Moderna]].
- Para Docker e DevOps, consulte [[02-Engenharia-Software/Docker-e-DevOps]].
- Para backend, APIs e bancos, consulte [[02-Engenharia-Software/APIs-Backend-Banco]].
- Para aprender melhor, consulte [[03-Estudos/Metodo-de-Estudo-Ativo]].
- Para decidir e priorizar, consulte [[04-Produtividade/Decisao-e-Priorizacao]].
- Para organizar dados, consulte [[05-Dados/Taxonomia-Metadados-e-Ontologia]].
- Para mapa de habilidades, consulte [[06-Habilidades/Mapa-de-Habilidades]].
- Para criar novas notas consistentes, use [[99-Templates/Template-Nota-Atomica]].

## Estrutura

```txt
Conhecimentos-Gerais/
├── README.md
├── 00-Como-usar-este-vault-com-IA.md
├── 01-IA/
│   ├── Prompt-Engineering.md
│   ├── RAG-e-Memoria-para-Agentes.md
│   └── Token-Economy.md
├── 02-Engenharia-Software/
│   ├── Arquitetura-Web-Moderna.md
│   ├── Docker-e-DevOps.md
│   └── APIs-Backend-Banco.md
├── 03-Estudos/
│   └── Metodo-de-Estudo-Ativo.md
├── 04-Produtividade/
│   └── Decisao-e-Priorizacao.md
├── 05-Dados/
│   └── Taxonomia-Metadados-e-Ontologia.md
├── 06-Habilidades/
│   └── Mapa-de-Habilidades.md
└── 99-Templates/
    └── Template-Nota-Atomica.md
```

## Princípios da pasta

### 1. Conhecimento modular

Cada nota deve responder a uma pergunta, resolver um problema ou guardar um conceito. Notas gigantes só devem existir quando forem índices, guias ou mapas.

### 2. Contexto reutilizável

Uma nota boa deve poder ser colada em uma conversa com IA e ainda fazer sentido. Ela precisa ter definição, contexto, exemplos, critérios e links.

### 3. Economia de tokens

A pasta deve evitar repetir explicações longas. Quando um conceito já existir, outras notas devem linkar para ele em vez de reexplicar tudo.

### 4. Indexação por IA

As notas usam YAML, títulos objetivos, listas, tabelas e blocos de decisão para facilitar chunking, busca semântica e resposta por agentes.

### 5. Ponte entre estudo e execução

Cada área deve conter conceitos, mas também aplicação prática: comandos, checklists, exemplos, critérios de decisão e erros comuns.

## Convenção de metadados

```yaml
title: "Nome da nota"
date: 2026-06-07
updated: 2026-06-07
type: guide | concept | moc | template | checklist | playbook
status: active
tags: [conhecimento-geral, area, subarea]
related: [[Outra nota]], [[Mais uma nota]]
summary: "Resumo curto para humanos e IA."
```

## Consulta rápida para IA

Ao usar uma IA, enviar primeiro:

> Use este vault como base de conhecimento. Priorize notas em `Conhecimentos-Gerais`, respeite os links internos, evite repetir conceitos já definidos e responda com base nos arquivos mais específicos antes dos genéricos.

## Relação com o JARVIS

Esta pasta alimenta o JARVIS como camada de conhecimento estável. Memórias pessoais e estados atuais ficam em `JARVIS/`, enquanto conhecimento técnico, estudo, IA, métodos e habilidades ficam aqui.

## Próximas expansões recomendadas

- Segurança da informação.
- Redes e infraestrutura.
- Banco de dados avançado.
- Engenharia de prompts por domínio.
- Matemática aplicada à computação.
- Psicologia cognitiva para estudos.
- Finanças pessoais e métricas.
- Saúde, rotina e rastreamento de sintomas.
- Templates para reuniões, decisões e debugging.
