---
title: "Docker Prod Gratuito"
description: "Traefik, Portainer CE, Watchtower auto-update para Jarvis/Auto-boletos."
tags:
  - docker
  - projetos
  - prod
  - gratuita
updated: 2026-06-13
date: 2026-04-27
---

# Docker Prod Gratuito [[README]]

Para Jarvis, Auto-boletos, gestor_aluguel:

**Traefik Reverse Proxy (HTTPS free)**:
- docker-compose.traefik.yml + Let's Encrypt auto
- Tut: https://doc.traefik.io/traefik/getting-started/quick-start-with-docker/

**Portainer CE (GUI Docker)**:
- `docker run -d -p 9000:9000 --restart always portainer/portainer-ce`
- Gerencie containers/volumes via web gratuita

**Watchtower Auto-update**:
- `docker run -d --name watchtower containrrr/watchtower`
- Atualiza containers auto sem downtime

**Volumes persistentes + DB**:
- Postgres free local ou Neon serverless
- MinIO local S3 para backups

**Stack completa gratuita**:
```
docker compose -f docker-compose.prod.yml -f traefik.yml up -d
```

Recursos: [[README]] #traefik #portainer
