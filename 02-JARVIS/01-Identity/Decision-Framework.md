---
title: "Decision Framework — Fast Technical Choices"
description: "Step-by-step framework for making technical decisions quickly and consistently"
tags: [identity, decision-making, framework, process, jarvis-identidade]
updated: 2026-06-10
date: 2026-04-27
---

# ⚡ Decision Framework

A systematic approach to technical decisions that balances speed with quality.

## 🎯 When to Use This Framework

**Use for:**
- Choosing technologies (framework, library, tool)
- Architecture decisions (monolith vs micro, SQL vs NoSQL)
- Build vs buy decisions
- Feature prioritization

**Don't use for:**
- Obvious choices (use what you know)
- Reversible decisions (just pick one and move)
- Time-critical bugs (fix first, optimize later)

---

## 📐 The Framework (5 Steps)

### Step 1: Define the Problem
**Time: 5 minutes**

Answer these questions:
1. What problem am I trying to solve?
2. Who is this for? (me, users, team)
3. What's the success metric?
4. What's the deadline/urgency?

**Example:**
```
Problem: Need to add authentication to gestor_aluguel_2.0
For: End users (landlords)
Success: Secure, multi-tenant auth with email/password
Deadline: 1 week
```

---

### Step 2: List Constraints
**Time: 3 minutes**

Identify hard constraints:
- [ ] **Budget:** Free / <$X per month / unlimited
- [ ] **Time:** Must ship in X days
- [ ] **Skills:** Only know X, Y (or willing to learn Z)
- [ ] **Scale:** Expected X users/requests
- [ ] **Privacy:** Must be local / cloud OK
- [ ] **Dependencies:** Must integrate with X

**Example:**
```
☑ Budget: $0 (free tier only)
☑ Time: 1 week
☑ Skills: Know React, Node, SQL
☐ Scale: <100 users initially
☑ Privacy: Cloud OK (not sensitive data)
☑ Dependencies: Works with Next.js + Prisma
```

---

### Step 3: Generate Options (Rule of 3)
**Time: 10 minutes**

List exactly **3 options**. No more, no less.

For each option, note:
- ✅ Pros (2-3 main benefits)
- ❌ Cons (2-3 main drawbacks)
- ⏱️ Time to implement
- 💰 Cost (setup + ongoing)

**Example:**

#### Option 1: NextAuth.js
- ✅ Pros: Built for Next.js, handles OAuth, session management
- ❌ Cons: Learning curve, opinionated structure
- ⏱️ Time: 2-3 days
- 💰 Cost: Free

#### Option 2: Supabase Auth
- ✅ Pros: Drop-in solution, includes database, RLS
- ❌ Cons: Vendor lock-in, adds external dependency
- ⏱️ Time: 1 day
- 💰 Cost: Free tier (enough for MVP)

#### Option 3: Custom JWT + Prisma
- ✅ Pros: Full control, learn deeply, minimal dependencies
- ❌ Cons: Security risk if wrong, more code to maintain
- ⏱️ Time: 4-5 days
- 💰 Cost: Free

---

### Step 4: Score Against Principles
**Time: 5 minutes**

Rate each option (0-5) on these criteria from [[Engineering-Principles]]:

| Criterion | Weight | Option 1 | Option 2 | Option 3 |
|-----------|--------|----------|----------|----------|
| **Local-first** | 2x | 5 (Next.js local) | 2 (cloud dep) | 5 (fully local) |
| **Pragmatic** | 3x | 4 (battle-tested) | 5 (fastest) | 2 (reinventing) |
| **Maintainable** | 2x | 4 (good docs) | 4 (managed) | 3 (DIY) |
| **Automatable** | 1x | 4 (standard) | 5 (API) | 3 (custom) |
| **Observable** | 1x | 3 (logs?) | 5 (dashboard) | 2 (manual) |
| **Total** | — | **38** | **39** | **28** |

**Scoring guide:**
- 5 = Excellent fit
- 4 = Good fit
- 3 = Acceptable
- 2 = Poor fit
- 1 = Terrible fit
- 0 = Dealbreaker

---

### Step 5: Decide & Document
**Time: 2 minutes**

1. **Pick the highest score** (unless gut says otherwise)
2. **Document the decision** in [[02-JARVIS/02-Operational/Decisions/INDEX]]
3. **Set a review date** (when will you revisit this?)

**Decision Template:**
```markdown
## Decision: Use Supabase Auth for gestor_aluguel_2.0

**Date:** 2026-04-23
**Context:** Need multi-tenant auth within 1 week
**Options considered:** NextAuth, Supabase, Custom JWT
**Chosen:** Supabase Auth
**Rationale:** 
- Fastest to implement (1 day vs 2-5)
- Free tier sufficient for MVP
- Built-in RLS for multi-tenancy
- Can migrate to NextAuth later if needed

**Trade-offs accepted:**
- Vendor dependency (OK for MVP)
- Slightly less local-first (acceptable)

**Review date:** 2026-07-23 (after 100 users)
```

---

## 🔥 Fast-Track Decisions (< 5 min)

For common scenarios, use these quick rules:

### Language/Framework Choice

```
Do I know it well? → YES → Use it
  ↓ NO
Is it the standard for this use case? → YES → Use it
  ↓ NO
Is it local-first? → YES → Try it
  ↓ NO
Can I use something local instead? → YES → Use that
  ↓ NO
Is the cloud version worth the cost? → YES → Use it, document why
  ↓ NO
Pick the most popular alternative and learn it
```

### Database Choice

```
How many users?
  <100 → SQLite
  100-10k → PostgreSQL local
  10k-1M → Neon/Supabase
  >1M → Consult expert
```

### Hosting Choice

```
Is it a prototype? → YES → Local dev server
  ↓ NO
Does it need to be online? → NO → Keep local
  ↓ YES
Static site? → YES → Vercel/Netlify
  ↓ NO
Node.js app? → YES → Railway/Render
  ↓ NO
Python app? → YES → Railway/Fly.io
```

---

## 🧠 Cognitive Biases to Watch

### 1. Sunk Cost Fallacy
**Bad:** "I've already spent 3 days on X, can't switch now."
**Good:** "X isn't working. Switch to Y, even if it costs 1 day."

### 2. Bandwagon Effect
**Bad:** "Everyone uses React, so I should too."
**Good:** "Does React solve MY problem better than Vue?"

### 3. Availability Heuristic
**Bad:** "I just learned Rust, let's use it for everything."
**Good:** "Is Rust the right tool for THIS job?"

### 4. Confirmation Bias
**Bad:** Only researching pros of your preferred option.
**Good:** Actively look for cons and dealbreakers.

---

## 📊 Decision Log Template

Every non-trivial decision should be logged in:
`JARVIS/02-Operational/Decisions/YYYY-MM-DD-topic.md`

```markdown
---
title: "Decision: [Topic]"
date: YYYY-MM-DD
status: active | deprecated | superseded
tags: [decision, architecture, [domain]]
---

## Context
What problem are we solving? Why now?

## Options Considered
1. Option A
2. Option B
3. Option C

## Decision
We chose [X] because [rationale].

## Consequences
**Positive:**
- Pro 1
- Pro 2

**Negative:**
- Con 1 (acceptable because...)
- Con 2 (will mitigate by...)

## Review Date
YYYY-MM-DD — revisit after [event/milestone]
```

---

## 🔄 When to Reverse a Decision

It's OK to change your mind. Reverse if:

1. **Assumptions changed**
   - User count 10x higher than expected
   - Budget constraints lifted
   - New requirement emerged

2. **Better option emerged**
   - New tool that solves 3 problems at once
   - Maintained by team you trust

3. **Pain outweighs benefit**
   - Maintenance burden too high
   - Performance unacceptable
   - Team can't understand it

**Process:**
1. Document why you're reversing
2. Update the original decision log (status: `superseded`)
3. Create new decision log for the replacement

---

## 🎯 Practice Scenarios

Try the framework on these:

### Scenario 1: Add real-time features
**Problem:** Need live updates in dashboard
**Options:** WebSockets, Polling, Server-Sent Events
**Constraints:** <100 users, must work on free tier

### Scenario 2: Store large files
**Problem:** Users uploading PDFs (50MB each)
**Options:** Database BLOB, Local FS, S3
**Constraints:** ~1GB total, must be secure

### Scenario 3: Add search
**Problem:** Need to search 10k documents
**Options:** SQL LIKE, PostgreSQL FTS, ElasticSearch, FAISS
**Constraints:** Must be local, semantic search preferred

---

## 🔗 Related Documents
- [[Engineering-Principles]] — Core principles that inform decisions
- [[02-JARVIS/02-Operational/Decisions/INDEX]] — Historical decision log
- [[05-Skills/README]] — Technical implementation guides

---

*Decision-making is a skill. This framework gets better with practice.*
*Update this doc when you find better heuristics.*

[[02-JARVIS/README|← Voltar ao Command Center]]
