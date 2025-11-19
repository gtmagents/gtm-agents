---
name: qualify-industrial-opportunity
description: Scores complex manufacturing opportunity, stakeholder map, and pursuit recommendation.
usage: /manufacturing-sales:qualify-industrial-opportunity --account "Northwind Plants" --deal-size 18m --timeline 6m --region emea
---

# Command: qualify-industrial-opportunity

## Inputs
- **account** – customer or program name.
- **deal-size** – estimated ACV or TCV.
- **timeline** – months to decision/close.
- **region** – apac | emea | amer | latam.
- **partner-ecosystem** – optional list of required partners/vendors.

## Workflow
1. **Signals Intake** – gather intel from CRM, partner notes, install base, and exec briefings.
2. **Stakeholder & Requirement Map** – identify buying centers (operations, engineering, finance, IT/OT, procurement).
3. **Maturity & Fit Assessment** – compare pains vs solution capabilities, gaps, and competitive position.
4. **Pursuit Readiness** – evaluate resources needed (technical, partners, funding) and risk profile.
5. **Recommendation** – go/no-go with action plan, exec asks, and next milestones.

## Outputs
- Opportunity qualification brief with scoring, fit analysis, and risk register.
- Stakeholder map and pursuit org chart.
- Next-steps tracker (workstreams, owners, dates).

## Agent/Skill Invocations
- `industrial-account-director` – leads qualification + exec alignment.
- `channel-integration-program-manager` – reviews partner dependencies.
- `account-based-blueprint` skill – enforces account intelligence template.
- `deal-health-dashboard` skill – sources KPI snapshot for leadership.

---
