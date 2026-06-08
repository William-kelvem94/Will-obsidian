#!/usr/bin/env python3
"""
Recomenda prioridades de estudo a partir dos gaps de conhecimento
(GAPS.md) e da taxonomia de skills do vault. Pode ser usado com
--mock para simular recomendações mesmo se nenhum gap real for detectado.

Uso:
    python scripts/gap_recommender.py [--mock]
"""
import argparse
from pathlib import Path
import re
import sys

VAULT = Path(__file__).parent.parent
GAPS_PATH = VAULT / "GAPS.md"
SKILLS_CATEGORIES = VAULT / "skills" / "01-agentic-intelligence" / "skills-categories.md"
SKILLS_README = VAULT / "skills" / "README.md"

def parse_gaps(gaps_path):
    content = gaps_path.read_text(encoding="utf-8")
    match = re.search(r"## Skills/Áreas sem nota dedicada.*?(?=##|\Z)([\s\S]*)", content, re.MULTILINE)
    if not match:
        return []
    lines = [l.strip("*- ") for l in match.group(1).splitlines() if l.strip() and not l.startswith("Nenhum gap")] 
    return [l for l in lines if l]

def extract_categories(categories_path):
    cats = []
    current = None
    lines = categories_path.read_text(encoding="utf-8").splitlines()
    for l in lines:
        if l.strip().startswith("### "):
            current = l.replace("### ", "").strip()
            cats.append({'category': current, 'examples': []})
        if l.strip().startswith("**Exemplos de uso**"):
            exs = []
        if l.strip().startswith("-") and cats:
            cats[-1]['examples'].append(l.strip("- "))
    return cats

def mock_gaps():
    return [
        "Desenvolvimento Fullstack",
        "Automacao e Produtividade",
        "Prompt Engineering",
    ]

def recommend_study_areas(gaps, category_info):
    if not gaps:
        return [
            {"area": "Parabéns! Nenhum gap detectado.",
             "recomendacao": "Acompanhe as skills avançadas, atualize exemplos e contribua com relatos práticos."}
        ]
    out = []
    for gap in gaps:
        cat = next((c for c in category_info if gap.lower() in c['category'].lower()), None)
        exemplos = cat['examples'] if cat and cat['examples'] else ["Sugere-se adicionar exemplos práticos."]
        out.append({
            "area": gap,
            "recomendacao": f"Priorize estudo em: {gap}.",
            "exemplos": exemplos
        })
    return out

def main():
    parser = argparse.ArgumentParser(description="Recomenda estudo baseado em gaps/skills do vault.")
    parser.add_argument('--mock', action='store_true', help='Outputa recomendações simuladas (não lê GAPS.md real).')
    args = parser.parse_args()

    if args.mock:
        gaps = mock_gaps()
    else:
        if not GAPS_PATH.exists():
            print("[WARN] GAPS.md não encontrado. Use --mock para simular.")
            sys.exit(0)
        gaps = parse_gaps(GAPS_PATH)

    if not SKILLS_CATEGORIES.exists():
        print("[WARN] skills-categories.md não encontrado. Recomendações serão genéricas.")
        cats = []
    else:
        cats = extract_categories(SKILLS_CATEGORIES)

    recs = recommend_study_areas(gaps, cats)
    for rec in recs:
        print(f"\n=== {rec['area']} ===")
        print(f"→ {rec['recomendacao']}")
        if rec.get('exemplos'):
            print(" Exemplos de uso:")
            for ex in rec['exemplos']:
                print(f"  - {ex}")

if __name__ == "__main__":
    main()
