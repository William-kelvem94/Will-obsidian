---
title: "Docker Not Starting — Troubleshooting"
description: "Systematic approach to fix Docker startup issues"
tags: [troubleshooting, docker, debug, playbook, jarvis-engenharia]
updated: 2026-06-13
date: 2026-04-27
---

# 🐳 Docker Not Starting

Systematic troubleshooting for Docker Desktop/Engine issues.

---

## 🔍 Quick Diagnosis

Run these commands to identify the problem:

### Windows
```powershell
# Check if Docker is running
Get-Service docker
Get-Service com.docker.service

# Check Docker version
docker --version

# Test Docker
docker run hello-world
```

### Linux
```bash
# Check Docker service
systemctl status docker

# Check Docker socket
ls -la /var/run/docker.sock

# Test Docker
docker run hello-world
```

---

## ❌ Problem 1: Docker Service Not Running

### Symptoms
- `Error: Cannot connect to the Docker daemon`
- `Is the docker daemon running?`

### Solution (Windows)
```powershell
# Restart Docker Desktop
Stop-Service com.docker.service
Start-Service com.docker.service

# Or restart from GUI
# Right-click Docker Desktop tray icon → Restart
```

### Solution (Linux)
```bash
sudo systemctl start docker
sudo systemctl enable docker  # Auto-start on boot
```

---

## ❌ Problem 2: WSL 2 Integration Issues (Windows)

### Symptoms
- Docker Desktop says "WSL 2 installation is incomplete"
- `docker: command not found` in WSL

### Solution
1. **Update WSL:**
   ```powershell
   wsl --update
   wsl --shutdown
   ```

2. **Check WSL version:**
   ```powershell
   wsl --list --verbose
   # Ensure your distro is using WSL 2
   ```

3. **Convert to WSL 2 if needed:**
   ```powershell
   wsl --set-version Ubuntu 2
   ```

4. **Enable WSL Integration in Docker Desktop:**
   - Settings → Resources → WSL Integration
   - Enable integration for your distro

---

## ❌ Problem 3: Permission Denied (Linux)

### Symptoms
- `Got permission denied while trying to connect to the Docker daemon socket`

### Solution
```bash
# Add user to docker group
sudo usermod -aG docker $USER

# Log out and back in, or run:
newgrp docker

# Verify
docker run hello-world
```

---

## ❌ Problem 4: Port Already in Use

### Symptoms
- `Error: port is already allocated`
- Container won't start

### Solution
```bash
# Find process using port (e.g., 5432)
# Windows:
netstat -ano | findstr :5432

# Linux:
sudo lsof -i :5432

# Kill the process
# Windows:
taskkill /PID <PID> /F

# Linux:
sudo kill -9 <PID>

# Or change port in docker-compose.yml
ports:
  - "5433:5432"  # Use 5433 on host instead
```

---

## ❌ Problem 5: Disk Space Full

### Symptoms
- `Error: no space left on device`
- Docker commands hang

### Solution
```bash
# Check disk usage
docker system df

# Clean up
docker system prune -a --volumes
# ⚠️ WARNING: This removes all unused data

# Or selectively:
docker container prune  # Remove stopped containers
docker image prune      # Remove unused images
docker volume prune     # Remove unused volumes
```

---

## ❌ Problem 6: Docker Compose Not Found

### Symptoms
- `docker-compose: command not found`
- `docker compose: 'compose' is not a docker command`

### Solution

**New way (Docker Compose V2):**
```bash
# Use 'docker compose' (no hyphen)
docker compose up
```

**Old way (if V2 not installed):**
```bash
# Install docker-compose separately
# Windows: included in Docker Desktop
# Linux:
sudo apt install docker-compose
# Or via pip:
pip install docker-compose
```

---

## ❌ Problem 7: Image Pull Timeout

### Symptoms
- `Error response from daemon: Get https://registry-1.docker.io/v2/: net/http: TLS handshake timeout`

### Solution
```bash
# Check internet connection
ping google.com

# Try with explicit registry
docker pull docker.io/library/nginx:latest

# Increase timeout (add to ~/.docker/config.json)
{
  "experimental": "enabled",
  "max-concurrent-downloads": 3,
  "max-concurrent-uploads": 5
}

# Use a mirror (if in region with restrictions)
# Add to Docker Desktop settings or /etc/docker/daemon.json
{
  "registry-mirrors": ["https://mirror.gcr.io"]
}
```

---

## ❌ Problem 8: Container Exits Immediately

### Symptoms
- Container starts then immediately stops
- `docker ps` shows nothing, but `docker ps -a` shows exited container

### Diagnosis
```bash
# Check logs
docker logs <container-name>

# Check exit code
docker ps -a  # Look at STATUS column

# Common exit codes:
# 0   = Success
# 1   = Application error
# 137 = Killed (OOM or manual kill)
# 139 = Segmentation fault
```

### Solutions
```bash
# Keep container alive (for debugging)
docker run -it <image> /bin/sh

# Check entrypoint/cmd
docker inspect <container> | grep -A5 "Entrypoint\|Cmd"

# Override entrypoint
docker run --entrypoint /bin/sh -it <image>
```

---

## ❌ Problem 9: DNS Resolution Issues

### Symptoms
- Can't reach external sites from container
- `ping google.com` fails inside container

### Solution
```bash
# Test DNS
docker run alpine ping -c 3 google.com

# Add custom DNS to docker-compose.yml
services:
  myapp:
    dns:
      - 8.8.8.8
      - 8.8.4.4

# Or in /etc/docker/daemon.json
{
  "dns": ["8.8.8.8", "8.8.4.4"]
}

# Restart Docker after editing daemon.json
```

---

## 🛠️ Nuclear Option: Full Reset

**⚠️ WARNING: This deletes ALL Docker data**

### Windows
1. Close Docker Desktop
2. Open PowerShell as Admin:
   ```powershell
   # Remove all data
   Remove-Item -Recurse -Force $env:APPDATA\Docker
   Remove-Item -Recurse -Force $env:LOCALAPPDATA\Docker
   
   # Restart Docker Desktop
   ```

### Linux
```bash
# Stop Docker
sudo systemctl stop docker

# Remove all data
sudo rm -rf /var/lib/docker

# Restart Docker
sudo systemctl start docker
```

---

## 📋 Prevention Checklist

- [ ] Keep Docker Desktop updated
- [ ] Allocate sufficient RAM (min 4GB)
- [ ] Allocate sufficient disk space (min 20GB)
- [ ] Run `docker system prune` monthly
- [ ] Back up important volumes
- [ ] Use `.dockerignore` to reduce build context
- [ ] Pin image versions (don't use `latest`)

---

## 🔗 Related Resources

- [[02-JARVIS/04-Engineering/Playbooks/Workflows-Praticos|Workflows]] — Docker best practices
- [[05-Skills/03-infrastructure-mcp/local-llm-ops|Local LLM Ops]] — Running models in Docker
- [Docker Documentation](https://docs.docker.com/)

---

## 📞 Still Stuck?

1. Check Docker Desktop logs: Settings → Troubleshoot → Show Logs
2. Check system logs:
   - Windows: Event Viewer → Windows Logs → Application
   - Linux: `journalctl -u docker`
3. Search for error message on [Docker Forums](https://forums.docker.com/)
4. Check GitHub issues for your OS: https://github.com/docker/for-win/issues

---

*Keep this playbook updated as you encounter and solve new issues*

[[02-JARVIS/README|← Voltar ao Command Center]]
