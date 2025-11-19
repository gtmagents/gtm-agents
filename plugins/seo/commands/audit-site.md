---
name: audit-site
description: Runs a technical SEO audit covering crawlability, indexation, and performance.
usage: /seo:audit-site --domain example.com --scope "core pages" --depth 3
---

# Command: audit-site

## Inputs
- **domain** – root domain or subdomain to audit.
- **scope** – optional focus (core pages, blog, docs, regional site).
- **depth** – crawl depth (default 3 levels).
- **include_logfiles** – flag indicating whether log files are available.

## Workflow
1. **Crawl Setup** – configure crawler (user agent, JS rendering, throttling) and run sample crawl.
2. **Issue Detection** – flag broken links, duplicate content, redirect chains, orphan pages, sitemap gaps.
3. **Technical Checks** – review Core Web Vitals, structured data coverage, hreflang, canonical tags, robots directives.
4. **Indexation Review** – compare sitemap vs Search Console coverage, identify noindex/blocked assets.
5. **Action Plan** – prioritize fixes with owners, dependencies, and estimated effort.

## Outputs
- Audit summary deck and spreadsheet with severity scoring.
- Ticket-ready backlog grouped by theme (performance, crawlability, content, infra).
- Monitoring recommendations (alerts, dashboards, regression tests).

## Agent/Skill Invocations
- `technical-seo-lead` – leads crawl and action plan.
- `technical-seo` skill – provides diagnostic templates and remediation references.
- `keyword-research` skill – aligns technical fixes with priority keyword clusters when relevant.

---
