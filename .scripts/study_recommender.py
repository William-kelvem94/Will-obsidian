#!/usr/bin/env python3
"""
Recomendador de Próximo Estudo — Sugere tópicos para estudar com base em
gaps de conhecimento, nível de skill baixo e histórico recente de estudos.

Estratégia de recomendação:
  1. Skills com #level-basic / #level-init (ou nivel: iniciante / level ≤ 2)
  2. Skills listadas como órfãs/não-referenciadas no skills_gap.md
  3. Gaps mencionados em GAPS.md
  4. Remove tópicos estudados nos últimos 14 dias (via Conhecimento-Geral/)
  5. Pondera por urgência aparente e ordena Top 3 + Quick Win
"""

import re
import subprocess
from pathlib import Path
from datetime import datetime, timedelta
from collections import defaultdict

SCRIPT_ROOT = Path(__file__).parent
VAULT_PATH = SCRIPT_ROOT.parent
OUTPUT_FILE = VAULT_PATH / "JARVIS" / "02-Operational" / "Proximo-Estudo.md"

# ── helpers ──────────────────────────────────────────────────────────────


def run(cmd, cwd=None):
    """Executa comando shell e retorna stdout limpo."""
    try:
        r = subprocess.run(
            cmd, shell=True, cwd=cwd or VAULT_PATH,
            capture_output=True, text=True, encoding="utf-8",
        )
        return r.stdout.strip()
    except Exception:
        return ""


def parse_frontmatter(content):
    """Extrai campos relevantes do frontmatter YAML de forma simples."""
    fm = {"tags": [], "nivel": None, "level": None, "title": ""}
    m = re.match(r"^---\s*\n(.*?)\n(?:---|\.\.\.)", content, re.DOTALL)
    if not m:
        return fm
    block = m.group(1)

    # title
    t = re.search(r'^title:\s*"?(.+?)"?\s*$', block, re.MULTILINE)
    if t:
        fm["title"] = t.group(1).strip()

    # tags inline array  tags: [a, b, c]
    m_tags = re.search(r"^tags:\s*\[(.+?)\]", block, re.MULTILINE)
    if m_tags:
        fm["tags"] = [x.strip().strip("\"'") for x in m_tags.group(1).split(",") if x.strip()]

    # nivel field
    m_nivel = re.search(r"^nivel:\s*(.+)", block, re.MULTILINE)
    if m_nivel:
        fm["nivel"] = m_nivel.group(1).strip().lower()

    # level field (numeric)
    m_level = re.search(r"^level:\s*(\d+)", block, re.MULTILINE)
    if m_level:
        fm["level"] = int(m_level.group(1))

    return fm


def is_basic(fm):
    """Retorna True se o frontmatter indica nível básico/iniciante."""
    if any(t in ("level-basic", "level-init") for t in fm["tags"]):
        return True
    if fm["nivel"] in ("basico", "básico", "iniciante"):
        return True
    if fm["level"] is not None and fm["level"] <= 2:
        return True
    return False


def wiki_path(path):
    """Converte caminho relativo para wiki-link (remove extensão)."""
    rel = path.relative_to(VAULT_PATH)
    return str(rel.with_suffix("")).replace("\\", "/")


# ── scanners ─────────────────────────────────────────────────────────────


def scan_low_skills():
    """Varre skills/ por notas com nível básico."""
    results = []
    skills_dir = VAULT_PATH / "skills"
    for p in sorted(skills_dir.rglob("*.md")):
        if p.name.lower() == "readme.md":
            continue
        try:
            raw = p.read_text(encoding="utf-8", errors="replace")
        except Exception:
            continue
        fm = parse_frontmatter(raw)
        if is_basic(fm):
            title = fm["title"] or p.stem.replace("-", " ").title()
            results.append({
                "name": title,
                "source": "low-skill",
                "reason": "Skill em nível básico",
                "note_path": p,
                "priority": 3,
            })
    return results


def parse_gaps():
    """Lê GAPS.md e extrai gaps relevantes (apenas seção de Skills/Áreas)."""
    gaps_file = VAULT_PATH / "GAPS.md"
    if not gaps_file.exists():
        return []
    try:
        text = gaps_file.read_text(encoding="utf-8", errors="replace")
    except Exception:
        return []

    gaps = []
    # Só considera gaps dentro da seção "Skills/Áreas sem nota dedicada"
    sections = text.split("##")
    target = None
    for s in sections:
        if "Skills/Áreas sem nota dedicada" in s or "Skills" in s.splitlines()[0] if s.splitlines() else False:
            target = s
            break
    if not target:
        target = text  # fallback

    for line in target.splitlines():
        line = line.strip()
        if not line.startswith("- "):
            continue
        content = line[2:].strip().lstrip("*").strip()
        if not content:
            continue
        # skip headers, emoji-only, or celebratory lines
        if "nenhum gap" in content.lower():
            continue
        if content.lower().startswith("sugira") or content.lower().startswith("anexe"):
            continue
        gaps.append({
            "name": content.strip(" *"),
            "source": "gaps-md",
            "reason": "Gap de conhecimento identificado no GAPS.md",
            "note_path": gaps_file,
            "priority": 5,
        })
    return gaps


def parse_skills_gap():
    """Lê .logs/skills_gap.md e extrai skills órfãs / não-referenciadas."""
    sg_file = VAULT_PATH / ".logs" / "skills_gap.md"
    if not sg_file.exists():
        return []
    try:
        text = sg_file.read_text(encoding="utf-8", errors="replace")
    except Exception:
        return []

    results = []
    in_orphan = False
    for line in text.splitlines():
        if "Defined Skills Not Referenced by Projects" in line:
            in_orphan = True
            continue
        if line.startswith("##") and in_orphan and "Defined Skills" not in line:
            break
        if in_orphan and line.startswith("- "):
            name = line.lstrip("- ").strip()
            if name and name.lower() != "none found":
                results.append({
                    "name": name,
                    "source": "skills-gap",
                    "reason": "Skill não referenciada por projetos ativos — lacuna potencial",
                    "note_path": sg_file,
                    "priority": 4,
                })
    return results


def get_recent_studies():
    """Retorna set de nomes de notas modificadas em Conhecimento-Geral/ nos últimos 14 dias."""
    recent_names = set()
    since = (datetime.now() - timedelta(days=14)).isoformat()

    # git-based (mais confiável)
    cmd = f"git log --since=\"{since}\" --name-only --pretty=format: --all -- \"Conhecimento-Geral/*.md\""
    output = run(cmd)
    for line in output.splitlines():
        line = line.strip()
        if line.endswith(".md"):
            stem = Path(line).stem.lower().replace("-", " ").replace("_", " ")
            recent_names.add(stem)

    # file-mtime fallback
    base = VAULT_PATH / "Conhecimento-Geral"
    cutoff = datetime.now() - timedelta(days=14)
    for p in base.rglob("*.md"):
        try:
            mtime = datetime.fromtimestamp(p.stat().st_mtime)
            if mtime >= cutoff:
                stem = p.stem.lower().replace("-", " ").replace("_", " ")
                recent_names.add(stem)
        except Exception:
            continue
    return recent_names


# ── recommendation engine ────────────────────────────────────────────────


def build_recommendations():
    """Junta todas as fontes, filtra recentes, pontua e ordena."""
    candidates = []
    candidates.extend(scan_low_skills())
    candidates.extend(parse_gaps())
    candidates.extend(parse_skills_gap())

    if not candidates:
        print("[WARN] Nenhum candidato encontrado — tudo coberto ou vazio!")
        return []

    recent = get_recent_studies()
    print(f"[INFO] {len(recent)} tópicos recentes ignorados (estudados nos últimos 14d)")

    # desduplica por nome (case-insensitive)
    seen = {}
    for c in candidates:
        key = c["name"].lower().strip()
        if key in recent:
            continue
        if key in seen:
            # merge — mantém a prioridade mais alta
            if c["priority"] > seen[key]["priority"]:
                seen[key]["priority"] = c["priority"]
                seen[key]["reason"] = c["reason"]
                seen[key]["source"] = c["source"]
            continue
        seen[key] = c

    recs = sorted(seen.values(), key=lambda x: (-x["priority"], x["name"]))

    if not recs:
        print("[INFO] Todos os gaps foram estudados recentemente — nada a recomendar.")
    return recs


def estimate_time(name):
    """Devolve estimativa de estudo baseada no nome do tópico."""
    name_l = name.lower()
    if any(w in name_l for w in ("kubernetes", "rag", "backend", "arquitetura", "orquestração", "multi-agent", "machine learning", "deep learning", "genai", "rag avancado", "advanced")):
        return "2–3h"
    if any(w in name_l for w in ("prompt", "mcp", "finops", "testes", "observabilidade", "monitoramento", "product")):
        return "1–2h"
    if any(w in name_l for w in ("web", "component", "git", "python", "node", "docker")):
        return "45min–1h30"
    return "1–2h"


def find_existing_note(name):
    """Tenta encontrar uma nota existente no vault que relacione ao nome."""
    name_l = name.lower()
    candidates = []

    # áreas mais prováveis
    for folder in ["skills", "Conhecimento-Geral"]:
        base = VAULT_PATH / folder
        if not base.exists():
            continue
        for p in base.rglob("*.md"):
            if p.name.lower() == "index.md" or p.name.lower() == "readme.md":
                # candidate if name appears in content
                try:
                    content = p.read_text(encoding="utf-8", errors="replace").lower()
                    if name_l in content:
                        candidates.append(p)
                except Exception:
                    continue
                continue
            stem = p.stem.lower().replace("-", " ").replace("_", " ")
            # check if name words appear in filename
            name_words = set(name_l.split())
            stem_words = set(stem.split())
            if name_words & stem_words:
                candidates.append(p)

    # Score candidates by match strength
    def score(p):
        stem = p.stem.lower().replace("-", " ").replace("_", " ")
        nw = set(name_l.split())
        sw = set(stem.split())
        common = len(nw & sw)
        return common

    candidates.sort(key=score, reverse=True)
    return candidates[:3] if candidates else []


def pick_quick_win(recs):
    """Escolhe a recomendação de quick win (mais fácil / menor escopo)."""
    if not recs:
        return None
    # prefere tópicos com tempo de estudo estimado menor ou que são "básicos"
    easy_keywords = ["web", "component", "prompt", "git", "testes", "monitoramento", "finops"]
    for r in recs:
        rl = r["name"].lower()
        if any(k in rl for k in easy_keywords):
            return r
    # fallback: última recomendação (menos prioritária = menos urgente = mais fácil)
    return recs[-1]


# ── output ───────────────────────────────────────────────────────────────


def generate_output(recs):
    """Produz o markdown da nota Proximo-Estudo.md."""
    now = datetime.now()
    date_str = now.strftime("%Y-%m-%d")

    top3 = recs[:3]
    quick = pick_quick_win(recs)

    def fmt_link(note_path):
        """Gera wiki-link com label legível."""
        if not note_path:
            return ""
        rp = wiki_path(note_path)
        # path relativo curto para fontes conhecidas
        name_map = {
            "GAPS": "GAPS.md",
            ".logs/skills_gap": ".logs/skills_gap.md",
        }
        for label, src in name_map.items():
            if src in str(note_path):
                return f"[[{rp}|{label}]]"
        return f"[[{rp}]]"

    # Tabela de top3
    table_rows = ""
    for i, r in enumerate(top3, 1):
        time_est = estimate_time(r["name"])
        link = fmt_link(r["note_path"])
        table_rows += (
            f"| {i} | **{r['name']}** | {r['reason']} | {link} | {time_est} |\n"
        )

    # Detalhamento de cada recomendação
    details = ""
    for r in recs:
        time_est = estimate_time(r["name"])
        links = find_existing_note(r["name"])
        link_str = ""
        if links:
            link_str = "\n".join(f"  - [[{wiki_path(p)}]]" for p in links)
        else:
            link_str = "  - *Nenhuma nota específica encontrada ainda*"

        details += f"""
### {r['name']}

| Campo | Valor |
|-------|-------|
| **Motivo** | {r['reason']} |
| **Fonte** | `{r['source']}` |
| **Estimativa** | {time_est} |
| **Prioridade** | {r['priority']}/5 |

**Notas relacionadas no vault:**
{link_str}

---
"""

    # Quick Win
    qw_section = ""
    if quick:
        qw_time = estimate_time(quick["name"])
        qw_links = find_existing_note(quick["name"])
        qw_links_str = ""
        if qw_links:
            qw_links_str = "\n".join(f"  - [[{wiki_path(p)}]]" for p in qw_links)
        else:
            qw_links_str = "  - *Nenhuma nota específica encontrada*"
        qw_section = f"""
## 🏆 Quick Win

**{quick['name']}** — {quick['reason']}

| Campo | Valor |
|-------|-------|
| **Estimativa** | {qw_time} |
| **Dificuldade** | Baixa |
| **Impacto** | Alto (fácil de progredir) |

**Notas relacionadas:**
{qw_links_str}
"""

    md = f"""---
title: "Próximo Estudo — Recomendação Automática"
description: "Recomendação gerada automaticamente em {date_str} com base em gaps, nível de skills e histórico de estudos"
tags: [jarvis, recomendacao, estudo, auto-generated]
generated: {now.strftime("%Y-%m-%d %H:%M:%S")}
---

# 🎯 Próximo Estudo — Recomendação Automática

**Gerado em:** {now.strftime("%Y-%m-%d %H:%M")}
**Total de recomendações:** {len(recs)}

---

## Top 3 Recomendações

| # | Tópico | Motivo | Nota Relacionada | Tempo Estimado |
|---|--------|--------|------------------|----------------|
{table_rows}
---

## Detalhamento das Recomendações

{details}
---

{qw_section}
---

## 📋 Metodologia

Esta recomendação foi gerada combinando:

1. **GAPS.md** — Gaps de conhecimento declarados
2. **skills_gap.md** — Skills não referenciadas por projetos ativos
3. **skills/** — Notas com nível básico (`#level-basic`, `#level-init`, `nivel: iniciante`, ou `level ≤ 2`)
4. **Conhecimento-Geral/** — Tópicos estudados nos últimos 14 dias (excluídos da recomendação)

*Recomendação gerada automaticamente por `.scripts/study_recommender.py`*
*Para regenerar, execute: `python .scripts/study_recommender.py`*
"""
    return md


# ── main ─────────────────────────────────────────────────────────────────


def main():
    """Execução principal do recomendador."""
    print("[GEN] Gerando recomendações de estudo...")

    recs = build_recommendations()

    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)

    content = generate_output(recs)

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write(content)

    rel_path = OUTPUT_FILE.relative_to(VAULT_PATH)
    print(f"[OK] Recomendação gerada: {rel_path}")

    if recs:
        top3_names = [r['name'] for r in recs[:3]]
        print(f"[INFO] Top 3: {' | '.join(top3_names)}")
    else:
        print("[INFO] Nenhuma recomendacao gerada")
    print("[INFO] Para executar manualmente: python .scripts/study_recommender.py")


if __name__ == "__main__":
    main()
