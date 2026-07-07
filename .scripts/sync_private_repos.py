#!/usr/bin/env python3
"""
sync_private_repos.py - Sincroniza repositorios locais irmaos com notas do Obsidian.

Atualizado para a estrutura numerada canonica do WILL-OBSIDIAN:
`03-Projetos/01-Ativos/Privados/` e preservando fallback para a estrutura legada.
"""

from __future__ import annotations

import json
import os
import re
import subprocess
from datetime import datetime
from pathlib import Path

SCRIPT_ROOT = Path(__file__).parent.resolve()
VAULT_ROOT = SCRIPT_ROOT.parent.resolve()
CANONICAL_PRIVADOS_DIR = VAULT_ROOT / "03-Projetos" / "01-Ativos" / "Privados"
LEGACY_PRIVADOS_DIR = VAULT_ROOT / "Projetos" / "01-Ativos" / "Privados"
GITHUB_ROOT = VAULT_ROOT.parent


def privados_dir() -> Path:
    """Return canonical project note directory and create it when needed."""
    if CANONICAL_PRIVADOS_DIR.exists() or not LEGACY_PRIVADOS_DIR.exists():
        CANONICAL_PRIVADOS_DIR.mkdir(parents=True, exist_ok=True)
        return CANONICAL_PRIVADOS_DIR
    return LEGACY_PRIVADOS_DIR


def run_cmd(cmd: str, cwd: Path | None = None) -> str:
    """Executa comando shell e retorna stdout limpo."""
    try:
        res = subprocess.run(
            cmd,
            cwd=cwd,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            shell=True,
            encoding="utf-8",
            errors="ignore",
        )
        if res.returncode == 0:
            return res.stdout.strip()
    except Exception:
        pass
    return ""


def get_git_info(repo_path: Path) -> dict[str, str]:
    """Retorna informacoes Git do repositorio local."""
    branch = run_cmd("git branch --show-current", cwd=repo_path) or "main"
    last_commit = run_cmd('git log -1 --format="%h - %s (%ad)" --date=short', cwd=repo_path) or "Nenhum commit encontrado"
    remote_url = run_cmd("git remote get-url origin", cwd=repo_path) or "Sem origem remota"
    status = run_cmd("git status --short", cwd=repo_path)
    return {
        "branch": branch,
        "last_commit": last_commit,
        "remote_url": remote_url,
        "dirty": "sim" if status else "nao",
    }


def read_json(path: Path) -> dict:
    try:
        return json.loads(path.read_text(encoding="utf-8", errors="ignore"))
    except Exception:
        return {}


def scan_dependencies(repo_path: Path) -> str:
    """Retorna resumo de dependencias estruturadas encontradas."""
    deps: list[str] = []

    req_file = repo_path / "requirements.txt"
    if req_file.exists():
        lines = req_file.read_text(encoding="utf-8", errors="ignore").splitlines()
        top_deps = [line.strip().split("==")[0].split(">=")[0] for line in lines if line.strip() and not line.startswith("#")][:8]
        deps.append(f"**Python (requirements):** `{', '.join(top_deps)}`")

    pyproject = repo_path / "pyproject.toml"
    if pyproject.exists():
        deps.append("**Python:** pyproject.toml encontrado")

    pipfile = repo_path / "Pipfile"
    if pipfile.exists():
        deps.append("**Python:** Pipfile encontrado")

    package_json = repo_path / "package.json"
    if package_json.exists():
        data = read_json(package_json)
        package_name = data.get("name", repo_path.name)
        dependencies = list((data.get("dependencies") or {}).keys())[:8]
        dev_dependencies = list((data.get("devDependencies") or {}).keys())[:5]
        if dependencies:
            deps.append(f"**Node.js ({package_name}):** `{', '.join(dependencies)}`")
        elif dev_dependencies:
            deps.append(f"**Node.js ({package_name}, dev):** `{', '.join(dev_dependencies)}`")
        else:
            deps.append(f"**Node.js ({package_name}):** package.json sem dependencias principais")

    composer = repo_path / "composer.json"
    if composer.exists():
        deps.append("**PHP (Composer):** composer.json configurado")

    return "\n".join(f"- {dep}" for dep in deps) if deps else "- Nenhuma dependência estruturada identificada."


def scan_infra_configs(repo_path: Path) -> str:
    configs = {
        "Dockerfile": "Dockerfile",
        "docker-compose.yml": "docker-compose.yml",
        "compose.yml": "Compose moderno",
        ".env.example": "Arquivo .env.example",
        ".github/workflows": "GitHub Actions",
        "tailwind.config.js": "Tailwind CSS",
        "tailwind.config.ts": "Tailwind CSS TS",
        "tsconfig.json": "TypeScript config",
        "vite.config.ts": "Vite Bundler",
        "next.config.js": "Next.js configuration",
        "next.config.mjs": "Next.js configuration (mjs)",
        "package.json": "TypeScript/JavaScript npm",
        "requirements.txt": "Python dependencies",
        "pyproject.toml": "Python pyproject",
    }

    results = []
    for filename, label in configs.items():
        exists = (repo_path / filename).exists()
        status = "[x]" if exists else "[ ]"
        results.append(f"- {status} {label}")
    return "\n".join(results)


def get_repo_short_description(repo_path: Path) -> str:
    """Extrai uma descricao curta do README real do repositorio."""
    for readme in [repo_path / "README.md", repo_path / "readme.md"]:
        if not readme.exists():
            continue
        content = readme.read_text(encoding="utf-8", errors="ignore")
        for line in content.splitlines():
            stripped = line.strip()
            if stripped and not stripped.startswith("#") and len(stripped) > 15:
                return stripped[:150] + "..." if len(stripped) > 150 else stripped
    return "Sem descrição detalhada no README local."


def detect_language(repo_path: Path) -> str:
    if (repo_path / "package.json").exists():
        if (repo_path / "tsconfig.json").exists():
            return "TypeScript"
        return "JavaScript/Node.js"
    if (repo_path / "requirements.txt").exists() or (repo_path / "pyproject.toml").exists() or any(repo_path.glob("*.py")):
        return "Python"
    if (repo_path / "composer.json").exists() or any(repo_path.glob("*.php")):
        return "PHP"
    if any(repo_path.glob("*.cs")):
        return "C#"
    return "N/A"


def update_vault_note(note_path: Path, git_info: dict[str, str], deps: str, configs: str, desc: str, local_path: Path) -> bool:
    if not note_path.exists():
        return False

    content = note_path.read_text(encoding="utf-8", errors="ignore")
    sync_block = f"""## 📊 Sincronização Local de Código (Automática)
*Dados técnicos lidos do repositório físico em {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}*

- **Caminho Físico Local:** `{str(local_path).replace('\\', '/')}`
- **Branch Ativa:** `{git_info['branch']}`
- **Último Commit:** `{git_info['last_commit']}`
- **Working Tree Suja:** `{git_info['dirty']}`
- **Repositório Remoto (Origin):** [{git_info['remote_url']}]({git_info['remote_url']})
- **Descrição de README:** {desc}

### 🛠️ Configurações e Arquivos de Infraestrutura
{configs}

### 📦 Principais Dependências Mapeadas
{deps}"""

    pattern = r"## 📊 Sincronização Local de Código \(Automática\)[\s\S]*"
    if re.search(pattern, content):
        new_content = re.sub(pattern, sync_block, content)
    else:
        new_content = content.strip() + "\n\n" + sync_block + "\n"

    note_path.write_text(new_content, encoding="utf-8")
    return True


def ensure_note_exists(folder_name: str, repo_path: Path) -> tuple[Path, bool]:
    """Garante nota canonica para um repo local."""
    target_dir = privados_dir()
    clean_name = folder_name.replace(" ", "-")
    candidates = [clean_name + ".md", folder_name + ".md", folder_name.replace(" ", "_") + ".md"]

    for candidate in candidates:
        path = target_dir / candidate
        if path.exists():
            return path, False

    target_path = target_dir / f"{clean_name}.md"
    lang = detect_language(repo_path)
    today = datetime.now().strftime("%Y-%m-%d")
    frontmatter = f"""---
title: "{folder_name} (Clonado)"
source: "{str(repo_path).replace('\\', '/')}"
language: {lang}
private: true
description: "Projeto sincronizado localmente — autogerado via varredura de diretório irmão."
updated: {today}
tags: [privados, projetos, autogerado]
date: {today}
---

# {folder_name} 📂

**Status**: 📁 Auto-Mapeado do GitHub Local
**Foco**: Portfólio, documentação e organização operacional

Este arquivo foi criado automaticamente porque o diretório clonado físico correspondente foi encontrado em `{str(repo_path).replace('\\', '/')}`.

## 📋 Resumo do Projeto

Adicione aqui objetivo, status, stack, decisões, riscos e próximos passos.

## ✅ Próxima ação

- [ ] Completar visão, comandos de execução e roadmap.

---
"""
    target_path.write_text(frontmatter, encoding="utf-8")
    print(f"✨ Criada nova nota do Obsidian para o repositório clonado: {target_path.name}")
    return target_path, True


def sync_projects() -> None:
    print("🚀 Iniciando sincronização de repositórios físicos para notas canônicas...")

    target_dir = privados_dir()
    print(f"📁 Diretório de notas: {target_dir.relative_to(VAULT_ROOT)}")

    if not GITHUB_ROOT.exists():
        print(f"❌ Diretório GitHub não encontrado em {GITHUB_ROOT}")
        return

    synced_count = 0
    scaffolded_count = 0
    local_repos = [entry for entry in GITHUB_ROOT.iterdir() if entry.is_dir() and (entry / ".git").is_dir() and entry.name != VAULT_ROOT.name]

    print(f"🔍 Encontrados {len(local_repos)} repositórios git locais irmãos.")

    for repo_path in sorted(local_repos, key=lambda p: p.name.lower()):
        note_path, created_new = ensure_note_exists(repo_path.name, repo_path)
        if created_new:
            scaffolded_count += 1

        git_info = get_git_info(repo_path)
        deps = scan_dependencies(repo_path)
        configs = scan_infra_configs(repo_path)
        desc = get_repo_short_description(repo_path)

        success = update_vault_note(note_path, git_info, deps, configs, desc, repo_path)
        if success:
            action_word = "Autogerada e sincronizada" if created_new else "Atualizada"
            print(f"   ✅ Nota {note_path.name} -> {action_word} com sucesso!")
            synced_count += 1
        else:
            print(f"   ❌ Falha ao gravar dados na nota {note_path.name}.")

    print("\n✨ Sincronização finalizada!")
    print(f"   - {scaffolded_count} novas notas autogeradas do zero baseadas em clonagem real local.")
    print(f"   - {synced_count} notas com dados técnicos e infraestrutura atualizados.")


if __name__ == "__main__":
    sync_projects()
