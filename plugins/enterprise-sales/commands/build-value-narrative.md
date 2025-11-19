---
name: build-value-narrative
description: Produces ROI/TCO models, executive storylines, and proof appendices for complex deals.
usage: /enterprise-sales:build-value-narrative --deal "GlobalCo ERP" --industry manufacturing --scenario base,upside --audience "CFO,CIO"
---

# Command: build-value-narrative

## Inputs
- **deal** – opportunity identifier.
- **industry** – customer industry to align benchmarks.
- **scenario** – comma-separated scenarios (base, upside, downside).
- **audience** – target exec roles for tailoring (CFO, CIO, COO, Procurement).
- **assumptions** – optional JSON overrides for metrics (ACV, adoption, productivity).

## Workflow
1. **Data Intake** – ingest discovery notes, product telemetry, benchmarks, and reference stories.
2. **Impact Modeling** – calculate ROI/TCO scenarios with sensitivity toggles.
3. **Narrative Crafting** – outline headline, drivers, proof, and decision asks per audience.
4. **Asset Assembly** – create deck, one-pager, and calculator outputs with transparent assumptions.
5. **Review & Packaging** – capture approvals, version history, and attach to deal room.

## Outputs
- Scenario-based ROI/TCO workbook.
- Executive value narrative deck + one-pager.
- Proof appendix with benchmarks, customer stories, and links.

## Agent/Skill Invocations
- `value-architect` – leads modeling + storyline.
- `pursuit-director` – ensures alignment with pursuit milestones.
- `procurement-strategist` – validates commercial guardrails.
- `value-story-framework` skill – structures the narrative.
- `cxo-briefing-kit` skill – packages outputs for executive audiences.

---
