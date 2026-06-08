---
title: "Sistemas Distribuidos e Escalabilidade"
date: 2026-06-07
updated: 2026-06-07
type: guide
status: active
tags: [conhecimento-geral, arquitetura, escalabilidade, sistemas-distribuidos]
related: [[Arquitetura-Web-Moderna]], [[APIs-Backend-Banco]], [[Docker-e-DevOps]]
summary: "Fundamentos de escalabilidade, filas, cache, consistência, serviços e trade-offs em sistemas distribuídos."
---

# Sistemas Distribuídos e Escalabilidade

Sistema distribuído é um conjunto de partes rodando em máquinas ou processos diferentes que cooperam para entregar uma função.

## Por que sistemas distribuídos são difíceis

- rede falha;
- latência varia;
- serviços caem;
- dados podem ficar inconsistentes;
- logs ficam espalhados;
- deploy fica mais complexo;
- debugging exige rastreabilidade.

## Conceitos essenciais

| Conceito | Função |
|---|---|
| cache | reduzir leitura repetida |
| fila | processar tarefas de forma assíncrona |
| worker | executar trabalho em segundo plano |
| load balancer | distribuir tráfego |
| réplica | copiar serviço ou banco |
| particionamento | dividir dados ou carga |
| idempotência | repetir ação sem duplicar efeito |
| observabilidade | entender o sistema em produção |

## Escala vertical e horizontal

### Escala vertical

Aumentar recursos da mesma máquina. É simples, mas tem limite.

### Escala horizontal

Adicionar mais instâncias. Exige coordenação, balanceamento e cuidado com estado.

## Cache

Cache melhora performance, mas pode entregar dado antigo.

Usar cache para:

- dados muito lidos;
- dados pouco alterados;
- respostas caras de calcular;
- integração externa lenta.

Evitar cache quando:

- dado muda o tempo todo;
- consistência é crítica;
- invalidação é mais complexa que o ganho.

## Filas

Filas ajudam a desacoplar tarefas demoradas.

Exemplos:

- envio de e-mail;
- processamento de imagem;
- geração de relatório;
- integração externa;
- atualização assíncrona.

## Trade-offs

| Escolha | Ganha | Perde |
|---|---|---|
| cache | velocidade | consistência imediata |
| fila | resiliência | complexidade |
| microsserviço | isolamento | coordenação |
| banco replicado | leitura rápida | sincronização |
| processamento assíncrono | fluidez | rastreio mais difícil |

## Checklist

- [ ] O gargalo é real ou imaginado?
- [ ] Dá para simplificar antes de distribuir?
- [ ] Logs permitem rastrear requisição?
- [ ] Tarefas demoradas podem ir para fila?
- [ ] Cache tem política de expiração?
- [ ] A operação é idempotente?
- [ ] Existe plano para falha parcial?

## Relações

- [[Arquitetura-Web-Moderna]]
- [[APIs-Backend-Banco]]
- [[Docker-e-DevOps]]
