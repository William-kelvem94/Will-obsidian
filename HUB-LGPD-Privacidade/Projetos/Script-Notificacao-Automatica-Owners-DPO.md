---
title: "Script Notificação Automática — Incidentes & Revisão LGPD"
tags: [#projeto, #script, #notificacao, #lgpd, #workflow]
updated: 2026-05-24
status: active
---
# SCRIPT DE NOTIFICAÇÃO AUTOMÁTICA A OWNERS/DPO

## 1. Objetivo
Automatizar envio de notificações semanais e alertas de incidentes para owners, gestores, DPO e, quando necessário, titulares e ANPD. Integração com outputs dos scripts de auditoria e workflow de compliance.

## 2. Características
- Leitura programática dos relatórios YAML/JSON da auditoria
- Geração dinâmica de mensagem para cada owner/gestor responsável por não conformidades ou incidentes
- Envio via webhook/HTTP, email ou integração direta com Slack/MS Teams
- Logs detalhados de todo envio

## 3. Bloco central (Python)
```python
import requests, yaml, json

def notificar(owner, msg, webhook):
    data = {"owner": owner, "mensagem": msg}
    print(f"Enviando para {webhook}: {msg}")
    resp = requests.post(webhook, json=data)
    if resp.status_code != 200:
        print(f"Falha ao notificar: {resp.text}")

with open('./auditoria/relatorio_auditoria.yaml', 'r', encoding='utf-8') as yf:
    rel = yaml.safe_load(yf)
for item in rel['não_conformes']:
    msg = f"ATENÇÃO: Não conformidade no arquivo {item['file']} — Motivo: {item['motivo']}"
    notificar(item.get('owner','gestor'), msg, 'https://hooks.empresa.com/lgpd-alertas')
```

## 4. Instruções
- Adaptar webhooks/remetentes conforme política interna
- Enviar cópia/digest para DPO
- Registrar log de cada tentativa/invio
- Usar como rotina pós-auditoria (semanal ou monitoramento em tempo real)
