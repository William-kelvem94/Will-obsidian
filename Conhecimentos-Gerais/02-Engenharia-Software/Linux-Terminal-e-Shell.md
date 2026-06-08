---
title: "Linux, Terminal e Shell"
date: 2026-06-07
updated: 2026-06-07
type: guide
status: active
tags: [conhecimento-geral, linux, terminal, shell, devops]
related: [[Docker-e-DevOps]], [[Observabilidade-Logs-e-Monitoramento]], [[Git-e-Controle-de-Versao]]
summary: "Guia essencial de Linux, terminal, comandos, permissões, processos, arquivos, logs e automação por shell."
---

# Linux, Terminal e Shell

Linux é base de muitos servidores, containers e ambientes de desenvolvimento. Terminal é a interface de comando para operar o sistema com precisão.

## Por que importa

Mesmo usando Windows, muitos projetos rodam em Linux dentro de Docker, WSL, VPS ou servidores. Saber terminal reduz dependência de interface gráfica e acelera diagnóstico.

## Conceitos fundamentais

| Conceito | Explicação |
|---|---|
| shell | programa que interpreta comandos |
| diretório | pasta no sistema de arquivos |
| processo | programa em execução |
| permissão | regra de leitura, escrita e execução |
| pipe | envia saída de um comando para outro |
| variável de ambiente | configuração disponível para processos |
| serviço | processo gerenciado pelo sistema |
| log | registro de eventos |

## Comandos essenciais

| Comando | Uso |
|---|---|
| `pwd` | mostrar diretório atual |
| `ls` | listar arquivos |
| `cd` | mudar diretório |
| `cat` | mostrar arquivo |
| `less` | ler arquivo grande |
| `grep` | buscar texto |
| `find` | localizar arquivos |
| `cp` | copiar |
| `mv` | mover ou renomear |
| `rm` | remover |
| `mkdir` | criar pasta |
| `chmod` | alterar permissão |
| `ps` | listar processos |
| `kill` | encerrar processo |
| `tail` | acompanhar fim do arquivo |

## Pipes e composição

A força do terminal está em combinar comandos.

```bash
cat app.log | grep error | tail -n 20
```

Esse comando lê um log, filtra linhas com erro e mostra as últimas 20.

## Permissões

Permissões comuns:

- `r`: read, leitura;
- `w`: write, escrita;
- `x`: execute, execução.

Evitar usar permissão ampla sem necessidade. O princípio é menor privilégio.

## Variáveis de ambiente

São usadas para configurar aplicações sem colocar valores fixos no código.

Exemplos:

- porta;
- URL do banco;
- modo de ambiente;
- chave de API;
- caminho de arquivo.

## Diagnóstico básico

Quando algo não roda:

1. verificar diretório;
2. verificar arquivo existe;
3. verificar permissão;
4. verificar processo;
5. verificar porta;
6. verificar log;
7. verificar variável de ambiente;
8. reproduzir comando mínimo.

## Erros comuns

- executar comando em pasta errada;
- apagar arquivo sem conferir;
- copiar comando sem entender;
- usar `sudo` para tudo;
- ignorar permissões;
- não ler logs;
- confundir terminal local com terminal do container.

## Checklist

- [ ] Sei onde estou com `pwd`?
- [ ] O arquivo existe?
- [ ] Tenho permissão?
- [ ] O processo está rodando?
- [ ] A porta está livre?
- [ ] O log mostra erro real?
- [ ] Estou no host ou no container?

## Resumo para IA

Linux e terminal são base operacional para dev, Docker, servidores e debugging. Ao ajudar com erro técnico, sempre considerar diretório, processo, permissão, porta, logs e variáveis de ambiente.

## Links internos

- [[Docker-e-DevOps]]
- [[Observabilidade-Logs-e-Monitoramento]]
- [[Git-e-Controle-de-Versao]]
