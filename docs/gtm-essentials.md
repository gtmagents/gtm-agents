# GTM Essentials Infrastructure

_Last updated: 2025-11-18_

## Overview
GTM teams should always have four foundational MCP tools ready: **Serena**, **Context7**, **Sequential Thinking**, and **Playwright**. This guide explains how to configure them so revenue teams can run audits, pull current documentation, reason through complex programs, and QA digital experiences without leaving Claude Code.

Use this document whenever you:
- Spin up a fresh GTM workspace and need deterministic tooling.
- Audit whether contributors still have the required MCP servers installed.
- Need concrete prompts/use cases for these tools inside GTM plugins.

## Tool Summary
| Tool | Purpose | Primary GTM Use Cases |
| --- | --- | --- |
| **Serena** | Semantic code navigation + manipulation via LSP. | Inspect/edit CRM automation scripts, landing-page snippets, data pipeline transforms used by RevOps. |
| **Context7** | Live documentation fetcher for open-source repos + major frameworks. | Pull latest Salesforce, HubSpot, GA4, and marketing automation docs during analysis or implementation. |
| **Sequential Thinking** | Structured reasoning harness that enforces step-by-step planning. | Campaign orchestration, pursuit strategies, troubleshooting funnels with explicit hypotheses. |
| **Playwright** | Browser automation, screenshots, PDF exports, web QA. | Validate landing pages, capture creative reviews, confirm tracking pixels + form flows pre-launch. |

## Installation & Configuration Checklist
Follow these steps per workstation (macOS/Linux/WSL). Windows users should adapt commands accordingly.

### Prerequisites
- **Node.js ≥ 18** (`node --version`)
- **Python 3.8+** for Serena/uv
- **curl** and **npm** available in shell

### Step 1 – Install `uv`
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
# restart shell or source ~/.zshrc
```

### Step 2 – Install Serena
```bash
uv tool install serena  # installs the binary + language servers on first run
```
Additional language requirements:
- Go: `go install golang.org/x/tools/gopls@latest`
- Rust: `rustup component add rust-analyzer`
- TypeScript/JS: bundled automatically

### Step 3 – Install Context7
```bash
npm install -g context7
# Optional: export CONTEXT7_TOKEN=your_api_key for higher rate limits
```

### Step 4 – Install Sequential Thinking
```bash
npm install -g sequential-thinking
```

### Step 5 – Install Playwright
```bash
npm init playwright@latest  # or
npx playwright install chromium
```
Expect ~200MB disk usage for Chromium binaries; document the install path if using shared runners.

## Usage Patterns by Plugin
| Plugin | Tool | Example Prompt |
| --- | --- | --- |
| `marketing-analytics` | Context7 | "Use Context7 to pull the latest GA4 event parameter reference, then update the measurement section accordingly." |
| `campaign-orchestration` | Sequential Thinking | "Invoke Sequential Thinking to reason through launch dependencies and produce a step-by-step execution plan." |
| `sales-operations` | Serena | "Open the RevOps automation repo and insert a logging statement after the `update_pipeline_health` function." |
| `content-marketing` | Playwright | "Run a Playwright script to capture screenshots of the new landing page hero section across desktop & mobile." |

## Troubleshooting & Maintenance
1. **Version Drift**: record tool versions monthly in `docs/audit-log.md`.
2. **Credential Issues**: Context7 may rate-limit anonymous traffic—set `CONTEXT7_TOKEN` when pulling heavy documentation.
3. **Playwright Storage**: clean `~/Library/Caches/ms-playwright` (mac) or equivalent if CI runners are constrained.
4. **Automation Hooks**: add `scripts/check_gtm_essentials.sh` (future) to Husky pre-commit to verify tools present.

## Integration Tips
- Reference this doc from QUICK_START and relevant SKILL.md files so users know when to reach for each tool.
- Encourage contributors to log MCP server issues in `docs/audit-log.md` alongside remediation steps.
- When adding new GTM skills, specify which of the four tools unlock deterministic workflows (e.g., “Requires Serena for codebase edits”).

## Next Updates
- Add screenshots/GIFs showing each tool in use.
- Provide sample scripts for Playwright-based landing page QA.
- Document Context7 repo coverage relevant to GTM (Salesforce docs, HubSpot templates, etc.).
