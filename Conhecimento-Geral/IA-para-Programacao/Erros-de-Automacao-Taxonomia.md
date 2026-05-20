---
title: Erros de Automacao (Taxonomia)
tags:
  - ia-para-programacao
  - psicologia
  - automacao
  - confiabilidade
type: knowledge_note
created: 2026-05-08
source: internal
---

# Erros de Automacao (Taxonomia)

Contexto: agentes e automacoes falham em padroes repetiveis. Nomear os padroes ajuda a prevenir recorrencias.

## Tipos de erro

### Erro de especificacao
O agente executa algo correto para um requisito errado/incompleto.

Sinais:
- falta de criterios de aceitacao
- ausencia de exemplos e casos limite

Mitigacao:
- transformar requisitos em exemplos concretos (input/output)
- confirmar suposicoes antes de mexer em partes sensiveis

### Erro de contexto
O agente tem contexto insuficiente ou desatualizado.

Sinais:
- paths/names errados
- confusao de versoes

Mitigacao:
- ler arquivos canonicos antes de propor mudanca
- registrar "fonte" do contexto usado (arquivos lidos)

### Erro de execucao
O plano e bom, mas a execucao tem bug (patch errado, comando errado).

Mitigacao:
- validar com teste/compilacao/lint local
- fazer mudancas pequenas e verificaveis

### Erro de verificacao
O agente nao valida o efeito real, so "assume" que funcionou.

Mitigacao:
- padrao: "mudanca + prova"
- checar logs, testes, output e efeitos colaterais

### Erro de seguranca
Exposicao de secrets, dados sensiveis, ou permissao indevida.

Mitigacao:
- regra de "never write secrets"
- revisao explicita de areas sensiveis

## Falhas psicologicas associadas (humanos e agentes)

- Excesso de confianca: agir sem evidencias.
- Aversao a custo: evitar rodar teste "porque demora".
- Efeito tunel: focar em um sintoma e ignorar sistema.

## Template de post-mortem curto

- O que aconteceu?
- Qual tipo de erro foi?
- Qual evidencia foi ignorada?
- Qual verificacao teria capturado antes?
- Qual guardrail vira regra daqui pra frente?

Relacionados:
- [[Conhecimento-Geral/IA-para-Programacao/Higiene-de-Repo-e-Git]]
- [[Conhecimento-Geral/IA-para-Programacao/Engenharia-de-Contexto]]


[[Conhecimento-Geral/IA-para-Programacao/INDEX|← Voltar ao índice de IA para Programação]]
