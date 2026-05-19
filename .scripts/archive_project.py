#!/usr/bin/env python3
"""
Arquivamento Inteligente com Git Tags — Move um project de
Projetos/01-Ativos/ para Projetos/02-Arquivo/ e cria uma tag git.

Uso:
    python .scripts/archive_project.py
    python .scripts/archive_project.py --project NomeDoProjeto

Testabilidade rápida:
    - Pode ser testado em projetos/diretórios dummy.
    - Fora de repositório git, não falha e apenas imprime mensagem amigável.
    - Para testes automatizados, mock da função run_git com unittest.mock é suficiente.
    - Não realiza operações destrutivas sem confirmação interativa.
"""

import argparse
import shutil
import subprocess
import sys
from datetime import datetime
from pathlib import Path

SCRIPT_ROOT = Path(__file__).parent
VAULT_PATH = SCRIPT_ROOT.parent
ATIVOS_DIR = VAULT_PATH / "Projetos" / "01-Ativos"
ARQUIVO_DIR = VAULT_PATH / "Projetos" / "02-Arquivo"
PROJETOS_HUB = VAULT_PATH / "Projetos.md"


def run_git(cmd, cwd=None):
    """Executa comando git e retorna o resultado."""
    try:
        return subprocess.run(
            cmd, shell=True, cwd=cwd or VAULT_PATH,
            capture_output=True, text=True, encoding='utf-8',
        )
    except Exception as e:
        print(f"[ERR] Erro ao executar git: {e}")
        sys.exit(1)


def list_active_projects():
    """Lista subdiretórios (projetos) dentro de Projetos/01-Ativos/."""
    if not ATIVOS_DIR.is_dir():
        print(f"[ERR] Diretório não encontrado: {ATIVOS_DIR}")
        sys.exit(1)

    projects = sorted(p.name for p in ATIVOS_DIR.iterdir() if p.is_dir())
    if not projects:
        print("[INFO] Nenhum subdiretório encontrado em Projetos/01-Ativos/.")
        sys.exit(0)

    return projects


def select_project(projects, arg_project=None):
    """Seleciona project por argumento ou interativamente."""
    if arg_project:
        if arg_project not in projects:
            print(f"[ERR] Projeto '{arg_project}' não encontrado em 01-Ativos.")
            print("[INFO] Projetos disponíveis:")
            for p in projects:
                print(f"      - {p}")
            sys.exit(1)
        return arg_project

    print("[INFO] Projetos ativos disponíveis para arquivar:\n")
    for i, p in enumerate(projects, 1):
        print(f"  {i}. {p}")
    print()

    while True:
        try:
            choice = input("Número do projeto para arquivar (ou 0 para cancelar): ").strip()
            if not choice:
                continue
            idx = int(choice)
            if idx == 0:
                print("[INFO] Operação cancelada.")
                sys.exit(0)
            if 1 <= idx <= len(projects):
                return projects[idx - 1]
            print(f"[ERR] Escolha um número entre 1 e {len(projects)}.")
        except ValueError:
            print("[ERR] Insira um número válido.")


def ensure_archive_dir():
    """Garante que Projetos/02-Arquivo/ existe."""
    ARQUIVO_DIR.mkdir(parents=True, exist_ok=True)
    print(f"[OK] Diretório de arquivo verificado: {ARQUIVO_DIR.relative_to(VAULT_PATH)}")


def move_project(project_name):
    """Move o project de 01-Ativos para 02-Arquivo."""
    src = ATIVOS_DIR / project_name
    dst = ARQUIVO_DIR / project_name

    if not src.is_dir():
        print(f"[ERR] Diretório de origem não encontrado: {src}")
        sys.exit(1)

    if dst.exists():
        print(f"[ERR] Já existe um diretório em 02-Arquivo com o nome '{project_name}'.")
        print("[INFO] Remova ou renomeie o destino primeiro, ou escolha outro projeto.")
        sys.exit(1)

    print(f"[GEN] Movendo '{project_name}' de 01-Ativos para 02-Arquivo...")
    shutil.move(str(src), str(dst))

    if dst.is_dir():
        print(f"[OK] Projeto movido para: {dst.relative_to(VAULT_PATH)}")
    else:
        print(f"[ERR] Falha ao mover o diretório.")
        sys.exit(1)


def create_summary_note(project_name):
    """Cria README.md no diretório arquivado com data e localização original."""
    project_dir = ARQUIVO_DIR / project_name
    now = datetime.now()
    date_str = now.strftime("%Y-%m-%d")
    original_path = f"Projetos/01-Ativos/{project_name}"

    readme_path = project_dir / "README.md"

    if readme_path.exists():
        backup = project_dir / "_original-readme.md"
        print(f"[INFO] README.md existente renomeado para {backup.relative_to(VAULT_PATH)}")
        shutil.move(str(readme_path), str(backup))

    content = f"""---
title: "{project_name} (Arquivado)"
description: "Projeto arquivado do vault Obsidian em {date_str}"
tags: [arquivo, projeto, archive]
archived: {date_str}
original_location: "{original_path}"
---

# 🗄️ {project_name}

> **Projeto arquivado em {date_str}**  
> Localização original: `{original_path}`

Este projeto foi movido para o arquivo como parte do processo de **Arquivamento Inteligente com Git Tags**.

## Metadados do Arquivamento

| Campo | Valor |
|-------|-------|
| Data de Arquivamento | {date_str} |
| Localização Original | `{original_path}` |
| Localização Atual | `Projetos/02-Arquivo/{project_name}` |
| Tag Git | `archive/{project_name.lower()}-{date_str}` |

---

*Arquivado automaticamente por `.scripts/archive_project.py`*
"""

    with open(readme_path, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"[OK] README.md de arquivamento criado em: {readme_path.relative_to(VAULT_PATH)}")


def update_projetos_hub(project_name):
    """Atualiza Projetos.md: adiciona comentário e corrige wikilinks."""
    if not PROJETOS_HUB.exists():
        print(f"[INFO] Projetos.md não encontrado, pulando atualização.")
        return

    now = datetime.now()
    date_str = now.strftime("%Y-%m-%d")
    old_prefix = f"Projetos/01-Ativos/{project_name}"
    new_prefix = f"Projetos/02-Arquivo/{project_name}"

    with open(PROJETOS_HUB, 'r', encoding='utf-8') as f:
        content = f.read()

    # Atualiza wikilinks de 01-Ativos para 02-Arquivo
    updated = content.replace(f"[[{old_prefix}/", f"[[{new_prefix}/")

    # Adiciona comentário de arquivamento logo após o bloco Dataview
    comment = f"\n<!-- Projeto '{project_name}' arquivado em {date_str}, movido para {new_prefix} -->\n"
    open_marker = "```dataview"
    close_marker = "```"
    open_idx = updated.find(open_marker)
    if open_idx != -1:
        close_idx = updated.find(close_marker, open_idx + len(open_marker))
        if close_idx != -1:
            after_close = close_idx + len(close_marker)
            existing_comment = f"<!-- Projeto '{project_name}' arquivado em"
            if existing_comment not in updated:
                updated = updated[:after_close] + comment + updated[after_close:]
                print(f"[OK] Comentário de arquivamento adicionado ao Projetos.md")
    else:
        print(f"[INFO] Bloco Dataview não encontrado em Projetos.md, comentário não adicionado.")

    # Verifica se houve alterações
    if updated == content:
        print(f"[INFO] Nenhuma alteração necessária em Projetos.md (links já atualizados).")
    else:
        with open(PROJETOS_HUB, 'w', encoding='utf-8') as f:
            f.write(updated)
        print(f"[OK] Projetos.md atualizado — wikilinks corrigidos para 02-Arquivo.")


def git_commit_and_tag(project_name):
    """Faz commit da movimentação e cria tag git archive/project-name-YYYY-MM-DD."""
    now = datetime.now()
    date_str = now.strftime("%Y-%m-%d")
    tag_name = f"archive/{project_name.lower()}-{date_str}"

    # Verifica se já existe um repositório git
    result = run_git("git rev-parse --git-dir")
    if result.returncode != 0:
        print("[INFO] Diretório não é um repositório git. Pulando commit e tag.")
        return

    # Verifica se tag já existe
    result = run_git(f'git tag --list "{tag_name}"')
    if result.stdout.strip() == tag_name:
        print(f"[INFO] Tag '{tag_name}' já existe. Pulando commit e tag.")
        return

    # Staging da movimentação
    print("[GEN] Preparando commit git...")

    # Adiciona todas as alterações (inclui a movimentação e o novo README)
    result = run_git("git add -A")
    if result.returncode != 0:
        print(f"[ERR] Falha ao executar git add:\n{result.stderr}")
        sys.exit(1)

    # Commit
    commit_msg = f"archive: move {project_name} to 02-Arquivo"
    result = run_git(f'git commit -m "{commit_msg}"')
    if result.returncode != 0:
        if "nothing to commit" in result.stderr or "nothing to commit" in result.stdout:
            print(f"[INFO] Nada a commitar. A movimentação já estava no índice.")
        else:
            print(f"[ERR] Falha ao commitar:\n{result.stderr}")
            sys.exit(1)
    else:
        print(f"[OK] Commit realizado: {commit_msg}")

    # Tag
    result = run_git(f'git tag -a "{tag_name}" -m "Projeto {project_name} arquivado em {date_str}"')
    if result.returncode != 0:
        print(f"[ERR] Falha ao criar tag:\n{result.stderr}")
        sys.exit(1)

    print(f"[OK] Tag criada: {tag_name}")


def parse_args():
    """Analisa argumentos da linha de comando."""
    parser = argparse.ArgumentParser(
        description="Arquiva um project de Projetos/01-Ativos/ para Projetos/02-Arquivo/"
    )
    parser.add_argument(
        "--project", "-p",
        type=str,
        default=None,
        help="Nome do projeto para arquivar (modo não-interativo)",
    )
    return parser.parse_args()


def main():
    """Execução principal do script de arquivamento."""
    args = parse_args()
    print("[GEN] Iniciando Arquivamento Inteligente...")

    ensure_archive_dir()
    projects = list_active_projects()
    project_name = select_project(projects, args.project)

    # Confirmação antes de arquivar
    if not args.project:
        confirm = input(f"\nConfirmar arquivamento de '{project_name}'? (s/N): ").strip().lower()
        if confirm not in ('s', 'sim', 'y', 'yes'):
            print("[INFO] Operação cancelada.")
            sys.exit(0)

    print(f"[INFO] Arquivando projeto: {project_name}")

    move_project(project_name)
    create_summary_note(project_name)
    update_projetos_hub(project_name)
    git_commit_and_tag(project_name)

    print(f"\n[OK] Projeto '{project_name}' arquivado com sucesso!")
    print(f"[INFO] Tag criada: archive/{project_name.lower()}-{datetime.now().strftime('%Y-%m-%d')}")


if __name__ == "__main__":
    main()
