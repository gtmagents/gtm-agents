---
name: diagnostics
description: Use for structured technical SEO audits, incident response, and validation.
---

# Technical Diagnostics Toolkit Skill

## When to Use
- Investigating crawl/index anomalies, traffic drops, or Core Web Vitals regressions.
- Running scheduled audits ahead of major launches or migrations.
- Validating fixes before/after engineering deployments.

## Framework
1. **Signal Triangulation** – combine Search Console, log files, crawler output, and analytics deltas.
2. **Replication Scripts** – document steps to reproduce issues (user agents, locales, device types).
3. **Root Cause Hypotheses** – map symptoms to likely causes (render blocking, redirects, robots, schema errors).
4. **Fix Design** – outline remediation options, risk level, dependencies, and testing approach.
5. **Validation & Monitoring** – specify metrics and alerts to confirm resolution.

## Templates
- Diagnostics worksheet (symptom, evidence, hypothesis, owner, next action).
- Crawl + render checklist per environment.
- Validation log capturing metrics pre/post change.

## Tips
- Keep historical baselines to quickly detect regressions.
- Pair with engineering release notes to correlate incidents.
- Automate recurring crawls and lighthouse runs to catch issues early.

---
