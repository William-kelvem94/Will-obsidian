---
title: "Comandos Essenciais de Terminal"
date: 2026-07-07
updated: 2026-07-07
type: cheatsheet
status: active
classe_privacidade: publico-tecnico
indexavel: true
uso_ia: livre
tags: [terminal, comandos, shell, cmd, powershell, bash, sistemas-operacionais]
summary: "Cheatsheet comparativo de comandos essenciais entre Windows CMD, PowerShell e Linux Bash."
---

# Comandos Essenciais de Terminal

Esta nota compara comandos equivalentes entre CMD, PowerShell e Bash.

Objetivo: permitir que o JARVIS escolha o comando certo para cada ambiente sem misturar sintaxe.

## Identificar ambiente

| Tarefa | CMD | PowerShell | Bash/Linux |
|---|---|---|---|
| usuário atual | `whoami` | `whoami` | `whoami` |
| hostname | `hostname` | `hostname` | `hostname` |
| versão do sistema | `ver` | `Get-ComputerInfo` | `cat /etc/os-release` |
| arquitetura | `wmic os get OSArchitecture` | `Get-CimInstance Win32_OperatingSystem` | `uname -m` |
| uptime | `systeminfo` | `(Get-Date) - (gcim Win32_OperatingSystem).LastBootUpTime` | `uptime` |

## Navegação

| Tarefa | CMD | PowerShell | Bash/Linux |
|---|---|---|---|
| diretório atual | `cd` | `Get-Location` | `pwd` |
| listar | `dir` | `Get-ChildItem` | `ls` |
| listar ocultos | `dir /a` | `Get-ChildItem -Force` | `ls -la` |
| entrar em pasta | `cd pasta` | `Set-Location pasta` | `cd pasta` |
| voltar uma pasta | `cd ..` | `Set-Location ..` | `cd ..` |
| criar pasta | `mkdir pasta` | `New-Item -ItemType Directory pasta` | `mkdir pasta` |

## Arquivos

| Tarefa | CMD | PowerShell | Bash/Linux |
|---|---|---|---|
| criar arquivo vazio | `type nul > a.txt` | `New-Item a.txt` | `touch a.txt` |
| ler arquivo | `type a.txt` | `Get-Content a.txt` | `cat a.txt` |
| ler paginado | `more a.txt` | `Get-Content a.txt | more` | `less a.txt` |
| copiar arquivo | `copy a.txt b.txt` | `Copy-Item a.txt b.txt` | `cp a.txt b.txt` |
| mover arquivo | `move a.txt pasta\` | `Move-Item a.txt pasta\` | `mv a.txt pasta/` |
| renomear | `ren a.txt b.txt` | `Rename-Item a.txt b.txt` | `mv a.txt b.txt` |

## Busca

| Tarefa | CMD | PowerShell | Bash/Linux |
|---|---|---|---|
| achar executável | `where node` | `Get-Command node` | `which node` |
| buscar arquivo | `dir /s /b *.log` | `Get-ChildItem -Recurse -Filter *.log` | `find . -name "*.log"` |
| buscar texto | `findstr /s /i erro *.log` | `Select-String -Path *.log -Pattern erro` | `grep -Rin "erro" .` |
| últimas linhas | não nativo simples | `Get-Content app.log -Tail 50` | `tail -50 app.log` |
| acompanhar log | não nativo simples | `Get-Content app.log -Wait` | `tail -f app.log` |

## Saída e redirecionamento

| Tarefa | CMD | PowerShell | Bash/Linux |
|---|---|---|---|
| salvar saída | `cmd > out.txt` | `cmd > out.txt` | `cmd > out.txt` |
| acrescentar saída | `cmd >> out.txt` | `cmd >> out.txt` | `cmd >> out.txt` |
| redirecionar erro | `cmd 2> err.txt` | `cmd 2> err.txt` | `cmd 2> err.txt` |
| pipe | `comando | findstr x` | `comando | Where-Object ...` | `comando | grep x` |

## Processos

| Tarefa | CMD | PowerShell | Bash/Linux |
|---|---|---|---|
| listar processos | `tasklist` | `Get-Process` | `ps aux` |
| filtrar processo | `tasklist | findstr node` | `Get-Process node` | `ps aux | grep node` |
| processo por PID | `tasklist /fi "PID eq 1234"` | `Get-Process -Id 1234` | `ps -p 1234 -f` |
| uso interativo | Task Manager | `Get-Process` | `top`, `htop` |

## Serviços

| Tarefa | CMD | PowerShell | Bash/Linux |
|---|---|---|---|
| listar serviços | `sc query` | `Get-Service` | `systemctl list-units --type=service` |
| status | `sc query nome` | `Get-Service nome` | `systemctl status nome` |
| iniciar | `net start nome` | `Start-Service nome` | `systemctl start nome` |
| parar | `net stop nome` | `Stop-Service nome` | `systemctl stop nome` |
| reiniciar | combinação stop/start | `Restart-Service nome` | `systemctl restart nome` |

## Rede

| Tarefa | CMD | PowerShell | Bash/Linux |
|---|---|---|---|
| IP | `ipconfig` | `Get-NetIPConfiguration` | `ip addr` |
| rota | `route print` | `Get-NetRoute` | `ip route` |
| ping | `ping host` | `Test-Connection host` | `ping host` |
| DNS | `nslookup host` | `Resolve-DnsName host` | `dig host` |
| rota até host | `tracert host` | `Test-NetConnection -TraceRoute host` | `traceroute host` |
| portas | `netstat -ano` | `Get-NetTCPConnection` | `ss -tulpn` |
| testar porta | não nativo simples | `Test-NetConnection host -Port 443` | `nc -vz host 443` |

## Logs

| Tarefa | CMD | PowerShell | Bash/Linux |
|---|---|---|---|
| logs do sistema | `eventvwr.msc` | `Get-WinEvent -LogName System` | `journalctl` |
| logs de app | Event Viewer | `Get-WinEvent -LogName Application` | `/var/log`, `journalctl -u` |
| erros recentes | Event Viewer | `Get-WinEvent -FilterHashtable @{LogName='System'; Level=2}` | `journalctl -p err` |

## Pacotes

| Tarefa | Windows | Debian/Ubuntu | Fedora/RHEL |
|---|---|---|---|
| buscar | `winget search app` | `apt search pacote` | `dnf search pacote` |
| instalar | `winget install app` | `apt install pacote` | `dnf install pacote` |
| listar | `winget list` | `apt list --installed` | `dnf list installed` |
| remover | `winget uninstall app` | `apt remove pacote` | `dnf remove pacote` |

## Leitura de comando

Ao analisar um comando, decompor em:

1. **programa:** o executável principal;
2. **subcomando:** ação dentro da ferramenta;
3. **flags/opções:** modificadores;
4. **argumentos:** alvo;
5. **redirecionamentos:** para onde vai a saída;
6. **pipe:** para quem a saída é enviada;
7. **contexto:** usuário, diretório, permissões e ambiente.

Exemplo:

```bash
journalctl -u nginx --since "1 hour ago" | grep error
```

- programa: `journalctl`;
- alvo: unidade `nginx`;
- filtro temporal: última hora;
- pipe: envia para `grep`;
- filtro textual: `error`.

## Regras de segurança operacional

- Sempre confirmar o sistema antes de sugerir comando.
- Preferir comandos de leitura antes de alteração.
- Em PowerShell, usar `-WhatIf` quando disponível.
- Em cópias grandes, simular primeiro quando a ferramenta permite.
- Nunca misturar comando Linux em CMD ou comando PowerShell em Bash sem indicar shell correto.
- Registrar evidência antes e depois.
