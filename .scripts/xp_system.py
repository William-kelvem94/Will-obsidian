#!/usr/bin/env python3
"""
Sistema de XP e Niveis para Skills do Vault Obsidian (E1)

Calcula XP automaticamente para cada skill note baseado em:
  - Git commits tocando o arquivo da skill
  - Wiki-links da skill para projetos
  - Tamanho do conteudo (capped)
  - Backlinks (links de outros arquivos para a skill)
  - Tags no vault que referenciam a categoria da skill
  - Mencoes em notas diarias

Gera/atualiza skills/xp_leaderboard.md com ranking, distribuicao e level-ups.
State salvo em JSON para persistencia entre execucoes.
"""

import argparse
import json
import os
import re
import subprocess
import sys
from collections import defaultdict
from datetime import datetime
from pathlib import Path

# -- Paths -------------------------------------------------------------------

SCRIPT_ROOT = Path(__file__).parent.resolve()
VAULT_PATH = SCRIPT_ROOT.parent
SKILLS_DIR = VAULT_PATH / "skills"
DEFAULT_STATE_PATH = SCRIPT_ROOT / "xp_state.json"
LEADERBOARD_PATH = VAULT_PATH / "skills" / "xp_leaderboard.md"

# -- Thresholds de nivel (nivel -> XP minimo) --------------------------------

LEVEL_THRESHOLDS = [
    (10, 10000),
    (9, 7500),
    (8, 5000),
    (7, 3500),
    (6, 2000),
    (5, 1000),
    (4, 500),
    (3, 250),
    (2, 100),
    (1, 0),
]

LEVEL_NAMES = {
    1: "Iniciante",
    2: "Iniciante",
    3: "Intermediario",
    4: "Intermediario",
    5: "Avancado",
    6: "Avancado",
    7: "Especialista",
    8: "Especialista",
    9: "Mestre",
    10: "Mestre",
}

# -- Pesos de XP por fonte ---------------------------------------------------

XP_COMMITS = 10
XP_WIKI_LINK = 5
XP_CONTENT_PER_100 = 1
XP_CONTENT_CAP = 50
XP_BACKLINK = 3
XP_TAG = 2
XP_DAILY = 15

EXCLUDE_DIRS = {'.git', '.obsidian', '__pycache__', 'node_modules', '.scripts',
                '.agents', '.github', '.continue', '.logs'}


# ============================================================================
# Utilitarios
# ============================================================================


def to_posix(path: str) -> str:
    """Converte separadores do Windows para POSIX (para wiki-links)."""
    return path.replace('\\', '/')


def run_git(cmd: str, cwd: Path | None = None) -> str:
    """Executa comando git e retorna stdout."""
    try:
        result = subprocess.run(
            cmd, shell=True, cwd=cwd or VAULT_PATH,
            capture_output=True, text=True, encoding='utf-8',
            errors='replace',
        )
        return result.stdout.strip()
    except Exception:
        return ""


def run_git_lines(cmd: str, cwd: Path | None = None) -> list[str]:
    out = run_git(cmd, cwd)
    return [l for l in out.split('\n') if l] if out else []


# ============================================================================
# Parser de frontmatter YAML (stdlib, regex)
# ============================================================================


def parse_frontmatter(content: str) -> tuple[dict, int]:
    """Extrai frontmatter YAML de conteudo markdown.

    Retorna (dict, linha_onde_comeca_o_body).
    Retorna ({}, 0) se nao houver frontmatter valido.
    """
    if not content.startswith('---'):
        return {}, 0

    lines = content.split('\n')
    end = None
    for i in range(1, len(lines)):
        if lines[i].strip() == '---':
            end = i
            break

    if end is None or end == 1:
        return {}, 0

    fm_lines = lines[1:end]
    frontmatter = _parse_yaml_lines(fm_lines)
    return frontmatter, end + 1


def _parse_yaml_lines(lines: list[str]) -> dict:
    """Processa linhas simples de YAML em um dicionario."""
    data: dict = {}
    current_key: str | None = None
    current_list: list | None = None

    for line in lines:
        stripped = line.strip()
        if not stripped or stripped.startswith('#'):
            continue

        # Item de lista indentado sob a chave atual
        if stripped.startswith('- ') and current_key is not None \
                and current_list is not None:
            value = _unquote(stripped[2:].strip())
            current_list.append(value)
            continue

        # Par chave: valor
        match = re.match(r'^([\w-]+):\s*(.*)', line)
        if not match:
            continue

        current_key = match.group(1)
        value = match.group(2).strip()
        current_list = None

        if value == '' or value.startswith('#'):
            data[current_key] = []
            current_list = data[current_key]
        elif value.startswith('['):
            data[current_key] = _parse_inline_list(value)
        else:
            data[current_key] = _unquote(value)

    return data


def _parse_inline_list(value: str) -> list[str]:
    """Parseia lista inline YAML: [item1, item2, 'item3']"""
    inner = value.strip()
    if inner.endswith(']'):
        inner = inner[:-1]
    if inner.startswith('['):
        inner = inner[1:]

    items = []
    for raw in re.finditer(r"""'([^']*)'|"([^"]*)"|([^,\[\]'"]+)""", inner):
        g = raw.groups()
        item = g[0] or g[1] or g[2]
        item = item.strip()
        if item:
            items.append(item)
    return items


def _unquote(value: str) -> str:
    """Remove aspas simples/duplas ao redor do valor."""
    if len(value) >= 2:
        if (value[0] == '"' and value[-1] == '"') or \
           (value[0] == "'" and value[-1] == "'"):
            return value[1:-1]
    return value


# ============================================================================
# Descoberta e extracao de skills
# ============================================================================


SKILL_EXCLUDE = {'xp_leaderboard.md'}


def find_skill_files() -> list[tuple[Path, str]]:
    """Retorna (caminho_absoluto, caminho_relativo_posix) para cada .md."""
    files = []
    for fpath in sorted(SKILLS_DIR.rglob("*.md")):
        if fpath.name in SKILL_EXCLUDE:
            continue
        rel = fpath.relative_to(SKILLS_DIR)
        files.append((fpath, to_posix(str(rel))))
    return files


def get_skill_info(filepath: Path, rel_path: str) -> dict:
    """Extrai metadados e conteudo de um arquivo de skill."""
    raw = filepath.read_text(encoding='utf-8', errors='replace')
    fm, body_start = parse_frontmatter(raw)

    title = (
        fm.get('title')
        or filepath.stem.replace('-', ' ').replace('_', ' ').title()
    )

    raw_level = fm.get('level')
    if raw_level is None:
        raw_level = fm.get('nivel')
    initial_level = _level_to_int(raw_level)

    category = fm.get('category', '') or ''

    projects = fm.get('projects') or fm.get('projetos') or []
    if isinstance(projects, str):
        projects = [projects]

    tags = fm.get('tags') or []
    if isinstance(tags, str):
        tags = [tags]

    return {
        'filepath': filepath,
        'rel_path': rel_path,
        'title': title,
        'level': initial_level,
        'category': category,
        'projects': projects,
        'tags': tags,
        'raw_content': raw,
        'frontmatter': fm,
    }


def _level_to_int(raw) -> int:
    """Converte nivel (int ou string PT) para inteiro 1-10."""
    if raw is None:
        return 1
    if isinstance(raw, (int, float)):
        return max(1, min(10, int(raw)))
    if isinstance(raw, str):
        mapping = {
            'iniciante': 1,
            'basico': 1,
            'básico': 1,
            'intermediario': 2,
            'intermediário': 2,
            'avancado': 4,
            'avançado': 4,
        }
        return mapping.get(raw.strip().lower(), 1)
    return 1


# ============================================================================
# Fontes de XP
# ============================================================================


class VaultIndex:
    """Pre-scan do vault inteiro, caching conteudo e indices para consultas O(1)."""

    def __init__(self, vault_path: Path):
        self.vault_path = vault_path
        self.all_files: list[Path] = []
        self._contents: dict[Path, str] = {}
        self._daily_paths: set[Path] = set()

        # Indice invertido: stem_alvo -> [(arquivo_origem, qtd_ocorrencias)]
        self._backlink_index: dict[str, list[tuple[Path, int]]] = {}

        # Indice de tags: tag_lower -> set[arquivos]
        self._tag_index: dict[str, set[Path]] = {}

        self._build()

    def _build(self) -> None:
        EXCLUDE = {'.git', '.obsidian', '__pycache__', 'node_modules',
                   '.scripts', '.agents', '.github', '.continue', '.logs'}
        for fpath in self.vault_path.rglob("*.md"):
            parts = fpath.relative_to(self.vault_path).parts
            if any(p in EXCLUDE or p.startswith('.') for p in parts):
                continue
            self.all_files.append(fpath)

        # Ler todos os arquivos uma unica vez
        for f in self.all_files:
            try:
                text = f.read_text(encoding='utf-8', errors='replace')
            except Exception:
                text = ''
            self._contents[f] = text

            # Identificar notas diarias
            name = f.name
            if re.match(r'\d{4}-\d{2}-\d{2}', name):
                self._daily_paths.add(f)
            else:
                parent = f.parent.name.lower()
                if parent in ('diario', 'diario', 'logs', 'log', 'journal'):
                    self._daily_paths.add(f)

            # Extrair wiki-links para backlink index
            self._index_wikilinks(f, text)

            # Extrair tags para tag index
            self._index_tags(f, text)

    def _index_wikilinks(self, source: Path, content: str) -> None:
        for m in re.finditer(r'\[\[([^\]]+)\]\]', content):
            target = m.group(1)
            stem = target.split('|')[0].split('/')[-1].split('\\')[-1]
            if stem:
                self._backlink_index.setdefault(stem.lower(), []).append(source)

    def _index_tags(self, source: Path, content: str) -> None:
        for m in re.finditer(r'#([\w-]+)', content):
            tag = m.group(1).lower()
            self._tag_index.setdefault(tag, set()).add(source)

    def get_content(self, path: Path) -> str:
        return self._contents.get(path, '')

    def get_backlink_count(self, stem: str) -> int:
        return len(self._backlink_index.get(stem.lower(), []))

    def get_tag_file_count(self, tag: str) -> int:
        return len(self._tag_index.get(tag.lower(), set()))

    def get_daily_files(self) -> list[Path]:
        return list(self._daily_paths)


class XPEngine:
    """Calcula XP para uma skill, usando VaultIndex para consultas rapidas."""

    def __init__(self, index: VaultIndex):
        self.index = index

    def compute(self, info: dict) -> tuple[int, dict[str, int]]:
        parts: dict[str, int] = {}

        parts['commits'] = self._commits(info)
        parts['wiki_links'] = self._wiki_links(info)
        parts['content_size'] = self._content_size(info)
        parts['backlinks'] = self._backlinks(info)
        parts['tags'] = self._tags(info)
        parts['daily_mentions'] = self._daily_mentions(info)

        return sum(parts.values()), parts

    # -- 1. Commits git ------------------------------------------------------

    def _commits(self, info: dict) -> int:
        lines = run_git_lines(
            f'git log --all --oneline -- "{info["rel_path"]}"'
        )
        return len(lines) * XP_COMMITS

    # -- 2. Wiki-links para projetos ----------------------------------------

    def _wiki_links(self, info: dict) -> int:
        links = re.findall(r'\[\[([^\]]+)\]\]', info['raw_content'])
        return len(links) * XP_WIKI_LINK

    # -- 3. Tamanho do conteudo ---------------------------------------------

    def _content_size(self, info: dict) -> int:
        chars = len(info['raw_content'])
        xp = (chars // 100) * XP_CONTENT_PER_100
        return min(xp, XP_CONTENT_CAP)

    # -- 4. Backlinks --------------------------------------------------------

    def _backlinks(self, info: dict) -> int:
        stem = info['filepath'].stem
        count = self.index.get_backlink_count(stem)
        return count * XP_BACKLINK

    # -- 5. Tags que referenciam a categoria --------------------------------

    def _tags(self, info: dict) -> int:
        if not info['category']:
            return 0
        cat_lower = info['category'].strip().lower()
        count = self.index.get_tag_file_count(cat_lower)
        return count * XP_TAG

    # -- 6. Mencoes em notas diarias ----------------------------------------

    def _daily_mentions(self, info: dict) -> int:
        stem = info['filepath'].stem
        title_lower = info['title'].lower()
        count = 0
        for daily in self.index.get_daily_files():
            content = self.index.get_content(daily)
            if not content:
                continue
            has_link = bool(re.search(
                r'\[\[([^\]]*' + re.escape(stem) + r'[^\]]*)\]\]', content,
            ))
            has_mention = title_lower in content.lower()
            if has_link or has_mention:
                count += 1
        return count * XP_DAILY


# ============================================================================
# Calculo de nivel
# ============================================================================


def xp_to_level(xp: int) -> int:
    """Determina o nivel a partir do XP total."""
    for level, threshold in LEVEL_THRESHOLDS:
        if xp >= threshold:
            return level
    return 1


# ============================================================================
# Persistencia de estado
# ============================================================================


def load_state(path: Path) -> dict:
    if not path.exists():
        return {}
    try:
        return json.loads(path.read_text(encoding='utf-8'))
    except Exception:
        return {}


def save_state(path: Path, data: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(data, indent=2, ensure_ascii=False), encoding='utf-8',
    )


# ============================================================================
# Geracao do leaderboard
# ============================================================================


def _safe_wikilink(text: str) -> str:
    """Envolve texto em wiki-link, escapando pipe para tabelas markdown."""
    return text.replace('|', '/')


def _fmt_wiki(target: str, display: str) -> str:
    """Gera wiki-link seguro para tabelas markdown."""
    disp = display.replace('|', '-')
    return f'[[{target}|{disp}]]'


def generate_leaderboard(
    skills: list[dict],
    previous_state: dict,
    now_str: str,
) -> str:
    """Monta o markdown do leaderboard."""
    sorted_skills = sorted(skills, key=lambda s: (-s['xp'], s['title']))

    level_dist: dict[int, int] = defaultdict(int)
    total_xp = 0
    for s in sorted_skills:
        level_dist[s['level']] += 1
        total_xp += s['xp']

    # Level-ups
    prev_skills = previous_state.get('skills', {})
    leveled_up = []
    for s in sorted_skills:
        prev = prev_skills.get(s['rel_path'], {})
        prev_lv = prev.get('level', 1)
        if s['level'] > prev_lv:
            leveled_up.append(s)

    lines: list[str] = []
    _w = lines.append

    _w('---')
    _w('title: "Leaderboard de XP - Skills"')
    _w(f'generated: {now_str}')
    _w('tags: [skills, xp, leaderboard, auto]')
    _w('---')
    _w('')
    _w('# Leaderboard de XP - Skills')
    _w('')
    _w(f'*Gerado em: {now_str}*')
    _w('')
    _w('---')
    _w('')

    # -- Ranking -------------------------------------------------------------
    _w('## Ranking')
    _w('')
    _w('| # | Skill | Nivel | XP | Categoria | Projetos |')
    _w('|---|-------|-------|----|-----------|----------|')

    for i, s in enumerate(sorted_skills, 1):
        cat = s['category'] or '-'
        lv_name = LEVEL_NAMES.get(s['level'], f'Lv.{s["level"]}')
        proj_col = ', '.join(
            _fmt_wiki(p, p) for p in s['projects']
        ) if s['projects'] else '-'
        skill_link = _fmt_wiki(
            f'skills/{s["rel_path"]}', s['title']
        )
        _w(
            f"| {i} | {skill_link} | "
            f"{lv_name} (Lv.{s['level']}) | {s['xp']} | {cat} | {proj_col} |"
        )

    _w('')
    _w('---')
    _w('')

    # -- Distribuicao por nivel --------------------------------------------
    _w('## Distribuicao por Nivel')
    _w('')
    _w('| Nivel | Classificacao | Quantidade |')
    _w('|-------|---------------|------------|')
    for level, _ in sorted(LEVEL_THRESHOLDS, reverse=True):
        name = LEVEL_NAMES.get(level, f'Lv.{level}')
        qty = level_dist.get(level, 0)
        bar = '#' * min(qty, 20)
        _w(f'| Lv.{level} | {name} | {qty} {bar} |')

    _w('')
    _w('---')
    _w('')

    # -- Subiram de nivel ----------------------------------------------------
    _w('## Subiram de Nivel Recentemente')
    _w('')
    if leveled_up:
        _w('| Skill | Nivel Anterior | Novo Nivel | XP Total |')
        _w('|-------|----------------|------------|----------|')
        for s in leveled_up:
            prev = prev_skills.get(s['rel_path'], {})
            prev_lv = prev.get('level', 1)
            skill_link = _fmt_wiki(
                f'skills/{s["rel_path"]}', s['title']
            )
            _w(
                f"| {skill_link} | "
                f"Lv.{prev_lv} | **Lv.{s['level']}** | {s['xp']} |"
            )
    else:
        _w('*Nenhuma skill subiu de nivel desde a ultima execucao.*')

    _w('')
    _w('---')
    _w('')

    # -- Totais --------------------------------------------------------------
    _w('## Totais')
    _w('')
    _w(f'- **Total de Skills:** {len(sorted_skills)}')
    _w(f'- **XP Total (todas as skills):** {total_xp}')
    _w(f'- **XP Medio por Skill:** '
       f'{total_xp // len(sorted_skills) if sorted_skills else 0}')
    _w(f'- **Skills no nivel maximo (Lv.10 - Mestre):** '
       f'{level_dist.get(10, 0)}')

    _w('')
    return '\n'.join(lines)


# ============================================================================
# Main
# ============================================================================


def main() -> None:
    parser = argparse.ArgumentParser(
        description='Sistema de XP e Niveis para Skills do Obsidian',
    )
    parser.add_argument(
        '--dry-run', action='store_true',
        help='Preview sem escrever leaderboard nem estado',
    )
    parser.add_argument(
        '--force', action='store_true',
        help='Regenerar leaderboard mesmo sem mudancas',
    )
    parser.add_argument(
        '--save-state', type=str, default=str(DEFAULT_STATE_PATH),
        help=f'Caminho do arquivo de estado (default: {DEFAULT_STATE_PATH})',
    )
    args = parser.parse_args()

    state_path = Path(args.save_state)
    now_str = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    # Indexar vault (cache de conteudo + indices invertidos)
    index = VaultIndex(VAULT_PATH)

    # Descobrir skills
    skill_files = find_skill_files()
    engine = XPEngine(index)

    # Calcular XP para cada skill
    skills_data: list[dict] = []
    for fpath, rel in skill_files:
        info = get_skill_info(fpath, rel)
        xp, breakdown = engine.compute(info)
        level = xp_to_level(xp)
        skills_data.append({
            'rel_path': rel,
            'title': info['title'],
            'level': level,
            'xp': xp,
            'category': info['category'],
            'projects': info['projects'],
            'breakdown': breakdown,
        })

    # Estado anterior
    previous_state = load_state(state_path)
    prev_skills = previous_state.get('skills', {})

    # Detectar mudancas
    has_changes = False
    for s in skills_data:
        prev = prev_skills.get(s['rel_path'], {})
        if prev.get('xp') != s['xp'] or prev.get('level') != s['level']:
            has_changes = True
            break

    if not has_changes and len(prev_skills) != len(skills_data):
        has_changes = True

    # Salvar novo estado
    new_state = {
        'last_run': now_str,
        'skills': {
            s['rel_path']: {
                'title': s['title'],
                'xp': s['xp'],
                'level': s['level'],
            }
            for s in skills_data
        },
    }

    if not args.dry_run:
        save_state(state_path, new_state)

    # Gerar leaderboard
    leaderboard = generate_leaderboard(skills_data, previous_state, now_str)

    # -- Dry-run: so print --------------------------------------------------
    if args.dry_run:
        print("=== DRY RUN ===")
        print(f"Skills processadas: {len(skills_data)}")
        print(f"Arquivos .md no vault: {len(index.all_files)}")
        print(f"Mudancas detectadas: {has_changes}")
        print()
        print(leaderboard)
        return

    # -- Sem mudancas -------------------------------------------------------
    if not has_changes and not args.force:
        print("Nenhuma mudanca detectada. Use --force para regenerar.")
        total = sum(s['xp'] for s in skills_data)
        print(f"Skills: {len(skills_data)} | XP Total: {total}")
        return

    # -- Escrever leaderboard -----------------------------------------------
    LEADERBOARD_PATH.write_text(leaderboard, encoding='utf-8')
    total_xp = sum(s['xp'] for s in skills_data)
    print(f"Leaderboard atualizado: {LEADERBOARD_PATH}")
    print(f"Skills processadas: {len(skills_data)}")
    print(f"XP Total: {total_xp}")

    leveled = [
        s for s in skills_data
        if s['level'] > prev_skills.get(s['rel_path'], {}).get('level', 1)
    ]
    if leveled:
        print(f"Subiram de nivel: {len(leveled)}")
        for s in leveled[:10]:
            prev_lv = prev_skills.get(s['rel_path'], {}).get('level', 1)
            print(f"  + {s['title']}: Lv.{prev_lv} -> Lv.{s['level']}")


if __name__ == '__main__':
    main()
