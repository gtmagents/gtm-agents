---
title: Phase 3 Orchestrator Build Plan
description: Outline of the next multi-agent orchestrator plugins to satisfy README claims.
---

# Phase 3 – Orchestrator Tranche (Draft)

This document captures the initial blueprint for the 18 orchestrator plugins promised in the README. Each entry lists:

- **Focus** – Business workflow addressed.
- **Planned Components** – Minimum commands, agents, and skills to author.
- **Dependencies** – Cross-plugin assets these orchestrators will rely on.
- **Notes** – Special considerations (e.g., telemetry, multi-plugin handoffs).

| Plugin ID | Focus | Planned Components | Dependencies | Notes |
| --- | --- | --- | --- | --- |
| `campaign-orchestration` (baseline) | Multi-channel campaign launch | Already built – use as pattern reference | Content, email, paid, analytics plugins | Ensure new orchestrators mirror depth |
| `abm-orchestration` | Account-based campaign coordination | 3 commands (target-accounts, plan-plays, monitor-abm), 3 agents (abm-strategist, account-planner, abm-analyst), 3 skills (account-tiering, personalization, intent-signals) | Sales-prospecting, data-enrichment, paid-media | Needs tight integration with CRM schemas |
| `lead-nurture-orchestration` | Automated nurture journeys from MQL → SQL | Commands: design-nurture, configure-branches, optimize-nurture. Agents: nurture-architect, marketing-ops, analytics partner. Skills: lifecycle-cadence, personalization-logic, nurture-testing | Marketing-automation, email-marketing, copywriting | Should reuse new smoke test + validator gating |
| `product-launch-orchestration` | GTM launch governance | Commands: assemble-war-room, run-launch, post-launch-retro. Agents: launch-director, workstream-lead, enablement-captain. Skills: tiering, war-room ops, risk playbooks | Product-marketing, campaign-orchestration, customer-marketing | Leverage `build-launch-plan` command outputs |
| `content-pipeline-orchestration` | Ideation → production → distribution for hero content | Commands: plan-pillar, manage-production, distribute-assets. Agents: editorial-director, creative-producer, distribution-lead. Skills: editorial-calendar, asset-tracking, distribution-checklist | Content-marketing, video-marketing, social-media | Should hook into asset metadata for smoke test |
| `analytics-pipeline` | Data capture → modeling → dashboards | Commands: define-events, build-model, ship-dashboards. Agents: data-strategist, modeling-lead, BI-publisher. Skills: instrumentation, quality gates, visualization patterns | Marketing-automation (data-orchestrator), revenue-analytics | Requires stricter validation for SQL snippets |
| `email-sequence-orchestration` | High-volume lifecycle email automation | Commands: plan-sequences, automate-delivery, analyze-sequences. Agents: email-architect, deliverability-lead, experiment-analyst. Skills: cadence-design, QA-gates, deliverability-ops (reuse) | Email-marketing, copywriting | Should re-use deliverability skill references |
| `sales-handoff-orchestration` | MQL → SQL routing + enablement | Commands: define-handoff, run-standups, monitor-SLA. Agents: revops-director, lifecycle-coordinator, sales-manager. Skills: routing-logic, SLA-tracking, enablement-kit | Sales-pipeline, marketing-automation | Needs CRM + MAP data contract spec |
| `personalization-engine` | Dynamic content and decisioning | Commands: define-profiles, configure-rules, monitor-personalization. Agents: personalization-architect, data-engineer, testing-lead. Skills: decision-trees, content-variants, governance | Copywriting, marketing-automation | Heavy dependency on customer-insights skill |
| `social-scheduler-orchestration` | Cross-network social calendar execution | Commands: plan-calendar, route-approvals, analyze-social. Agents: social-program-manager, asset-coordinator, analytics partner. Skills: calendar-governance, brand-guardrails, performance-metrics | Social-media plugin | Requires time zone + localization guidance |
| `seo-workflow-orchestration` | Keyword research → content → technical fixes | Commands: prioritize-keywords, deploy-optimizations, audit-technical. Agents: seo-director, on-page-lead, technical-analyst. Skills: keyword-strategy, publishing-process, diagnostics | SEO plugin | Should align with technical-seo skill outputs |
| `revenue-forecasting-pipeline` | Data ingestion and forecast refresh | Commands: ingest-pipeline, run-forecast, report-variance. Agents: forecast-architect, revops-analyst, finance-partner. Skills: forecast-modeling, variance-analysis, executive-briefs | Sales-pipeline, revenue-analytics | Needs metric definitions consistent with README claims |
| `customer-journey-orchestration` | 360° customer experience mapping | Commands: map-journey, prioritize-gaps, implement-actions. Agents: cx-strategist, research-lead, ops-owner. Skills: journey-mapping, voice-of-customer, governance | Customer-marketing, marketing-automation | Connects to lifecycle journeys built earlier |
| `community-orchestration` | Community programming + moderation | Commands: plan-community-calendar, run-community-event, measure-engagement. Agents: community-lead, moderator, analytics. Skills: community-ops, sentiment-analysis, escalation | Social-media, event-marketing | Requires moderation + compliance guidance |
| `referral-program-orchestration` | Referral incentive programs | Commands: design-referral, launch-program, optimize-referrals. Agents: referral-architect, lifecycle-ops, partner-manager. Skills: incentive-design, fraud-detection, partner-ops | Growth experiments, customer-marketing | Contains shared assets with partnership plugins |
| `partner-co-marketing-orchestration` | Joint campaigns with partners | Commands: co-plan-campaign, manage-assets, track-source. Agents: partner-marketer, asset-manager, analytics. Skills: co-branding, asset-approval, attribution | Event-marketing, campaign-orchestration | Need shared folder for co-brand templates |
| `intent-signal-orchestration` | Signal ingestion + activation workflows | Commands: connect-signals, prioritize-accounts, trigger-plays. Agents: intent-analyst, automation-lead, sales-liaison. Skills: signal-scoring, suppression-logic, outbound-plays | Data-enrichment-master, sales-prospecting | Will re-use enrichment orchestrator knowledge |
| `renewal-orchestration` | Renewal forecasting + play execution | Commands: forecast-renewals, orchestrate-renewal-play, run-retro. Agents: renewal-director, cs-ops, exec sponsor. Skills: renewal-playbooks, escalation-framework, deal-desk | Customer-marketing, sales-pipeline | Align metrics with NDR goals |
| `customer-feedback-orchestration` | Surveys → insights → roadmap loops | Commands: run-survey, synthesize-feedback, route-insights. Agents: research-lead, product-liaison, cs-analyst. Skills: survey-design, insight-synthesis, stakeholder-ops | Product marketing, customer marketing | Feed into roadmap + comms |

*(Campaign Orchestration already exists and will act as the reference template when implementing the remaining orchestrators.)*

## Initial Execution Order
1. **ABM Orchestration** – highest urgency per README promises, overlaps with sales + marketing.
2. **Lead Nurture Orchestration** – leverages new marketing automation assets.
3. **Product Launch Orchestration** – pairs with product marketing plugin completed earlier.
4. **Content Pipeline Orchestration** – supports cross-channel enablement.
5. Continue sequentially while integrating smoke-test + validation outputs in each PR.

## Next Actions
- Create directories under `plugins/` for each orchestrator following existing structure.
- Reuse new smoke test to ensure orchestrator assets stay in compliance.
- Update README counts and docs once first orchestrator tranche ships.
