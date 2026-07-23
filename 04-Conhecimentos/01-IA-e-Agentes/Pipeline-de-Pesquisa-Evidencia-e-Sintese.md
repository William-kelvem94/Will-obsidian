---
title: "Pipeline de Pesquisa, Evidência e Síntese"
updated: 2026-07-10
type: playbook
status: active
tags: [pesquisa, evidencia, sintese, fontes, inteligencia]
indexavel: true
uso_ia: livre
related: [[../00-Mapas-e-Ontologia/Engenharia-de-Conhecimento-para-Segundo-Cerebro]], [[Avaliacao-de-RAG-e-Qualidade-de-Contexto]]
---

# Pesquisa massiva com economia de tokens

## Fases

1. Formular pergunta, escopo, data de corte e critério de sucesso.
2. Buscar fontes primárias e revisões de qualidade.
3. Fazer triagem rápida por relevância, autoridade e atualidade.
4. Extrair apenas afirmações, dados, definições, métodos e limitações.
5. Comparar convergências, conflitos e condições de validade.
6. Sintetizar em linguagem própria, mantendo citações.
7. Validar números, causalidade, generalizações e lacunas.
8. Persistir fonte, conceitos, síntese, links e registro de expansão.

## Profundidade

| Nível | Uso | Saída |
|---|---|---|
| scan | orientação | mapa de termos e fontes |
| light | fato pontual | resposta com 1–3 fontes |
| medium | decisão | comparação e recomendação |
| deep | domínio | síntese, grafo e lacunas |
| exhaustive | base canônica | revisão, replicação e atualização |

## Regras anti-alucinação

- Separar fato observado, inferência e hipótese.
- Nunca transformar ausência de evidência em evidência de ausência.
- Registrar data de acesso para temas mutáveis.
- Preferir fonte primária; usar secundária para descoberta e contexto.
- Se fontes discordarem, expor o desacordo.

## Registro compacto

```yaml
question: ""
scope: ""
claims: []
sources: []
confidence: low|medium|high
disagreements: []
gaps: []
next_queries: []
```
