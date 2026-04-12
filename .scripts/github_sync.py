import urllib.request
import urllib.error
import json
import os
import re
from datetime import datetime

# Configurações
GITHUB_USERNAME = "William-kelvem94"
VAULT_PATH = "d:/Documents/GitHub/Will-obsidian"
TARGET_FILE = os.path.join(VAULT_PATH, "Projetos/GitHub-Completo.md")

def get_json(url):
    headers = {"User-Agent": "Mozilla/5.0"}
    req = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(req) as response:
            if response.getcode() == 200:
                return json.loads(response.read().decode())
    except urllib.error.HTTPError as e:
        if e.code == 409: # Repository is empty
            return []
        print(f"Erro HTTP {e.code} ao acessar {url}: {e.reason}")
    except Exception as e:
        print(f"Erro inesperado ao acessar {url}: {e}")
    return None

def get_repositories(username):
    url = f"https://api.github.com/users/{username}/repos?per_page=100&sort=updated"
    return get_json(url) or []

def get_commits(owner, repo):
    url = f"https://api.github.com/repos/{owner}/{repo}/commits?per_page=3"
    data = get_json(url)
    if data:
        return [f"{c['commit']['message'][:50]} ({c['commit']['author']['date'][:10]})" for c in data]
    return ["Sem histórico recente"]

def update_markdown(repos):
    now = datetime.now().strftime("%Y-%m-%d %H:%M")
    
    # Gerar a lista de repositórios com commits
    repo_md_lines = []
    print("Buscando detalhes dos repositórios...")
    for repo in repos[:15]: # Limitar aos 15 mais recentes para performance/rate-limit
        name = repo['name']
        commits = get_commits(GITHUB_USERNAME, name)
        commits_str = " | ".join(commits)
        line = f"- [{name}]({repo['html_url']}) ({repo['language'] or 'N/A'}) - {repo['description'] or 'Sem descrição'}\n    - *Últimos:* {commits_str}"
        repo_md_lines.append(line)
        print(f"  ✓ {name} processado.")
    
    repo_list_md = "\n".join(repo_md_lines)
    stats_table = f"| Métrica | Valor |\n|---|---|\n| Total de Repos | {len(repos)} |\n| Atualizado em | {now} |\n"
    
    if not os.path.exists(TARGET_FILE):
        return

    with open(TARGET_FILE, "r", encoding="utf-8") as f:
        content = f.read()

    # Atualizar data
    content = re.sub(r"Atualizado: \d{4}-\d{2}-\d{2}.*", f"Atualizado: {now} via Pro-Sync", content)
    
    # Atualizar Stats
    if "## 📈 Stats Gerais" in content:
        content = re.sub(
            r"## 📈 Stats Gerais\n.*?(\n\n|##|$)", 
            f"## 📈 Stats Gerais\n\n{stats_table}\n\n", 
            content, 
            flags=re.DOTALL
        )

    # Lista Automática
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
    
    print(f"Sucesso! {len(repos)} repositórios (15 com histórico) mapeados em {TARGET_FILE}")

if __name__ == "__main__":
    repos = get_repositories(GITHUB_USERNAME)
    if repos:
        update_markdown(repos)
