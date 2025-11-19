---
name: optimize-deliverability
description: Diagnoses email deliverability issues and produces remediation steps.
usage: /email-marketing:optimize-deliverability --issue spam-folder --domain example.com
---

# Command: optimize-deliverability

## Inputs
- **issue** – primary symptom (spam-folder, bounce-spike, low-open, blacklist, reputation-drop).
- **domain** – sending domain or subdomain experiencing issues.
- **volume_change** – optional volume delta % to assess sudden scaling.
- **ip_pool** – optional dedicated/shared IP identifier.

## Workflow
1. **Signal Intake** – gather metrics (opens, clicks, spam, bounces, blocklist hits, complaint rate).
2. **Infrastructure Review** – authenticate SPF/DKIM/DMARC/BIMI status, TLS, reverse DNS, feedback loops.
3. **Reputation Analysis** – evaluate Postmaster, SNDS, Talos, Barracuda, Spamhaus signals.
4. **Audience Health** – inspect segmentation, engagement tiers, inactivity policies, data collection sources.
5. **Content Audit** – scan for spam triggers, code issues, heavy imagery, link redirection.
6. **Remediation Plan** – propose warmup ramps, segmentation filters, copy tweaks, infrastructure fixes.

## Outputs
- Deliverability diagnostic report (tables for reputation, infrastructure, audience, content).
- Action plan prioritized by impact vs effort.
- Monitoring checklist with KPIs and time horizons.

## Agent/Skill Invocations
- `deliverability-analyst` – leads investigation and remediation plan.
- `deliverability` skill – references playbooks for IP warmups, segmentation adjustments, authentication.

---
