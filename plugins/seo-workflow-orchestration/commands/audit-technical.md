---
name: audit-technical
description: Runs technical SEO diagnostics, prioritizes issues, and packages remediation guidance.
usage: /seo-workflow-orchestration:audit-technical --scope "core-web-vitals" --window 30d --detail full
---

# Command: audit-technical

## Inputs
- **scope** – focus area (crawl, index, CWV, schema, hreflang, redirects).
- **window** – data range (7d, 30d, 90d) for Search Console/log metrics.
- **detail** – summary | full output detail.
- **environment** – optional prod | staging to analyze releases.
- **pages** – optional URL or directory filter for targeted audits.

## Workflow
1. **Signal Collection** – pull Search Console, log files, crawler data, Lighthouse/CWV metrics for specified scope.
2. **Diagnostics** – run automated checks (status codes, render depth, CLS/LCP, schema validation, hreflang pairs).
3. **Impact Assessment** – quantify affected pages, traffic at risk, and business impact.
4. **Remediation Plan** – outline recommended fixes, owners, SLAs, and dependencies.
5. **Governance Logging** – document incidents, change requests, and QA requirements before deployment.

## Outputs
- Technical audit report (issue, severity, pages impacted, evidence links, proposed fix).
- Ticket backlog or PRD with prioritized actions.
- Monitoring plan (dashboards/alerts) for post-fix validation.

## Agent/Skill Invocations
- `technical-analyst` – leads diagnostics and remediation planning.
- `diagnostics` skill – provides checklists, tooling references, and QA steps.
- `seo-director` – reviews impact and signs off on priorities.

---
