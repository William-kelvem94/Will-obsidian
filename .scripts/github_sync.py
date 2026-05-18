import json
import os
import re
from datetime import datetime
import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

# Configurações
SCRIPT_ROOT = os.path.dirname(os.path.abspath(__file__))
GITHUB_USERNAME = "William-kelvem94"
VAULT_PATH = os.path.normpath(os.path.join(SCRIPT_ROOT, ".."))
TARGET_FILE = os.path.join(VAULT_PATH, "Projetos/GitHub-Completo.md")
LOCAL_PRIVADOS_DIR = os.path.normpath(os.path.join(VAULT_PATH, "Projetos/Privados"))

def build_session():
    """Build a requests.Session with retries and optional Authorization header.

    Reads GITHUB_TOKEN from env and adds Authorization header if present.
    """
    session = requests.Session()
    retries = Retry(total=3, backoff_factor=1, status_forcelist=(429, 500, 502, 503, 504))
    adapter = HTTPAdapter(max_retries=retries)
    session.mount("https://", adapter)
    session.mount("http://", adapter)

    headers = {"User-Agent": "Will-Vault-Sync/1.0"}
    token = os.getenv("GITHUB_TOKEN")
    if token:
        headers["Authorization"] = f"token {token}"
    session.headers.update(headers)
    return session


def get_json(url, session=None):
    if session is None:
        session = build_session()
    try:
        resp = session.get(url, timeout=30)
        if resp.status_code == 200:
            return resp.json()
        if resp.status_code == 409:  # Repository is empty
            return []
        print(f"Erro HTTP {resp.status_code} ao acessar {url}: {resp.text[:200]}")
    except requests.RequestException as e:
        print(f"Erro inesperado ao acessar {url}: {e}")
    return None

def get_repositories(username):
    session = build_session()
    url = f"https://api.github.com/users/{username}/repos?per_page=100&sort=updated"
    return get_json(url, session=session) or []

def get_commits(owner, repo):
    session = build_session()
    url = f"https://api.github.com/repos/{owner}/{repo}/commits?per_page=3"
    data = get_json(url, session=session)
    if data:
        return [f"{c['commit']['message'][:50]} ({c['commit']['author']['date'][:10]})" for c in data]
    return ["Sem histórico recente"]


def get_local_clone_names():
    if not os.path.isdir(LOCAL_PRIVADOS_DIR):
        return set()
    results = set()
    for entry in os.listdir(LOCAL_PRIVADOS_DIR):
        if os.path.isdir(os.path.join(LOCAL_PRIVADOS_DIR, entry)):
            results.add(entry.lower())
        elif entry.lower().endswith('.md'):
            results.add(os.path.splitext(entry)[0].lower())
    return results


def update_markdown(repos):
    now = datetime.now().strftime("%Y-%m-%d %H:%M")
    local_clones = get_local_clone_names()
    
    # Gerar a lista de repositórios com commits
    repo_md_lines = []
    print("Buscando detalhes dos repositórios...")
    for repo in repos[:15]: # Limitar aos 15 mais recentes para performance/rate-limit
        name = repo['name']
        commits = get_commits(GITHUB_USERNAME, name)
        commits_str = " | ".join(commits)
        status = "🔒 Clone local" if name.lower() in local_clones else "☁️ GitHub"
        line = f"- [{name}]({repo['html_url']}) ({repo['language'] or 'N/A'}) - {repo['description'] or 'Sem descrição'} ({status})\n    - *Últimos:* {commits_str}"
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
