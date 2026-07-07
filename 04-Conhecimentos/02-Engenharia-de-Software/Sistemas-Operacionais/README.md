---
title: "Sistemas Operacionais - Trilha Mestre"
date: 2026-07-07
updated: 2026-07-07
type: index
status: active
classe_privacidade: publico-tecnico
indexavel: true
uso_ia: livre
tags: [sistemas-operacionais, windows, linux, terminal, cmd, powershell, bash, troubleshooting]
summary: "Trilha canônica para proficiência em Windows, Linux, terminal, comandos, administração, rede, logs, serviços e diagnóstico de sistemas operacionais."
---

# Sistemas Operacionais - Trilha Mestre

Esta pasta concentra conhecimento de Sistemas Operacionais para uso humano e por agentes do JARVIS.

Objetivo: transformar o vault em uma base capaz de responder, diagnosticar, operar e documentar problemas de Windows, Linux, terminal, rede, permissões, processos, serviços e automação.

## Mapa mental

Sistemas operacionais devem ser estudados em camadas:

1. **Shell e terminal** - como conversar com o sistema.
2. **Sistema de arquivos** - onde as coisas vivem e como se movem.
3. **Processos** - o que está rodando.
4. **Serviços** - o que inicializa, reinicia e mantém o ambiente vivo.
5. **Usuários e permissões** - quem pode fazer o quê.
6. **Rede** - como o sistema fala com outros sistemas.
7. **Logs** - o diário de bordo do caos.
8. **Pacotes e atualização** - como instalar, corrigir e manter.
9. **Automação** - scripts, tarefas e rotinas repetíveis.
10. **Troubleshooting** - método para descobrir causa raiz.

## Índice canônico

- [[04-Conhecimentos/02-Engenharia-de-Software/Sistemas-Operacionais/Windows-CMD-PowerShell|Windows, CMD e PowerShell]]
- [[04-Conhecimentos/02-Engenharia-de-Software/Sistemas-Operacionais/Linux-Terminal-Bash|Linux, Terminal e Bash]]
- [[04-Conhecimentos/02-Engenharia-de-Software/Sistemas-Operacionais/Comandos-Essenciais-Terminal|Comandos essenciais de terminal]]
- [[04-Conhecimentos/02-Engenharia-de-Software/Sistemas-Operacionais/Processos-Servicos-e-Logs|Processos, serviços e logs]]
- [[04-Conhecimentos/02-Engenharia-de-Software/Sistemas-Operacionais/Redes-e-Diagnostico|Redes e diagnóstico]]
- [[04-Conhecimentos/02-Engenharia-de-Software/Sistemas-Operacionais/Permissoes-Usuarios-e-Seguranca|Permissões, usuários e segurança]]
- [[04-Conhecimentos/02-Engenharia-de-Software/Sistemas-Operacionais/Shell-Scripting-e-Automacao|Shell scripting e automação]]
- [[04-Conhecimentos/02-Engenharia-de-Software/Sistemas-Operacionais/Troubleshooting-SO-Runbook|Runbook de troubleshooting de S.O.]]

## Perfil de proficiência esperado

Uma pessoa ou agente proficiente em S.O. deve conseguir:

- identificar sistema, versão, arquitetura e recursos;
- navegar e manipular arquivos sem causar perda acidental;
- diagnosticar CPU, memória, disco, rede e serviços;
- entender diferença entre processo, serviço, daemon, job e tarefa agendada;
- ler logs relevantes no Windows e Linux;
- diferenciar erro de DNS, gateway, rota, firewall, porta fechada e serviço fora;
- criar comandos reproduzíveis;
- escrever scripts simples e seguros;
- documentar causa, evidência, ação e validação;
- saber quando **não** executar um comando destrutivo.

## Regra de ouro

> Antes de alterar, observe. Antes de apagar, copie. Antes de automatizar, teste em pequeno escopo.

## Trilha de estudo sugerida

### Nível 1 - Fundamentos

- terminal, diretórios e arquivos;
- variáveis de ambiente;
- PATH;
- pipes e redirecionamento;
- comandos de leitura e busca.

### Nível 2 - Operação

- processos;
- serviços;
- logs;
- rede local;
- permissões;
- instalação de pacotes.

### Nível 3 - Diagnóstico

- gargalos de CPU, memória e disco;
- falhas de DNS e conectividade;
- portas e sockets;
- eventos do Windows;
- journal/systemd no Linux;
- boot e inicialização.

### Nível 4 - Automação

- PowerShell;
- Batch/CMD;
- Bash;
- tarefas agendadas;
- cron/systemd timers;
- scripts idempotentes;
- logs de execução.

### Nível 5 - Administração avançada

- hardening básico;
- ACLs;
- auditoria;
- serviços críticos;
- troubleshooting guiado por evidências;
- documentação operacional;
- criação de playbooks para agentes.

## Padrão de nota operacional

Toda nota prática de S.O. deve conter:

- objetivo;
- quando usar;
- comandos seguros;
- sinais de risco;
- evidências esperadas;
- validação;
- rollback ou saída segura;
- links para runbooks.
