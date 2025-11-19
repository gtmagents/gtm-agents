---
name: quality-gates
description: Use when establishing tests, monitoring, and incident response for analytics
  models.
---

# Analytics Quality Gates Skill

## When to Use
- Designing validation steps for new models or dashboards.
- Setting up automated data quality monitoring.
- Running incident reviews after data breaks.

## Framework
1. **Test Coverage** – schema, freshness, unique, referential, accepted values, volume thresholds.
2. **Alerting** – severity tiers, alert channels, on-call rotation, escalation policies.
3. **Incident Response** – triage checklist, communication templates, resolution targets.
4. **Change Management** – approval workflow, rollback plan, audit logging.
5. **Postmortems** – root cause analysis, remediation tasks, knowledge base updates.

## Templates
## Templates
- **QA Checklist**: See `assets/qa_checklist.md` for validation steps.
- **Quality matrix** (model/table → tests → owner → SLA).
- **Incident playbook** (trigger, response steps, communication log).
- **Change request form** with risk assessment.

## Tips
- Tie quality gates to CI/CD or dbt Cloud jobs to block bad deploys.
- Keep alert fatigue low by tuning thresholds.
- Document every incident for future prevention.

---
