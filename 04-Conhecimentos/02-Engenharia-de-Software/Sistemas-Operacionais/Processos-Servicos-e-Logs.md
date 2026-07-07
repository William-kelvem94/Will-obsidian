---
title: "Processos, Serviços e Logs"
date: 2026-07-07
updated: 2026-07-07
type: knowledge
status: active
classe_privacidade: publico-tecnico
indexavel: true
uso_ia: livre
tags: [processos, servicos, logs, windows, linux, systemd, eventviewer, troubleshooting]
summary: "Guia prático para entender processos, serviços, daemons, logs e diagnóstico operacional em Windows e Linux."
---

# Processos, Serviços e Logs

Processos, serviços e logs são o triângulo central do diagnóstico.

- **Processo:** programa em execução agora.
- **Serviço/daemon:** processo gerenciado pelo sistema para rodar em segundo plano.
- **Log:** registro de eventos, erros, avisos e estado histórico.

## Perguntas de diagnóstico

1. O processo existe?
2. O serviço está ativo?
3. O serviço falhou recentemente?
4. Existe log de erro?
5. O problema é aplicação, sistema, permissão, porta ou recurso?

## Processos no Windows

```powershell
Get-Process
Get-Process | Sort-Object CPU -Descending | Select-Object -First 10
Get-Process | Sort-Object WorkingSet -Descending | Select-Object -First 10
Get-Process -Id 1234
```

CMD clássico:

```bat
tasklist
tasklist /svc
tasklist /fi "PID eq 1234"
```

## Processos no Linux

```bash
ps aux
ps -p 1234 -f
top
htop
pgrep nome
pidof nome
```

Antes de intervir em um processo, identificar usuário, PID, serviço associado e impacto.

## Serviços no Windows

```powershell
Get-Service
Get-Service | Where-Object Status -eq Running
Get-Service | Where-Object Status -eq Stopped
Get-Service -Name Spooler
```

CMD clássico:

```bat
sc query
sc query nomeDoServico
sc qc nomeDoServico
net start
```

Para ações de mudança de estado, usar janela planejada e confirmar impacto antes.

## Serviços no Linux com systemd

```bash
systemctl status nome.service
systemctl is-enabled nome.service
systemctl is-active nome.service
systemctl --failed
systemctl list-units --type=service
systemctl list-unit-files --type=service
```

## Logs no Windows

Abrir visualizador:

```bat
eventvwr.msc
```

PowerShell:

```powershell
Get-WinEvent -LogName System -MaxEvents 50
Get-WinEvent -LogName Application -MaxEvents 50
Get-WinEvent -FilterHashtable @{LogName='System'; Level=2} -MaxEvents 20
Get-WinEvent -FilterHashtable @{LogName='Application'; Level=2} -MaxEvents 20
```

Logs importantes:

| Log | Uso |
|---|---|
| System | sistema, drivers, serviços, boot |
| Application | aplicações e runtime |
| Security | auditoria e login |
| Setup | instalação e updates |

## Logs no Linux

```bash
journalctl
journalctl -xe
journalctl -p err
journalctl --since "1 hour ago"
journalctl -u nginx
journalctl -u nginx -f
journalctl -b
journalctl -k
```

Arquivos comuns:

```bash
ls /var/log
tail -f /var/log/syslog
tail -f /var/log/messages
tail -f /var/log/auth.log
```

## Diagnóstico por sintomas

### Serviço não responde

1. Ver status.
2. Ver logs do serviço.
3. Ver se existe porta ouvindo.
4. Ver consumo de CPU e memória.
5. Ver permissões e usuário de execução.
6. Ver configuração alterada recentemente.
7. Validar dependências.

Windows:

```powershell
Get-Service nome
Get-WinEvent -LogName System -MaxEvents 20
Get-NetTCPConnection -State Listen
```

Linux:

```bash
systemctl status nome
journalctl -u nome -xe
ss -tulpn
```

### Alto consumo de CPU

Windows:

```powershell
Get-Process | Sort-Object CPU -Descending | Select-Object -First 10
```

Linux:

```bash
top
ps aux --sort=-%cpu | head
```

### Alto consumo de memória

Windows:

```powershell
Get-Process | Sort-Object WorkingSet -Descending | Select-Object -First 10
```

Linux:

```bash
free -h
ps aux --sort=-%mem | head
```

### Disco cheio

Windows:

```powershell
Get-Volume
Get-PSDrive -PSProvider FileSystem
```

Linux:

```bash
df -h
du -h --max-depth=1 /var | sort -h
```

## Registro de incidente

- horário;
- hostname;
- usuário afetado;
- serviço ou processo afetado;
- comandos de leitura usados;
- saída relevante;
- trecho de log;
- hipótese;
- ação tomada;
- validação;
- próximo monitoramento.

## Anti-padrões

- reiniciar sem ler log;
- tratar sintoma como causa;
- ignorar horário exato do erro;
- apagar evidência antes de registrar;
- misturar comandos de shells diferentes;
- mudar estado de serviço sem saber impacto.

## Fórmula operacional

> Processo mostra o agora. Serviço mostra o ciclo de vida. Log mostra a história.
