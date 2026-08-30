---
title: "Windows, CMD e PowerShell"
date: 2026-07-07
updated: 2026-07-07
type: knowledge
status: active
classe_privacidade: publico-tecnico
indexavel: true
uso_ia: livre
tags: [windows, cmd, powershell, terminal, sistemas-operacionais, administracao]
summary: "Base operacional para dominar Windows via CMD, PowerShell, serviços, processos, rede, logs e diagnóstico."
---

# Windows, CMD e PowerShell

Windows deve ser entendido em três camadas:

1. **Interface gráfica:** painel de controle, configurações, services.msc, eventvwr.
2. **CMD:** comandos clássicos, compatibilidade, scripts batch e diagnóstico rápido.
3. **PowerShell:** automação moderna baseada em objetos, pipelines e módulos.

## CMD x PowerShell

| Critério | CMD | PowerShell |
|---|---|---|
| Modelo | texto puro | objetos .NET |
| Script | `.bat`, `.cmd` | `.ps1` |
| Melhor para | compatibilidade, comandos antigos, suporte rápido | automação, inventário, administração, filtros avançados |
| Pipeline | passa texto | passa objetos |
| Exemplos | `dir`, `copy`, `ipconfig`, `netstat` | `Get-Process`, `Get-Service`, `Get-NetIPConfiguration` |

## Identificação do sistema

### CMD

```bat
ver
hostname
whoami
systeminfo
wmic os get Caption,Version,OSArchitecture
```

### PowerShell

```powershell
$PSVersionTable
Get-ComputerInfo
Get-CimInstance Win32_OperatingSystem | Select-Object Caption, Version, OSArchitecture, LastBootUpTime
Get-CimInstance Win32_ComputerSystem | Select-Object Manufacturer, Model, TotalPhysicalMemory
```

## Navegação e arquivos

### CMD

```bat
cd
cd C:\Users
dir
dir /a
dir /s nome-do-arquivo.txt
mkdir pasta
copy origem.txt destino.txt
move arquivo.txt pasta\
ren antigo.txt novo.txt
type arquivo.txt
more arquivo.txt
```

### PowerShell

```powershell
Get-Location
Set-Location C:\Users
Get-ChildItem
Get-ChildItem -Force
Get-ChildItem -Recurse -Filter "*.log"
New-Item -ItemType Directory -Name logs
Copy-Item .\origem.txt .\destino.txt
Move-Item .\arquivo.txt .\pasta\
Rename-Item .\antigo.txt novo.txt
Get-Content .\arquivo.txt
Get-Content .\arquivo.log -Tail 50 -Wait
```

## Busca de arquivos e texto

### CMD

```bat
dir /s /b *.log
findstr /s /i "erro" *.log
where python
where node
```

### PowerShell

```powershell
Get-ChildItem -Recurse -Filter "*.log"
Select-String -Path .\*.log -Pattern "erro"
Get-Command python
Get-Command node
```

## Variáveis de ambiente e PATH

### CMD

```bat
set
echo %PATH%
echo %USERNAME%
echo %COMPUTERNAME%
```

### PowerShell

```powershell
Get-ChildItem Env:
$env:Path
$env:USERNAME
$env:COMPUTERNAME
```

## Processos

### CMD

```bat
tasklist
tasklist | findstr chrome
tasklist /svc
```

### PowerShell

```powershell
Get-Process
Get-Process chrome
Get-Process | Sort-Object CPU -Descending | Select-Object -First 10
Get-Process | Sort-Object WorkingSet -Descending | Select-Object -First 10
```

Para encerrar processo, confirme nome/PID antes:

```powershell
Stop-Process -Id 1234 -WhatIf
Stop-Process -Id 1234
```

## Serviços

### Interface gráfica

```txt
services.msc
```

### CMD

```bat
sc query
sc query nomeDoServico
net start
net start nomeDoServico
net stop nomeDoServico
```

### PowerShell

```powershell
Get-Service
Get-Service | Where-Object Status -eq Running
Get-Service -Name Spooler
Restart-Service -Name Spooler -WhatIf
Restart-Service -Name Spooler
```

## Rede

### CMD

```bat
ipconfig
ipconfig /all
ping 8.8.8.8
ping google.com
tracert google.com
nslookup google.com
netstat -ano
route print
arp -a
```

### PowerShell

```powershell
Get-NetIPConfiguration
Get-NetAdapter
Test-Connection google.com -Count 4
Resolve-DnsName google.com
Test-NetConnection google.com -Port 443
Get-NetTCPConnection
Get-NetRoute
Get-NetNeighbor
```

## Portas e processos ouvindo conexão

### CMD

```bat
netstat -ano | findstr LISTENING
```

Depois cruzar PID com processo:

```bat
tasklist /fi "PID eq 1234"
```

### PowerShell

```powershell
Get-NetTCPConnection -State Listen
Get-Process -Id 1234
```

## Logs e eventos

### Abrir visualizador

```bat
eventvwr.msc
```

### PowerShell

```powershell
Get-EventLog -LogName System -Newest 50
Get-WinEvent -LogName System -MaxEvents 50
Get-WinEvent -FilterHashtable @{LogName='System'; Level=2} -MaxEvents 20
Get-WinEvent -FilterHashtable @{LogName='Application'; Level=2} -MaxEvents 20
```

Níveis comuns:

| Level | Significado |
|---:|---|
| 1 | Critical |
| 2 | Error |
| 3 | Warning |
| 4 | Information |

## Disco e armazenamento

### CMD

```bat
wmic logicaldisk get name,size,freespace
chkdsk C:
```

### PowerShell

```powershell
Get-Volume
Get-Disk
Get-Partition
Get-PSDrive -PSProvider FileSystem
```

## Integridade do sistema

Comandos úteis para diagnóstico e reparo controlado:

```bat
sfc /scannow
DISM /Online /Cleanup-Image /CheckHealth
DISM /Online /Cleanup-Image /ScanHealth
DISM /Online /Cleanup-Image /RestoreHealth
```

Usar quando houver corrupção de arquivos do sistema, falhas de atualização ou comportamento estranho persistente.

## Usuários e grupos

### CMD

```bat
whoami
whoami /groups
net user
net localgroup
net localgroup administrators
```

### PowerShell

```powershell
Get-LocalUser
Get-LocalGroup
Get-LocalGroupMember Administrators
```

## Tarefas agendadas

### CMD

```bat
schtasks /query
schtasks /query /fo LIST /v
```

### PowerShell

```powershell
Get-ScheduledTask
Get-ScheduledTask | Where-Object State -eq Ready
```

## Robocopy para cópia robusta

`robocopy` é melhor que `copy` para diretórios grandes.

```bat
robocopy C:\Origem D:\Destino /E /R:2 /W:2 /LOG:copia.log
```

Opções úteis:

| Opção | Função |
|---|---|
| `/E` | copia subpastas, inclusive vazias |
| `/R:2` | tenta novamente 2 vezes |
| `/W:2` | espera 2 segundos entre tentativas |
| `/LOG:` | grava log |
| `/L` | simula sem copiar |

Antes de copiar em massa, testar com:

```bat
robocopy C:\Origem D:\Destino /E /L
```

## Comandos de risco

Evitar executar sem revisão:

- comandos que removem diretórios inteiros;
- comandos que limpam disco ou partição;
- alterações de permissão recursivas sem escopo;
- scripts baixados da internet;
- comandos de reparo sem backup quando há suspeita de falha física.

## Checklist de diagnóstico Windows

1. Identificar versão e uptime.
2. Conferir CPU, memória e disco.
3. Conferir serviços críticos.
4. Conferir eventos de erro em System e Application.
5. Testar IP, DNS, gateway e porta.
6. Conferir atualizações recentes.
7. Reproduzir problema.
8. Registrar evidência.
9. Aplicar menor correção possível.
10. Validar resultado.

## Modelo mental

Windows é uma cidade com muitos balcões. CMD é o balcão antigo, PowerShell é a central de operações, Event Viewer é a caixa-preta, Serviços são os motores e o Registro é a sala elétrica. Mexer sem mapa funciona até a luz piscar. ⚡
