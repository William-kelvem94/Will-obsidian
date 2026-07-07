---
title: "Redes e Diagnóstico em Sistemas Operacionais"
date: 2026-07-07
updated: 2026-07-07
type: knowledge
status: active
classe_privacidade: publico-tecnico
indexavel: true
uso_ia: livre
tags: [redes, diagnostico, windows, linux, dns, tcp, portas, troubleshooting]
summary: "Guia de diagnóstico de rede em Windows e Linux: IP, gateway, DNS, rota, portas, sockets e HTTP."
---

# Redes e Diagnóstico em Sistemas Operacionais

Diagnóstico de rede deve seguir camadas. Não comece pelo navegador. Comece pelo chão.

## Camadas de análise

1. Interface existe?
2. Tem IP?
3. Tem rota padrão?
4. Resolve DNS?
5. Chega no destino?
6. Porta está aberta?
7. Serviço responde?
8. Aplicação responde corretamente?

## Windows - comandos essenciais

### Ver configuração de rede

```bat
ipconfig
ipconfig /all
route print
arp -a
```

PowerShell:

```powershell
Get-NetIPConfiguration
Get-NetAdapter
Get-NetRoute
Get-NetNeighbor
```

### Testar conectividade

```bat
ping 8.8.8.8
ping google.com
tracert google.com
nslookup google.com
```

PowerShell:

```powershell
Test-Connection google.com -Count 4
Resolve-DnsName google.com
Test-NetConnection google.com -Port 443
```

### Ver conexões e portas

```bat
netstat -ano
netstat -ano | findstr LISTENING
```

PowerShell:

```powershell
Get-NetTCPConnection
Get-NetTCPConnection -State Listen
```

## Linux - comandos essenciais

### Ver configuração de rede

```bash
ip addr
ip link
ip route
hostname -I
resolvectl status
```

### Testar conectividade

```bash
ping 8.8.8.8
ping google.com
traceroute google.com
dig google.com
nslookup google.com
```

### Ver conexões e portas

```bash
ss -tulpn
ss -tunap
```

### Testar HTTP

```bash
curl -I https://example.com
curl -v https://example.com
```

## Interpretação rápida

| Sintoma | Hipótese provável | Teste |
|---|---|---|
| IP ausente | DHCP, interface, cabo, Wi-Fi | `ipconfig`, `ip addr` |
| ping para IP funciona, domínio não | DNS | `nslookup`, `dig` |
| DNS resolve, mas não conecta | rota, firewall, porta, serviço | `tracert`, `traceroute`, teste de porta |
| porta fechada | serviço fora ou firewall | `netstat`, `ss`, `Test-NetConnection` |
| HTTP 500 | aplicação respondeu com erro | logs da aplicação |
| timeout | rota, firewall, destino indisponível | trace e teste de porta |
| connection refused | host respondeu, porta sem serviço | verificar serviço no destino |

## DNS

DNS converte nome em IP. Se DNS falha, o usuário costuma dizer “internet caiu”, mas a rede pode estar funcionando.

Windows:

```bat
nslookup dominio.com
ipconfig /displaydns
```

PowerShell:

```powershell
Resolve-DnsName dominio.com
```

Linux:

```bash
dig dominio.com
nslookup dominio.com
resolvectl query dominio.com
```

## Gateway e rota

Sem rota padrão, o host pode falar com a rede local, mas não com a internet.

Windows:

```bat
route print
```

Linux:

```bash
ip route
```

Procurar por rota default:

```txt
default via <gateway>
```

## Portas e sockets

Porta aberta não garante aplicação saudável. Ela só indica que algo está ouvindo.

| Estado | Significado |
|---|---|
| LISTEN | processo aguardando conexão |
| ESTABLISHED | conexão ativa |
| TIME_WAIT | conexão encerrada aguardando limpeza |
| SYN_SENT | tentativa de conexão saindo |

## Firewall

Diagnóstico seguro começa observando regras e sintomas, não desligando firewall.

Windows:

```powershell
Get-NetFirewallProfile
Get-NetFirewallRule | Select-Object -First 20
```

Linux, depende da distro:

```bash
ufw status
firewall-cmd --state
nft list ruleset
```

## Roteiro de diagnóstico

### Caso: site não abre

1. Testar IP local.
2. Testar gateway.
3. Testar IP externo.
4. Testar DNS.
5. Testar porta 443.
6. Testar HTTP com cabeçalho.
7. Conferir proxy/VPN/firewall.
8. Conferir logs de aplicação se o servidor for próprio.

### Caso: API local não responde

1. Ver processo.
2. Ver porta local.
3. Ver bind address: `127.0.0.1` vs `0.0.0.0`.
4. Ver firewall.
5. Testar `localhost`.
6. Testar IP da máquina.
7. Ver logs.

## Bind address

| Bind | Significado |
|---|---|
| `127.0.0.1` | acessível só localmente |
| `0.0.0.0` | escuta em todas as interfaces IPv4 |
| `::` | escuta em IPv6, pode incluir IPv4 dependendo do sistema |

Erro comum: aplicação está rodando, mas presa em `localhost`, então outra máquina não consegue acessar.

## Checklist final

- [ ] IP existe?
- [ ] Gateway existe?
- [ ] DNS resolve?
- [ ] Rota chega perto do destino?
- [ ] Porta está ouvindo?
- [ ] Firewall permite?
- [ ] Serviço está saudável?
- [ ] Aplicação responde?
- [ ] Logs confirmam?

## Regra de ouro

> Ping testa alcance básico. DNS testa nome. Porta testa serviço ouvindo. HTTP testa aplicação.
