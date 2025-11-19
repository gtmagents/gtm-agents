# Research Playbook: Finding Custom Signals

## The Research Mindset
**Bad research:** "Let me find their role and company size so I can plug them into my template."
**Good research:** "What is happening in their world RIGHT NOW that makes my solution urgent?"

The best cold emails feel like you've been watching their company for weeks. Signals must be:
1. **Specific** (not "you're growing" but "you hired 12 SDRs in Q4")
2. **Recent** (last 90 days ideally)
3. **Directionally aligned** with the pain your product solves

## Before Research: Define Your Perfect Signal
Complete this sentence for every campaign:
> "The ideal prospect would show evidence of **[specific behavior/change/problem]** because it means they're experiencing **[pain]** right now."

## Research Priority (10 Minutes Max)

### Tier 1: Case Studies (3 min) - START HERE
**Where to look:**
- Company website → /customers, /case-studies
- Blog → search for "case study"
- Press page

**What to extract:**
- Customer type/industry
- Problem solved
- Specific metric/outcome
- Timeframe

**Variables:** `{{case_study_company}}`, `{{case_study_result}}`, `{{case_study_metric}}`

### Tier 2: Custom Signals (6-7 min) - THE DIFFERENTIATOR
Hunt for campaign-specific signals using tools.

#### Tool 1: Claygent (AI Web Scraper)
- **Use for:** Pricing pages, case studies, news summaries.
- **Workflow:** "Find pricing page" → Scrape → "Summarize difference between Starter and Pro".

#### Tool 2: ZenRows (Full Page Scraper)
- **Use for:** Full text of pricing, about, blog pages.
- **Why:** Gets nuance that summaries miss.

#### Tool 3: Serper (Google Search API)
- **Use for:** Google Reviews, news mentions.
- **Workflow:** Search company → Get CID → Get reviews → Extract negative review details.

#### Tool 4: SimilarWeb (Competitor Intelligence)
- **Use for:** Traffic data, keyword overlap.
- **Workflow:** Compare domain to competitor → "Saw {{competitor}} is taking your keywords..."

#### Tool 5: LinkedIn
- **Use for:** Recent posts, hiring activity, tenure.
- **Workflow:** Check recent posts (topic, date), hiring (roles, count).

### Tier 3: Standard Variables (3-4 min) - BACKUP
- LinkedIn basics: Role, tenure.
- Company site: Blog topics, press.
- Hiring page: Open roles.

## Signal Freshness Rules
| Signal Type | Fresh Until |
|-------------|-------------|
| Funding news | 90 days |
| LinkedIn posts | 30 days |
| Hiring activity | 60 days |
| G2 reviews | 90 days |
| Negative review | 180 days |

## The "So What?" Test
Before using a signal, ask:
1. Is it recent?
2. Does it connect to MY offer?
3. Would THEY care that I noticed?
4. Can I tie it to a specific pain?

## When to Skip
If after 10 minutes you find no Tier 1/2 signals and can't tie anything to your offer:
- **Skip** or mark for later.
- **OR** use Whole Offer strategy if targeting is solid.
