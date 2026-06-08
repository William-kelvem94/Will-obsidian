---
name: advanced-debugging
description: Systematic troubleshooting, memory leak analysis, tracebacks, and profiling across stacks.
title: "Advanced Debugging & Diagnostics Skill"
date: 2026-06-08
tags: [skills, debugging, diagnostic, profiling, troubleshooting]
updated: 2026-06-08
---

# Advanced Debugging & Diagnostics Skill

Use this skill when diagnosing complex crashes, locating memory leaks, analyzing tracebacks, or profiling application performance.

## Systematic Debugging Method

1. **Reproduce**: Confirm the bug is reproducible and isolate the minimal input/context required.
2. **Locate**: Trace the execution path using logs, step-through debuggers (pdb, gdb, Chrome DevTools), or stack traces.
3. **Analyze**: Formulate hypotheses about the root cause (e.g., race conditions, memory mismanagement, type mismatches).
4. **Fix & Verify**: Apply a fix and verify with automated regression tests.

## Tools & Profilers

- **Python**: `pdb`/`ipdb` (interactive debugger), `cProfile` (CPU profiling), `tracemalloc` (memory leaks).
- **Node.js**: Chrome DevTools, `clinic.js` (performance bottlenecks).
- **System Level**: `strace` (system calls), `lsof` (open files), `htop`/`glances` (resource allocation).
- **Core Dumps**: Configuring core dump generation for native applications to debug segfaults post-mortem.
