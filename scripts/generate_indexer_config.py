import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

config = {
    "allowlist": [
        "skills/**",
        "Conhecimento-Geral/**",
        "JARVIS/**",
        "Master-Glossary.md",
        "Vault-*",
    ],
    "denylist": [
        ".obsidian/**",
        ".agents/**",
        ".continue/**",
        ".logs/**",
        "Templates/**",
        "Projetos/Privados/**",
        "**/*template*.md",
        "**/*TODO*.md",
        "tests/fixtures/**",
        "**/*.png",
        "**/*.jpg",
        "**/*.jpeg",
        "**/*.pdf",
    ],
    "notes": {
        "chunk_size_tokens": 700,
        "chunk_overlap": 0.15
    }
}

out = ROOT / "indexer_config.json"
out.write_text(json.dumps(config, indent=2, ensure_ascii=False))
print(f"Wrote indexer config to {out}")
