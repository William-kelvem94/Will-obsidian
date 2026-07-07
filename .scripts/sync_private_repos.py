#!/usr/bin/env python3
"""
sync_private_repos.py - sincroniza sinais basicos de repositorios locais com notas do Obsidian.

Versao canonica segura: usa `03-Projetos/01-Ativos/Privados/`, preserva fallback legado
e evita ler conteudo sensivel. O script registra apenas sinais estruturais: README,
package.json, requirements, Docker, compose e .env.example.
"""

from __future__ import annotations

import json
import re
from datetime import datetime
from pathlib import Path

SCRIPT_ROOT = Path(__file__).parent.resolve()
VAULT_ROOT = SCRIPT_ROOT.parent.resolve()
CANONICAL_PRIVADOS_DIR = VAULT_ROOT / "03-Projetos" / "01-Ativos" / "Privados"
LEGACY_PRIVADOS_DIR = VAULT_ROOT / "Projetos" / "01-Ativos" / "Privados"
GITHUB_ROOT = VAULT_ROOT.parent


def path_text(path: Path) -> str:
    return path.as_posix()


def privados_dir() -> Path:
    if CANONICAL_PRIVADOS_DIR.exists() or not LEGACY_PRIVADOS_DIR.exists():
        CANONICAL_PRIVADOS_DIR.mkdir(parents=True, exist_ok=True)
        return CANONICAL_PRIVADOS_DIR
    return LEGACY_PRIVADOS_DIR


def read_json(path: Path) -> dict:
    try:
        return json.loads(path.read_text(encoding="utf-8", errors="ignore"))
    except Exception:
        return {}


def detect_language(repo_path: Path) -> str:
    if (repo_path / "package.json").exists():
        return "TypeScript" if (repo_path / "tsconfig.json").exists() else "JavaScript/Node.js"
    if (repo_path / "requirements.txt").exists() or (repo_path / "pyproject.toml").exists() or any(repo_path.glob("*.py")):
        return "Python"
    if (repo_path / "composer.json").exists() or any(repo_path.glob("*.php")):
        return "PHP"
    if any(repo_path.glob("*.cs")):
        return "C#"
    return "N/A"


def scan_dependencies(repo_path: Path) -> str:
    deps: list[str] = []

    req_file = repo_path / "requirements.txt"
    if req_file.exists():
        lines = req_file.read_text(encoding="utf-8", errors="ignore").splitlines()
        top_deps = [line.strip().split("==")[0].split(">=")[0] for line in lines if line.strip() and not line.startswith("#")][:8]
        deps.append(f"**Python:** `{', '.join(top_deps)}`")

    package_json = repo_path / "package.json"
    if package_json.exists():
        data = read_json(package_json)
        package_name = data.get("name", repo_path.name)
        dependencies = list((data.get("dependencies") or {}).keys())[:8]
        dev_dependencies = list((data.get("devDependencies") or {}).keys())[:5]
        visible = dependencies or dev_dependencies
        deps.append(f"**Node.js ({package_name}):** `{', '.join(visible)}`" if visible else f"**Node.js ({package_name}):** package.json presente")

    if (repo_path / "pyproject.toml").exists():
        deps.append("**Python:** pyproject.toml presente")
    if (repo_path / "composer.json").exists():
        deps.append("**PHP:** composer.json presente")

    return "\n".join(f"- {dep}" for dep in deps) if deps else "- Nenhuma dependência estruturada identificada."


def scan_infra_configs(repo_path: Path) -> str:
    checks = {
        "README.md": "README",
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
        "next.config.mjs": "Next.js configuration mjs",
        "package.json": "TypeScript/JavaScript npm",
        "requirements.txt": "Python dependencies",
        "pyproject.toml": "Python pyproject",
    }
    lines = []
    for filename, label in checks.items():
        status = "[x]" if (repo_path / filename).exists() else "[ ]"
        lines.append(f"- {status} {label}")
    return "\n".join(lines)


def get_repo_short_description(repo_path: Path) -> str:
    for readme in [repo_path / "README.md", repo_path / "readme.md"]:
        if not readme.exists():
            continue
        content = readme.read_text(encoding="utf-8", errors="ignore")
        for line in content.splitlines():
            clean = line.strip()
            if clean and not clean.startswith("#") and len(clean) > 15:
                return clean[:150] + "..." if len(clean) > 150 else clean
    return "Sem descrição detalhada no README local."


def ensure_note_exists(folder_name: str, repo_path: Path) -> tuple[Path, bool]:
    target_dir = privados_dir()
    clean_name = folder_name.replace(" ", "-")
    for candidate in [clean_name + ".md", folder_name + ".md", folder_name.replace(" ", "_") + ".md"]:
        path = target_dir / candidate
        if path.exists():
            return path, False

    today = datetime.now().strftime("%Y-%m-%d")
    repo_path_text = path_text(repo_path)
    target_path = target_dir / f"{clean_name}.md"
    content = f"""---
title: "{folder_name} (Clonado)"
source: "{repo_path_text}"
language: {detect_language(repo_path)}
private: true
description: "Projeto sincronizado localmente; nota autogerada por varredura estrutural."
updated: {today}
tags: [privados, projetos, autogerado]
date: {today}
---

# {folder_name} 📂

**Status**: 📁 Auto-mapeado do GitHub local
**Foco**: documentação, execução e organização operacional

## 📋 Resumo do Projeto

Adicionar objetivo, status, stack, decisões, riscos e próximos passos.

## ✅ Próxima ação

- [ ] Completar visão, comandos de execução e roadmap.
"""
    target_path.write_text(content, encoding="utf-8")
    return target_path, True


def update_vault_note(note_path: Path, repo_path: Path) -> bool:
    if not note_path.exists():
        return False

    content = note_path.read_text(encoding="utf-8", errors="ignore")
    sync_block = f"""## 📊 Sincronização Local de Código (Automática)
*Dados técnicos lidos do repositório físico em {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}*

- **Caminho Físico Local:** `{path_text(repo_path)}`
- **Descrição de README:** {get_repo_short_description(repo_path)}

### 🛠️ Configurações e Arquivos de Infraestrutura
{scan_infra_configs(repo_path)}

### 📦 Principais Dependências Mapeadas
{scan_dependencies(repo_path)}"""

    pattern = r"## 📊 Sincronização Local de Código \(Automática\)[\s\S]*"
    new_content = re.sub(pattern, sync_block, content) if re.search(pattern, content) else content.strip() + "\n\n" + sync_block + "\n"
    note_path.write_text(new_content, encoding="utf-8")
    return True


def sync_projects() -> None:
    print("🚀 Iniciando sincronização estrutural de repositórios físicos...")
    target_dir = privados_dir()
    print(f"📁 Diretório de notas: {target_dir.relative_to(VAULT_ROOT)}")

    if not GITHUB_ROOT.exists():
        print(f"❌ Diretório GitHub não encontrado em {GITHUB_ROOT}")
        return

    local_repos = [entry for entry in GITHUB_ROOT.iterdir() if entry.is_dir() and (entry / ".git").is_dir() and entry.name != VAULT_ROOT.name]
    synced_count = 0
    created_count = 0

    for repo_path in sorted(local_repos, key=lambda path: path.name.lower()):
        note_path, created = ensure_note_exists(repo_path.name, repo_path)
        created_count += 1 if created else 0
        if update_vault_note(note_path, repo_path):
            synced_count += 1
            print(f"✅ {note_path.name} sincronizada")

    print("\n✨ Sincronização finalizada!")
    print(f"   - {created_count} notas novas")
    print(f"   - {synced_count} notas atualizadas")


if __name__ == "__main__":
    sync_projects()
