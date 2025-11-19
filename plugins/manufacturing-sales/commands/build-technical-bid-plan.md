---
name: build-technical-bid-plan
description: Generates bid plan covering solution architecture, validation steps, pricing, and approvals.
usage: /manufacturing-sales:build-technical-bid-plan --account "Northwind Plants" --scope "Smart Factory" --format deck --value-driver productivity
---

# Command: build-technical-bid-plan

## Inputs
- **account** – pursuit/account identifier.
- **scope** – program or initiative name (smart factory, robotics retrofit, energy efficiency).
- **format** – deck | memo | docset.
- **value-driver** – productivity | quality | safety | sustainability | cost.
- **deadline** – proposal due date or milestone.

## Workflow
1. **Requirement Consolidation** – compile RFP sections, specs, standards, and success criteria.
2. **Architecture & BOM Draft** – outline solution components, partner roles, and integration points.
3. **Validation & Pilot Plan** – define proof points, resources, and KPIs.
4. **Commercial Modeling** – produce pricing scenarios, incentives, and financing options.
5. **Approval & Submission Timeline** – map approvers, document owners, and key dates.

## Outputs
- Technical bid plan with architecture diagrams, BOM, and narrative.
- Validation/pilot schedule with owners and resource plan.
- Pricing/ROI appendix plus approval checklist.

## Agent/Skill Invocations
- `technical-solutions-architect` – authors architecture + validation plan.
- `industrial-account-director` – aligns executive narrative + approvals.
- `technical-bid-library` skill – injects reusable modules and compliance boilerplate.
- `partner-integration-kit` skill – ensures partner artifacts and testing plans are included.

---
