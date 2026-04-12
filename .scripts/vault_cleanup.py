import os
import re

VAULT_ROOT = "d:/Documents/GitHub/Will-obsidian"

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

def add_tag_to_file(filepath, tag):
    if not filepath.endswith(".md"):
        return
    
    content = ""
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
    except UnicodeDecodeError:
        try:
            with open(filepath, "r", encoding="iso-8859-1") as f:
                content = f.read()
        except Exception as e:
            print(f"Erro ao ler {filepath}: {e}")
            return

    # Se a tag já existe (com ou sem #), ignora
    clean_tag = tag.replace('#', '')
    if clean_tag in content:
        return

    # Tenta encontrar frontmatter
    frontmatter_match = re.search(r"^---\s*\n(.*?)\n---\s*\n", content, re.DOTALL)
    
    if frontmatter_match:
        frontmatter = frontmatter_match.group(1)
        if "tags:" in frontmatter:
            # Verifica se a tag já está no frontmatter
            if clean_tag not in frontmatter:
                new_frontmatter = re.sub(r"(tags:\s*(?:\[.*?\]|.*))", f"\\1\n  - {clean_tag}", frontmatter)
                content = content.replace(frontmatter, new_frontmatter)
        else:
            new_frontmatter = frontmatter + f"\ntags: [{clean_tag}]"
            content = content.replace(frontmatter, new_frontmatter)
    else:
        content = f"---\ntags: [{clean_tag}]\n---\n\n" + content

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Tag {tag} adicionada a: {os.path.basename(filepath)}")

def run_cleanup():
    for folder, tag in MAPPING.items():
        dir_path = os.path.join(VAULT_ROOT, folder)
        if not os.path.exists(dir_path):
            continue
            
        for root, dirs, files in os.walk(dir_path):
            current_rel_path = os.path.relpath(root, VAULT_ROOT).replace("\\", "/")
            
            best_tag = tag
            # Busca a tag mais específica
            for m_folder, m_tag in MAPPING.items():
                if current_rel_path.startswith(m_folder) and len(m_folder) > len(folder):
                    best_tag = m_tag
            
            for file in files:
                if file.endswith(".md"):
                    add_tag_to_file(os.path.join(root, file), best_tag)

if __name__ == "__main__":
    run_cleanup()
