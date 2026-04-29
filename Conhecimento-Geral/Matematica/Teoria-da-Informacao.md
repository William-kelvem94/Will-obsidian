---
title: "Teoria da Informação"
date: 2026-04-29
area: "Matemática para IA"
tags: [conhecimento, conceito, matematica]
related: ["Conhecimento-Geral/Matematica/Probabilidade-e-Estatistica", "Conhecimento-Geral/Psicologia/Vieses-em-LLMs"]
aliases: ["Informação", "Entropia"]
---

# Teoria da Informação

## Definição

A teoria da informação quantifica a incerteza e o conteúdo de mensagens. A entropia de Shannon mede a imprevisibilidade de uma distribuição; a entropia cruzada e a divergência KL medem a distância entre distribuições de probabilidade.

## Contexto Histórico/Filosófico

Claude Shannon formalizou a teoria da informação na década de 1940, estabelecendo uma linguagem comum para comunicação, compressão e codificação. Seu trabalho transformou a forma como medimos o valor e a redundância de sinais.

## Relações com Outros Conceitos
- [[Conhecimento-Geral/Matematica/Probabilidade-e-Estatistica|Probabilidade e Estatística]] — distribuições de probabilidade são o fundamento da entropia.
- [[Conhecimento-Geral/Psicologia/Vieses-em-LLMs|Vieses em LLMs]] — a informação processada por modelos influencia como vieses são amplificados ou reduzidos.
- [[Conhecimento-Geral/Neurociencia/Sistemas-de-Memoria|Sistemas de Memória]] — sistemas de memória eficientes dependem de compressão e recuperação de informação relevante.

## Aplicações Práticas (para IA)

A entropia de Shannon avalia quão imprevisível é uma previsão. A entropia cruzada é usada como função de perda em classificadores e em LLMs para medir a distância entre a distribuição prevista e a distribuição de tokens reais.

A divergência KL aparece em VAEs e outros modelos probabilísticos como um regularizador que força a distribuição latente a se aproximar de uma prior. Informação mútua quantifica dependência entre variáveis, útil para seleção de features e avaliação de representações.

## Referências
- Shannon, C. E.
- Uso de entropia cruzada e KL em redes neurais
- Artigos sobre informação mútua e representação.