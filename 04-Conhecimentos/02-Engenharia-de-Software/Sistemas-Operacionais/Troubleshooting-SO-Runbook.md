---
title: "Runbook de Troubleshooting de Sistemas Operacionais"
date: 2026-07-07
updated: 2026-07-07
type: runbook
status: active
classe_privacidade: publico-tecnico
indexavel: true
uso_ia: livre
tags: [runbook, troubleshooting, sistemas-operacionais, windows, linux, suporte, diagnostico]
summary: "Método operacional para diagnosticar problemas de Windows e Linux por evidência, hipótese, teste e validação."
---

# Runbook de Troubleshooting de Sistemas Operacionais

Este runbook define o método padrão para diagnosticar problemas de S.O. no WILL-OBSIDIAN.

## Regra principal

> Observar antes de alterar. Medir antes de concluir. Validar depois de corrigir.

## Fluxo geral

1. Entender o sintoma.
2. Identificar ambiente.
3. Coletar evidências.
4. Formular hipótese.
5. Testar hipótese com menor impacto possível.
6. Aplicar correção controlada.
7. Validar.
8. Documentar.

## Etapa 1 - Entender o sintoma

Perguntas:

- O que exatamente falhou?
- Quando começou?
- Afeta um usuário, uma máquina ou todos?
- O problema é constante ou intermitente?
- Houve atualização, instalação, queda de energia ou mudança de rede?
- Existe mensagem de erro?
- O problema acontece em outro usuário ou outra máquina?

## Etapa 2 - Identificar ambiente

Windows:

```powershell
Get-ComputerInfo
Get-NetIPConfiguration
Get-Volume
```

Linux:

```bash
cat /etc/os-release
uname -a
ip addr
df -h
```

Registrar:

- hostname;
- sistema e versão;
- usuário;
- IP;
- uptime;
- espaço em disco;
- horário local.

## Etapa 3 - Recursos básicos

### CPU

Windows:

```powershell
Get-Process | Sort-Object CPU -Descending | Select-Object -First 10
```

Linux:

```bash
top
ps aux --sort=-%cpu | head
```

### Memória

Windows:

```powershell
Get-Process | Sort-Object WorkingSet -Descending | Select-Object -First 10
```

Linux:

```bash
free -h
ps aux --sort=-%mem | head
```

### Disco

Windows:

```powershell
Get-Volume
Get-PSDrive -PSProvider FileSystem
```

Linux:

```bash
df -h
du -h --max-depth=1 . | sort -h
```

## Etapa 4 - Rede

Perguntas:

- Tem IP?
- Tem gateway?
- DNS resolve?
- Porta responde?
- Serviço local está ouvindo?

Windows:

```powershell
Get-NetIPConfiguration
Test-Connection google.com -Count 4
Resolve-DnsName google.com
Test-NetConnection google.com -Port 443
```

Linux:

```bash
ip addr
ip route
ping google.com
dig google.com
ss -tulpn
```

## Etapa 5 - Serviços e logs

Windows:

```powershell
Get-Service
Get-WinEvent -LogName System -MaxEvents 50
Get-WinEvent -LogName Application -MaxEvents 50
```

Linux:

```bash
systemctl --failed
journalctl -p err --since "1 hour ago"
journalctl -xe
```

## Etapa 6 - Classificar causa provável

| Sinal | Categoria provável |
|---|---|
| disco quase cheio | armazenamento |
| CPU alta | processo ou loop |
| memória alta | vazamento ou carga excessiva |
| DNS falha | resolução de nomes |
| IP externo responde, domínio não | DNS |
| porta não responde | serviço/firewall/rota |
| serviço falhou | configuração, dependência ou permissão |
| erro de acesso | permissão ou usuário incorreto |
| após atualização | regressão ou incompatibilidade |

## Etapa 7 - Correção controlada

Antes de corrigir:

- salvar evidência;
- anotar hipótese;
- limitar escopo;
- prever impacto;
- ter caminho de retorno;
- avisar se houver usuário afetado.

## Etapa 8 - Validação

Validar com o mesmo teste que comprovou o problema.

Exemplos:

- se porta falhava, testar porta novamente;
- se serviço estava falhando, verificar status e log;
- se disco estava cheio, verificar espaço;
- se DNS falhava, resolver domínio novamente;
- se aplicação dava erro, repetir fluxo real.

## Template de registro

```md
## Incidente

- Data/hora:
- Host:
- Sistema:
- Usuário afetado:
- Sintoma:
- Impacto:

## Evidências

- Comandos executados:
- Logs relevantes:
- Prints ou mensagens:

## Hipótese

## Ação aplicada

## Validação

## Próxima prevenção
```

## Anti-padrões

- reiniciar sem evidência;
- limpar arquivos sem entender origem;
- alterar permissão ampla;
- trocar configuração sem backup;
- confundir sintoma com causa;
- não registrar o que foi feito.

## Resultado esperado

Ao final, deve existir resposta clara para:

1. Qual era o problema?
2. Como foi identificado?
3. O que foi alterado?
4. Como foi validado?
5. Como evitar repetição?
