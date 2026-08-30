---
title: "Linux, Terminal e Bash"
date: 2026-07-07
updated: 2026-07-07
type: knowledge
status: active
classe_privacidade: publico-tecnico
indexavel: true
uso_ia: livre
tags: [linux, bash, terminal, shell, sistemas-operacionais, administracao]
summary: "Base operacional para dominar Linux via terminal, Bash, processos, serviços, logs, rede, permissões e pacotes."
---

# Linux, Terminal e Bash

Linux é melhor entendido como um conjunto de peças pequenas, composáveis e observáveis.

O terminal é o painel de instrumentos. Bash é a linguagem do cockpit. O sistema de arquivos é o mapa. Processos, serviços, logs e rede são os sinais vitais.

## Distribuições e famílias

| Família | Exemplos | Gerenciador comum |
|---|---|---|
| Debian/Ubuntu | Ubuntu, Debian, Mint | `apt` |
| Red Hat | Fedora, RHEL, Rocky, Alma | `dnf`, `yum` |
| Arch | Arch, Manjaro | `pacman` |
| SUSE | openSUSE, SLES | `zypper` |
| Alpine | Alpine Linux | `apk` |

## Identificação do sistema

```bash
uname -a
hostname
whoami
id
cat /etc/os-release
lsb_release -a
uptime
hostnamectl
```

## Navegação

```bash
pwd
ls
ls -la
cd /etc
cd ~
cd -
tree
```

Atalhos úteis:

| Atalho | Função |
|---|---|
| `~` | home do usuário |
| `.` | diretório atual |
| `..` | diretório acima |
| `-` | último diretório |

## Arquivos e diretórios

```bash
mkdir logs
touch app.log
cp origem.txt destino.txt
cp -r pasta copia-pasta
mv antigo.txt novo.txt
mv arquivo.txt pasta/
cat arquivo.txt
less arquivo.txt
head arquivo.txt
tail arquivo.txt
tail -f app.log
```

## Busca de arquivos e texto

```bash
find . -name "*.log"
find /var/log -type f -name "*.log"
grep "erro" app.log
grep -R "erro" ./logs
grep -Rin "timeout" .
which python
whereis python
```

Ferramentas modernas, quando disponíveis:

```bash
rg "erro"
fd "*.log"
bat arquivo.txt
exa -la
```

## Pipes e redirecionamento

```bash
comando > saida.txt
comando >> saida.txt
comando 2> erro.txt
comando > saida.txt 2>&1
cat app.log | grep erro | tail -20
```

| Símbolo | Função |
|---|---|
| `>` | sobrescreve saída |
| `>>` | adiciona ao final |
| `2>` | redireciona erro |
| `|` | envia saída para outro comando |

## Processos

```bash
ps aux
ps aux | grep nginx
top
htop
pgrep nginx
pidof nginx
```

Encerrar processo exige cuidado:

```bash
kill -TERM 1234
kill -KILL 1234
pkill -TERM nome-processo
```

Preferir `TERM` antes de `KILL`. `KILL` não dá chance de limpeza ao processo.

## Serviços com systemd

```bash
systemctl status nginx
systemctl start nginx
systemctl stop nginx
systemctl restart nginx
systemctl enable nginx
systemctl disable nginx
systemctl list-units --type=service
systemctl --failed
```

## Logs com journalctl

```bash
journalctl
journalctl -xe
journalctl -u nginx
journalctl -u nginx -f
journalctl --since "1 hour ago"
journalctl -p err
```

Logs clássicos:

```bash
ls /var/log
tail -f /var/log/syslog
tail -f /var/log/auth.log
tail -f /var/log/messages
```

## Rede

```bash
ip addr
ip route
ping 8.8.8.8
ping google.com
traceroute google.com
ss -tulpn
dig google.com
nslookup google.com
curl -I https://example.com
wget --spider https://example.com
```

Ferramentas por camada:

| Camada | Comandos |
|---|---|
| IP/interface | `ip addr`, `ip link` |
| Rota | `ip route` |
| DNS | `dig`, `nslookup`, `resolvectl` |
| Porta/socket | `ss -tulpn` |
| HTTP | `curl -I`, `curl -v` |

## Permissões

```bash
ls -l
chmod 644 arquivo.txt
chmod 755 script.sh
chown usuario:grupo arquivo.txt
id
groups
umask
```

Permissões comuns:

| Permissão | Arquivo | Diretório |
|---|---|---|
| `644` | dono lê/escreve, outros leem | não ideal para diretórios |
| `755` | executável por todos, escrita só dono | padrão comum de diretório |
| `600` | só dono lê/escreve | arquivos sensíveis |
| `700` | só dono acessa | diretórios sensíveis |

## Pacotes

### Debian/Ubuntu

```bash
apt update
apt search pacote
apt show pacote
apt install pacote
apt remove pacote
apt list --installed
```

### Fedora/RHEL

```bash
dnf search pacote
dnf info pacote
dnf install pacote
dnf remove pacote
dnf list installed
```

### Arch

```bash
pacman -Ss pacote
pacman -Qi pacote
pacman -S pacote
pacman -R pacote
```

## Disco e filesystem

```bash
df -h
du -sh *
lsblk
mount
findmnt
blkid
free -h
vmstat 1
```

Analisar diretórios grandes:

```bash
du -h --max-depth=1 /var | sort -h
```

## Variáveis de ambiente

```bash
env
printenv
printenv PATH
echo $HOME
echo $SHELL
export APP_ENV=dev
```

Arquivos comuns:

| Arquivo | Uso |
|---|---|
| `~/.bashrc` | configuração interativa do Bash |
| `~/.profile` | ambiente do usuário |
| `/etc/environment` | variáveis globais simples |
| `/etc/profile` | shell global |

## Usuários e grupos

```bash
whoami
id
who
w
last
cat /etc/passwd
cat /etc/group
getent passwd usuario
getent group grupo
```

## Cron e tarefas

```bash
crontab -l
crontab -e
systemctl list-timers
```

Exemplo de cron diário às 02:30:

```cron
30 2 * * * /caminho/script.sh >> /var/log/script.log 2>&1
```

## Shell scripting mínimo

```bash
#!/usr/bin/env bash
set -euo pipefail

log() {
  printf '[%s] %s\n' "$(date '+%Y-%m-%d %H:%M:%S')" "$*"
}

log "Iniciando verificação"
command -v curl >/dev/null || { log "curl ausente"; exit 1; }
curl -I https://example.com
log "Finalizado"
```

## Comandos de risco

Evitar sem backup e revisão:

- remoção recursiva ampla;
- alteração recursiva de permissões na raiz;
- escrita direta em discos e partições;
- comandos de rede que alterem firewall/rotas sem janela de manutenção;
- scripts rodando como root sem escopo claro.

## Checklist Linux

1. Identificar distro, kernel e uptime.
2. Conferir CPU, memória, disco e load average.
3. Conferir processos de maior consumo.
4. Conferir serviços falhando.
5. Conferir logs do serviço e do sistema.
6. Testar DNS, rota, porta e HTTP.
7. Validar permissões e usuário de execução.
8. Conferir pacote, versão e configuração.
9. Aplicar correção mínima.
10. Registrar evidência e resultado.

## Modelo mental

Linux é uma oficina com ferramentas pequenas penduradas na parede. O poder vem de combinar ferramentas, não de decorar botão. Quem domina `grep`, `find`, `ss`, `systemctl`, `journalctl` e `chmod` já acende metade da cidade. 🔦
