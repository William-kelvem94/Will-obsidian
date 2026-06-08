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

## Rotas principais

### Núcleo do hub

- [[00-Mapa-de-Lacunas-e-Roadmap]] — auditoria crítica, lacunas e plano de expansão.
- [[00-Ontologia-de-Conhecimento-para-IA]] — entidades, relações e regras para IA interpretar o vault.
- [[00-Como-usar-este-vault-com-IA]] — guia operacional para usar o vault com qualquer IA.

### IA e agentes

- [[01-IA/Modelos-de-Linguagem-LLMs]] — nota canônica sobre LLMs.
- [[01-IA/Prompt-Engineering]] — como formular pedidos melhores.
- [[01-IA/Context-Engineering]] — como montar contexto útil para IA.
- [[01-IA/RAG-e-Memoria-para-Agentes]] — RAG, memória e agentes.
- [[01-IA/Embeddings-e-Busca-Semantica]] — vetores e busca semântica.
- [[01-IA/Avaliacao-de-RAG-e-Qualidade-de-Contexto]] — avaliação de recuperação e contexto.
- [[01-IA/Agentes-Autonomos-e-Workflows]] — agentes, ferramentas e execução.
- [[01-IA/Avaliacao-de-Respostas-de-IA]] — checklist para avaliar respostas.
- [[01-IA/IA-Local-Ollama-e-Modelos-Abertos]] — IA local, Ollama e modelos abertos.
- [[01-IA/Token-Economy]] — economia de tokens e contexto.

### Engenharia de software

- [[02-Engenharia-Software/Arquitetura-Web-Moderna]] — arquitetura web fullstack.
- [[02-Engenharia-Software/APIs-Backend-Banco]] — APIs, backend e banco.
- [[02-Engenharia-Software/Docker-e-DevOps]] — Docker e práticas DevOps.
- [[02-Engenharia-Software/Linux-Terminal-e-Shell]] — terminal, processos, permissões e logs.
- [[02-Engenharia-Software/Git-e-Controle-de-Versao]] — Git, commits, branches e fluxo.
- [[02-Engenharia-Software/TypeScript-e-JavaScript-Moderno]] — JS moderno e TypeScript.
- [[02-Engenharia-Software/React-Next-e-Frontend-Moderno]] — frontend moderno com React/Next.
- [[02-Engenharia-Software/Testes-e-Qualidade-de-Software]] — testes e qualidade.
- [[02-Engenharia-Software/Sistemas-Distribuidos-e-Escalabilidade]] — escala, cache, filas e trade-offs.
- [[02-Engenharia-Software/Observabilidade-Logs-e-Monitoramento]] — logs, métricas e diagnóstico.
- [[02-Engenharia-Software/Design-Patterns-e-Arquitetura-Limpa]] — patterns e arquitetura limpa.

### Estudos, produtividade e decisão

- [[03-Estudos/Metodo-de-Estudo-Ativo]] — estudo ativo e prática.
- [[03-Estudos/Ciencia-da-Aprendizagem]] — revisão, memória e aprendizagem aplicada.
- [[04-Produtividade/Decisao-e-Priorizacao]] — decisões e priorização.
- [[04-Produtividade/Revisao-Semanal-e-Gestao-de-Energia]] — revisão semanal e energia.

### Dados

- [[05-Dados/Taxonomia-Metadados-e-Ontologia]] — taxonomia e metadados.
- [[05-Dados/Banco-de-Dados-Avancado]] — índices, transações e performance.
- [[05-Dados/SQL-Avancado-e-Consultas]] — SQL, joins, CTEs e janelas.
- [[05-Dados/Analytics-ETL-e-Qualidade-de-Dados]] — analytics, ETL e qualidade.

### Habilidades, segurança e redes

- [[06-Habilidades/Mapa-de-Habilidades]] — mapa de competências.
- [[07-Seguranca/Seguranca-da-Informacao]] — fundamentos de segurança.
- [[07-Seguranca/OWASP-e-Seguranca-Web]] — segurança web e APIs.
- [[07-Seguranca/Threat-Modeling-e-Gestao-de-Riscos]] — modelagem de ameaça e risco.
- [[08-Redes/Redes-e-Internet]] — redes, DNS, HTTP, portas e diagnóstico.

### Produto, matemática, carreira e vida prática

- [[09-Produto-UX/Produto-UX-e-Validacao]] — produto, UX e validação.
- [[10-Matematica/Matematica-Aplicada-a-Computacao]] — matemática aplicada a computação.
- [[11-Carreira/Carreira-Tech-e-Portifolio]] — carreira tech e portfólio.
- [[12-Saude-Rotina/Saude-Rotina-e-Rastreamento]] — rotina, sintomas e registros.
- [[13-Financas/Financas-Pessoais-e-Metricas]] — finanças pessoais e métricas.
- [[14-Comunicacao/Comunicacao-Clara-e-Reunioes]] — comunicação e reuniões.

### Documentação e humanidades

- [[15-Documentacao/Documentacao-Tecnica-Runbooks-e-ADRs]] — README, runbooks e ADRs.
- [[16-Humanidades/Pensamento-Critico-e-Logica-Informal]] — pensamento crítico e argumentação.
- [[16-Humanidades/Filosofia-Pratica-para-Decisoes]] — valores, consequências e decisões.

### Templates

- [[99-Templates/Template-Nota-Atomica]] — modelo de nota atômica.
- [[99-Templates/Template-ADR-Decisao-Arquitetural]] — modelo de decisão arquitetural.
- [[99-Templates/Template-Runbook-Operacional]] — modelo de runbook operacional.

## Estrutura

```txt
Conhecimentos-Gerais/
├── README.md
├── INDEX.md
├── 00-Mapa-de-Lacunas-e-Roadmap.md
├── 00-Ontologia-de-Conhecimento-para-IA.md
├── 00-Como-usar-este-vault-com-IA.md
├── 01-IA/
│   ├── Modelos-de-Linguagem-LLMs.md
│   ├── Prompt-Engineering.md
│   ├── Context-Engineering.md
│   ├── RAG-e-Memoria-para-Agentes.md
│   ├── Embeddings-e-Busca-Semantica.md
│   ├── Avaliacao-de-RAG-e-Qualidade-de-Contexto.md
│   ├── Agentes-Autonomos-e-Workflows.md
│   ├── Avaliacao-de-Respostas-de-IA.md
│   ├── IA-Local-Ollama-e-Modelos-Abertos.md
│   └── Token-Economy.md
├── 02-Engenharia-Software/
│   ├── Arquitetura-Web-Moderna.md
│   ├── APIs-Backend-Banco.md
│   ├── Docker-e-DevOps.md
│   ├── Linux-Terminal-e-Shell.md
│   ├── Git-e-Controle-de-Versao.md
│   ├── TypeScript-e-JavaScript-Moderno.md
│   ├── React-Next-e-Frontend-Moderno.md
│   ├── Testes-e-Qualidade-de-Software.md
│   ├── Sistemas-Distribuidos-e-Escalabilidade.md
│   ├── Observabilidade-Logs-e-Monitoramento.md
│   └── Design-Patterns-e-Arquitetura-Limpa.md
├── 03-Estudos/
│   ├── Metodo-de-Estudo-Ativo.md
│   └── Ciencia-da-Aprendizagem.md
├── 04-Produtividade/
│   ├── Decisao-e-Priorizacao.md
│   └── Revisao-Semanal-e-Gestao-de-Energia.md
├── 05-Dados/
│   ├── Taxonomia-Metadados-e-Ontologia.md
│   ├── Banco-de-Dados-Avancado.md
│   ├── SQL-Avancado-e-Consultas.md
│   └── Analytics-ETL-e-Qualidade-de-Dados.md
├── 06-Habilidades/
│   └── Mapa-de-Habilidades.md
├── 07-Seguranca/
│   ├── Seguranca-da-Informacao.md
│   ├── OWASP-e-Seguranca-Web.md
│   └── Threat-Modeling-e-Gestao-de-Riscos.md
├── 08-Redes/
│   └── Redes-e-Internet.md
├── 09-Produto-UX/
│   └── Produto-UX-e-Validacao.md
├── 10-Matematica/
│   └── Matematica-Aplicada-a-Computacao.md
├── 11-Carreira/
│   └── Carreira-Tech-e-Portifolio.md
├── 12-Saude-Rotina/
│   └── Saude-Rotina-e-Rastreamento.md
├── 13-Financas/
│   └── Financas-Pessoais-e-Metricas.md
├── 14-Comunicacao/
│   └── Comunicacao-Clara-e-Reunioes.md
├── 15-Documentacao/
│   └── Documentacao-Tecnica-Runbooks-e-ADRs.md
├── 16-Humanidades/
│   ├── Pensamento-Critico-e-Logica-Informal.md
│   └── Filosofia-Pratica-para-Decisoes.md
└── 99-Templates/
    ├── Template-Nota-Atomica.md
    ├── Template-ADR-Decisao-Arquitetural.md
    └── Template-Runbook-Operacional.md
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
type: guide | concept | moc | template | checklist | playbook | roadmap | runbook | decision
status: active
tags: [conhecimento-geral, area, subarea]
related: [[Outra nota]], [[Mais uma nota]]
summary: "Resumo curto para humanos e IA."
```

## Consulta rápida para IA

Ao usar uma IA, enviar primeiro:

> Use este vault como base de conhecimento. Priorize notas em `Conhecimentos-Gerais`, respeite os links internos, evite repetir conceitos já definidos e responda com base nos arquivos mais específicos antes dos genéricos.

## Relação com o JARVIS

Esta pasta alimenta o JARVIS como camada de conhecimento estável. Memórias pessoais e estados atuais ficam em `JARVIS/`, enquanto conhecimento técnico, estudo, IA, métodos, rotinas, finanças, comunicação, documentação e habilidades ficam aqui.

## Próximas expansões recomendadas

- Python avançado.
- FastAPI, NestJS e Prisma em notas separadas.
- Redes avançadas e VPN.
- Criptografia prática.
- Prompt engineering por domínio.
- Projetos guiados por trilha.
- Templates para reunião, bug report, postmortem e estudo.
