import urllib.request
import json
import os
import re
from datetime import datetime

# Configurações
GITHUB_USERNAME = "William-kelvem94"
VAULT_PATH = "d:/Documents/GitHub/Will-obsidian"
TARGET_FILE = os.path.join(VAULT_PATH, "Projetos/GitHub-Completo.md")

def get_repositories(username):
    url = f"https://api.github.com/users/{username}/repos?per_page=100&sort=updated"
    headers = {"User-Agent": "Mozilla/5.0"} # GitHub API requer um user-agent
    req = urllib.request.Request(url, headers=headers)
    
    try:
        with urllib.request.urlopen(req) as response:
            if response.getcode() == 200:
                return json.loads(response.read().decode())
            else:
                print(f"Erro ao buscar repositórios: {response.getcode()}")
                return []
    except Exception as e:
        print(f"Erro na requisição: {e}")
        return []

def update_markdown(repos):
    now = datetime.now().strftime("%Y-%m-%d %H:%M")
    
    # Gerar a lista de repositórios
    repo_list_md = "\n".join([
        f"- [{repo['name']}]({repo['html_url']}) ({repo['language'] or 'N/A'}) - {repo['description'] or 'Sem descrição'}"
        for repo in repos
    ])
    
    stats_table = f"| Métrica | Valor |\n|---|---|\n| Total de Repos | {len(repos)} |\n| Atualizado em | {now} |\n"
    
    if not os.path.exists(TARGET_FILE):
        print(f"Arquivo alvo não encontrado: {TARGET_FILE}")
        return

    with open(TARGET_FILE, "r", encoding="utf-8") as f:
        content = f.read()

    # Atualizar data de atualização no texto
    content = re.sub(r"Atualizado: \d{4}-\d{2}-\d{2}.*", f"Atualizado: {now} via Sync Script", content)
    
    # Seção de estatísticas (Stats Gerais)
    if "## 📈 Stats Gerais" in content:
        # Tenta substituir a tabela de stats se existir
        content = re.sub(
            r"## 📈 Stats Gerais\n.*?(\n\n|##|$)", 
            f"## 📈 Stats Gerais\n\n{stats_table}\n\n", 
            content, 
            flags=re.DOTALL
        )

    # Seção de lista automática
    if "## Lista de Repositórios (Automática)" in content:
        content = re.sub(
            r"## Lista de Repositórios \(Automática\).*?(?=\n##|$)", 
            f"## Lista de Repositórios (Automática)\n\n{repo_list_md}\n", 
            content, 
            flags=re.DOTALL
        )
    else:
        content += f"\n\n## Lista de Repositórios (Automática)\n\n{repo_list_md}\n"

    with open(TARGET_FILE, "w", encoding="utf-8") as f:
        f.write(content)
    
    print(f"Sucesso! {len(repos)} repositórios mapeados em {TARGET_FILE}")

if __name__ == "__main__":
    repos = get_repositories(GITHUB_USERNAME)
    if repos:
        update_markdown(repos)
