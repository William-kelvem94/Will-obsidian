---
title: "Redes e Internet"
date: 2026-06-07
updated: 2026-06-07
type: guide
status: active
tags: [conhecimento-geral, redes, internet, infraestrutura]
related: [[../../02-Engenharia-de-Software/Docker-e-DevOps]], [[../Seguranca/Seguranca-da-Informacao]], [[../../02-Engenharia-de-Software/Arquitetura-Web-Moderna]]
summary: "Fundamentos de redes, internet, DNS, HTTP, portas, IPs e diagnóstico para desenvolvimento e infraestrutura."
---

# Redes e Internet

Redes permitem que computadores troquem dados. Para desenvolvimento web e infraestrutura, entender o básico reduz muito tempo de debugging.

## Conceitos principais

| Conceito | Função |
|---|---|
| IP | endereço de um dispositivo na rede |
| porta | canal lógico de comunicação |
| DNS | traduz nome para IP |
| HTTP | protocolo de comunicação web |
| HTTPS | HTTP com criptografia |
| roteador | encaminha tráfego entre redes |
| firewall | filtra tráfego permitido |
| latência | tempo de ida e volta |
| bandwidth | capacidade de transferência |

## Fluxo ao acessar um site

1. Usuário digita domínio.
2. DNS resolve domínio para IP.
3. Navegador abre conexão.
4. Servidor recebe requisição.
5. Aplicação processa.
6. Resposta volta ao navegador.
7. Browser renderiza conteúdo.

## Portas comuns

| Porta | Uso comum |
|---|---|
| 22 | SSH |
| 53 | DNS |
| 80 | HTTP |
| 443 | HTTPS |
| 5432 | PostgreSQL |
| 3306 | MySQL |
| 6379 | Redis |
| 3000 | dev web comum |
| 8000 | APIs locais comuns |

## Problemas comuns

| Sintoma | Possível causa |
|---|---|
| site não abre | DNS, servidor fora, firewall |
| API local não responde | porta errada, serviço parado |
| conexão recusada | nada escutando na porta |
| timeout | rede lenta, firewall, serviço travado |
| funciona local mas não em produção | variáveis, CORS, firewall, DNS |

## Diagnóstico básico

- verificar se serviço está rodando;
- verificar porta;
- testar DNS;
- testar conexão;
- olhar logs do serviço;
- checar firewall;
- comparar ambiente local e produção.

## Relações

- [[../../02-Engenharia-de-Software/Docker-e-DevOps]]
- [[../Seguranca/Seguranca-da-Informacao]]
- [[../../02-Engenharia-de-Software/Arquitetura-Web-Moderna]]
