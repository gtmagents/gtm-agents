---
name: optimize-page
description: Audits and enhances an existing page for target keywords, UX, and conversion goals.
usage: /seo:optimize-page --url https://example.com/guide --target "sales enablement platform"
---

# Command: optimize-page

## Inputs
- **url** – page to audit.
- **target** – primary keyword or topic.
- **secondary_terms** – optional supporting keywords.
- **goal** – conversion goal (lead, signup, demo) to align CTAs.

## Workflow
1. **Baseline Snapshot** – capture current rankings, traffic, SERP snippet, schema.
2. **Gap Analysis** – compare page structure vs ranking competitors, search intent alignment.
3. **Optimization Plan** – recommend updates for title/meta, headings, copy depth, media, CTAs, internal links.
4. **Technical Check** – validate core web vitals, structured data, mobile usability.
5. **Measurement Plan** – document KPIs, publish date, refresh reminders.

## Outputs
- Optimization diff (table of recommended changes).
- Updated metadata + structured data snippets.
- Internal link recommendations and CTA experiments.

## Agent/Skill Invocations
- `content-optimizer` – crafts updated copy/brief.
- `on-page` skill – enforces placement/checklists.
- `technical-seo-lead` – ensures performance/schema compliance.

---
