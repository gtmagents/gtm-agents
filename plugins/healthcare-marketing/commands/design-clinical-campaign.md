---
name: design-clinical-campaign
description: Produces clinical-grade campaign brief with targeting, creative guidance, and review plan.
usage: /healthcare-marketing:design-clinical-campaign --product "Cardio AI" --audience providers --channels email,webinar,field --evidence dossier.pdf
---

# Command: design-clinical-campaign

## Inputs
- **product** – product/treatment/service being promoted.
- **audience** – providers | payers | patients | mixed.
- **channels** – comma-separated (email, webinar, paid_social, display, field, events, referral).
- **evidence** – optional link/file with clinical studies, claims, or testimonials.
- **objectives** – KPIs (leads, enrollments, prescriptions, education, adherence).

## Workflow
1. **Evidence Review** – summarize key claims, safety considerations, and regulatory constraints.
2. **Audience Targeting** – define personas, segments, and channel mix per audience.
3. **Messaging Architecture** – craft value pillars, proof points, disclaimers, and CTAs.
4. **Creative & Content Plan** – outline asset list, KOL content, and required approvals.
5. **Launch & Measurement Plan** – specify KPIs, dashboards, and post-launch reporting cadence.

## Outputs
- Clinical campaign brief (messaging framework, creative requirements, timeline).
- Compliance checklist with assigned reviewers and deadlines.
- Measurement plan document with KPI definitions + reporting cadence.

## Agent/Skill Invocations
- `clinical-campaign-strategist` – leads narrative and targeting decisions.
- `compliance-marketing-director` – injects regulatory guidance + review path.
- `clinical-proof-library` skill – sources evidence and proof points.
- `patient-journey-mapping` skill – aligns messaging to journey stages.

---
