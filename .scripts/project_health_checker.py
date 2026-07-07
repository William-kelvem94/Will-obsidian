#!/usr/bin/env python3
"""
Project Health Checker - auditoria leve dos projetos ativos do Will Vault.

Este script foi atualizado para a estrutura numerada canonica do WILL-OBSIDIAN.
Ele prioriza notas de projeto em `03-Projetos/01-Ativos/Privados/` e, quando
existe um clone local apontado por `source:` ou pelo bloco de sincronizacao,
enriquece a analise com sinais tecnicos do repositorio fisico.
"""

from __future__ import annotations

import re
from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path
from typing import Iterable

SCRIPT_ROOT = Path(__file__).parent.resolve()
VAULT_PATH = SCRIPT_ROOT.parent.resolve()

CANONICAL_PROJECTS_DIR = VAULT_PATH / "03-Projetos" / "01-Ativos" / "Privados"
LEGACY_PROJECTS_DIR = VAULT_PATH / "Projetos" / "01-Ativos" / "Privados"
SKILLS_DIR = VAULT_PATH / "05-Skills"
OUTPUT_FILE = VAULT_PATH / "02-JARVIS" / "02-Operational" / "Project-Health-Report.md"
SKILLS_GAP_FILE = VAULT_PATH / ".logs" / "skills_gap.md"

IGNORED_NOTE_NAMES = {
    "README.md",
    "INDEX.md",
    "GitHub-Completo.md",
    "search_works.md",
}
IGNORED_DIR_NAMES = {"LEGACY", "__pycache__", ".obsidian"}


@dataclass
class Check:
    category: str
    score: int
    max_score: int
    message: str

    @property
    def percentage(self) -> float:
        return (self.score / self.max_score * 100) if self.max_score else 0


@dataclass
class ProjectHealth:
    name: str
    note_path: Path
    repo_path: Path | None = None
    checks: list[Check] = field(default_factory=list)

    @property
    def score(self) -> int:
        return sum(check.score for check in self.checks)

    @property
    def max_score(self) -> int:
        return sum(check.max_score for check in self.checks)

    @property
    def percentage(self) -> float:
        return (self.score / self.max_score * 100) if self.max_score else 0

    def grade(self) -> tuple[str, str]:
        pct = self.percentage
        if pct >= 90:
            return "A", "🟢"
        if pct >= 80:
            return "B", "🟢"
        if pct >= 70:
            return "C", "🟡"
        if pct >= 60:
            return "D", "🟡"
        return "F", "🔴"

    def add(self, category: str, score: int, max_score: int, message: str) -> None:
        self.checks.append(Check(category, score, max_score, message))


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="ignore")


def active_projects_dir() -> Path:
    """Return the canonical project notes directory, falling back to legacy."""
    if CANONICAL_PROJECTS_DIR.exists():
        return CANONICAL_PROJECTS_DIR
    return LEGACY_PROJECTS_DIR


def parse_frontmatter(content: str) -> dict[str, str]:
    match = re.match(r"^---\s*\n(.*?)\n---\s*\n", content, re.DOTALL)
    if not match:
        return {}

    fm: dict[str, str] = {}
    for line in match.group(1).splitlines():
        if ":" not in line or line.startswith(" "):
            continue
        key, value = line.split(":", 1)
        fm[key.strip()] = value.strip().strip('"\'')
    return fm


def extract_list_field(content: str, field_name: str) -> set[str]:
    match = re.search(rf"^{field_name}:\s*\[(.*?)\]", content, re.MULTILINE | re.DOTALL)
    if not match:
        return set()
    return {item.strip().strip('"\'').lower() for item in match.group(1).split(",") if item.strip()}


def extract_repo_path(content: str, fm: dict[str, str]) -> Path | None:
    candidates: list[str] = []

    source = fm.get("source")
    if source and (":" in source or source.startswith("/")):
        candidates.append(source)

    local_path_match = re.search(r"Caminho F[íi]sico Local:\*\*\s*`([^`]+)`", content)
    if local_path_match:
        candidates.append(local_path_match.group(1))

    for raw in candidates:
        normalized = raw.replace("\\", "/")
        path = Path(normalized)
        if path.exists():
            return path
    return None


def iter_project_notes(projects_dir: Path) -> Iterable[Path]:
    if not projects_dir.exists():
        return []

    notes: list[Path] = []
    for path in sorted(projects_dir.glob("*.md")):
        if path.name in IGNORED_NOTE_NAMES:
            continue
        if path.name.endswith("-old.md"):
            continue
        notes.append(path)
    return notes


def has_any_heading(content: str, names: Iterable[str]) -> bool:
    for name in names:
        if re.search(rf"^#+\s+.*{re.escape(name)}", content, re.IGNORECASE | re.MULTILINE):
            return True
    return False


def check_note_quality(project: ProjectHealth, content: str, fm: dict[str, str]) -> None:
    score = 0
    required_fields = ["title", "source", "language", "description", "updated", "tags"]
    present = [field for field in required_fields if fm.get(field)]
    score += min(len(present), len(required_fields))

    if has_any_heading(content, ["Visão", "Visao", "Resumo", "Contexto"]):
        score += 2
    if has_any_heading(content, ["Roadmap", "Meta 90 Dias", "Próximos", "Proximos"]):
        score += 2
    if has_any_heading(content, ["Arquitetura", "Estrutura", "Tech Stack", "Engenharia"]):
        score += 2
    if has_any_heading(content, ["Riscos", "Decisões", "Decisoes", "Diário", "Diario"]):
        score += 1
    if len(content) > 900:
        score += 2

    project.add("Nota canônica", min(score, 15), 15, f"{len(present)}/{len(required_fields)} metadados principais + seções de projeto")


def check_project_links(project: ProjectHealth, content: str) -> None:
    score = 0
    if "GitHub-Completo" in content:
        score += 2
    if "Plano-de-Acao" in content or "Plano de Ação" in content or "Plano de Acao" in content:
        score += 2
    if "05-Skills" in content or "skills" in content.lower():
        score += 2
    if "02-JARVIS" in content or "JARVIS" in content:
        score += 1
    project.add("Links internos", score, 7, f"links operacionais detectados: {score}/7")


def check_execution_contract(project: ProjectHealth, content: str) -> None:
    score = 0
    if re.search(r"\b(run|start|dev|build|test|docker compose|pnpm|npm|python|uvicorn)\b", content, re.IGNORECASE):
        score += 4
    if ".env.example" in content:
        score += 2
    if "Dockerfile" in content or "docker-compose" in content or "docker compose" in content:
        score += 2
    if "CI" in content or "GitHub Actions" in content:
        score += 2
    project.add("Contrato de execução", score, 10, f"sinais de execução/deploy/ambiente: {score}/10")


def check_repo_health(project: ProjectHealth) -> None:
    repo = project.repo_path
    if not repo:
        project.add("Clone local", 0, 8, "clone local não acessível neste ambiente")
        return

    score = 0
    signals = []
    for filename, points, label in [
        ("README.md", 2, "README"),
        ("package.json", 2, "Node"),
        ("requirements.txt", 2, "Python"),
        ("Dockerfile", 1, "Dockerfile"),
        ("docker-compose.yml", 1, "Compose"),
        (".env.example", 1, ".env.example"),
        (".github/workflows", 2, "GitHub Actions"),
    ]:
        if (repo / filename).exists():
            score += points
            signals.append(label)
    project.add("Clone local", min(score, 8), 8, ", ".join(signals) if signals else "sem sinais estruturados no clone")


def load_defined_skills(skills_root: Path) -> set[str]:
    skills: set[str] = set()
    if not skills_root.exists():
        return skills
    for path in skills_root.rglob("*.md"):
        if path.name.lower() in {"readme.md", "index.md"}:
            continue
        content = read_text(path)
        title_match = re.search(r'^title:\s*"?(.*?)"?\s*$', content, re.MULTILINE)
        skills.add((title_match.group(1) if title_match else path.stem).strip().lower())
    return skills


def check_skills_gap(projects: list[ProjectHealth], skills_root: Path, output_path: Path) -> None:
    defined_skills = load_defined_skills(skills_root)
    referenced: set[str] = set()
    missing: list[tuple[str, str]] = []

    for project in projects:
        content = read_text(project.note_path)
        project_skills = extract_list_field(content, "skills_usados") | extract_list_field(content, "skills")
        inline_skills = {tag.lstrip("#").lower() for tag in re.findall(r"#skills[\w/-]*", content)}
        project_skills |= inline_skills
        referenced |= project_skills
        for skill in project_skills:
            if defined_skills and skill not in defined_skills:
                missing.append((project.name, skill))

    orphan_skills = sorted(defined_skills - referenced)

    output_path.parent.mkdir(parents=True, exist_ok=True)
    lines = [
        "# Skills Gap Report",
        "",
        f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
        "",
        "## Missing Skills Referenced by Projects",
        "",
    ]
    lines.extend([f"- {project}: {skill}" for project, skill in missing] or ["- None found"])
    lines.extend(["", "## Defined Skills Not Referenced by Projects", ""])
    lines.extend([f"- {skill}" for skill in orphan_skills] or ["- None found"])
    output_path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def analyze_project(note_path: Path) -> ProjectHealth:
    content = read_text(note_path)
    fm = parse_frontmatter(content)
    name = fm.get("title") or note_path.stem
    project = ProjectHealth(name=name, note_path=note_path, repo_path=extract_repo_path(content, fm))
    check_note_quality(project, content, fm)
    check_project_links(project, content)
    check_execution_contract(project, content)
    check_repo_health(project)
    return project


def generate_full_report(projects: list[ProjectHealth], projects_dir: Path) -> str:
    now = datetime.now()
    projects_sorted = sorted(projects, key=lambda item: item.percentage, reverse=True)
    total_score = sum(project.score for project in projects_sorted)
    total_max = sum(project.max_score for project in projects_sorted)
    overall = (total_score / total_max * 100) if total_max else 0

    grade_counts: dict[str, int] = {}
    for project in projects_sorted:
        grade, _ = project.grade()
        grade_counts[grade] = grade_counts.get(grade, 0) + 1

    lines = [
        "---",
        'title: "Project Health Report"',
        'description: "Automated health check of active project notes"',
        "tags: [report, health, projects, automated, jarvis-operacao]",
        f"generated: {now.strftime('%Y-%m-%d %H:%M:%S')}",
        f"updated: {now.strftime('%Y-%m-%d')}",
        "---",
        "",
        "# 📊 Project Health Report",
        "",
        f"**Generated:** {now.strftime('%Y-%m-%d at %H:%M:%S')}",
        f"**Projects Directory:** `{projects_dir.relative_to(VAULT_PATH)}`",
        f"**Projects Scanned:** {len(projects_sorted)}",
        "",
        "---",
        "",
        "## 📈 Overall Summary",
        "",
        "| Metric | Value |",
        "|--------|-------|",
        f"| **Overall Health** | {overall:.0f}% |",
        f"| **Total Score** | {total_score}/{total_max} |",
    ]
    for grade in ["A", "B", "C", "D", "F"]:
        if grade in grade_counts:
            lines.append(f"| **Grade {grade}** | {grade_counts[grade]} projects |")

    lines.extend(["", "---", "", "## 🏆 Project Rankings", ""])
    for index, project in enumerate(projects_sorted, 1):
        grade, icon = project.grade()
        lines.append(f"{index}. {icon} **{project.name}** — {project.percentage:.0f}% ({grade})")

    lines.extend(["", "---", "", "## 📋 Detailed Reports", ""])
    for project in projects_sorted:
        grade, icon = project.grade()
        rel_note = project.note_path.relative_to(VAULT_PATH)
        lines.extend([
            f"### {icon} {project.name}",
            "",
            f"**Nota:** [[{str(rel_note.with_suffix('')).replace('\\\\', '/')}]]",
            f"**Score:** {project.score}/{project.max_score} ({project.percentage:.0f}%) — Grade: **{grade}**",
            "",
            "| Check | Score | Status |",
            "|-------|-------|--------|",
        ])
        for check in project.checks:
            lines.append(f"| {check.category} | {check.score}/{check.max_score} | {check.message} |")

        low = [check for check in project.checks if check.percentage < 50]
        if low:
            lines.extend(["", "**Recommendations:**"])
            for check in low:
                if check.category == "Nota canônica":
                    lines.append("- 📝 Completar metadados, visão, roadmap, arquitetura, riscos e diário de bordo.")
                elif check.category == "Links internos":
                    lines.append("- 🔗 Linkar a nota ao plano de ação, skills, JARVIS e GitHub Completo.")
                elif check.category == "Contrato de execução":
                    lines.append("- ⚙️ Registrar comandos de run/dev/test/build, ambiente e deploy.")
                elif check.category == "Clone local":
                    lines.append("- 📦 Confirmar `source:` local ou manter nota como documentação sem clone acessível.")
        lines.append("")

    lines.extend([
        "---",
        "",
        "## 🔗 Related Documents",
        "",
        "- [[02-JARVIS/README|JARVIS]]",
        "- [[03-Projetos/01-Ativos/Plano-de-Acao|Plano de Ação]]",
        "- [[03-Projetos/01-Ativos/Privados/README|Projects Index]]",
        "- [[10-Interfaces/Painel-Cockpit-Operacional|Painel Cockpit Operacional]]",
        "",
        "---",
        "",
        "*Generated by `.scripts/project_health_checker.py` using canonical numbered paths.*",
    ])
    return "\n".join(lines) + "\n"


def scan_projects() -> list[ProjectHealth]:
    projects_dir = active_projects_dir()
    if not projects_dir.exists():
        print(f"❌ Projects directory not found: {projects_dir}")
        return []
    projects = [analyze_project(note) for note in iter_project_notes(projects_dir)]
    return projects


def main() -> None:
    print("🔍 Scanning canonical project notes...")
    projects = scan_projects()
    if not projects:
        print("⚠️ No project notes found to scan")
        return

    projects_dir = active_projects_dir()
    print(f"📊 Analyzed {len(projects)} projects from {projects_dir.relative_to(VAULT_PATH)}")

    check_skills_gap(projects, SKILLS_DIR, SKILLS_GAP_FILE)
    print(f"✅ Skills gap report generated: {SKILLS_GAP_FILE.relative_to(VAULT_PATH)}")

    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_FILE.write_text(generate_full_report(projects, projects_dir), encoding="utf-8")
    print(f"✅ Health report generated: {OUTPUT_FILE.relative_to(VAULT_PATH)}")

    print("\n📈 Quick Summary:")
    for project in sorted(projects, key=lambda item: item.percentage, reverse=True)[:5]:
        grade, icon = project.grade()
        print(f"  {icon} {project.name}: {project.percentage:.0f}% (Grade {grade})")


if __name__ == "__main__":
    main()
