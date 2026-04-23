#!/usr/bin/env python3
"""
Project Health Checker - Analyzes project quality and completeness
Generates health score and actionable recommendations.
"""

import os
import json
from pathlib import Path
from datetime import datetime
import re

# Configuration
SCRIPT_ROOT = Path(__file__).parent
VAULT_PATH = SCRIPT_ROOT.parent
PROJECTS_DIR = VAULT_PATH / "Projetos" / "01-Ativos" / "Privados"
OUTPUT_FILE = VAULT_PATH / "JARVIS" / "02-Operational" / "Project-Health-Report.md"


class ProjectHealthChecker:
    def __init__(self, project_path):
        self.project_path = Path(project_path)
        self.name = self.project_path.name
        self.score = 0
        self.max_score = 0
        self.checks = []
        
    def check_readme(self):
        """Check for README.md existence and quality"""
        readme = self.project_path / "README.md"
        
        if not readme.exists():
            self.add_check("README", 0, 10, "❌ Missing README.md")
            return
        
        content = readme.read_text(encoding='utf-8', errors='ignore')
        score = 2  # Base score for existence
        
        # Check for key sections
        if re.search(r'#+.*Install', content, re.I):
            score += 2
        if re.search(r'#+.*Usage', content, re.I):
            score += 2
        if re.search(r'#+.*Features', content, re.I):
            score += 1
        if re.search(r'```', content):  # Code blocks
            score += 2
        if len(content) > 500:  # Substantial content
            score += 1
        
        status = "✅" if score >= 7 else "⚠️" if score >= 4 else "❌"
        self.add_check("README", score, 10, f"{status} README quality: {score}/10")
    
    def check_dependencies(self):
        """Check for dependency files"""
        dep_files = {
            "requirements.txt": "Python",
            "package.json": "Node.js",
            "Gemfile": "Ruby",
            "go.mod": "Go",
            "Cargo.toml": "Rust"
        }
        
        found = []
        for dep_file, lang in dep_files.items():
            if (self.project_path / dep_file).exists():
                found.append(lang)
        
        if found:
            score = 5
            langs = ", ".join(found)
            self.add_check("Dependencies", score, 5, f"✅ Deps managed: {langs}")
        else:
            self.add_check("Dependencies", 0, 5, "⚠️ No dependency file found")
    
    def check_docker(self):
        """Check for Docker setup"""
        dockerfile = self.project_path / "Dockerfile"
        compose = self.project_path / "docker-compose.yml"
        
        score = 0
        messages = []
        
        if dockerfile.exists():
            score += 3
            messages.append("Dockerfile")
        if compose.exists():
            score += 2
            messages.append("docker-compose.yml")
        
        if score > 0:
            status = "✅" if score == 5 else "⚠️"
            self.add_check("Docker", score, 5, f"{status} {', '.join(messages)}")
        else:
            self.add_check("Docker", 0, 5, "❌ No Docker config")
    
    def check_tests(self):
        """Check for test files"""
        test_patterns = [
            "test_*.py", "*_test.py", "*.test.js", "*.spec.js",
            "*.test.ts", "*.spec.ts"
        ]
        
        test_files = []
        for pattern in test_patterns:
            test_files.extend(self.project_path.rglob(pattern))
        
        # Check for test directories
        test_dirs = ['tests', 'test', '__tests__', 'spec']
        has_test_dir = any((self.project_path / d).exists() for d in test_dirs)
        
        score = 0
        if test_files:
            score = min(len(test_files), 5) + (3 if has_test_dir else 0)
        elif has_test_dir:
            score = 2
        
        score = min(score, 8)
        status = "✅" if score >= 5 else "⚠️" if score >= 2 else "❌"
        msg = f"{len(test_files)} test files" if test_files else "No tests"
        self.add_check("Tests", score, 8, f"{status} {msg}")
    
    def check_env_example(self):
        """Check for .env.example"""
        env_example = self.project_path / ".env.example"
        env_file = self.project_path / ".env"
        
        score = 0
        if env_example.exists():
            score = 5
            status = "✅ Has .env.example"
        elif env_file.exists():
            score = 2
            status = "⚠️ Has .env but no .env.example"
        else:
            status = "✅ No env files (may not need)"
            score = 3  # Not a problem if truly not needed
        
        self.add_check("Environment", score, 5, status)
    
    def check_git(self):
        """Check git repository health"""
        git_dir = self.project_path / ".git"
        gitignore = self.project_path / ".gitignore"
        
        score = 0
        messages = []
        
        if git_dir.exists():
            score += 3
            messages.append("Git repo")
        if gitignore.exists():
            score += 2
            messages.append(".gitignore")
        
        status = "✅" if score == 5 else "⚠️" if score > 0 else "❌"
        msg = ", ".join(messages) if messages else "Not a git repo"
        self.add_check("Git", score, 5, f"{status} {msg}")
    
    def check_ci_cd(self):
        """Check for CI/CD configuration"""
        ci_files = [
            ".github/workflows",
            ".gitlab-ci.yml",
            ".circleci",
            "Jenkinsfile",
            ".travis.yml"
        ]
        
        found = []
        for ci_path in ci_files:
            if (self.project_path / ci_path).exists():
                found.append(ci_path.split('/')[-1].split('.')[0])
        
        if found:
            score = 5
            self.add_check("CI/CD", score, 5, f"✅ {', '.join(found)}")
        else:
            self.add_check("CI/CD", 0, 5, "❌ No CI/CD")
    
    def check_obsidian_note(self):
        """Check if there's a matching Obsidian note"""
        note_path = VAULT_PATH / "Projetos" / "01-Ativos" / "Privados" / f"{self.name}.md"
        
        if note_path.exists():
            content = note_path.read_text(encoding='utf-8', errors='ignore')
            score = 2 if len(content) > 200 else 1
            status = "✅" if score == 2 else "⚠️"
            self.add_check("Documentation", score, 2, f"{status} Has vault note")
        else:
            self.add_check("Documentation", 0, 2, "❌ No vault note")
    
    def add_check(self, category, score, max_score, message):
        """Add a check result"""
        self.checks.append({
            'category': category,
            'score': score,
            'max_score': max_score,
            'message': message,
            'percentage': (score / max_score * 100) if max_score > 0 else 0
        })
        self.score += score
        self.max_score += max_score
    
    def run_all_checks(self):
        """Run all health checks"""
        self.check_readme()
        self.check_dependencies()
        self.check_docker()
        self.check_tests()
        self.check_env_example()
        self.check_git()
        self.check_ci_cd()
        self.check_obsidian_note()
    
    def get_grade(self):
        """Calculate letter grade"""
        percentage = (self.score / self.max_score * 100) if self.max_score > 0 else 0
        
        if percentage >= 90:
            return "A", "🟢"
        elif percentage >= 80:
            return "B", "🟢"
        elif percentage >= 70:
            return "C", "🟡"
        elif percentage >= 60:
            return "D", "🟡"
        else:
            return "F", "🔴"
    
    def generate_report_section(self):
        """Generate markdown report section for this project"""
        grade, icon = self.get_grade()
        percentage = (self.score / self.max_score * 100) if self.max_score > 0 else 0
        
        md = f"\n### {icon} {self.name}\n\n"
        md += f"**Score:** {self.score}/{self.max_score} ({percentage:.0f}%) — Grade: **{grade}**\n\n"
        md += "| Check | Score | Status |\n"
        md += "|-------|-------|--------|\n"
        
        for check in self.checks:
            md += f"| {check['category']} | {check['score']}/{check['max_score']} | {check['message']} |\n"
        
        # Recommendations
        low_scores = [c for c in self.checks if c['percentage'] < 50]
        if low_scores:
            md += "\n**Recommendations:**\n"
            for check in low_scores:
                if check['category'] == "README":
                    md += "- 📝 Improve README with installation, usage, and examples\n"
                elif check['category'] == "Tests":
                    md += "- 🧪 Add unit tests (pytest, jest, etc.)\n"
                elif check['category'] == "Docker":
                    md += "- 🐳 Add Dockerfile and docker-compose.yml\n"
                elif check['category'] == "CI/CD":
                    md += "- ⚙️ Set up GitHub Actions for automated testing\n"
                elif check['category'] == "Git":
                    md += "- 📦 Initialize git repository and add .gitignore\n"
        
        return md


def scan_projects():
    """Scan all projects in the Privados directory"""
    if not PROJECTS_DIR.exists():
        print(f"❌ Projects directory not found: {PROJECTS_DIR}")
        return []
    
    projects = []
    for item in PROJECTS_DIR.iterdir():
        if item.is_dir() and not item.name.startswith('.') and item.name != '__pycache__':
            checker = ProjectHealthChecker(item)
            checker.run_all_checks()
            projects.append(checker)
    
    return projects


def generate_full_report(projects):
    """Generate full markdown report"""
    now = datetime.now()
    
    md = f"""---
title: "Project Health Report"
description: "Automated health check of all active projects"
tags: [report, health, projects, automated]
generated: {now.strftime("%Y-%m-%d %H:%M:%S")}
---

# 📊 Project Health Report

**Generated:** {now.strftime("%Y-%m-%d at %H:%M:%S")}
**Projects Scanned:** {len(projects)}

---

## 📈 Overall Summary

"""
    
    # Calculate overall stats
    total_score = sum(p.score for p in projects)
    total_max = sum(p.max_score for p in projects)
    avg_percentage = (total_score / total_max * 100) if total_max > 0 else 0
    
    grade_counts = {}
    for project in projects:
        grade, _ = project.get_grade()
        grade_counts[grade] = grade_counts.get(grade, 0) + 1
    
    md += f"| Metric | Value |\n"
    md += f"|--------|-------|\n"
    md += f"| **Overall Health** | {avg_percentage:.0f}% |\n"
    md += f"| **Total Score** | {total_score}/{total_max} |\n"
    for grade in ['A', 'B', 'C', 'D', 'F']:
        if grade in grade_counts:
            md += f"| **Grade {grade}** | {grade_counts[grade]} projects |\n"
    
    # Sort projects by score (best first)
    projects_sorted = sorted(projects, key=lambda p: p.score / p.max_score if p.max_score > 0 else 0, reverse=True)
    
    md += "\n---\n\n## 🏆 Project Rankings\n"
    
    for i, project in enumerate(projects_sorted, 1):
        _, icon = project.get_grade()
        percentage = (project.score / project.max_score * 100) if project.max_score > 0 else 0
        md += f"{i}. {icon} **{project.name}** — {percentage:.0f}%\n"
    
    md += "\n---\n\n## 📋 Detailed Reports\n"
    
    for project in projects_sorted:
        md += project.generate_report_section()
    
    md += f"""

---

## 🔗 Related Documents

- [[JARVIS/02-Operational/Dashboard|Operational Dashboard]]
- [[Projetos/01-Ativos/Plano-de-Acao|Action Plan]]
- [[Projetos/01-Ativos/Privados/README|Projects Index]]

---

*This report was automatically generated by `.scripts/project_health_checker.py`*
*To regenerate, run: `python .scripts/project_health_checker.py`*
*Schedule this weekly for continuous monitoring*
"""
    
    return md


def main():
    """Main execution"""
    print("🔍 Scanning projects...")
    
    projects = scan_projects()
    
    if not projects:
        print("⚠️ No projects found to scan")
        return
    
    print(f"📊 Analyzed {len(projects)} projects")
    
    # Generate report
    report = generate_full_report(projects)
    
    # Ensure output directory exists
    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    
    # Write report
    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        f.write(report)
    
    print(f"✅ Health report generated: {OUTPUT_FILE.relative_to(VAULT_PATH)}")
    
    # Print summary
    print("\n📈 Quick Summary:")
    for project in sorted(projects, key=lambda p: p.score / p.max_score if p.max_score > 0 else 0, reverse=True)[:5]:
        grade, icon = project.get_grade()
        percentage = (project.score / project.max_score * 100) if project.max_score > 0 else 0
        print(f"  {icon} {project.name}: {percentage:.0f}% (Grade {grade})")


if __name__ == "__main__":
    main()
