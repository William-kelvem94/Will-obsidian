import hashlib
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[1]

def file_hash(p: Path):
    h = hashlib.sha1()
    with p.open("rb") as f:
        while True:
            b = f.read(8192)
            if not b:
                break
            h.update(b)
    return h.hexdigest()

def collect_md_files():
    return [p for p in ROOT.rglob("*.md") if p.is_file()]

def main():
    files = collect_md_files()
    mapping = {}
    for p in files:
        try:
            h = file_hash(p)
        except Exception:
            continue
        mapping.setdefault(h, []).append(str(p))

    duplicates = {h: paths for h, paths in mapping.items() if len(paths) > 1}
    out = ROOT / "dedupe_report.json"
    out.write_text(json.dumps({"duplicates": duplicates}, indent=2, ensure_ascii=False))
    print(f"Wrote dedupe report to {out} with {len(duplicates)} duplicate groups")

if __name__ == '__main__':
    main()
