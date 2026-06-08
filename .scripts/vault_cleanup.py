import argparse
import os
import re
import sys
from datetime import datetime

SCRIPT_ROOT = os.path.dirname(os.path.abspath(__file__))
VAULT_ROOT = os.path.normpath(os.path.join(SCRIPT_ROOT, ".."))
REPORT_PATH = os.path.join(SCRIPT_ROOT, "vault_cleanup_report.md")

MAPPING = {
    "03-Projetos/01-Ativos/Privados": "#privados",
    "03-Projetos": "#projetos",
    "02-JARVIS/01-Identity": "#jarvis-identidade",
    "02-JARVIS/02-Operational": "#jarvis-operacao",
    "02-JARVIS/03-Memory": "#jarvis-memoria",
    "02-JARVIS/04-Engineering": "#jarvis-engenharia",
    "02-JARVIS/05-System": "#jarvis-sistema",
    "02-JARVIS": "#jarvis",
    "06-Will-Pessoal/01-Identidade": "#perfil-identidade",
    "06-Will-Pessoal/02-Visao": "#perfil-visao",
    "06-Will-Pessoal": "#perfil",
    "05-Skills/01-agentic-intelligence": "#skills-ai",
    "05-Skills/02-software-engineering": "#skills-eng",
    "05-Skills/03-infrastructure-mcp": "#skills-mcp",
    "05-Skills/04-knowledge-systems": "#skills-knowledge",
    "05-Skills": "#skills"
}


def _infer_title(filepath, body):
    match = re.search(r"^#\s+(.*)", body, re.MULTILINE)
    if match:
        return match.group(1).strip()

    name = os.path.splitext(os.path.basename(filepath))[0]
    return name.replace('-', ' ').replace('_', ' ').strip().title()


def normalize_frontmatter(frontmatter, tag, report, filepath, body):
    clean_tag = tag.replace('#', '')
    updated = datetime.now().strftime("%Y-%m-%d")
    new_frontmatter = frontmatter

    if "title:" not in frontmatter:
        title = _infer_title(filepath, body)
        new_frontmatter += f'\ntitle: "{title}"'
        report.append(f"Adicionado title em {filepath}")

    if "date:" not in frontmatter:
        new_frontmatter += f"\ndate: {updated}"
        report.append(f"Adicionado date em {filepath}")

    if "tags:" not in frontmatter:
        new_frontmatter += f"\ntags: [{clean_tag}]"
        report.append(f"Adicionado tag {clean_tag} em {filepath}")
    elif clean_tag not in frontmatter:
        if re.search(r"tags:\s*\[.*?\]", new_frontmatter, re.DOTALL):
            tags_content = re.search(r"tags:\s*\[(.*?)\]", new_frontmatter, re.DOTALL).group(1)
            tags = [t.strip() for t in tags_content.split(",") if t.strip()]
            if clean_tag not in tags:
                tags.append(clean_tag)
                tags_list = ", ".join(tags)
                new_frontmatter = re.sub(r"tags:\s*\[.*?\]", f"tags: [{tags_list}]", new_frontmatter, count=1, flags=re.DOTALL)
                report.append(f"Atualizado tags em {filepath}: {clean_tag}")
        else:
            new_frontmatter = re.sub(r"(tags:\s*.*)", r"\1\n  - " + clean_tag, new_frontmatter, count=1)
            report.append(f"Atualizado tags em {filepath}: {clean_tag}")

    if "updated:" not in new_frontmatter:
        new_frontmatter += f"\nupdated: {updated}"
        report.append(f"Adicionado updated em {filepath}")
    else:
        new_frontmatter = re.sub(r"updated:\s*.*", f"updated: {updated}", new_frontmatter, count=1)

    return new_frontmatter


def add_tag_to_file(filepath, tag, report, write=True):
    if not filepath.endswith(".md"):
        return False

    try:
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
    except UnicodeDecodeError:
        try:
            with open(filepath, "r", encoding="iso-8859-1") as f:
                content = f.read()
        except Exception as e:
            report.append(f"Falha ao ler {filepath}: {e}")
            return False

    clean_tag = tag.replace('#', '')
    frontmatter_match = re.search(r"^---\s*\n(.*?)\n---\s*\n", content, re.DOTALL)
    updated = datetime.now().strftime("%Y-%m-%d")
    modified = False

    if frontmatter_match:
        frontmatter = frontmatter_match.group(1)
        body = content[frontmatter_match.end():]
        new_frontmatter = normalize_frontmatter(frontmatter, tag, report, filepath, body)
        if new_frontmatter != frontmatter:
            modified = True
            if write:
                content = content.replace(frontmatter, new_frontmatter, 1)
    else:
        modified = True
        title = _infer_title(filepath, content)
        date = updated
        content = (
            f"---\n"
            f"title: \"{title}\"\n"
            f"date: {date}\n"
            f"tags: [{clean_tag}]\n"
            f"updated: {updated}\n"
            f"---\n\n"
            + content
        )
        report.append(f"Criado frontmatter em {filepath}")

    if modified and write:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)

    return modified


def write_report(actions):
    now = datetime.now().strftime("%Y-%m-%d %H:%M")
    lines = [
        "# Vault Cleanup Report",
        "",
        f"Gerado: {now}",
        "",
        "## Ações realizadas",
        ""
    ]

    if actions:
        for item in actions:
            lines.append(f"- {item}")
    else:
        lines.append("- Nenhuma alteração necessária.")

    with open(REPORT_PATH, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))


def run_cleanup(check_only=False):
    report = []

    for folder, tag in MAPPING.items():
        dir_path = os.path.join(VAULT_ROOT, folder)
        if not os.path.exists(dir_path):
            report.append(f"Pasta não encontrada: {dir_path}")
            continue

        for root, dirs, files in os.walk(dir_path):
            current_rel_path = os.path.relpath(root, VAULT_ROOT).replace("\\", "/")
            best_tag = tag

            for m_folder, m_tag in MAPPING.items():
                if current_rel_path.startswith(m_folder) and len(m_folder) > len(folder):
                    best_tag = m_tag

            for file in files:
                if file.endswith(".md"):
                    path = os.path.join(root, file)
                    add_tag_to_file(path, best_tag, report, write=not check_only)

    if check_only:
        if report:
            write_report(report)
            print("Falharam verificações de frontmatter no vault.")
            print(f"Veja o relatório em: {REPORT_PATH}")
            sys.exit(1)
        print("Verificacao completa. Nao ha inconsistencias de frontmatter.")
        sys.exit(0)

    write_report(report)
    print(f"Relatório de limpeza gerado em: {REPORT_PATH}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Vault cleanup and frontmatter hygiene")
    parser.add_argument("--check-only", action="store_true", help="Verifica inconsistências sem alterar arquivos")
    args = parser.parse_args()
    run_cleanup(check_only=args.check_only)
