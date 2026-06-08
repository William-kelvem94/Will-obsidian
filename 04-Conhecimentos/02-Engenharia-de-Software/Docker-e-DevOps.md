---
title: "Docker e DevOps"
date: 2026-06-07
updated: 2026-06-07
type: guide
status: active
tags: [conhecimento-geral, docker, devops, infraestrutura, engenharia-software]
related: [[Arquitetura-Web-Moderna]], [[APIs-Backend-Banco]], [[../08-Vida-Pratica/Produtividade/Decisao-e-Priorizacao]]
summary: "Guia prático para usar Docker e práticas DevOps em projetos locais e web, com foco em reprodutibilidade e manutenção."
---

# Docker e DevOps

Docker empacota aplicação, dependências e ambiente em contêineres. Em projetos locais, ele reduz conflito de versões e evita instalar pacotes diretamente no sistema operacional.

## Quando usar Docker

Usar Docker quando o projeto tem banco de dados, filas, serviços auxiliares, múltiplas linguagens, dependências difíceis ou necessidade de setup reproduzível.

## Conceitos

| Conceito | Definição |
|---|---|
| imagem | pacote com aplicação e dependências |
| contêiner | instância em execução de uma imagem |
| volume | persistência fora do ciclo de vida do contêiner |
| network | comunicação entre serviços |
| Dockerfile | receita para construir imagem |
| compose | coordenação local de vários serviços |

## Exemplo conceitual de compose

```yaml
services:
  app:
    build: .
    ports:
      - "3000:3000"
    depends_on:
      - db

  db:
    image: postgres:16
    volumes:
      - db_data:/var/lib/postgresql/data

volumes:
  db_data:
```

## Boas práticas

- manter arquivo de exemplo de configuração;
- não versionar configurações privadas;
- nomear serviços de forma clara;
- usar volumes para banco;
- evitar imagens pesadas sem necessidade;
- documentar comandos no README;
- manter portas previsíveis;
- separar ambiente local e produção.

## Comandos comuns

```bash
docker compose up -d
docker compose down
docker compose logs -f
docker compose ps
docker compose build
```

## Checklist de projeto Docker

- [ ] Existe compose?
- [ ] Existe exemplo de configuração?
- [ ] Banco usa volume?
- [ ] README mostra como subir?
- [ ] Portas estão documentadas?
- [ ] Logs são acessíveis?
- [ ] O projeto roda em outra máquina sem ajustes manuais?

## DevOps mínimo

DevOps é prática de entrega confiável. Um projeto saudável deve ter versionamento, setup reprodutível, logs, processo de build, deploy documentado, rollback pensado e monitoramento proporcional ao tamanho do sistema.

## Erros comuns

- criar Dockerfile sem entender portas;
- perder dados por não usar volume;
- misturar configuração local com produção;
- não documentar comandos;
- usar Docker para esconder bagunça de arquitetura.

## Relações

- [[Arquitetura-Web-Moderna]]
- [[APIs-Backend-Banco]]
- [[../01-IA-e-Agentes/Token-Economy]]
- [[../03-Dados-e-Analytics/Taxonomia-Metadados-e-Ontologia]]
