---
title: "Port Already in Use — Quick Fix"
description: "Resolve 'address already in use' errors"
tags: [troubleshooting, port, process, network, playbook, jarvis-engenharia]
updated: 2026-04-27
date: 2026-04-27
---

# 🔌 Port Already in Use

Fix "port already in use" or "address already in use" errors.

---

## 🔍 Understanding the Problem

**Error messages:**
```bash
Error: listen EADDRINUSE: address already in use :::3000
Error: bind: address already in use
OSError: [Errno 48] Address already in use
```

**Cause:** Another process is already using the port you're trying to bind to.

---

## ❌ Problem: Common Ports (3000, 8000, 5000, etc.)

### Quick Solution (Windows)

**Find and kill the process:**
```powershell
# Find what's using port 3000
netstat -ano | findstr :3000

# Output example:
# TCP    0.0.0.0:3000    0.0.0.0:0    LISTENING    12345
#                                                   ^^^^^ PID

# Kill process by PID
taskkill /PID 12345 /F

# Verify it's free
netstat -ano | findstr :3000
# (should show nothing)
```

**One-liner (PowerShell):**
```powershell
# Kill whatever is using port 3000
$port = 3000
Get-NetTCPConnection -LocalPort $port -ErrorAction SilentlyContinue | 
  ForEach-Object { Stop-Process -Id $_.OwningProcess -Force }
```

### Quick Solution (Linux/Mac)

**Find and kill:**
```bash
# Find what's using port 3000
lsof -i :3000

# Output example:
# COMMAND   PID USER   FD   TYPE DEVICE SIZE/OFF NODE NAME
# node    12345 will   21u  IPv6  0t0     TCP *:3000 (LISTEN)

# Kill by port (Mac/Linux)
kill -9 $(lsof -t -i:3000)

# Or manually by PID
kill -9 12345

# Verify
lsof -i :3000
```

**One-liner:**
```bash
# Kill process on port 3000
sudo fuser -k 3000/tcp  # Linux

# Or
lsof -ti:3000 | xargs kill -9  # Mac/Linux
```

---

## ❌ Problem: Can't Kill Process (Permission Denied)

### Solution (Windows)
```powershell
# Run PowerShell as Administrator
# Right-click → Run as Administrator

# Then kill
taskkill /PID 12345 /F
```

### Solution (Linux/Mac)
```bash
# Use sudo
sudo kill -9 12345

# Or
sudo fuser -k 3000/tcp
```

---

## ❌ Problem: Don't Know Which Port

### Solution

**Find all listening ports:**

**Windows:**
```powershell
# See all listening ports
netstat -ano | findstr LISTENING

# Or with process names
Get-NetTCPConnection -State Listen | 
  Select-Object LocalAddress, LocalPort, OwningProcess, 
  @{Name="ProcessName";Expression={(Get-Process -Id $_.OwningProcess).ProcessName}}
```

**Linux/Mac:**
```bash
# See all listening ports
sudo lsof -iTCP -sTCP:LISTEN -n -P

# Or simpler
sudo netstat -tulpn | grep LISTEN
```

---

## ❌ Problem: Process Respawns Immediately

### Symptoms
- Kill process but port is immediately in use again
- Service auto-restarts

### Solution

**Windows (Service):**
```powershell
# Check if it's a service
Get-Service | Where-Object {$_.Status -eq "Running"} | 
  Select-Object Name, DisplayName | 
  Out-GridView

# Stop service
Stop-Service -Name "ServiceName"

# Disable from starting
Set-Service -Name "ServiceName" -StartupType Disabled
```

**Linux (Systemd):**
```bash
# Check if it's a service
systemctl list-units --type=service --state=running

# Stop service
sudo systemctl stop nginx  # example

# Disable from starting
sudo systemctl disable nginx
```

**Docker container:**
```bash
# Check if it's a container
docker ps

# Stop container
docker stop container_name

# Or stop by port
docker ps --filter "publish=3000"
docker stop <container_id>
```

---

## ❌ Problem: Port Used by Old Dev Server

### Symptoms
- Started dev server, crashed, now can't restart
- Port still held by zombie process

### Solution

**Next.js:**
```bash
# Kill Next.js dev server
pkill -f "next dev"

# Or by port
kill -9 $(lsof -t -i:3000)

# Restart
npm run dev
```

**React (Create React App):**
```bash
# Kill React dev server
pkill -f "react-scripts"

# Or
kill -9 $(lsof -t -i:3000)

# Restart
npm start
```

**Python/Flask/FastAPI:**
```bash
# Kill Python dev server
pkill -f "uvicorn|flask|python"

# Or by port
kill -9 $(lsof -t -i:8000)

# Restart
uvicorn main:app --reload
```

---

## ❌ Problem: Can't Find Process but Port is "Busy"

### Solution (Windows)
```powershell
# Check Hyper-V reserved ports (Windows issue)
netsh interface ipv4 show excludedportrange protocol=tcp

# If your port is in a reserved range:
# 1. Stop Hyper-V
net stop winnat

# 2. Start your app
# 3. Restart Hyper-V (if needed)
net start winnat

# Permanent fix: Reserve your port
netsh int ipv4 add excludedportrange protocol=tcp startport=3000 numberofports=1
```

### Solution (Linux/Mac)
```bash
# Check if port is in TIME_WAIT
netstat -an | grep 3000

# If TIME_WAIT, just wait 30-60 seconds
# Or change SO_REUSEADDR in your app

# Force reuse (in your code):
# Python:
import socket
s = socket.socket()
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(('', 3000))

# Node.js:
server.listen(3000, () => {
  server.on('error', (e) => {
    if (e.code === 'EADDRINUSE') {
      console.log('Port in use, retrying...');
      setTimeout(() => server.listen(3000), 1000);
    }
  });
});
```

---

## 🛠️ Prevention Strategies

### 1. Use Different Ports per Project

**Set port in environment:**
```bash
# .env
PORT=3001  # Instead of default 3000

# Or command line:
npm run dev -- -p 3001  # Next.js
uvicorn main:app --port 8001  # FastAPI
```

### 2. Auto-Find Available Port

**Node.js:**
```javascript
// package.json
"scripts": {
  "dev": "PORT=0 next dev"  // Auto-finds free port
}
```

**Python:**
```python
import socket

def find_free_port():
    with socket.socket() as s:
        s.bind(('', 0))
        return s.getsockname()[1]

port = find_free_port()
uvicorn.run(app, host="0.0.0.0", port=port)
```

### 3. Graceful Shutdown

**Always stop servers properly:**
```bash
# Good: Ctrl+C (sends SIGTERM)
# Bad: Closing terminal without stopping

# If process hangs, Ctrl+C twice
```

### 4. Port Management Script

**Create `.scripts/free-port.ps1`:**
```powershell
param($port)
$proc = Get-NetTCPConnection -LocalPort $port -ErrorAction SilentlyContinue
if ($proc) {
    Stop-Process -Id $proc.OwningProcess -Force
    Write-Host "Freed port $port"
} else {
    Write-Host "Port $port already free"
}
```

**Usage:**
```powershell
.\.scripts\free-port.ps1 3000
```

---

## 📋 Common Port Reference

| Port | Common Use |
|------|-----------|
| 3000 | React, Next.js dev server |
| 5173 | Vite dev server |
| 8000 | FastAPI, Django dev |
| 5000 | Flask dev server |
| 4000 | GraphQL, various APIs |
| 8080 | Alternative HTTP, Tomcat |
| 5432 | PostgreSQL |
| 3306 | MySQL |
| 6379 | Redis |
| 11434 | Ollama |
| 27017 | MongoDB |

---

## 🔗 Related Resources

- [[JARVIS/04-Engineering/Playbooks/Debug/Docker-Not-Starting|Docker Not Starting]] — If Docker is holding the port
- [[JARVIS/02-Operational/Config/ENV-Registry|ENV Registry]] — Managing port environment variables
- [[skills/02-software-engineering/debugging|Debugging Skills]]

---

## 📞 Nuclear Options

**Windows: Restart network stack**
```powershell
# Run as Admin
netsh winsock reset
netsh int ip reset
ipconfig /release
ipconfig /renew
ipconfig /flushdns

# Restart computer
```

**Linux: Restart networking**
```bash
sudo systemctl restart NetworkManager
# Or
sudo service networking restart
```

**Mac: Restart network interface**
```bash
sudo ifconfig en0 down
sudo ifconfig en0 up
```

---

## ✅ Quick Reference Card

```bash
# FIND PROCESS
Windows:  netstat -ano | findstr :3000
Linux:    lsof -i :3000
Mac:      lsof -i :3000

# KILL PROCESS
Windows:  taskkill /PID 12345 /F
Linux:    kill -9 12345
Mac:      kill -9 12345

# KILL BY PORT
Windows:  Get-NetTCPConnection -LocalPort 3000 | %{Stop-Process -Id $_.OwningProcess -Force}
Linux:    sudo fuser -k 3000/tcp
Mac:      lsof -ti:3000 | xargs kill -9
```

---

*Pro tip: Save these one-liners as shell aliases for instant access*
