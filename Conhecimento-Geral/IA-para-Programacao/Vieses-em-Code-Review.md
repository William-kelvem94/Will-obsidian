---
title: Vieses em Code Review
tags:
  - ia-para-programacao
  - psicologia
  - code-review
  - vieses-cognitivos
type: knowledge_note
created: 2026-05-08
source: internal
---

# Vieses em Code Review

Objetivo: reduzir erros de julgamento em reviews (humanos ou com agentes), melhorando qualidade, seguranca e previsibilidade.

## Sintomas comuns

- Review foca em estilo e ignora corretude.
- Review "aprova pela reputacao" do autor.
- Review busca justificar uma opiniao inicial, em vez de testar hipoteses.
- Review acumula muitos pontos pequenos e perde o risco principal.

## Vieses frequentes e contramedidas

### Ancoragem
Definicao: a primeira leitura/interpretacao define o resto do julgamento.

Contramedidas:
- Releia o diff "de tras pra frente" (arquivos mais criticos primeiro).
- Formule 2 explicacoes alternativas do comportamento antes de concluir.

### Confirmacao
Definicao: procurar evidencias que confirmem a tese inicial.

Contramedidas:
- Pergunta obrigatoria: "Como isso poderia falhar em producao?"
- Tente achar um contraexemplo (entrada adversarial, concorrencia, dados nulos).

### Halo (reputacao)
Definicao: confiar demais porque "fulano sempre faz bom codigo".

Contramedidas:
- Exigir verificacao objetiva: testes, invariantes, logs, safe probes.
- Separar julgamento do patch do julgamento da pessoa.

### Status quo / aversao a mudanca
Definicao: preferir nao mexer, mesmo quando o patch reduz risco.

Contramedidas:
- Avaliar risco de nao mudar (custo do bug atual, tempo de manutencao).
- Pedir um "plano de rollback" simples para mudancas maiores.

### Carga cognitiva / fadiga
Definicao: cansaco aumenta aprovacao automatica e reduz deteccao de bugs.

Contramedidas:
- Timebox de review (ex.: 20-30 min), depois pausa.
- Dividir PRs grandes por unidades revisaveis.

## Heuristica de foco (ordem recomendada)

1. Seguranca e dados sensiveis.
2. Corretude (casos limites, invariantes, erro/timeout).
3. Concorrencia (race, idempotencia, retries).
4. Observabilidade (logs, metricas, tracing).
5. Performance e custo.
6. Manutenibilidade (clareza, duplicacao, acoplamento).
7. Estilo e naming.

## Perguntas que reduzem vieses

- Qual e o "contrato" deste codigo (inputs/outputs/invariantes)?
- O que muda em falhas: o sistema falha aberto ou falha fechado?
- Existe uma forma simples de provar o comportamento (teste ou propriedade)?
- Quais sao os piores casos (dados ruins, latencia, concorrencia)?

## Exemplo de comentario RAG-friendly

Formato:
- "Risco:" descreva falha.
- "Evidencia:" aponte trecho e condicao.
- "Mitigacao:" proponha teste ou ajuste.

Relacionados:
- [[Conhecimento-Geral/Psicologia/Vieses-Cognitivos]]
- [[Conhecimento-Geral/IA-para-Programacao/Avaliacao-de-Respostas-de-IA]]


[[Conhecimento-Geral/IA-para-Programacao/INDEX|← Voltar ao índice de IA para Programação]]
