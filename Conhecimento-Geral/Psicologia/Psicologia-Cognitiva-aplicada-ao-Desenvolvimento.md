---
title: "Psicologia Cognitiva Aplicada ao Desenvolvimento e Design de Sistemas"
description: "Aplicação de carga cognitiva, vieses, atenção e motivação no design de software, agentes e automações."
tags: [psicologia, cognitiva, desenvolvimento, design, IA, produtividade]
date: 2026-05-20
updated: 2026-05-20
---

# Psicologia Cognitiva aplicada ao Desenvolvimento

Esta nota conecta psicologia cognitiva ao design de sistemas. Use junto de [[Psicologia-Cognitiva]], [[Reducao-de-Carga-Cognitiva-para-Programacao]] e [[Checklist-Antivieses-para-Decisoes-Tecnicas]].

## Ideia central

Software não interage com “usuários abstratos”; interage com atenção limitada, memória de trabalho pequena, emoção, hábito e vieses. Sistemas melhores respeitam esses limites.

## Princípios para devs e designers

| Princípio | Implicação prática |
|---|---|
| Memória de trabalho é limitada | reduzir opções simultâneas |
| Atenção é disputada | evitar alertas inúteis |
| Context switching custa caro | agrupar tarefas por fluxo |
| Feedback molda comportamento | mostrar progresso claro |
| Vieses afetam decisão | usar checklist em decisões críticas |

## Aplicação em agentes

Agentes devem:

- explicar incerteza;
- mostrar fontes;
- pedir confirmação para ações irreversíveis;
- resumir próximos passos sem esconder detalhes críticos;
- reduzir carga do usuário, não criar mais decisões.

## Design de fluxo

Bom fluxo:

```text
intenção clara → opções limitadas → execução visível → feedback → possibilidade de desfazer
```

Fluxo ruim:

```text
muitas opções → estado invisível → ação irreversível → erro difícil de rastrear
```

## Checklist antivieses para decisões técnicas

- Estou buscando evidência contrária?
- Estou favorecendo a solução que já conheço?
- O custo de manutenção foi considerado?
- A decisão é reversível?
- Há risco de automação amplificar erro humano?
- O usuário final entenderá o resultado?

## Aplicação no vault

- criar templates com perguntas de decisão;
- manter notas de trade-off;
- usar links para evidências;
- evitar notas duplicadas por impulso;
- transformar aprendizados recorrentes em checklists.

## Links relacionados

- [[Psicologia-Cognitiva]]
- [[Reducao-de-Carga-Cognitiva-para-Programacao]]
- [[Checklist-Antivieses-para-Decisoes-Tecnicas]]
- [[Saude-Mental-e-Foco]]
- [[Neurociencia-do-Habito-Foco-Decisao]]
