import datetime
import os
import re
import subprocess
import sys
from pathlib import Path


VAULT_ROOT = Path(
    os.getenv("JARVIS_VAULT_ROOT")
    or os.getenv("OBSIDIAN_VAULT_PATH")
    or r"D:/DOCUMENTOS/GitHub/Will-obsidian"
)
TEMPLATES_DIR = VAULT_ROOT / "Templates"
MEMORY_DIR = Path(os.getenv("JARVIS_LEARNED_PATTERNS_DIR") or VAULT_ROOT / "JARVIS" / "03-Memory" / "Learned-Patterns")
INDEXER_SCRIPT = Path(os.getenv("JARVIS_INDEXER_SCRIPT") or VAULT_ROOT / ".scripts" / "knowledge_indexer.py")
TEMPLATE_FILE = TEMPLATES_DIR / "Post-Mortem-JARVIS.md"


def ensure_directories():
    """Garante que a pasta segura de memorias exista."""
    MEMORY_DIR.mkdir(parents=True, exist_ok=True)


def _slugify(value: str) -> str:
    value = value.strip().lower()
    value = re.sub(r"[^a-z0-9_-]+", "-", value, flags=re.IGNORECASE)
    return value.strip("-") or "tarefa-sem-nome"


def _fill_template(template_content: str, task_data: dict) -> str:
    today = datetime.date.today().isoformat()
    replacements = {
        "{{title}}": task_data.get("title", "Tarefa Sem Nome"),
        "{{project}}": task_data.get("project", "Projeto Geral"),
        "{{date}}": task_data.get("date", today),
    }

    content = template_content
    for marker, value in replacements.items():
        content = content.replace(marker, str(value))

    section_values = {
        "- **O que foi solicitado:** ": task_data.get("goal", "N/A"),
        "- **Problema a resolver:** ": task_data.get("problem", "N/A"),
        "- **Resumo Técnico:** ": task_data.get("solution", "N/A"),
        "- **Resumo TÃ©cnico:** ": task_data.get("solution", "N/A"),
        "- **Arquivos Alterados:** ": task_data.get("files", "N/A"),
        "- **Lógica Principal:** ": task_data.get("logic", "N/A"),
        "- **LÃ³gica Principal:** ": task_data.get("logic", "N/A"),
        '- **O "Pulo do Gato":** ': task_data.get("insights", "N/A"),
        "- **Conexões:** ": task_data.get("connections", "N/A"),
        "- **ConexÃµes:** ": task_data.get("connections", "N/A"),
        "- **Obstáculos:** ": task_data.get("debts", "N/A"),
        "- **ObstÃ¡culos:** ": task_data.get("debts", "N/A"),
        "- **Melhorias Futuras:** ": task_data.get("future", "N/A"),
        "- **Risco:** ": task_data.get("risk", "N/A"),
    }

    for marker, value in section_values.items():
        content = content.replace(marker, f"{marker}{value}\n")

    return content


def create_post_mortem(task_data: dict):
    """
    Cria uma nota de Post-Mortem em area segura do JARVIS.

    task_data: dict contendo title, project, goal, problem, solution, files,
    logic, insights, connections, debts, future e risk.
    """
    ensure_directories()

    if not TEMPLATE_FILE.exists():
        print(f"Erro: Template nao encontrado em {TEMPLATE_FILE}")
        return None

    with open(TEMPLATE_FILE, "r", encoding="utf-8") as f:
        template_content = f.read()

    title = task_data.get("title", "Tarefa Sem Nome")
    date = task_data.get("date", datetime.date.today().isoformat())
    content = _fill_template(template_content, task_data)

    filename = f"{date}-post-mortem-{_slugify(title)}.md"
    file_path = MEMORY_DIR / filename

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"Memoria consolidada em: {file_path}")
    return file_path


def trigger_rag_update():
    """Chama o indexador de conhecimento para atualizar o indice local."""
    if INDEXER_SCRIPT.exists():
        print("Atualizando indice RAG...")
        try:
            subprocess.run([sys.executable, str(INDEXER_SCRIPT), "--update"], check=True)
            print("Indice RAG atualizado com sucesso.")
        except subprocess.CalledProcessError as e:
            print(f"Erro ao atualizar indice: {e}")
    else:
        print(f"Script de indexacao nao encontrado em {INDEXER_SCRIPT}. Pulando atualizacao RAG.")


if __name__ == "__main__":
    print(f"Vault root: {VAULT_ROOT}")
    print(f"Memory dir: {MEMORY_DIR}")
    print(f"Template: {TEMPLATE_FILE}")
    print(f"Indexer: {INDEXER_SCRIPT}")
    print("Importe create_post_mortem(task_data) para registrar uma memoria real.")
