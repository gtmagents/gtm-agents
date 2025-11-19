---
name: build-keyword-strategy
description: Generates intent-based keyword clusters and prioritization for SEO roadmaps.
usage: /seo:build-keyword-strategy --topic "revops automation" --locale en-US --tier 3
---

# Command: build-keyword-strategy

## Inputs
- **topic** – seed topic, product, or persona focus.
- **locale** – market/language (default en-US).
- **tier** – optional priority (1 = must-win, 3 = explore).
- **competitors** – optional competitor domains for SERP gap analysis.

## Workflow
1. **Seed Expansion** – build keyword universe via semantic expansion + intent variants.
2. **Classification** – bucket by funnel stage, search intent, and pillar vs cluster.
3. **Scoring** – attach volume, difficulty, SERP features, click potential.
4. **Gap Analysis** – compare against existing URLs + competitor coverage.
5. **Roadmap** – prioritize clusters with recommended owners, assets, and deadlines.

## Outputs
- Keyword cluster table (term, intent, volume, KD, current URL, opportunity).
- Pillar/cluster mapping visual (mermaid or table).
- Action plan with sprint-ready tasks.

## Agent/Skill Invocations
- `seo-architect` – oversees strategy and architecture.
- `keyword-research` skill – supplies research frameworks and quality gates.
- `technical-seo-lead` – validates feasibility for new pillar structures.

---
