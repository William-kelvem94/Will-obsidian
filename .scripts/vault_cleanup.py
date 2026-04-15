import os
import re
from datetime import datetime

SCRIPT_ROOT = os.path.dirname(os.path.abspath(__file__))
VAULT_ROOT = os.path.normpath(os.path.join(SCRIPT_ROOT, ".."))
REPORT_PATH = os.path.join(SCRIPT_ROOT, "vault_cleanup_report.md")

MAPPING = {
    "Projetos/Privados": "#privados",
    "Projetos": "#projetos",
    "JARVIS/Memorias": "#memoria",
    "JARVIS/Decisoes": "#decisao",
    "JARVIS/Aprendizado": "#aprendizado",
    "JARVIS": "#jarvis",
    "Will-Pessoal": "#perfil",
    "skills": "#skills"
}


def normalize_frontmatter(frontmatter, tag, report, filepath):
    clean_tag = tag.replace('#', '')
    updated = datetime.now().strftime("%Y-%m-%d")
    new_frontmatter = frontmatter

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


def add_tag_to_file(filepath, tag, report):
    if not filepath.endswith(".md"):
        return

    try:
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
    except UnicodeDecodeError:
        try:
            with open(filepath, "r", encoding="iso-8859-1") as f:
                content = f.read()
        except Exception as e:
            report.append(f"Falha ao ler {filepath}: {e}")
            return

    clean_tag = tag.replace('#', '')
    frontmatter_match = re.search(r"^---\s*\n(.*?)\n---\s*\n", content, re.DOTALL)

    if frontmatter_match:
        frontmatter = frontmatter_match.group(1)
        new_frontmatter = normalize_frontmatter(frontmatter, tag, report, filepath)
        if new_frontmatter != frontmatter:
            content = content.replace(frontmatter, new_frontmatter, 1)
    else:
        today = datetime.now().strftime("%Y-%m-%d")
        content = f"---\ntags: [{clean_tag}]\nupdated: {today}\n---\n\n" + content
        report.append(f"Criado frontmatter em {filepath}")

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)


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


def run_cleanup():
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
                    add_tag_to_file(path, best_tag, report)

    write_report(report)
    print(f"Relatório de limpeza gerado em: {REPORT_PATH}")


if __name__ == "__main__":
    run_cleanup()
