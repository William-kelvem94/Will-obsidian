---
title: "Docker Cheat Sheet"
description: "Quick reference for Docker commands and best practices"
tags: [cheatsheet, docker, containers, devops, deployment, jarvis-engenharia]
updated: 2026-05-03
date: 2026-04-27
---

# Docker Cheat Sheet

Quick reference for Docker containers and images.

---

## 🚀 Installation

```bash
# Windows (with WSL2)
# Download from: https://www.docker.com/products/docker-desktop

# Linux
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh

# Verify
docker --version
docker compose version
```

---

## 📦 Images

```bash
# List images
docker images

# Pull image
docker pull nginx:latest
docker pull postgres:15

# Remove image
docker rmi nginx:latest

# Remove unused images
docker image prune
docker image prune -a  # Remove all unused

# Build image
docker build -t myapp:latest .
docker build -t myapp:v1.0 -f Dockerfile.prod .

# Tag image
docker tag myapp:latest myapp:v1.0

# Push to registry
docker push myapp:latest

# Inspect image
docker inspect nginx:latest
docker history nginx:latest
```

---

## 🏃 Containers

```bash
# Run container
docker run nginx
docker run -d nginx  # Detached (background)
docker run -it ubuntu bash  # Interactive

# Run with name
docker run -d --name my-nginx nginx

# Run with port mapping
docker run -d -p 8080:80 nginx  # Host:Container

# Run with volume
docker run -d -v $(pwd):/app nginx

# Run with environment variables
docker run -d -e DB_HOST=localhost -e DB_PORT=5432 myapp

# List containers
docker ps  # Running
docker ps -a  # All (including stopped)

# Stop container
docker stop my-nginx
docker stop $(docker ps -q)  # Stop all

# Start container
docker start my-nginx

# Restart container
docker restart my-nginx

# Remove container
docker rm my-nginx
docker rm -f my-nginx  # Force remove (even if running)

# Remove stopped containers
docker container prune

# Logs
docker logs my-nginx
docker logs -f my-nginx  # Follow
docker logs --tail 100 my-nginx  # Last 100 lines

# Execute command in container
docker exec -it my-nginx bash
docker exec my-nginx ls /app

# Inspect container
docker inspect my-nginx

# Container stats
docker stats
docker stats my-nginx
```

---

## 📄 Dockerfile

### Basic Example

```dockerfile
FROM node:18-alpine

WORKDIR /app

COPY package*.json ./
RUN npm ci --only=production

COPY . .

EXPOSE 3000

CMD ["node", "index.js"]
```

### Multi-stage Build

```dockerfile
# Build stage
FROM node:18-alpine AS builder

WORKDIR /app

COPY package*.json ./
RUN npm ci

COPY . .
RUN npm run build

# Production stage
FROM node:18-alpine

WORKDIR /app

COPY package*.json ./
RUN npm ci --only=production

COPY --from=builder /app/dist ./dist

EXPOSE 3000

USER node

CMD ["node", "dist/index.js"]
```

### Python Example

```dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```

### Best Practices

```dockerfile
# Use specific versions
FROM node:18.16.0-alpine

# Create non-root user
RUN addgroup -g 1001 -S nodejs && \
    adduser -S nodejs -u 1001

# Multi-stage for smaller images
FROM node:18-alpine AS deps
FROM node:18-alpine AS builder
FROM node:18-alpine AS runner

# Leverage layer caching
COPY package*.json ./
RUN npm ci
COPY . .

# Use .dockerignore
# node_modules
# .git
# .env

# Health check
HEALTHCHECK --interval=30s --timeout=3s \
  CMD curl -f http://localhost:3000/health || exit 1

# Run as non-root
USER nodejs

# Use ENTRYPOINT + CMD
ENTRYPOINT ["docker-entrypoint.sh"]
CMD ["node", "server.js"]
```

---

## 🐳 Docker Compose

### docker-compose.yml

```yaml
version: '3.8'

services:
  # Web app
  app:
    build: .
    ports:
      - "3000:3000"
    environment:
      - NODE_ENV=production
      - DATABASE_URL=postgresql://user:pass@db:5432/mydb
    depends_on:
      - db
      - redis
    volumes:
      - ./uploads:/app/uploads
    restart: unless-stopped

  # Database
  db:
    image: postgres:15
    environment:
      POSTGRES_USER: user
      POSTGRES_PASSWORD: pass
      POSTGRES_DB: mydb
    ports:
      - "5432:5432"
    volumes:
      - postgres_data:/var/lib/postgresql/data
    restart: unless-stopped

  # Redis
  redis:
    image: redis:7-alpine
    ports:
      - "6379:6379"
    volumes:
      - redis_data:/data
    restart: unless-stopped

  # Nginx (reverse proxy)
  nginx:
    image: nginx:alpine
    ports:
      - "80:80"
    volumes:
      - ./nginx.conf:/etc/nginx/nginx.conf:ro
    depends_on:
      - app
    restart: unless-stopped

volumes:
  postgres_data:
  redis_data:
```

### Commands

```bash
# Start services
docker compose up
docker compose up -d  # Detached

# Build and start
docker compose up --build

# Stop services
docker compose down

# Stop and remove volumes
docker compose down -v

# View logs
docker compose logs
docker compose logs -f app  # Follow specific service

# Execute command
docker compose exec app bash
docker compose exec db psql -U user -d mydb

# Restart service
docker compose restart app

# Scale service
docker compose up -d --scale app=3

# List services
docker compose ps
```

---

## 🌐 Networking

```bash
# List networks
docker network ls

# Create network
docker network create mynetwork

# Run container in network
docker run -d --network mynetwork --name app1 nginx

# Connect container to network
docker network connect mynetwork app2

# Inspect network
docker network inspect mynetwork

# Remove network
docker network rm mynetwork
```

---

## 💾 Volumes

```bash
# List volumes
docker volume ls

# Create volume
docker volume create myvolume

# Use volume
docker run -d -v myvolume:/data nginx

# Inspect volume
docker volume inspect myvolume

# Remove volume
docker volume rm myvolume

# Remove unused volumes
docker volume prune

# Bind mount (host directory)
docker run -d -v /host/path:/container/path nginx
docker run -d -v $(pwd):/app nginx  # Current directory
```

---

## 🔍 Debugging

```bash
# Inspect everything
docker inspect <container-or-image>

# View processes in container
docker top my-nginx

# Resource usage
docker stats

# Disk usage
docker system df

# Container logs
docker logs -f my-nginx

# Execute shell
docker exec -it my-nginx sh

# View changes to filesystem
docker diff my-nginx

# Export container
docker export my-nginx > nginx.tar

# Save/load images
docker save nginx:latest > nginx.tar
docker load < nginx.tar
```

---

## 🧹 Cleanup

```bash
# Remove stopped containers
docker container prune

# Remove unused images
docker image prune
docker image prune -a  # All unused

# Remove unused volumes
docker volume prune

# Remove unused networks
docker network prune

# Remove everything unused
docker system prune
docker system prune -a  # Including stopped containers

# Remove everything (nuclear option)
docker system prune -a --volumes
```

---

## 🚀 Production Patterns

### Health Checks

```dockerfile
HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \
  CMD curl -f http://localhost:3000/health || exit 1
```

### Secrets (Docker Swarm)

```yaml
version: '3.8'

services:
  app:
    image: myapp
    secrets:
      - db_password

secrets:
  db_password:
    file: ./secrets/db_password.txt
```

### Resource Limits

```yaml
services:
  app:
    image: myapp
    deploy:
      resources:
        limits:
          cpus: '0.5'
          memory: 512M
        reservations:
          cpus: '0.25'
          memory: 256M
```

### Restart Policies

```yaml
services:
  app:
    image: myapp
    restart: unless-stopped  # Or: no, always, on-failure
```

---

## 🔐 Security Best Practices

```dockerfile
# 1. Use official base images
FROM node:18-alpine  # Alpine is smaller

# 2. Don't run as root
RUN addgroup -g 1001 -S nodejs && \
    adduser -S nodejs -u 1001
USER nodejs

# 3. Use specific versions
FROM node:18.16.0-alpine

# 4. Multi-stage builds (smaller final image)
FROM node:18 AS builder
FROM node:18-alpine AS runner

# 5. Scan images
docker scan myapp:latest

# 6. Use .dockerignore
# .git
# node_modules
# .env

# 7. Read-only root filesystem
docker run --read-only myapp

# 8. Drop capabilities
docker run --cap-drop=ALL --cap-add=NET_BIND_SERVICE myapp

# 9. Use secrets, not ENV for sensitive data
docker run --secret db_password myapp
```

---

## 📊 Useful Aliases

```bash
# Add to ~/.bashrc or ~/.zshrc

alias dps='docker ps'
alias dpsa='docker ps -a'
alias di='docker images'
alias drm='docker rm'
alias drmi='docker rmi'
alias dex='docker exec -it'
alias dlogs='docker logs -f'
alias dstop='docker stop'
alias dstart='docker start'
alias dcu='docker compose up -d'
alias dcd='docker compose down'
alias dcl='docker compose logs -f'
```

---

## 🐛 Common Issues

### Issue: Port already in use

```bash
# Find what's using the port
netstat -ano | findstr :3000  # Windows
lsof -i :3000  # Mac/Linux

# Kill process or use different port
docker run -p 3001:3000 myapp
```

### Issue: Permission denied

```bash
# Linux: Add user to docker group
sudo usermod -aG docker $USER
newgrp docker

# Or run with sudo
sudo docker ps
```

### Issue: Out of disk space

```bash
# Clean up
docker system prune -a --volumes

# Check usage
docker system df
```

### Issue: Build fails

```bash
# Build with no cache
docker build --no-cache -t myapp .

# View build context size
du -sh .

# Check .dockerignore
cat .dockerignore
```

---

## 🔗 Related

- [Docker Docs](https://docs.docker.com/)
- [[JARVIS/04-Engineering/Playbooks/Debug/Docker-Not-Starting|Docker Troubleshooting]]
- [[JARVIS/04-Engineering/Playbooks/Debug/Port-Already-In-Use|Port Issues]]
- [[skills/03-infrastructure-mcp|Infrastructure Skills]]
