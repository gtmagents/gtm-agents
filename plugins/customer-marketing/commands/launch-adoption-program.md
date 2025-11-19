---
name: launch-adoption-program
description: Generates an adoption program plan covering onboarding assets, automation, and success plays.
usage: /customer-marketing:launch-adoption-program --segment smb --product "AI Copilot" --objective activation
---

# Command: launch-adoption-program

## Inputs
- **segment** – customer cohort (SMB, MM, enterprise, vertical).
- **product** – product/feature focus.
- **objective** – activation, feature adoption, cross-sell readiness.
- **timeline** – optional start/end dates.
- **constraints** – optional notes (limited CS bandwidth, compliance, etc.).

## Workflow
1. **Program Intake** – review success goals, telemetry gaps, stakeholder expectations.
2. **Playbook Draft** – outline touchpoints (email/in-app, webinars, office hours, community).
3. **Content & Assets** – recommend guides, videos, success plan templates.
4. **Automation Wiring** – map triggers, tools, and routing rules (CS, marketing automation, product notifications).
5. **Measurement Plan** – define activation metrics, adoption goals, feedback loop.

## Outputs
- Adoption playbook timeline (touchpoint, owner, channel, asset).
- Asset checklist + content brief for gaps.
- Dashboard requirements + SLA tracker.

## Agent/Skill Invocations
- `adoption-program-manager` – drives execution + enablement.
- `expansion-plays` skill – suggests follow-on offers post-adoption.
- `customer-insights` skill – ensures telemetry signals are wired.

---
