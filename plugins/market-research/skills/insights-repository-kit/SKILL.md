---
name: insights-repository-kit
description: Governance + tooling pattern for storing research artifacts, tagging,
  and discovery.
---

# Insights Repository Kit Skill

## When to Use
- Archiving research deliverables, raw data, transcripts, and notes.
- Enabling self-serve discovery of past research to prevent duplicate studies.
- Setting up governance for access control, tagging, and retention policies.

## Framework
1. **Structure** – libraries for briefs, raw data, synthesis, decision logs, assets.
2. **Metadata** – tags for persona, lifecycle, product area, method, confidence, expiry.
3. **Access & Permissions** – roles for contributors, reviewers, consumers, legal.
4. **Versioning** – changelog, superseded flags, linkage to experiments or roadmap items.
5. **Discovery** – search templates, digest generation, and notification hooks.

## Templates
- Repository IA diagram + folder/Notion/database schema.
- Metadata dictionary with tag definitions and required fields.
- Intake/update form for adding new studies with validation logic.

## Tips
- Automate ingestion from survey tools and recording platforms when possible.
- Require executive summaries + decisions so assets stay actionable.
- Pair with `run-market-landscape-study` and `orchestrate-qualitative-lab` to auto-file outputs.

---
