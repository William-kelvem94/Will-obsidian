#!/usr/bin/env python3
"""
sync_private_repos.py - Sincroniza informações de repositórios locais (irmãos no GitHub)
com suas respectivas notas no Obsidian Vault em Projetos/01-Ativos/Privados/.
Cria automaticamente notas de templates se um diretório clonado local for encontrado
mas não tiver um arquivo markdown correspondente.
"""

import os
import re
import subprocess
from pathlib import Path
from datetime import datetime

# Caminhos
SCRIPT_ROOT = Path(__file__).parent.resolve()
VAULT_ROOT = SCRIPT_ROOT.parent
PRIVADOS_DIR = VAULT_ROOT / "Projetos" / "01-Ativos" / "Privados"
GITHUB_ROOT = VAULT_ROOT.parent # d:\DOCUMENTOS\GitHub\

def run_cmd(cmd, cwd=None):
    """Executa um comando de sistema e retorna a string limpa."""
    try:
        res = subprocess.run(
            cmd,
            cwd=cwd,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            shell=True,
            encoding='utf-8',
            errors='ignore'
        )
        if res.returncode == 0:
            return res.stdout.strip()
    except Exception as e:
        pass
    return ""

def get_git_info(repo_path):
    """Retorna um dicionário com informações do git do repositório."""
    branch = run_cmd("git branch --show-current", cwd=repo_path) or "main"
    last_commit = run_cmd('git log -1 --format="%h - %s (%ad)" --date=short', cwd=repo_path) or "Nenhum commit encontrado"
    remote_url = run_cmd("git remote get-url origin", cwd=repo_path) or "Sem origem remota"
    return {
        "branch": branch,
        "last_commit": last_commit,
        "remote_url": remote_url
    }

def scan_dependencies(repo_path):
    """Retorna uma string resumida sobre dependências encontradas."""
    deps = []
    
    # Python
    req_file = Path(repo_path) / "requirements.txt"
    if req_file.exists():
        lines = req_file.read_text(encoding='utf-8', errors='ignore').splitlines()
        top_deps = [l.strip().split('==')[0] for l in lines if l.strip() and not l.startswith('#')][:6]
        deps.append(f"**Python (requirements):** `{', '.join(top_deps)}`")
        
    # Python Pipfile / poetry
    if (Path(repo_path) / "Pipfile").exists():
        deps.append("**Python:** Pipfile encontrado")
        
    # Node.js
    pkg_file = Path(repo_path) / "package.json"
    if pkg_file.exists():
        try:
            with open(pkg_file, 'r', encoding='utf-8', errors='ignore') as f:
                data = f.read()
                dependencies = re.findall(r'"dependencies"\s*:\s*\{([^}]+)\}', data, re.DOTALL)
                if dependencies:
                    dep_lines = re.findall(r'"([^"]+)"', dependencies[0])
                    top_deps = [d for d in dep_lines if not d.startswith('@')][:6]
                    deps.append(f"**Node.js (package.json):** `{', '.join(top_deps)}`")
        except:
            pass
            
    # PHP Composer
    cmp_file = Path(repo_path) / "composer.json"
    if cmp_file.exists():
        deps.append("**PHP (Composer):** composer.json configurado")

    return "\n".join([f"- {d}" for d in deps]) if deps else "- Nenhuma dependência estruturada identificada."

def scan_infra_configs(repo_path):
    """Retorna checklists de arquivos de configuração encontrados."""
    configs = {
        "Dockerfile": "Dockerfile",
        "docker-compose.yml": "docker-compose.yml",
        ".env.example": "Arquivo .env.example",
        "tailwind.config.js": "Tailwind CSS",
        "tsconfig.json": "TypeScript config",
        "vite.config.ts": "Vite Bundler",
        "next.config.js": "Next.js configuration",
        "next.config.mjs": "Next.js configuration (mjs)",
        "package.json": "TypeScript/JavaScript npm",
        "requirements.txt": "Python dependencies"
    }
    
    results = []
    for filename, label in configs.items():
        exists = (Path(repo_path) / filename).exists()
        status = "[x]" if exists else "[ ]"
        results.append(f"- {status} {label}")
        
    return "\n".join(results)

def get_repo_short_description(repo_path):
    """Extrai uma descrição curta do README real do repositório."""
    readme_paths = [Path(repo_path) / "README.md", Path(repo_path) / "readme.md"]
    for rp in readme_paths:
        if rp.exists():
            content = rp.read_text(encoding='utf-8', errors='ignore')
            lines = content.splitlines()
            for line in lines:
                l = line.strip()
                if l and not l.startswith('#') and len(l) > 15:
                    return l[:150] + "..." if len(l) > 150 else l
    return "Sem descrição detalhada no README local."

def update_vault_note(note_path, git_info, deps, configs, desc, local_path):
    """Atualiza a nota do Obsidian com os dados de sincronização de código ajustados."""
    if not note_path.exists():
        return False
        
    content = note_path.read_text(encoding='utf-8', errors='ignore')
    
    sync_block = f"""## 📊 Sincronização Local de Código (Automática)
*Dados técnicos lidos do repositório físico em {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}*

- **Caminho Físico Local:** `{local_path}`
- **Branch Ativa:** `{git_info['branch']}`
- **Último Commit:** `{git_info['last_commit']}`
- **Repositório Remoto (Origin):** [{git_info['remote_url']}]({git_info['remote_url']})
- **Descrição de README:** {desc}

### 🛠️ Configurações e Arquivos de Infraestrutura
{configs}

### 📦 Principais Dependências Mapeadas
{deps}"""

    # Se já existir o cabeçalho de Sincronização, substitui tudo do cabeçalho de Sincronização em diante
    pattern = r"## 📊 Sincronização Local de Código \(Automática\)[\s\S]*"
    if re.search(pattern, content):
        new_content = re.sub(pattern, sync_block, content)
    else:
        # Adiciona no final da nota, garantindo um espaçamento limpo
        new_content = content.strip() + "\n\n" + sync_block
        
    note_path.write_text(new_content, encoding='utf-8')
    return True

def ensure_note_exists(folder_name):
    """Verifica se existe uma nota com esse nome e se não, cria uma."""
    # Corrige nome da nota trocando espaços por traço comercial
    clean_name = folder_name.replace(" ", "-")
    candidates = [
        clean_name + ".md",
        folder_name + ".md",
        folder_name.replace(" ", "_") + ".md"
    ]
    
    for cand in candidates:
        filepath = PRIVADOS_DIR / cand
        if filepath.exists():
            return filepath, False
            
    # Cria uma nova nota padrão
    target_path = PRIVADOS_DIR / (clean_name + ".md")
    
    lang = "N/A"
    repo_path = GITHUB_ROOT / folder_name
    if (repo_path / "package.json").exists():
        lang = "TypeScript"
    elif (repo_path / "requirements.txt").exists():
        lang = "Python"
    elif any(repo_path.glob("*.py")):
        lang = "Python"
    elif any(repo_path.glob("*.php")):
        lang = "PHP"
    elif any(repo_path.glob("*.cs")):
        lang = "C#"
        
    frontmatter = f"""---
title: "{folder_name} (Clonado)"
source: "d:/DOCUMENTOS/GitHub/{folder_name}"
language: {lang}
private: true
description: "Projeto sincronizado localmente — autogerado via varredura de diretório irmão."
updated: {datetime.now().strftime("%Y-%m-%d")}
tags: [privados, projetos, autogerado]
date: {datetime.now().strftime("%Y-%m-%d")}
---

# {folder_name} 📂

**Status**: 📁 Auto-Mapeado do GitHub Local
**Foco**: Portfólio e Organização

Este arquivo foi criado de forma automática porque o diretório clonado físico correspondente foi encontrado em `{repo_path.as_posix()}`.

## 📋 Resumo do Projeto

*Adicione aqui as suas anotações sobre os objetivos deste repositório, documentações, decisões de arquitetura e planos práticos de evolução.*

---
"""
    target_path.write_text(frontmatter, encoding='utf-8')
    print(f"✨ Criada nova nota do Obsidian para o repositório clonado: {target_path.name}")
    return target_path, True

def sync_projects():
    """Varre os diretórios físicos locais e sincroniza ou gera as notas markdown."""
    print("🚀 Iniciando Sincronização e Autogeração de Notas de Repositórios Físicos...")
    
    if not PRIVADOS_DIR.exists():
        os.makedirs(PRIVADOS_DIR, exist_ok=True)
        
    if not GITHUB_ROOT.exists():
        print(f"❌ Diretório GitHub não encontrado em {GITHUB_ROOT}")
        return
        
    synced_count = 0
    scaffolded_count = 0
    
    # 1. Procurar por todas as pastas no GitHub_ROOT que sejam repositórios git válidos
    local_repos = []
    for entry in GITHUB_ROOT.iterdir():
        if entry.is_dir() and (entry / ".git").is_dir():
            if entry.name == "Will-obsidian":
                continue
            local_repos.append(entry)
            
    print(f"🔍 Encontrados {len(local_repos)} repositórios git locais irmãos.")
    
    # 2. Para cada repositório local, garantir que a nota correspondente existe e sincronizá-la
    for repo_path in local_repos:
        folder_name = repo_path.name
        
        # Garante a nota (se não existir, o script cria com template completo)
        note_path, created_new = ensure_note_exists(folder_name)
        if created_new:
            scaffolded_count += 1
            
        # Extrai dados do código real e grava
        git_info = get_git_info(repo_path)
        deps = scan_dependencies(repo_path)
        configs = scan_infra_configs(repo_path)
        desc = get_repo_short_description(repo_path)
        
        success = update_vault_note(
            note_path, 
            git_info, 
            deps, 
            configs, 
            desc, 
            str(repo_path).replace("\\", "/")
        )
        if success:
            action_word = "Autogerada e Sincronizada" if created_new else "Atualizada"
            print(f"   ✅ Nota {note_path.name} -> {action_word} com sucesso!")
            synced_count += 1
        else:
            print(f"   ❌ Falha ao gravar dados na nota {note_path.name}.")
            
    print(f"\n✨ Sincronização finalizada!")
    print(f"   - {scaffolded_count} novas notas autogeradas do zero baseadas em clonagem real local.")
    print(f"   - {synced_count} notas totalizando dados de sincronização técnica e infraestrutura.")

if __name__ == "__main__":
    sync_projects()
