---
name: launch-brand-kit
description: Packages updated brand guidelines, assets, and enablement resources for GTM teams.
usage: /design-creative:launch-brand-kit --audience "marketing,sales,product" --includes "logo,templates,messaging" --launch 2025-12-01
---

# Command: launch-brand-kit

## Inputs
- **audience** – teams to notify (marketing, sales, product, success, partners).
- **includes** – components to package (logo, templates, messaging, photography, motion).
- **launch** – go-live date for the brand kit.
- **channels** – optional distribution channels (Notion, Figma, email, LMS).
- **training** – true/false to include enablement session outline.

## Workflow
1. **Inventory & Audit** – gather latest brand assets, guidelines, and approvals.
2. **Packaging** – organize kits (logos, typography, color, templates, messaging) with metadata.
3. **Communication Plan** – craft announcements, changelog, and adoption instructions.
4. **Enablement Plan** – outline training session, office hours, and certification checklists if enabled.
5. **Measurement** – define adoption metrics (downloads, requests, usage feedback) and feedback loop.

## Outputs
- Brand kit index with download links and usage guidance.
- Communication + enablement plan.
- Adoption tracker template with KPIs and feedback log.

## Agent/Skill Invocations
- `brand-strategist` – ensures messaging + guidelines are up to date.
- `creative-director` – reviews visual direction and approvals.
- `design-ops-lead` – manages asset packaging + access.
- `brand-governance` skill – enforces versioning + usage policies.
- `enablement-kit` skill – builds training plan + feedback forms.

---
