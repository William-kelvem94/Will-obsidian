---
title: "Linux e WSL2 — Cheat Sheet"
description: "Guia de referência rápida para Linux (Ubuntu/Debian) e WSL2 — comandos, shell scripting, administração e integração"
tags: [cheatsheet, linux, wsl, terminal, comandos, jarvis-engenharia]
updated: 2026-06-08
date: 2026-05-16
---

# Linux e WSL2 — Cheat Sheet

Referência completa para o terminal Linux, shell scripting, administração do sistema e configuração do WSL2.

---

## 📋 Sumário

- [⚙️ WSL2 — Instalação e Configuração](#-wsl2--instalação-e-configuração)
- [📂 Navegação e Arquivos](#-navegação-e-arquivos)
- [📝 Texto e Visualização](#-texto-e-visualização)
- [🔐 Permissões e Propriedade](#-permissões-e-propriedade)
- [👤 Usuários e Grupos](#-usuários-e-grupos)
- [📦 Gerenciamento de Pacotes](#-gerenciamento-de-pacotes)
- [📁 Hierarquia do Sistema](#-hierarquia-do-sistema)
- [⚡ Processos](#-processos)
- [🌐 Rede](#-rede)
- [🔗 SSH](#-ssh)
- [📜 Shell Scripting (Bash)](#-shell-scripting-bash)
- [🐳 Docker no WSL2](#-docker-no-wsl2)
- [🛠️ Utilitários Essenciais](#-utilitários-essenciais)
- [🔍 Diagnóstico e Performance](#-diagnóstico-e-performance)
- [🐛 Troubleshooting](#-troubleshooting)
- [🔗 Relacionados](#-relacionados)

---

## ⚙️ WSL2 — Instalação e Configuração

### Instalação (Windows)

```powershell
# Terminal Windows (PowerShell como Admin)

# Instalar WSL
wsl --install
wsl --install -d Ubuntu-24.04  # Versão específica

# Verificar status
wsl --status
wsl -l -v                      # Lista distros com versão WSL

# Configurar WSL2 como padrão
wsl --set-default-version 2

# Alterar versão de uma distro
wsl --set-version Ubuntu-24.04 2

# Encerrar WSL
wsl --shutdown

# Exportar/Importar distro
wsl --export Ubuntu-24.04 D:\backup\ubuntu.tar
wsl --import Ubuntu-clone D:\wsl\ubuntu-clone D:\backup\ubuntu.tar

# Desinstalar
wsl --unregister Ubuntu-24.04
```

### .wslconfig (global, em %UserProfile%)

```ini
[wsl2]
memory=8GB
processors=4
localhostForwarding=true
swap=2GB
swapFile=D:\\wsl\\swap.vhdx
kernelCommandLine = "vsyscall=emulate"

# Aplicar: wsl --shutdown e reiniciar
```

### Configuração por distro (/etc/wsl.conf)

```ini
# Dentro do WSL: /etc/wsl.conf
[network]
hostname = devbox
generateHosts = false
generateResolvConf = true

[interop]
enabled = true
appendWindowsPath = true

[user]
default = william

[boot]
command = "service docker start"

# Aplicar: wsl --shutdown e reiniciar
```

### Dicas WSL2

```bash
# Acessar arquivos do Windows
cd /mnt/c/Users/William/
cd /mnt/d/projetos/

# Abrir diretório no Explorer
explorer.exe .

# Executar exe Windows do WSL
notepad.exe ~/.bashrc
code .

# Acessar WSL do Windows
\\wsl.localhost\Ubuntu-24.04\home\william

# Integração com terminal
# Recomendado: Windows Terminal + Oh My Zsh
# Instalar: sudo apt install zsh
# chsh -s /usr/bin/zsh
```

---

## 📂 Navegação e Arquivos

```bash
# Navegação
pwd                              # Diretório atual
ls                               # Listar
ls -la                           # Detalhado + ocultos
ls -lhS                          # Detalhado + ordenado por tamanho
tree                             # Árvore (sudo apt install tree)
tree -L 2                        # Profundidade 2

# Mudar diretório
cd ~                             # Home
cd -                             # Diretório anterior
cd /                             # Raiz

# Manipulação
touch arquivo.txt                # Criar vazio
cp origem.txt destino.txt
cp -r pasta/ backup/
mv arquivo.txt ~/Documents/
rm arquivo.txt
rm -rf pasta/                   # Recursivo + forçado (CUIDADO!)
rm -i arquivo.txt               # Interativo (pergunta)

# Diretórios
mkdir nova-pasta
mkdir -p a/b/c/d                # Cria hierarquia
rmdir pasta-vazia

# Links
ln -s /caminho/real link        # Link simbólico
ln arquivo.txt hard-link        # Hard link

# Busca
find . -name "*.py"             # Por nome
find . -type f -size +10M       # Arquivos > 10MB
find . -mtime -7                # Modificados nos últimos 7 dias
find . -exec grep -l "TODO" {} \;  # Busca texto + executa

# Locate (banco indexado, mais rápido)
sudo updatedb
locate docker-compose.yml

# Disk usage
du -sh *                        # Tamanho dos itens
du -sh .                        # Total do diretório
df -h                           # Espaço livre nos discos
```

---

## 📝 Texto e Visualização

```bash
# Visualização
cat arquivo.txt                 # Conteúdo completo
less arquivo.txt                # Paginação (q sai, / busca)
head -n 20 arquivo.txt          # Primeiras 20 linhas
tail -n 20 arquivo.txt          # Últimas 20 linhas
tail -f log.txt                 # Follow (logs em tempo real)

# Edição in-place com sed
sed -i 's/antigo/novo/g' arquivo.txt
sed -i '/linha/d' arquivo.txt   # Remove linha

# awk (processamento por colunas)
awk '{print $1, $3}' dados.txt  # Colunas 1 e 3
awk -F: '{print $1}' /etc/passwd  # Separador :
awk '$3 > 50' dados.txt         # Filtro por valor

# grep
grep "erro" arquivo.log
grep -r "TODO" src/             # Recursivo
grep -i "warning" log.txt       # Case-insensitive
grep -l "function" *.py         # Só nomes de arquivos
grep -c "erro" *.log            # Contagem
grep -v "debug" log.txt         # Inverte (exclui)
grep -E "err(or|or)" log.txt    # Regex estendida

# sort / uniq
sort arquivo.txt
sort -n numeros.txt             # Numérico
sort -u arquivo.txt             # Únicas
sort arquivo.txt | uniq -c      # Contagem de ocorrências

# wc (word count)
wc -l arquivo.txt               # Linhas
wc -w arquivo.txt               # Palavras
wc -c arquivo.txt               # Bytes

# diff
diff arquivo1.txt arquivo2.txt
diff -u arquivo1.txt arquivo2.txt  # Unified (format diff)

# cut
cut -d: -f1,3 /etc/passwd       # Colunas 1 e 3 com separador :

# tr (translate)
echo "hello" | tr 'a-z' 'A-Z'  # HELLO
cat arquivo.txt | tr -d '\r'    # Remove CR (Windows)
```

---

## 🔐 Permissões e Propriedade

```bash
# Entendendo permissões (rwxr-xr-x)
# r=4, w=2, x=1
# 755 = rwxr-xr-x (dono=rwx, grupo=rx, outros=rx)
# 644 = rw-r--r-- (dono=rw, grupo=r, outros=r)

# Alterar permissões
chmod 755 script.sh
chmod +x script.sh               # +x executável
chmod -R 644 pasta/              # Recursivo
chmod u+x arquivo                # Só dono
chmod g+w arquivo                # Só grupo
chmod o-r arquivo                # Remove leitura de outros

# Alterar proprietário
sudo chown william:william arquivo.txt
sudo chown -R william:william pasta/
sudo chgrp grupo arquivo.txt

# Umask (permissões padrão)
umask                           # Mostra (022 = 755 dir, 644 file)
umask 077                       # Restritivo (apenas dono)
```

---

## 👤 Usuários e Grupos

```bash
# Usuários
whoami                          # Usuário atual
id                              # UID, GID, grupos
users                           # Usuários logados
who                             # Detalhes dos logados

# Gerenciar
sudo useradd -m joao            # Cria com home
sudo userdel -r joao            # Remove com home
sudo usermod -aG docker $USER   # Adiciona a grupo
sudo passwd joao                # Altera senha

# Grupos
groups                          # Grupos do usuário
groupadd devops                 # Criar grupo
groupdel devops                 # Remover grupo

# sudo
sudo -i                         # Shell como root
sudo -u joao comando            # Executar como joao
sudo -l                         # Listar permissões sudo
sudo visudo                     # Editar /etc/sudoers
```

---

## 📦 Gerenciamento de Pacotes

### APT (Debian/Ubuntu)

```bash
# Repositórios
sudo apt update                 # Atualiza lista
sudo apt upgrade                # Atualiza pacotes
sudo apt full-upgrade           # Com remoção se necessário
sudo apt dist-upgrade           # Atualiza distro

# Buscar
apt search python
apt show python3

# Instalar/Remover
sudo apt install python3 nodejs
sudo apt remove nginx
sudo apt purge nginx            # Remove + configs
sudo apt autoremove             # Remove dependências órfãs

# PPAs
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt update
sudo apt install python3.12
```

### Homebrew (Linux)

```bash
# Instalar
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Usar
brew search pacote
brew install gh jq ripgrep
brew update
brew upgrade
brew cleanup
```

### Pip / NPM / Cargo

```bash
# Python
pip install poetry black ruff
pip install --user pipx
pipx ensurepath
pipx run black .               # Executa sem instalar

# Node
npm install -g pnpm tsx
npx create-next-app@latest

# Rust (Cargo)
cargo install bat exa ripgrep fd-find
```

---

## 📁 Hierarquia do Sistema

```bash
/               # Raiz
├── bin/        # Binários essenciais (ls, cp, mv)
├── boot/       # Kernel e bootloader
├── dev/        # Dispositivos
├── etc/        # Configurações do sistema
│   ├── nginx/
│   ├── ssh/
│   └── systemd/
├── home/       # Diretórios dos usuários
├── lib/        # Bibliotecas compartilhadas
├── media/      # Montagem automática (USB, CD)
├── mnt/        # Montagem manual (/mnt/c no WSL)
├── opt/        # Pacotes opcionais (Google Chrome, ...)
├── proc/       # Sistema de arquivos virtual (processos)
├── root/       # Home do root
├── run/        # Arquivos temporários em execução
├── sbin/       # Binários de sistema (fdisk, mkfs)
├── snap/       # Pacotes Snap
├── srv/        # Dados de serviços (HTTP, FTP)
├── sys/        # Informações do kernel
├── tmp/        # Arquivos temporários (limpos no boot)
└── usr/        # Programas do usuário
    ├── bin/
    ├── lib/
    └── local/  # Instalações locais
```

---

## ⚡ Processos

```bash
# Visualizar
ps aux                           # Todos os processos
ps aux --sort=-%mem              # Ordenado por memória
ps aux | grep nginx              # Filtrar

# htop (visual, interativo)
sudo apt install htop
htop                             # F4 busca, F9 kill, F10 sai

# Gerenciar
kill 1234                        # SIGTERM (pede pra parar)
kill -9 1234                     # SIGKILL (mata na hora)
killall nginx                    # Mata pelo nome

# Background / Foreground
comando &                        # Roda em background
Ctrl + Z                         # Suspende
bg                               # Retoma em background
fg                               # Retoma em foreground
jobs                             # Lista jobs

# systemd (gerenciamento de serviços)
sudo systemctl status nginx
sudo systemctl start nginx
sudo systemctl stop nginx
sudo systemctl restart nginx
sudo systemctl enable nginx      # Iniciar no boot
sudo systemctl disable nginx     # Não iniciar no boot
sudo systemctl daemon-reload     # Recarregar configs
sudo systemctl --failed          # Serviços com falha
journalctl -u nginx -f           # Logs de serviço
```

---

## 🌐 Rede

```bash
# curl
curl https://api.github.com
curl -o arquivo.zip https://exemplo.com/file.zip
curl -L http://bit.ly/url-curta  # Follow redirect
curl -H "Authorization: Bearer token" https://api.exemplo.com
curl -X POST -d '{"key":"value"}' -H "Content-Type: application/json" url

# wget
wget https://exemplo.com/arquivo.zip
wget -c https://exemplo.com/grande.zip  # Continuar download
wget -r -np https://site.com/pasta/     # Recursivo

# netstat / ss
netstat -tulpn                     # Portas escutando
netstat -an | grep :80             # Conexões na porta 80
ss -tulpn                          # Alternativa moderna
ss -s                              # Estatísticas

# nmap
sudo apt install nmap
nmap localhost                    # Escaneia portas locais
nmap -p 1-1000 192.168.1.1       # Range de portas
nmap -sn 192.168.1.0/24          # Descoberta de hosts

# DNS
host exemplo.com
dig exemplo.com
nslookup exemplo.com
cat /etc/resolv.conf              # DNS configurado

# IP
ip addr                           # Interfaces (substituto ifconfig)
ip route                          # Roteamento (substituto route)
ip link set eth0 up               # Ativar interface
ping -c 4 google.com

# Firewall (UFW)
sudo ufw status
sudo ufw allow 22/tcp
sudo ufw allow 80
sudo ufw enable
sudo ufw disable

# iptables (avançado)
sudo iptables -L -n -v
```

---

## 🔗 SSH

```bash
# Gerar chave
ssh-keygen -t ed25519 -C "seu@email.com"
ssh-keygen -t rsa -b 4096 -C "seu@email.com"

# Gerenciar chaves
ls ~/.ssh/
cat ~/.ssh/id_ed25519.pub

# Conectar
ssh usuario@host
ssh -p 2222 usuario@host          # Porta personalizada
ssh -i ~/.ssh/chave_privada user@host
ssh -J jump@host1 user@host2     # Jump host (bounce)

# Config (~/.ssh/config)
# Host myserver
#     HostName 192.168.1.100
#     User william
#     Port 2222
#     IdentityFile ~/.ssh/server
#     LocalForward 3000 localhost:3000

ssh myserver                     # Usa a config acima

# SCP
scp arquivo.txt user@host:/caminho/
scp -r pasta/ user@host:/caminho/
scp user@host:/caminho/arquivo.txt ./

# Rsync
rsync -avz pasta/ user@host:/caminho/
rsync -avz --progress user@host:/caminho/ pasta/
rsync -avz --delete pasta/ user@host:/caminho/  # Sincroniza remoções

# SSH agent
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_ed25519
ssh-add -l                       # Lista chaves carregadas

# Tunnel reverso
ssh -R 8080:localhost:3000 user@host  # Expõe porta local no host remoto
```

---

## 📜 Shell Scripting (Bash)

### Variáveis

```bash
# Atribuição (sem espaços!)
NOME="William"
IDADE=30

# Uso
echo "$NOME tem $IDADE anos"
echo "$NOME"                     # Aspas preservam espaços

# Array
FRUTAS=("maçã" "banana" "laranja")
echo "${FRUTAS[0]}"             # maçã
echo "${FRUTAS[@]}"             # Todos
echo "${#FRUTAS[@]}"            # Tamanho

# Especiais
$0, $1, $2...                   # Argumentos do script
$#                              # Número de argumentos
$@                              # Todos argumentos
$?                              # Código de saída do último comando
$$                              # PID do script
```

### Condicionais

```bash
if [[ "$NOME" == "William" ]]; then
    echo "Olá William"
elif [[ -z "$NOME" ]]; then
    echo "Nome vazio"
else
    echo "Quem é você?"
fi

# Operadores de arquivo
[[ -f "$arquivo" ]]           # Existe e é arquivo
[[ -d "$pasta" ]]             # Existe e é diretório
[[ -x "$script" ]]            # É executável
[[ -z "$var" ]]               # String vazia
[[ -n "$var" ]]               # String não vazia

# Lógicos
[[ -f "$file" && -r "$file" ]]  # Existe E é legível
[[ "$a" == "x" || "$b" == "y" ]]
```

### Loops

```bash
# For
for i in {1..10}; do
    echo "Número $i"
done

for file in *.txt; do
    echo "Processando $file"
done

for ((i=0; i<10; i++)); do
    echo $i
done

# While
count=0
while [[ $count -lt 5 ]]; do
    echo "Contagem: $count"
    ((count++))
done

# Until
until ping -c1 google.com &>/dev/null; do
    echo "Aguardando rede..."
    sleep 2
done
```

### Funções

```bash
function log_info() {
    local message="$1"           # local = escopo da função
    echo "[INFO] $(date '+%H:%M:%S'): $message"
}

log_error() {
    echo "[ERROR] $*" >&2        # stderr
    exit 1
}

# Retorno numérico (0-255)
is_valid() {
    [[ "$1" =~ ^[0-9]+$ ]] && return 0 || return 1
}

if is_valid "42"; then
    echo "É número"
fi

# Função com --flags
usage() {
    cat <<EOF
Uso: $0 [opções]
  -h, --help     Mostra ajuda
  -v, --verbose  Modo verboso
EOF
}
```

### Script exemplo completo

```bash
#!/usr/bin/env bash
set -euo pipefail                 # Segurança: para no erro, undefined vars, pipe fails

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
LOG_FILE="${SCRIPT_DIR}/setup.log"

log() {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] $*" | tee -a "$LOG_FILE"
}

error() {
    log "ERRO: $*"
    exit 1
}

check_dependency() {
    command -v "$1" &>/dev/null || error "$1 não encontrado. Instale com: sudo apt install $1"
}

main() {
    log "Iniciando setup..."

    check_dependency "docker"
    check_dependency "node"

    if [[ ! -f ".env" ]]; then
        cp .env.example .env
        log "Arquivo .env criado"
    fi

    log "Instalando dependências..."
    npm install || error "Falha no npm install"

    log "Setup concluído com sucesso!"
}

main "$@"
```

---

## 🐳 Docker no WSL2

```bash
# Instalar Docker (dentro do WSL)
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh

# OU usar Docker Desktop (Windows) com integração WSL2
# Settings > Resources > WSL Integration > Habilitar distro

# Adicionar usuário ao grupo docker (evitar sudo)
sudo usermod -aG docker $USER
newgrp docker                    # Aplicar na sessão atual

# Verificar
docker run hello-world
docker info

# Docker Compose
sudo apt install docker-compose-plugin
docker compose version

# Performance: montar projetos dentro do WSL (não /mnt/c)
# /mnt/c/ é lento para I/O intensivo
# Use ~/projects/ ao invés de /mnt/c/Users/...

# Dica: WSL2 + Docker = performance quase nativa
# Monitorar uso:
docker stats
docker system df
```

### docker-compose.yml para dev local

```yaml
version: "3.8"

services:
  app:
    build: .
    ports:
      - "3000:3000"
    volumes:
      - .:/app
      - /app/node_modules
    environment:
      - DATABASE_URL=postgresql://user:pass@db:5432/dev
    depends_on:
      - db

  db:
    image: postgres:16
    environment:
      POSTGRES_USER: user
      POSTGRES_PASSWORD: pass
      POSTGRES_DB: dev
    volumes:
      - pgdata:/var/lib/postgresql/data
    ports:
      - "5432:5432"

volumes:
  pgdata:
```

---

## 🛠️ Utilitários Essenciais

```bash
# Substituições modernas para comandos clássicos
sudo apt install bat ripgrep fd-find eza htop jq

# cat com syntax highlighting
bat arquivo.py                   # Alternativa ao cat

# grep mais rápido
rg "padrão" src/                 # Alternativa ao grep -r
rg -l "TODO"                     # Só nomes
rg -C 3 "função" *.py            # Contexto 3 linhas

# find mais rápido
fd "*.py"                        # Alternativa ao find
fd -e md -x wc -l {}             # Executa comando

# ls melhorado
eza -la                          # Alternativa ao ls (exa)
eza --tree                       # Árvore

# JSON
jq '.users[] | {name, email}' data.json
curl api.github.com | jq '.[0].name'
jq -r '.version' package.json

# Ver/editar arquivos binários
xxd arquivo.bin | head
hexdump -C arquivo.bin

# Monitorar
watch -n 1 "docker ps"           # Executa a cada 1s
watch df -h

# Screen / Tmux
tmux new -s sessao
tmux attach -t sessao
# Ctrl+B % = split vertical
# Ctrl+B " = split horizontal
# Ctrl+B d = detach
```

---

## 🔍 Diagnóstico e Performance

```bash
# Sistema
uname -a                         # Kernel info
lsb_release -a                   # Distro + versão
hostnamectl                      # Tudo sobre o sistema

# Hardware
lscpu                            # CPU
free -h                          # RAM
lsblk                            # Discos
lspci                            # Dispositivos PCI
lsusb                            # USB

# Logs
dmesg | tail -20                 # Mensagens do kernel
journalctl -xe                   # Logs do sistema (últimos)
journalctl -p err -b             # Erros do boot atual

# Performance
uptime                           # Tempo ativo + load average
top -o %MEM                      # Processos por memória
htop                             # Visual (instalar antes)

# Discos
iostat -x 1                      # I/O por disco (sysstat)
iotop                            # I/O por processo

# Rede
iperf3 -c servidor               # Teste de banda
mtr google.com                   # traceroute + ping
nethogs                          # Banda por processo (sudo)
```

---

## 🐛 Troubleshooting

### Issue: WSL não inicia (0x80370102, 0x800701bc, etc.)

```powershell
# Terminal PowerShell (Admin)

# 1. Verificar virtualização habilitada
systeminfo | findstr "Virtualization"
# Deve mostrar: "Yes"

# 2. Habilitar WSL
dism.exe /online /enable-feature /featurename:Microsoft-Windows-Subsystem-Linux /all /norestart
dism.exe /online /enable-feature /featurename:VirtualMachinePlatform /all /norestart

# 3. Atualizar kernel WSL2
# Baixar de: https://aka.ms/wsl2kernel

# 4. Reiniciar
wsl --shutdown
```

### Issue: "Permission denied" em scripts

```bash
# Dar permissão de execução
chmod +x script.sh

# Ou executar explicitamente
bash script.sh

# Verificar dono
ls -la script.sh
# Se for de outro usuário: sudo chown $USER:$USER script.sh
```

### Issue: Porta já em uso (WSL vs Windows)

```bash
# WSL e Windows compartilham localhost
# Verificar conflitos no Windows:
netstat -ano | findstr :3000

# Ou dentro do WSL:
ss -tulpn | grep 3000

# Soluções:
# 1. Use porta diferente
# 2. Mate o processo: kill -9 $(lsof -ti:3000)
# 3. Desligue o serviço Windows (ex: IIS, postgres local)
```

### Issue: Erro de DNS no WSL

```bash
# "Temporary failure in name resolution"
# Causa: resolv.conf gerado pelo WSL

# Solução temporária:
sudo echo "nameserver 8.8.8.8" > /etc/resolv.conf

# Solução permanente (/etc/wsl.conf):
# [network]
# generateResolvConf = false

# Depois:
sudo rm /etc/resolv.conf
sudo nano /etc/resolv.conf
# Adicionar: nameserver 8.8.8.8
# Adicionar: nameserver 1.1.1.1

wsl --shutdown  # E reiniciar
```

### Issue: Disco cheio no WSL

```bash
# Verificar uso
df -h /
du -sh ~/* | sort -rh | head -10

# Arquivos grandes (cache apt, docker, npm)
sudo apt clean                   # Limpa cache apt
docker system prune -a           # Limpa Docker
npm cache clean --force
pip cache purge

# VHDX não reduz automaticamente
# No Windows (Admin PowerShell):
diskpart
select vdisk file="C:\Users\William\AppData\Local\Packages\...\LocalState\ext4.vhdx"
compact vdisk
detach vdisk
exit
```

### Issue: "command not found" após instalar

```bash
# Caminho não está no PATH
echo $PATH

# Adicionar ao ~/.bashrc (~/.zshrc)
export PATH="$HOME/.local/bin:$PATH"
export PATH="$HOME/.cargo/bin:$PATH"
# source ~/.bashrc

# Verificar onde foi instalado
which comando
# Se vazio: find / -name "comando" 2>/dev/null
```

### Issue: Memória WSL2 cresce sem limite

```powershell
# Arquivo .wslconfig em %UserProfile%:
# [wsl2]
# memory=4GB    # Limite de RAM
# swap=2GB

# Aplicar: wsl --shutdown
# Para liberar sem reiniciar:
sudo sh -c "echo 1 > /proc/sys/vm/drop_caches"
```

---

## 🔗 Relacionados

- [WSL Docs](https://learn.microsoft.com/en-us/windows/wsl/)
- [Linux Command](https://linuxcommand.org/)
- [[05-Skills/03-infrastructure-mcp|Infrastructure Skills]]
- [[02-JARVIS/04-Engineering/Wiki/CheatSheets/Docker|Docker Cheat Sheet]]
- [[02-JARVIS/04-Engineering/Playbooks/Debug/WSL-Not-Starting|WSL Troubleshooting]]

[[02-JARVIS/README|← Voltar ao Command Center]]
