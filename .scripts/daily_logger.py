#!/usr/bin/env python3
"""
Daily Logger - Automatic activity snapshot generator
Captures git activity, file changes, and generates a daily log.
"""

import os
import subprocess
import json
from datetime import datetime, timedelta
from pathlib import Path
import re

# Configuration
SCRIPT_ROOT = Path(__file__).parent
VAULT_PATH = SCRIPT_ROOT.parent
LOGS_DIR = VAULT_PATH / "JARVIS" / "03-Memory" / "Logs"
OUTPUT_FILE = LOGS_DIR / f"{datetime.now().strftime('%Y-%m-%d')}.md"


def run_command(cmd, cwd=None):
    """Run shell command and return output"""
    try:
        result = subprocess.run(
            cmd,
            shell=True,
            cwd=cwd or VAULT_PATH,
            capture_output=True,
            text=True,
            encoding='utf-8'
        )
        return result.stdout.strip()
    except Exception as e:
        print(f"Error running command '{cmd}': {e}")
        return ""


def get_git_commits_today():
    """Get all git commits from today"""
    today = datetime.now().strftime("%Y-%m-%d")
    cmd = f'git log --since="{today} 00:00" --pretty=format:"%h|%s|%an|%ar" --all'
    output = run_command(cmd)
    
    commits = []
    if output:
        for line in output.split('\n'):
            if line:
                parts = line.split('|')
                if len(parts) == 4:
                    commits.append({
                        'hash': parts[0],
                        'message': parts[1],
                        'author': parts[2],
                        'time': parts[3]
                    })
    return commits


def get_files_modified_today():
    """Get files modified today"""
    today = datetime.now().strftime("%Y-%m-%d")
    cmd = f'git log --since="{today} 00:00" --name-only --pretty=format: --all'
    output = run_command(cmd)
    
    if not output:
        return []
    
    files = set()
    for line in output.split('\n'):
        if line.strip() and not line.startswith(' '):
            files.add(line.strip())
    
    return sorted(files)


def get_git_stats_today():
    """Get git statistics for today"""
    today = datetime.now().strftime("%Y-%m-%d")
    cmd = f'git log --since="{today} 00:00" --shortstat --all'
    output = run_command(cmd)
    
    total_files = 0
    total_insertions = 0
    total_deletions = 0
    
    # Parse output like: "2 files changed, 10 insertions(+), 3 deletions(-)"
    for line in output.split('\n'):
        if 'changed' in line:
            files_match = re.search(r'(\d+) files? changed', line)
            ins_match = re.search(r'(\d+) insertions?', line)
            del_match = re.search(r'(\d+) deletions?', line)
            
            if files_match:
                total_files += int(files_match.group(1))
            if ins_match:
                total_insertions += int(ins_match.group(1))
            if del_match:
                total_deletions += int(del_match.group(1))
    
    return {
        'files': total_files,
        'insertions': total_insertions,
        'deletions': total_deletions
    }


def get_recent_md_files(hours=24):
    """Get markdown files modified in the last N hours"""
    cutoff_time = datetime.now() - timedelta(hours=hours)
    recent_files = []
    
    for md_file in VAULT_PATH.rglob("*.md"):
        if md_file.is_file():
            mtime = datetime.fromtimestamp(md_file.stat().st_mtime)
            if mtime > cutoff_time:
                rel_path = md_file.relative_to(VAULT_PATH)
                recent_files.append({
                    'path': str(rel_path),
                    'modified': mtime.strftime("%H:%M")
                })
    
    # Sort by modification time (most recent first)
    recent_files.sort(key=lambda x: x['modified'], reverse=True)
    return recent_files[:20]  # Top 20


def count_md_files():
    """Count total markdown files in vault"""
    return sum(1 for _ in VAULT_PATH.rglob("*.md"))


def detect_active_projects(commits, files):
    """Detect which projects were worked on today"""
    projects = {}
    
    # Check commits for project mentions
    for commit in commits:
        msg = commit['message'].lower()
        
        # Check for project folders in files
        for file in files:
            parts = file.split('/')
            if len(parts) >= 2:
                if parts[0] == 'Projetos' and len(parts) >= 3:
                    project = parts[2] if parts[1] in ['01-Ativos', 'Privados'] else parts[1]
                    projects[project] = projects.get(project, 0) + 1
                elif parts[0] == 'JARVIS':
                    projects['JARVIS'] = projects.get('JARVIS', 0) + 1
                elif parts[0] == 'skills':
                    projects['Skills'] = projects.get('Skills', 0) + 1
    
    # Sort by activity
    return sorted(projects.items(), key=lambda x: x[1], reverse=True)


def generate_daily_log():
    """Generate the daily log markdown"""
    now = datetime.now()
    date_str = now.strftime("%Y-%m-%d")
    day_name = now.strftime("%A")
    
    # Gather data
    commits = get_git_commits_today()
    files = get_files_modified_today()
    stats = get_git_stats_today()
    recent_md = get_recent_md_files()
    total_md = count_md_files()
    active_projects = detect_active_projects(commits, files)
    
    # Build markdown
    md = f"""---
title: "Daily Log — {date_str}"
description: "Automatic activity snapshot for {day_name}, {date_str}"
tags: [log, daily, memory, auto-generated]
generated: {now.strftime("%Y-%m-%d %H:%M:%S")}
---

# 📅 Daily Log — {date_str} ({day_name})

**Generated:** {now.strftime("%H:%M:%S")}

---

## 📊 Summary

"""
    
    # Statistics
    md += f"""| Metric | Value |
|--------|-------|
| **Git Commits** | {len(commits)} |
| **Files Changed** | {stats['files']} |
| **Lines Added** | +{stats['insertions']} |
| **Lines Removed** | -{stats['deletions']} |
| **Net Change** | {stats['insertions'] - stats['deletions']:+d} |
| **Vault Files** | {total_md} markdown files |
| **Modified Today** | {len(recent_md)} files |

"""
    
    # Active Projects
    if active_projects:
        md += "### 🎯 Active Projects\n\n"
        for project, count in active_projects[:5]:
            md += f"- **{project}** ({count} files)\n"
        md += "\n"
    
    # Git Commits
    if commits:
        md += f"""---

## 📝 Git Activity ({len(commits)} commits)

"""
        for commit in commits:
            md += f"### `{commit['hash']}` — {commit['time']}\n"
            md += f"**{commit['message']}**\n\n"
    else:
        md += """---

## 📝 Git Activity

*No commits today yet*

"""
    
    # Files Changed
    if files:
        md += f"""---

## 📂 Files Changed ({len(files)} files)

"""
        # Group by folder
        grouped = {}
        for file in files:
            folder = file.split('/')[0] if '/' in file else 'Root'
            if folder not in grouped:
                grouped[folder] = []
            grouped[folder].append(file)
        
        for folder, folder_files in sorted(grouped.items()):
            md += f"\n### {folder}/\n"
            for file in folder_files[:10]:  # Limit to 10 per folder
                md += f"- `{file}`\n"
            if len(folder_files) > 10:
                md += f"- *...and {len(folder_files) - 10} more*\n"
    
    # Recent Vault Activity
    if recent_md:
        md += f"""

---

## 🔄 Recent Vault Activity (Last 24h)

"""
        for file_info in recent_md[:15]:
            md += f"- **{file_info['modified']}** — [{file_info['path']}]({file_info['path']})\n"
    
    # Footer
    md += f"""

---

## 🔗 Related

- [[JARVIS/02-Operational/Dashboard|Dashboard]] — Current operational state
- [[JARVIS/02-Operational/Context/Estado|Context]] — What I'm focused on
- [[02-JARVIS/03-Memory/Logs/INDEX|Log Index]] — All daily logs

---

*This log was automatically generated by `.scripts/daily_logger.py`*
*To regenerate, run: `python .scripts/daily_logger.py`*
"""
    
    return md


def main():
    """Main execution"""
    print("🔍 Generating daily log...")
    
    # Ensure logs directory exists
    LOGS_DIR.mkdir(parents=True, exist_ok=True)
    
    # Generate log
    log_content = generate_daily_log()
    
    # Write to file
    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        f.write(log_content)
    
    print(f"✅ Daily log generated: {OUTPUT_FILE.relative_to(VAULT_PATH)}")
    print(f"📊 Run this script daily or add to cron/Task Scheduler")


if __name__ == "__main__":
    main()
