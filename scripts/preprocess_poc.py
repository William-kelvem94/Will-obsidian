import re
from pathlib import Path
import json
from yaml import safe_load

ROOT = Path(__file__).resolve().parents[1]

def extract_frontmatter(text):
    if text.lstrip().startswith("---"):
        parts = text.split("---", 2)
        if len(parts) >= 3:
            try:
                return safe_load(parts[1]), parts[2].lstrip()
            except Exception:
                return None, text
    return None, text

def strip_inline_base64(text):
    # remove data:image/...base64, replace with [inline_image]
    return re.sub(r"data:image/[^;]+;base64,[A-Za-z0-9+/=\\n\\r]+", "[inline_image]", text)

def chunk_by_headings(text, max_chars=3500):
    # naive heading-based splitter: split by H1/H2 (lines starting with #)
    lines = text.splitlines()
    chunks = []
    current = []
    for line in lines:
        if line.startswith('#') and current:
            chunks.append('\n'.join(current))
            current = [line]
        else:
            current.append(line)
    if current:
        chunks.append('\n'.join(current))

    # if chunks too large, split by char
    out = []
    for c in chunks:
        if len(c) <= max_chars:
            out.append(c)
        else:
            for i in range(0, len(c), max_chars):
                out.append(c[i:i+max_chars])
    return out

def process_file(p: Path):
    try:
        text = p.read_text(encoding='utf-8')
    except UnicodeDecodeError:
        text = p.read_text(encoding='latin-1', errors='replace')
    fm, body = extract_frontmatter(text)
    body = strip_inline_base64(body)
    chunks = chunk_by_headings(body)
    out_chunks = []
    for i, c in enumerate(chunks):
        fm_clean = {}
        if fm:
            for k, v in (fm.items() if isinstance(fm, dict) else []):
                # convert dates and non-serializable types to str
                try:
                    json.dumps({k: v})
                    fm_clean[k] = v
                except Exception:
                    fm_clean[k] = str(v)
        out_chunks.append({
            'source_path': str(p),
            'chunk_id': f"{p.name}::{i}",
            'text': c[:10000],
            'frontmatter': fm_clean
        })
    return out_chunks

def main():
    # pick 5 largest markdown files as POC
    md = [p for p in ROOT.rglob('*.md') if p.is_file()]
    md_sorted = sorted(md, key=lambda p: p.stat().st_size, reverse=True)
    poc = md_sorted[:5]
    results = []
    for p in poc:
        print(f"Processing {p} size={p.stat().st_size}")
        results.extend(process_file(p))

    out = ROOT / 'preprocess_poc.jsonl'
    with out.open('w', encoding='utf-8') as f:
        for r in results:
            f.write(json.dumps(r, ensure_ascii=False) + '\n')
    print(f"Wrote {len(results)} chunks to {out}")

if __name__ == '__main__':
    main()

