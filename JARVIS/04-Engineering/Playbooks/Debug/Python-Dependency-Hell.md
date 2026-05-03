---
title: "Python Dependency Hell — Troubleshooting"
description: "Resolve Python package conflicts and installation issues"
tags: [troubleshooting, python, pip, dependencies, playbook, jarvis-engenharia]
updated: 2026-05-03
date: 2026-04-27
---

# 🐍 Python Dependency Hell

Systematic approach to fixing Python package issues.

---

## 🔍 Quick Diagnosis

```bash
# Check Python version
python --version

# Check pip version
pip --version

# List installed packages
pip list

# Check for broken dependencies
pip check
```

---

## ❌ Problem 1: Package Installation Fails

### Symptoms
- `ERROR: Could not find a version that satisfies the requirement`
- `ERROR: No matching distribution found`

### Solution
```bash
# Update pip first
python -m pip install --upgrade pip

# Try with --pre (allow pre-releases)
pip install --pre package-name

# Try specific version
pip install package-name==1.2.3

# Check if package name is correct
pip search package-name  # (Note: search is disabled on PyPI)
# Use https://pypi.org/ instead
```

---

## ❌ Problem 2: Conflicting Dependencies

### Symptoms
- `ERROR: package-a 1.0 has requirement package-b<2.0, but you have package-b 2.1`

### Solution

**Option 1: Use a virtual environment (RECOMMENDED)**
```bash
# Create venv
python -m venv venv

# Activate
# Windows:
venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate

# Install requirements
pip install -r requirements.txt
```

**Option 2: Use pip-compile (advanced)**
```bash
# Install pip-tools
pip install pip-tools

# Create requirements.in (list top-level deps only)
echo "fastapi\nuvicorn\nsqlalchemy" > requirements.in

# Generate locked requirements.txt
pip-compile requirements.in

# Install
pip-sync requirements.txt
```

---

## ❌ Problem 3: Module Not Found After Installation

### Symptoms
- `ModuleNotFoundError: No module named 'package_name'`
- Package installs successfully but can't be imported

### Diagnosis & Solution
```bash
# Check which Python is running
which python  # Linux/Mac
where python  # Windows

# Check where package is installed
pip show package-name

# Ensure you're using the same Python
python -m pip list  # Use 'python -m pip' instead of just 'pip'

# If using venv, ensure it's activated
# You should see (venv) in your prompt
```

---

## ❌ Problem 4: Permission Denied (Linux/Mac)

### Symptoms
- `ERROR: Could not install packages due to an EnvironmentError: [Errno 13] Permission denied`

### Solution
```bash
# DON'T use sudo pip install (creates more problems)

# Use --user flag
pip install --user package-name

# OR create virtual environment (better)
python -m venv venv
source venv/bin/activate
pip install package-name
```

---

## ❌ Problem 5: SSL Certificate Error

### Symptoms
- `SSLError: [SSL: CERTIFICATE_VERIFY_FAILED]`

### Solution
```bash
# Temporary fix (not recommended for production)
pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org package-name

# Proper fix: Update certificates
# Windows: Update your Python installation
# Mac: Run /Applications/Python\ 3.x/Install\ Certificates.command
# Linux: sudo apt install ca-certificates
```

---

## ❌ Problem 6: Different Versions Needed by Different Projects

### Symptoms
- Project A needs `requests==2.25.0`
- Project B needs `requests==2.28.0`

### Solution: Always Use Virtual Environments
```bash
# Project A
cd /path/to/project-a
python -m venv venv-a
source venv-a/bin/activate  # or venv-a\Scripts\activate on Windows
pip install -r requirements.txt

# Project B
cd /path/to/project-b
python -m venv venv-b
source venv-b/bin/activate
pip install -r requirements.txt
```

---

## ❌ Problem 7: requirements.txt Has Conflicts

### Symptoms
- `pip install -r requirements.txt` fails with dependency conflicts

### Solution
```bash
# Install one by one to find the culprit
while IFS= read -r package; do
    echo "Installing: $package"
    pip install "$package" || echo "Failed: $package"
done < requirements.txt

# Use pip-compile to generate compatible versions
pip install pip-tools
pip-compile requirements.in --upgrade
```

---

## ❌ Problem 8: C Extension Compilation Fails

### Symptoms
- `error: Microsoft Visual C++ 14.0 is required` (Windows)
- `gcc: command not found` (Linux)

### Solution

**Windows:**
1. Install [Microsoft C++ Build Tools](https://visualstudio.microsoft.com/visual-cpp-build-tools/)
2. Or install pre-built wheels: `pip install package-name --only-binary :all:`

**Linux:**
```bash
# Ubuntu/Debian
sudo apt install build-essential python3-dev

# Fedora/RHEL
sudo dnf install gcc gcc-c++ python3-devel

# Then retry installation
pip install package-name
```

**macOS:**
```bash
# Install Xcode Command Line Tools
xcode-select --install
```

---

## ❌ Problem 9: Old pip Cache Causing Issues

### Symptoms
- Installation succeeds but imports old code
- Changes in package not reflected

### Solution
```bash
# Clear pip cache
pip cache purge

# Reinstall package
pip install --force-reinstall --no-cache-dir package-name

# For development packages
pip install --editable . --force-reinstall
```

---

## ❌ Problem 10: Multiple Python Versions Conflict

### Symptoms
- `python` points to Python 2.x
- Packages installed for wrong Python version

### Solution
```bash
# Always use explicit version
python3 -m pip install package-name  # Use python3, not python
python3.11 -m pip install package-name  # Even more explicit

# Set alias (Linux/Mac)
echo "alias python=python3" >> ~/.bashrc
echo "alias pip=pip3" >> ~/.bashrc
source ~/.bashrc

# Windows: Use py launcher
py -3.11 -m pip install package-name
```

---

## 🛠️ Nuclear Option: Fresh Environment

**⚠️ Use when everything else fails**

```bash
# Delete existing venv
rm -rf venv

# Create fresh venv
python -m venv venv

# Activate
source venv/bin/activate  # or venv\Scripts\activate

# Upgrade pip
python -m pip install --upgrade pip setuptools wheel

# Install from requirements
pip install -r requirements.txt
```

---

## 📋 Best Practices (Prevention)

### 1. Always Use Virtual Environments
```bash
# Per-project venv
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

### 2. Pin Dependencies
```bash
# Generate requirements.txt with exact versions
pip freeze > requirements.txt

# Or use requirements.in + pip-compile
fastapi>=0.100.0,<1.0.0
uvicorn[standard]
```

### 3. Use pyproject.toml (Modern)
```toml
[project]
dependencies = [
    "fastapi>=0.100.0",
    "uvicorn[standard]>=0.22.0",
]
```

### 4. Document Python Version
```bash
# Add to README.md
echo "Python 3.11+ required" >> README.md

# Or use pyenv
pyenv local 3.11.5
```

### 5. Regular Maintenance
```bash
# Check for outdated packages
pip list --outdated

# Update safely (one at a time)
pip install --upgrade package-name

# Run tests after each update
pytest
```

---

## 🔧 Tools to Help

### pipenv (Alternative to pip + venv)
```bash
pip install pipenv
pipenv install package-name
pipenv run python script.py
```

### poetry (Modern dependency management)
```bash
pip install poetry
poetry add package-name
poetry install
```

### pip-audit (Security scanning)
```bash
pip install pip-audit
pip-audit
```

---

## 🔗 Related Resources

- [[JARVIS/01-Identity/Will/Engineering-Principles|Engineering Principles]] — Dependency philosophy
- [[JARVIS/02-Operational/Config/ENV-Registry|ENV Registry]] — Virtual environment setup
- [[skills/02-software-engineering/backend|Backend Skills]] — Python best practices

---

## 📞 Still Stuck?

1. Check if issue is known: https://github.com/pypa/pip/issues
2. Check package-specific issues: https://github.com/[package-name]/[package-name]/issues
3. Ask on Stack Overflow with full error message
4. Check Python version compatibility on PyPI

---

*Update this playbook when you discover new solutions*
