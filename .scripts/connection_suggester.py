#!/usr/bin/env python3
"""
connection_suggester.py — Sugestor Automatico de Conexoes (B1)

Escaneia o vault Obsidian, calcula similaridade entre notas
e sugere [[wikilinks]] que ainda nao existem.

Uso:
    python connection_suggester.py
    python connection_suggester.py --method jaccard --min-score 0.4
    python connection_suggester.py --top-n 100 --output ~/sugestoes.md

Metodos:
    tfidf    TF-IDF + cosseno (sklearn se disponivel, senao Python puro)
    jaccard  Bag-of-words + Jaccard (stdlib apenas, sempre disponivel)
"""

import argparse
import logging
import math
import re
import sys
from collections import defaultdict
from datetime import datetime
from pathlib import Path

# ---------------------------------------------------------------------------
# Dependencias opcionais (requirements.txt / requirements-locked.txt)
# ---------------------------------------------------------------------------
try:
    import numpy as np

    HAS_NUMPY = True
except ImportError:
    HAS_NUMPY = False

try:
    from sklearn.feature_extraction.text import TfidfVectorizer as _Tfidf
    from sklearn.metrics.pairwise import cosine_similarity as _sk_cosine

    HAS_SKLEARN = True
except ImportError:
    HAS_SKLEARN = False

try:
    from tqdm import tqdm as _pbar

    HAS_TQDM = True
except ImportError:
    HAS_TQDM = False

# ---------------------------------------------------------------------------
# Configuracoes
# ---------------------------------------------------------------------------
VAULT_ROOT = Path(__file__).resolve().parent.parent
EXCLUDED_DIRS = frozenset(
    {
        ".git",
        ".obsidian",
        "__pycache__",
        "node_modules",
        ".knowledge_index",
        "tmp",
        ".scripts",
        ".github",
        ".agents",
        ".continue",
    }
)
MIN_NOTE_LENGTH = 100

log = logging.getLogger("sugestor")
_handler = logging.StreamHandler(sys.stdout)
_handler.setFormatter(logging.Formatter("%(message)s"))
log.addHandler(_handler)
log.setLevel(logging.INFO)


# ===================================================================
#  PARSING DE ARQUIVOS .md
# ===================================================================


def strip_frontmatter(text: str) -> str:
    """Remove frontmatter YAML (--- ... ---) do inicio do texto."""
    m = re.match(r"^---\s*\n.*?\n---\s*\n", text, re.DOTALL)
    return text[m.end() :] if m else text


def strip_markdown(text: str) -> str:
    """Remove formatacao markdown mantendo apenas o texto legivel."""
    # blocos de codigo
    text = re.sub(r"```[\s\S]*?```", "", text)
    # codigo inline
    text = re.sub(r"`[^`]+`", "", text)
    # imagens
    text = re.sub(r"!\[.*?\]\(.*?\)", "", text)
    # links markdown: [texto](url) -> texto
    text = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", text)
    # wikilinks com display: [[target|display]] -> display
    text = re.sub(r"\[\[[^\]|]+\|([^\]]+)\]\]", r"\1", text)
    # wikilinks simples: [[target]] -> target (preserva palavras)
    text = re.sub(r"\[\[([^\]]+)\]\]", r"\1", text)
    # tags HTML
    text = re.sub(r"<[^>]+>", "", text)
    # bold/italic/strikethrough
    text = re.sub(r"[*_~]{1,3}", "", text)
    # headers
    text = re.sub(r"^#{1,6}\s+", "", text, flags=re.MULTILINE)
    # marcadores de lista
    text = re.sub(r"^\s*[-*+]\s+", "", text, flags=re.MULTILINE)
    text = re.sub(r"^\s*\d+[.)]\s+", "", text, flags=re.MULTILINE)
    # linhas horizontais
    text = re.sub(r"^[-*_]{3,}\s*$", "", text, flags=re.MULTILINE)
    # pipes de tabela -> espaco
    text = re.sub(r"\|", " ", text)
    # whitespace multiplo
    text = re.sub(r"\s+", " ", text).strip()
    return text


def extract_wikilinks(text: str) -> set:
    """Extrai alvos de [[wikilink]] do texto."""
    return set(re.findall(r"\[\[([^\]|]+?)(?:\|[^\]]+)?\]\]", text))


def extract_frontmatter_field(text: str, field: str) -> str:
    """Extrai valor de um campo do frontmatter YAML via regex."""
    m = re.search(rf"^{re.escape(field)}:\s*(.+?)$", text, re.MULTILINE)
    return m.group(1).strip().strip("\"'") if m else ""


def tokenize(text: str) -> list[str]:
    """Tokeniza texto em palavras minusculas (acentos portugues)."""
    return re.findall(r"[a-záéíóúâêîôûãõçäëïöüñàèìòù\w]+", text.lower())


# ===================================================================
#  MOTORES DE SIMILARIDADE
# ===================================================================


class TfidfEngine:
    """TF-IDF + similaridade por cosseno (sklearn ou Python puro com vetores esparsos)."""

    MAX_FEATURES = 8000

    def __init__(self, notes: list[dict]):
        self.notes = notes

    def compute(self) -> list[tuple]:
        """Retorna lista [(i, j, score)] ordenada do mais similar para o menos."""
        corpus = [n["clean_text"] for n in self.notes]

        if HAS_SKLEARN:
            log.info("  Usando sklearn TfidfVectorizer...")
            vec = _Tfidf(
                max_features=self.MAX_FEATURES,
                stop_words=None,
                token_pattern=r"(?u)\b\w+\b",
                sublinear_tf=True,
            )
            matrix = vec.fit_transform(corpus)
            sim = _sk_cosine(matrix)
            return self._pairs_from_matrix(sim)

        log.info("  Usando TF-IDF puro com vetores esparsos (stdlib)...")
        return self._pure_tfidf(corpus)

    # ---------------------------------------------------------------
    #  TF-IDF puro com vetores esparsos {term_idx: tfidf_value}
    # ---------------------------------------------------------------

    def _pure_tfidf(self, corpus: list[str]) -> list[tuple]:
        tok = [tokenize(d) for d in corpus]
        N = len(tok)

        # --- vocabulario (limitado aos MAX_FEATURES termos mais frequentes) ---
        freq: dict[str, int] = {}
        for doc in tok:
            for t in doc:
                freq[t] = freq.get(t, 0) + 1

        top_terms = sorted(freq, key=freq.__getitem__, reverse=True)[
            : self.MAX_FEATURES
        ]
        vocab: dict[str, int] = {t: i for i, t in enumerate(top_terms)}
        V = len(vocab)
        log.debug(f"    Vocabulario: {V} termos (de {len(freq)} unicos)")

        # --- IDF para termos no vocabulario ---
        df = [0] * V
        for doc in tok:
            seen = set()
            for t in doc:
                if t in vocab and t not in seen:
                    seen.add(t)
                    df[vocab[t]] += 1
        idf = [math.log((N + 1) / (d + 1)) + 1.0 for d in df]

        # --- vetores TF-IDF esparsos: {term_idx: tfidf_value} ---
        sparse_vecs: list[dict[int, float]] = []
        for doc in tok:
            tf: dict[str, int] = {}
            for t in doc:
                if t in vocab:
                    tf[t] = tf.get(t, 0) + 1
            denom = len(doc) or 1
            sv = {}
            for t, f in tf.items():
                sv[vocab[t]] = (f / denom) * idf[vocab[t]]
            sparse_vecs.append(sv)

        # --- pre-computar normas ---
        norms = [
            math.sqrt(sum(v * v for v in sv.values())) for sv in sparse_vecs
        ]

        # --- similaridade par a par (apenas interseccao de termos) ---
        pairs = []
        n = len(sparse_vecs)
        for i in range(n):
            si = sparse_vecs[i]
            ni = norms[i]
            for j in range(i + 1, n):
                dot = 0.0
                # itera sobre o menor vetor
                smaller, larger = (si, sparse_vecs[j]) if len(si) <= len(
                    sparse_vecs[j]
                ) else (sparse_vecs[j], si)
                for term, val in smaller.items():
                    if term in larger:
                        dot += val * larger[term]
                nj = norms[j]
                s = dot / (ni * nj) if ni * nj > 0 else 0.0
                if s > 0:
                    pairs.append((i, j, s))

        pairs.sort(key=lambda x: -x[2])
        return pairs

    # ---------------------------------------------------------------
    #  sklearn helper
    # ---------------------------------------------------------------

    def _pairs_from_matrix(self, matrix) -> list[tuple]:
        n = len(self.notes)
        pairs = []
        for i in range(n):
            for j in range(i + 1, n):
                s = float(matrix[i][j])
                if s > 0:
                    pairs.append((i, j, s))
        pairs.sort(key=lambda x: -x[2])
        return pairs


class JaccardEngine:
    """Bag-of-words + similaridade Jaccard (stdlib apenas)."""

    def __init__(self, notes: list[dict]):
        self.notes = notes

    def compute(self) -> list[tuple]:
        tok = [set(tokenize(n["clean_text"])) for n in self.notes]
        pairs = []
        n = len(tok)
        iterator = range(n)
        if HAS_TQDM:
            iterator = _pbar(iterator, desc="  Jaccard", unit="doc")
        for i in iterator:
            for j in range(i + 1, n):
                s = _jaccard(tok[i], tok[j])
                if s > 0:
                    pairs.append((i, j, s))
        pairs.sort(key=lambda x: -x[2])
        return pairs


def _jaccard(a: set, b: set) -> float:
    if not a or not b:
        return 0.0
    return len(a & b) / len(a | b)


# ===================================================================
#  SUGESTOR
# ===================================================================


class Sugestor:
    """Orquestrador: scan -> similaridade -> filtro -> relatorio."""

    def __init__(
        self,
        vault_root: Path = VAULT_ROOT,
        method: str = "tfidf",
        min_score: float = 0.3,
        top_n: int = 50,
    ):
        self.vault_root = Path(vault_root)
        self.method = method
        self.min_score = min_score
        self.top_n = top_n
        self.notes: list[dict] = []
        self.suggestions: list[tuple] = []
        self.total_pairs = 0
        self.total_existing_links = 0

    # ---------------------------------------------------------------
    #  Scan
    # ---------------------------------------------------------------

    def scan(self) -> list[dict]:
        """Escaneia o vault e retorna lista de notas processadas."""
        md_files = sorted(self.vault_root.rglob("*.md"))
        notes = []

        for fpath in md_files:
            if self._is_excluded(fpath):
                continue
            note = self._process_file(fpath)
            if note is not None:
                notes.append(note)

        log.info(f"  Notas analisadas: {len(notes)}")
        self.notes = notes
        return notes

    # ---------------------------------------------------------------
    #  Similaridade
    # ---------------------------------------------------------------

    def run(self):
        """Executa pipeline completa."""
        log.info("Escaneando vault...")
        self.scan()
        log.info("")

        log.info(f"Calculando similaridade (metodo: {self.method})...")
        if self.method == "jaccard":
            engine = JaccardEngine(self.notes)
        else:
            engine = TfidfEngine(self.notes)
        all_pairs = engine.compute()

        self.total_pairs = len(all_pairs)
        log.info(f"  Pares computados: {self.total_pairs}")

        # --- contar links existentes ---
        self._count_existing_links()
        log.info(f"  Links existentes: {self.total_existing_links}")

        # --- filtrar pares ja conectados e com score minimo ---
        suggestions = self._filter_pairs(all_pairs)
        log.info(f"  Sugestoes (>={self.min_score}): {len(suggestions)}")
        self.suggestions = suggestions[: self.top_n]
        return self.suggestions

    # ---------------------------------------------------------------
    #  Relatorio
    # ---------------------------------------------------------------

    def report(self, output_path: Path) -> str:
        """Gera relatorio markdown com wikilinks clicaveis."""
        now = datetime.now().strftime("%Y-%m-%d %H:%M")
        method_label = {
            "tfidf": "TF-IDF + Cosseno",
            "jaccard": "Jaccard (Bag-of-Words)",
        }.get(self.method, self.method)

        lines = [
            "# Sugestoes de Conexoes — Obsidian Vault",
            "",
            f"Gerado em: {now}",
            f"Metodo: {method_label}",
            f"Limiar minimo: {self.min_score}",
            f"Total de notas analisadas: {len(self.notes)}",
            f"Total de pares comparados: {self.total_pairs}",
            f"Links existentes: {self.total_existing_links}",
            f"Sugestoes encontradas (≥{self.min_score}): {len(self.suggestions)}",
            "",
            "---",
            "",
            f"## Top {len(self.suggestions)} Sugestoes",
            "",
            "| # | Nota A | Nota B | Score | Direcao |",
            "|---|--------|--------|-------|---------|",
        ]

        for rank, (i, j, score) in enumerate(self.suggestions, 1):
            a_path = self.notes[i]["path"]
            b_path = self.notes[j]["path"]
            if a_path.endswith(".md"):
                a_path = a_path[:-3]
            if b_path.endswith(".md"):
                b_path = b_path[:-3]
            a_title = self.notes[i]["title"]
            b_title = self.notes[j]["title"]
            lines.append(
                f"| {rank} | [[{a_path}|{a_title}]] | [[{b_path}|{b_title}]] | "
                f"{score:.4f} | ↔ |"
            )

        # --- orfaos com alta similaridade ---
        lines.extend(self._orphan_section())
        lines.append("")
        lines.append("---")
        lines.append("")
        lines.extend(self._stats_section())

        content = "\n".join(lines) + "\n"
        output_path.write_text(content, encoding="utf-8")
        log.info(f"\nRelatorio salvo em: {output_path}")
        return content

    # ---------------------------------------------------------------
    #  Internos
    # ---------------------------------------------------------------

    @staticmethod
    def _is_excluded(path: Path) -> bool:
        try:
            rel = path.relative_to(VAULT_ROOT)
            return any(part in EXCLUDED_DIRS for part in rel.parts)
        except ValueError:
            return True

    def _process_file(self, fpath: Path) -> dict | None:
        try:
            raw = fpath.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            try:
                raw = fpath.read_text(encoding="latin-1")
            except Exception:
                return None
        except Exception:
            return None

        rel = str(fpath.relative_to(self.vault_root)).replace("\\", "/")
        title = extract_frontmatter_field(raw, "title") or fpath.stem
        body = strip_frontmatter(raw)
        clean = strip_markdown(body)

        if len(clean) < MIN_NOTE_LENGTH:
            return None

        return {
            "path": rel,
            "title": title,
            "clean_text": clean,
            "existing_links": extract_wikilinks(raw),
            "stem": fpath.stem,
        }

    def _count_existing_links(self):
        """Conta quantos pares de notas ja tem pelo menos um wikilink."""
        # para cada nota, criamos um mapa de stem -> indice para consulta rapida
        id_map: dict[str, int] = {}
        for idx, n in enumerate(self.notes):
            id_map[n["stem"]] = idx
            p = n["path"]
            if p.endswith(".md"):
                p = p[:-3]
            id_map[p] = idx

        connected = set()
        for i, a in enumerate(self.notes):
            for link in a["existing_links"]:
                if link in id_map:
                    j = id_map[link]
                    if i != j:
                        connected.add((min(i, j), max(i, j)))

        self.total_existing_links = len(connected)

    def _filter_pairs(self, all_pairs: list[tuple]) -> list[tuple]:
        """Remove pares que ja estao conectados e abaixo do score minimo."""
        # pre-computar mapa de conectados
        conn: set[tuple[int, int]] = set()
        id_map: dict[str, int] = {}
        for idx, n in enumerate(self.notes):
            id_map[n["stem"]] = idx
            p = n["path"]
            if p.endswith(".md"):
                p = p[:-3]
            id_map[p] = idx

        for i, a in enumerate(self.notes):
            for link in a["existing_links"]:
                if link in id_map:
                    j = id_map[link]
                    if i != j:
                        conn.add((min(i, j), max(i, j)))

        filtered = []
        for i, j, score in all_pairs:
            if score < self.min_score:
                continue
            if (i, j) in conn:
                continue
            filtered.append((i, j, score))

        return filtered

    def _orphan_section(self) -> list[str]:
        """Notas orfas (zero links recebidos) com similaridade alta."""
        # computar links recebidos
        id_map: dict[str, int] = {}
        for idx, n in enumerate(self.notes):
            id_map[n["stem"]] = idx
            p = n["path"]
            if p.endswith(".md"):
                p = p[:-3]
            id_map[p] = idx

        incoming: defaultdict[int, set[int]] = defaultdict(set)
        for i, a in enumerate(self.notes):
            for link in a["existing_links"]:
                if link in id_map:
                    j = id_map[link]
                    if i != j:
                        incoming[j].add(i)

        orphans = [i for i in range(len(self.notes)) if i not in incoming]
        if not orphans:
            return ["", "---", "", "### Notas Orfas", "", "Nenhuma nota orfa encontrada."]

        # das sugestoes, quais envolvem orfaos?
        orphan_suggestions = []
        for i, j, score in self.suggestions:
            if i in orphans or j in orphans:
                orphan_suggestions.append((i, j, score))

        lines = ["", "---", "", "### Notas Orfas com Alta Similaridade", ""]
        if not orphan_suggestions:
            lines.append(
                f"*{len(orphans)} notas orfas encontradas, mas nenhuma aparece "
                "no topo das sugestoes.*"
            )
            return lines

        lines.append(
            "| # | Nota Orfa | Par Similar | Score | Direcao |"
        )
        lines.append("|---|-----------|-------------|-------|---------|")
        for rank, (i, j, score) in enumerate(orphan_suggestions[:15], 1):
            orphan_idx = i if i in orphans else j
            other_idx = j if i in orphans else i
            o_path = self.notes[orphan_idx]["path"]
            p_path = self.notes[other_idx]["path"]
            if o_path.endswith(".md"):
                o_path = o_path[:-3]
            if p_path.endswith(".md"):
                p_path = p_path[:-3]
            o_title = self.notes[orphan_idx]["title"]
            p_title = self.notes[other_idx]["title"]
            lines.append(
                f"| {rank} | [[{o_path}|{o_title}]] | [[{p_path}|{p_title}]] | "
                f"{score:.4f} | ← receber link |"
            )

        return lines

    def _stats_section(self) -> list[str]:
        """Estatisticas do vault."""
        lines = [
            "## Estatisticas",
            "",
            f"- **Total de notas .md**: {len(self.notes)}",
            f"- **Pares comparados**: {self.total_pairs}",
            f"- **Links existentes**: {self.total_existing_links}",
            f"- **Sugestoes (≥{self.min_score})**: {len(self.suggestions)}",
            f"- **Metodo**: {self.method}",
            f"- **Limiar minimo**: {self.min_score}",
            "",
        ]

        # distribuir scores das sugestoes
        if self.suggestions:
            scores = [s[2] for s in self.suggestions]
            avg = sum(scores) / len(scores)
            lines.append(f"- **Score medio das sugestoes**: {avg:.4f}")
            lines.append(f"- **Maior score**: {max(scores):.4f}")
            lines.append(f"- **Menor score**: {min(scores):.4f}")
            lines.append("")

        # top 5 notas mais conectadas
        id_map: dict[str, int] = {}
        for idx, n in enumerate(self.notes):
            id_map[n["stem"]] = idx
            p = n["path"]
            if p.endswith(".md"):
                p = p[:-3]
            id_map[p] = idx

        degree = [0] * len(self.notes)
        for i, a in enumerate(self.notes):
            for link in a["existing_links"]:
                if link in id_map:
                    degree[i] += 1

        top5 = sorted(
            enumerate(degree), key=lambda x: -x[1]
        )[:5]
        lines.append("### Top 5 Notas Mais Conectadas")
        lines.append("")
        lines.append("| # | Nota | Links |")
        lines.append("|---|------|-------|")
        for rank, (idx, deg) in enumerate(top5, 1):
            p = self.notes[idx]["path"]
            if p.endswith(".md"):
                p = p[:-3]
            t = self.notes[idx]["title"]
            lines.append(f"| {rank} | [[{p}|{t}]] | {deg} |")

        return lines


# ===================================================================
#  CLI
# ===================================================================


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        description="Sugestor Automatico de Conexoes para Obsidian",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Exemplos:
  python connection_suggester.py
  python connection_suggester.py --method jaccard --min-score 0.4
  python connection_suggester.py --top-n 100 --output ~/sugestoes.md
  python connection_suggester.py --method tfidf --min-score 0.25 --top-n 30
        """,
    )
    p.add_argument(
        "--vault",
        default=str(VAULT_ROOT),
        help=f"Caminho do vault Obsidian (default: {VAULT_ROOT})",
    )
    p.add_argument(
        "--method",
        choices=["tfidf", "jaccard"],
        default="tfidf",
        help="Metodo de similaridade (default: tfidf)",
    )
    p.add_argument(
        "--min-score",
        type=float,
        default=0.3,
        help="Score minimo de similaridade (default: 0.3)",
    )
    p.add_argument(
        "--top-n",
        type=int,
        default=50,
        help="Numero de sugestoes no relatorio (default: 50)",
    )
    p.add_argument(
        "--output",
        type=str,
        default=str(VAULT_ROOT / "conexoes_sugeridas.md"),
        help="Caminho do relatorio de saida (default: conexoes_sugeridas.md na raiz do vault)",
    )
    p.add_argument(
        "--verbose",
        action="store_true",
        help="Log detalhado (debug)",
    )
    return p


def main():
    parser = build_parser()
    args = parser.parse_args()

    if args.verbose:
        log.setLevel(logging.DEBUG)

    vault = Path(args.vault).resolve()
    if not vault.is_dir():
        log.error(f"Vault nao encontrado: {vault}")
        sys.exit(1)

    if args.method == "tfidf" and not HAS_SKLEARN:
        log.info(
            "sklearn nao disponivel. Usando implementacao TF-IDF pura (stdlib)."
        )

    sugestor = Sugestor(
        vault_root=vault,
        method=args.method,
        min_score=args.min_score,
        top_n=args.top_n,
    )

    sugestor.run()
    sugestor.report(Path(args.output))


if __name__ == "__main__":
    main()
