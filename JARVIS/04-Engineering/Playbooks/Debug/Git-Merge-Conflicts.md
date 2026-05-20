---
title: "Git Merge Conflicts — Resolution Guide"
description: "Step-by-step guide to resolve git merge conflicts"
tags: [troubleshooting, git, merge, conflict, playbook, jarvis-engenharia]
updated: 2026-05-03
date: 2026-04-27
---

# 🔀 Git Merge Conflicts

Systematic approach to resolving merge conflicts.

---

## 🔍 What Happened?

Merge conflict occurs when:
- You and another developer (or branch) modified the same lines
- Git can't automatically decide which changes to keep

**Visual:**
```
main:    A---B---C
                  \
feature:           D---E

Merge:   A---B---C---M
                  \   /
                   D-E

Conflict: C and D both modified the same file
```

---

## ❌ Symptoms

```bash
$ git merge feature-branch
Auto-merging file.py
CONFLICT (content): Merge conflict in file.py
Automatic merge failed; fix conflicts and then commit the result.

$ git status
Unmerged paths:
  (use "git add <file>..." to mark resolution)
        both modified:   file.py
```

---

## ✅ Resolution Process

### Step 1: Identify Conflicts

```bash
# See which files have conflicts
git status

# Or more detail:
git diff --name-only --diff-filter=U
```

### Step 2: Open Conflicted File

Conflicts look like this:

```python
def calculate(x, y):
<<<<<<< HEAD  (Current branch)
    return x + y  # Your changes
=======
    return x * y  # Incoming changes
>>>>>>> feature-branch
```

**Parts explained:**
- `<<<<<<< HEAD`: Start of YOUR changes (current branch)
- `=======`: Separator
- `>>>>>>> feature-branch`: End of THEIR changes (incoming)

### Step 3: Choose Resolution

**Option A: Keep your changes**
```python
def calculate(x, y):
    return x + y
```

**Option B: Keep their changes**
```python
def calculate(x, y):
    return x * y
```

**Option C: Keep both (if makes sense)**
```python
def calculate(x, y, operation="add"):
    if operation == "add":
        return x + y
    return x * y
```

**Option D: Rewrite entirely**
```python
def calculate(x, y):
    return x ** y  # New solution
```

### Step 4: Remove Conflict Markers

**Delete these lines:**
```
<<<<<<< HEAD
=======
>>>>>>> feature-branch
```

**Final clean code:**
```python
def calculate(x, y):
    return x + y
```

### Step 5: Test Your Changes

```bash
# Run tests
pytest

# Or run the code manually
python file.py
```

### Step 6: Mark as Resolved

```bash
# Stage the resolved file
git add file.py

# Check status
git status
# Should say: "All conflicts fixed but you are still merging"
```

### Step 7: Complete the Merge

```bash
# Commit the merge
git commit

# Or with a message:
git commit -m "Merge feature-branch, resolved conflicts in file.py"
```

---

## 🛠️ Using Tools

### VS Code (GUI)

1. Open conflicted file in VS Code
2. You'll see colored sections:
   - **Current Change** (green)
   - **Incoming Change** (blue)
3. Click one of:
   - `Accept Current Change`
   - `Accept Incoming Change`
   - `Accept Both Changes`
   - `Compare Changes` (side-by-side)

### Git Mergetool

```bash
# Launch default merge tool
git mergetool

# Or specify tool:
git mergetool --tool=vimdiff
git mergetool --tool=code  # VS Code
```

### Aborting the Merge

**If you want to start over:**
```bash
git merge --abort
# Returns to state before merge started
```

---

## 🔄 Common Scenarios

### Scenario 1: Pulling from Remote

```bash
$ git pull origin main
CONFLICT (content): Merge conflict in README.md

# Resolution:
1. Edit README.md
2. Remove conflict markers
3. git add README.md
4. git commit
5. git push origin main
```

### Scenario 2: Merging Feature Branch

```bash
$ git checkout main
$ git merge feature-xyz
CONFLICT (content): Merge conflict in app.py

# Resolution:
1. Edit app.py
2. git add app.py
3. git commit -m "Merge feature-xyz"
4. git push origin main
```

### Scenario 3: Rebasing

```bash
$ git rebase main
CONFLICT (content): Merge conflict in config.yml

# Resolution:
1. Edit config.yml
2. git add config.yml
3. git rebase --continue  # Note: --continue, not commit

# If multiple conflicts:
# Repeat edit → add → rebase --continue until done
```

---

## 🚨 Complex Conflicts

### Multiple Files with Conflicts

```bash
# See all conflicts
git diff --name-only --diff-filter=U

# Resolve one by one
vim file1.py
git add file1.py

vim file2.js
git add file2.js

# Check if all resolved
git status

# Commit
git commit
```

### Binary File Conflicts

**Can't be merged (images, PDFs, etc.)**

```bash
# Keep your version:
git checkout --ours file.png
git add file.png

# Keep their version:
git checkout --theirs file.png
git add file.png
```

### Deleted File Conflicts

```bash
# File deleted in one branch, modified in another

# Keep deletion:
git rm file.txt
git commit

# Keep file (and modifications):
git add file.txt
git commit
```

---

## 📋 Prevention Tips

### 1. Pull Frequently
```bash
# Before starting work:
git pull origin main

# Reduces chance of conflicts
```

### 2. Small, Frequent Commits
```bash
# Instead of one huge commit:
git commit -m "Add feature X"

# Do:
git commit -m "Add X model"
git commit -m "Add X view"
git commit -m "Add X tests"
```

### 3. Communicate with Team
- Announce when working on shared files
- Use feature branches
- Pull requests for code review

### 4. Use .gitattributes
```bash
# .gitattributes
*.json merge=union  # Combine changes
*.lock merge=ours   # Always keep our version
```

---

## 🔧 Advanced Techniques

### Rerere (Reuse Recorded Resolution)

Git can remember how you resolved conflicts:

```bash
# Enable rerere
git config --global rerere.enabled true

# Now when same conflict happens again,
# Git will auto-resolve using your previous solution
```

### Diff3 Conflict Style

Shows original code + both changes:

```bash
# Enable globally
git config --global merge.conflictstyle diff3

# Conflict will show:
<<<<<<< HEAD
your changes
||||||| base
original code
=======
their changes
>>>>>>> branch
```

### Ours vs Theirs (Bulk)

```bash
# Keep all "ours" (your branch)
git merge -Xours feature-branch

# Keep all "theirs" (incoming)
git merge -Xtheirs feature-branch

# ⚠️ Use carefully - doesn't check individual conflicts
```

---

## 🔗 Related Resources

- [[JARVIS/01-Identity/Will/Engineering-Principles|Engineering Principles]] — Git workflow
- [[JARVIS/04-Engineering/Playbooks/Workflows-Praticos|Workflows]] — Git best practices
- [Git Documentation](https://git-scm.com/book/en/v2/Git-Tools-Advanced-Merging)

---

## 📞 Emergency Commands

### Undo Everything
```bash
# Abort merge
git merge --abort

# Abort rebase
git rebase --abort

# Return to previous state (last commit)
git reset --hard HEAD

# Return to specific commit
git reset --hard abc1234
```

### Backup Before Resolving
```bash
# Create backup branch
git branch backup-before-merge

# Now resolve conflicts
# If something goes wrong:
git checkout backup-before-merge
```

---

## ✅ Resolution Checklist

- [ ] Identified all conflicted files (`git status`)
- [ ] Opened and edited each file
- [ ] Removed ALL conflict markers (`<<<<`, `====`, `>>>>`)
- [ ] Code compiles/runs without errors
- [ ] Tests pass
- [ ] Staged all resolved files (`git add`)
- [ ] Committed the merge (`git commit`)
- [ ] Pushed to remote (if needed)

---

*Conflicts are normal. Stay calm, resolve systematically.*

[[JARVIS/README|← Voltar ao Command Center]]
