---
title: "Ontologia de Conhecimento para IA"
date: 2026-06-07
updated: 2026-06-07
type: guide
status: active
tags: [conhecimento-geral, ontologia, ia, rag, taxonomia]
related: [[00-Mapa-de-Lacunas-e-Roadmap]], [[05-Dados/Taxonomia-Metadados-e-Ontologia]], [[01-IA/RAG-e-Memoria-para-Agentes]], [[01-IA/Context-Engineering]]
summary: "Define entidades, relações e padrões para que o vault seja compreensível por humanos e agentes de IA."
---

# Ontologia de Conhecimento para IA

Esta nota define como o conhecimento deve ser representado no vault para ser útil a humanos e agentes de IA.

## Objetivo

Transformar notas soltas em uma rede de conceitos, decisões, procedimentos, projetos, evidências e templates.

## Entidades principais

| Entidade | Definição | Exemplo |
|---|---|---|
| conceito | ideia ou definição reutilizável | LLM, RAG, cache |
| guia | explicação estruturada | Docker e DevOps |
| playbook | procedimento para resolver problema | debug de API |
| template | modelo reutilizável | ADR, runbook |
| decisão | escolha registrada | usar PostgreSQL |
| projeto | iniciativa em andamento | JARVIS |
| evidência | dado que sustenta análise | log, métrica, reunião |
| habilidade | competência a desenvolver | SQL, React, comunicação |
| risco | possibilidade de perda ou falha | token exposto |
| métrica | indicador definido | taxa de erro |

## Relações recomendadas

| Relação | Uso |
|---|---|
| `related` | notas próximas |
| `depends_on` | pré-requisito |
| `used_by` | onde o conceito é aplicado |
| `solves` | problema resolvido |
| `risks` | riscos associados |
| `evidence` | fontes ou provas |
| `template_for` | tipo de nota gerada |
| `supersedes` | substitui versão antiga |
| `decision_for` | projeto ou tema afetado |

## Tipos de nota

| Tipo | Quando usar |
|---|---|
| `concept` | para definição canônica |
| `guide` | para explicação ampla |
| `playbook` | para passo a passo operacional |
| `checklist` | para revisão rápida |
| `moc` | para mapa de conteúdo |
| `template` | para modelo reutilizável |
| `roadmap` | para plano de evolução |
| `decision` | para registrar escolha |
| `runbook` | para operação e recuperação |

## Padrão de granularidade

- conceito pequeno vira `concept`;
- tema amplo vira `guide`;
- ação repetível vira `playbook`;
- operação crítica vira `runbook`;
- escolha importante vira `decision`;
- conjunto de notas vira `moc`.

## Regras para IA

Ao usar o vault:

1. Preferir nota específica antes de nota geral.
2. Preferir nota com `updated` mais recente.
3. Preservar distinção entre fato, decisão, hipótese e opinião.
4. Não tratar template como evidência.
5. Não tratar log bruto como conhecimento curado sem validação.
6. Usar MOCs para navegar, não como fonte única.
7. Quando houver conflito, apontar conflito.

## Vocabulário controlado

Termos que devem ser usados de forma consistente:

- LLM;
- RAG;
- embedding;
- chunk;
- MOC;
- playbook;
- runbook;
- ADR;
- contexto;
- decisão;
- evidência;
- risco;
- métrica.

## Checklist de nova nota

- [ ] Tipo correto definido?
- [ ] Relações internas adicionadas?
- [ ] Resumo para IA existe?
- [ ] O conteúdo não duplica nota canônica?
- [ ] Links apontam para conceitos mais profundos?
- [ ] A nota ajuda alguma tarefa real?

## Resumo para IA

Esta ontologia orienta como interpretar o vault. Ao responder, identificar tipo da nota, relação com outras notas e confiabilidade do conteúdo antes de usar como base.

## Links internos

- [[00-Mapa-de-Lacunas-e-Roadmap]]
- [[05-Dados/Taxonomia-Metadados-e-Ontologia]]
- [[01-IA/RAG-e-Memoria-para-Agentes]]
- [[01-IA/Context-Engineering]]
