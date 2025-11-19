---
name: design-onboarding-journey
description: Builds persona-specific onboarding journeys with milestones, messaging, and measurement.
usage: /product-led-growth:design-onboarding-journey --persona "Admin" --tier enterprise --channels in-app,email --window 30d
---

# Command: design-onboarding-journey

## Inputs
- **persona** – target persona or job-to-be-done (Admin, IC, Exec, Developer).
- **tier** – plan/tier focus (free, pro, enterprise, beta).
- **channels** – comma-separated channels (in-app, email, chat, docs).
- **window** – onboarding time horizon (7d, 14d, 30d, custom).
- **metrics** – optional activation KPIs to emphasize.

## Workflow
1. **Signal Review** – pull activation metrics, qualitative feedback, and experiment data.
2. **Milestone Mapping** – define aha moments, success metrics, and instrumentation requirements.
3. **Journey Blueprint** – lay out steps, channel mix, triggers, and dynamic variants.
4. **Enablement Pack** – create messaging, tutorials, and support resources.
5. **Measurement Plan** – document KPIs, guardrails, and reporting cadence.

## Outputs
- Journey blueprint (diagram + table) with steps, channels, triggers.
- Content/messaging kit aligned to persona + milestones.
- Measurement + experiment plan with owners and timelines.

## Agent/Skill Invocations
- `product-adoption-strategist` – architect journey + enablement.
- `usage-growth-scientist` – supplies activation data + experiment ideas.
- `onboarding-blueprint` skill – enforces structure + templates.
- `in-app-messaging-kit` skill – populates message library.

---
