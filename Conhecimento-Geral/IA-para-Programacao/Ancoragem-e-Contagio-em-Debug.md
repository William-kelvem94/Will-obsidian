---
title: Ancoragem e Contagio em Debug
tags:
  - ia-para-programacao
  - psicologia
  - debugging
  - vieses-cognitivos
type: knowledge_note
created: 2026-05-08
source: internal
---

# Ancoragem e Contagio em Debug

Ancoragem: a primeira hipotese cola. Contagio: a hipotese de outra pessoa/commit vira "verdade" e guia tudo.

## Como isso aparece

- "Deve ser cache" vira explicacao padrao para qualquer sintoma.
- Um comentario no PR vira narrativa oficial, mesmo sem evidencia.
- O time repete o mesmo experimento inutil porque "foi assim da outra vez".

## Contramedidas praticas

- Hipoteses concorrentes: manter 2-3 hipoteses vivas ate ter evidencias.
- Experimentos discriminatorios: testes que diferenciam hipoteses, nao confirmam.
- Registro de evidencia: anotar "observacao -> conclusao" explicitamente.

## Perguntas que quebram ancoragem

- Se a minha hipotese estiver errada, que sinal eu esperaria ver?
- Qual outra area do sistema poderia produzir o mesmo sintoma?
- O que mudou recentemente (deploy, config, dados, trafego)?

## Mini-template para log de debug

- Sintoma:
- Ambiente:
- Hipoteses:
- Experimento:
- Resultado:
- Proxima acao:

Relacionados:
- [[Conhecimento-Geral/Psicologia/Teoria-da-Mente]]
- [[Conhecimento-Geral/IA-para-Programacao/Debug-com-Agentes]]


[[Conhecimento-Geral/IA-para-Programacao/INDEX|← Voltar ao índice de IA para Programação]]
