---
title: "OS Diagnostics"
date: 2026-07-07
updated: 2026-07-07
type: skill
status: active
level: 3
classe_privacidade: publico-tecnico
indexavel: true
uso_ia: livre
tags: [skill, sistemas-operacionais, diagnostico, windows, linux, terminal]
summary: "Skill para diagnosticar problemas de sistemas operacionais por evidência, hipótese, teste e validação."
---

# Skill: OS Diagnostics

## Objetivo

Diagnosticar problemas de Windows e Linux com método operacional, evitando chute e ações impulsivas.

## Quando usar

Usar quando houver:

- lentidão;
- serviço fora;
- falha de rede;
- erro de permissão;
- disco cheio;
- aplicação que não inicia;
- porta inacessível;
- máquina instável;
- problema intermitente.

## Entrada esperada

- sistema operacional;
- sintoma;
- horário aproximado;
- impacto;
- mensagem de erro;
- comandos já testados;
- contexto de mudança recente.

## Processo

1. Identificar ambiente.
2. Coletar sinais básicos: CPU, memória, disco, rede, serviços e logs.
3. Separar sintoma de causa.
4. Formular hipótese.
5. Testar hipótese com comando de leitura.
6. Sugerir menor ação corretiva possível.
7. Validar com evidência.
8. Registrar resultado.

## Checklist

- [ ] O sistema foi identificado?
- [ ] O usuário atual foi identificado?
- [ ] O problema é local ou de rede?
- [ ] O disco tem espaço?
- [ ] CPU ou memória estão saturadas?
- [ ] O serviço existe e está ativo?
- [ ] Há erro em logs?
- [ ] DNS foi testado separadamente de conexão?
- [ ] Permissões foram verificadas?
- [ ] Há validação pós-correção?

## Saída esperada

A resposta deve conter:

- diagnóstico provável;
- evidências;
- comandos de leitura sugeridos;
- risco da intervenção;
- próximo teste;
- validação esperada.

## Anti-padrões

- mandar reiniciar sem evidência;
- ignorar logs;
- misturar shell de Windows com Linux;
- sugerir ação administrativa sem confirmar impacto;
- não registrar mensagem de erro.

## Métrica de qualidade

Uma execução boa desta skill deve permitir responder:

1. O que falhou?
2. Onde falhou?
3. Como foi comprovado?
4. Qual é a menor próxima ação?
5. Como validar?
