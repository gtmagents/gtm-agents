---
name: deploy-optimizations
description: Coordinates content, technical, and linking updates for priority SEO initiatives.
usage: /seo-workflow-orchestration:deploy-optimizations --cluster "AI sales enablement" --owner content --due 2025-12-01
---

# Command: deploy-optimizations

## Inputs
- **cluster** – keyword/theme reference from `prioritize-keywords`.
- **owner** – responsible team (content, web, technical, revops).
- **due** – target completion date.
- **scope** – optional notes (net-new page, refresh, technical fix, structured data).
- **dependencies** – optional list (design, product, partners).

## Workflow
1. **Brief Retrieval** – load cluster data, content brief, and technical requirements.
2. **Task Breakdown** – create checklist covering copy, design, CMS, technical fixes, internal links, schema, QA.
3. **Execution Coordination** – assign owners, manage approvals, and track status in shared board.
4. **QA & Publishing** – validate metadata, performance (CWV), accessibility, and analytics tagging before go-live.
5. **Post-launch Monitoring** – collect early KPI signals, ensure logs/reporting are updated.

## Outputs
- Optimization checklist with owners, status, and evidence links.
- Publishing confirmation (URL, timestamp, environment, approvals).
- Follow-up tasks for link building, experimentation, or refresh cadence.

## Agent/Skill Invocations
- `on-page-lead` – manages content + CMS workflow.
- `technical-analyst` – validates technical requirements and QA.
- `publishing-process` skill – enforces approval gates and evidence capture.

---
