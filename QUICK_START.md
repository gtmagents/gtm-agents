# 🚀 Quick Start Guide for GTM Teams

> **👋 Never used Claude Code before?** Check out our [Getting Started Guide](GETTING_STARTED.md) first! It walks you through installation, setup, and your first commands step-by-step.

## 5-Minute Setup

### Recommended Baseline: GTM Essentials ⚙️
Before installing role-specific plugins, make sure the four GTM Essentials MCP tools are configured. They power code navigation, live docs, structured reasoning, and browser QA across GTM workflows.

1. Follow the installation guide in [`docs/gtm-essentials.md`](docs/gtm-essentials.md) to set up **Serena**, **Context7**, **Sequential Thinking**, and **Playwright**.
2. Verify each tool runs (`serena --help`, `context7 --version`, etc.) and record versions in `docs/audit-log.md` during onboarding.
3. Reference the "Usage Patterns" table in that doc to know which GTM plugins leverage each tool (e.g., marketing-analytics + Context7, campaign-orchestration + Sequential Thinking).

Once the essentials are installed, proceed with the role-specific steps below.

### For Sales Teams 💼

```bash
# 1. Add the marketplace (one-time setup)
/plugin marketplace add gtmagents/gtm-agents

# 2. Install essential sales plugins
/plugin install sales-prospecting
/plugin install sales-pipeline
/plugin install sales-enablement

# 3. Start generating leads immediately
/sales-prospecting:generate-leads --criteria "Your ICP here"
```

**Your first lead list will be ready in seconds!**

### For Marketing Teams 📣

```bash
# 1. Add the marketplace (one-time setup)
/plugin marketplace add gtmagents/gtm-agents

# 2. Install essential marketing plugins
/plugin install content-marketing
/plugin install email-marketing
/plugin install campaign-orchestration

# 3. Create your first campaign
/campaign-orchestration:launch-campaign "Your Campaign Name"
```

**Your campaign strategy will be generated instantly!**

### For Growth Teams 📈

```bash
# 1. Add the marketplace (one-time setup)
/plugin marketplace add gtmagents/gtm-agents

# 2. Install essential growth plugins
/plugin install growth-experiments
/plugin install customer-analytics
/plugin install revenue-analytics

# 3. Analyze your metrics
/revenue-analytics:calculate-ltv
```

**Your analytics will be ready immediately!**

---

## Top 10 Commands Every GTM Pro Should Know

### 1. Find Your Next Best Customers
```bash
/sales-prospecting:generate-leads --criteria "Companies like [your best customer]"
```

### 2. Write Perfect Cold Emails
```bash
"Write a cold email to [prospect] at [company] about [value prop]"
# The cold-outreach skill activates automatically!
```

### 3. Create a Month of Content
```bash
/content-marketing:content-pipeline "Topic" --duration 1month
```

### 4. Analyze Your Pipeline Health
```bash
/sales-pipeline:analyze-pipeline --identify-risks
```

### 5. Build a Complete Campaign
```bash
/campaign-orchestration:launch-campaign "Campaign Name" --budget 50000
```

### 6. Segment Your Customers
```bash
/customer-analytics:segment-customers --method behavioral
```

### 7. Predict Customer Churn
```bash
/customer-analytics:predict-churn --timeframe 90days
```

### 8. Create Sales Battlecards
```bash
/sales-enablement:create-battlecard --competitor "Competitor Name"
```

### 9. Design A/B Tests
```bash
/growth-experiments:design-experiment --hypothesis "Your hypothesis"
```

### 10. Calculate Marketing ROI
```bash
/marketing-analytics:calculate-roi --campaign "Campaign Name"
```

---

## Real-World Scenarios

### Scenario 1: "I need leads for next week's outreach"
```bash
/sales-prospecting:generate-leads \
  --criteria "SaaS, Series A, 50-200 employees" \
  --count 100 \
  --enrich comprehensive
```
**Result**: 100 qualified leads with contact info and personalized talking points

### Scenario 2: "We're launching a new product next month"
```bash
/campaign-orchestration:launch-campaign \
  "Q2 Product Launch" \
  --type product-launch \
  --timeline 4weeks
```
**Result**: Complete campaign plan with timeline, assets, and channel strategy

### Scenario 3: "Our email open rates are dropping"
```bash
/email-marketing:optimize-campaign \
  --metric open-rate \
  --test subject-lines
```
**Result**: A/B test variations and optimization recommendations

### Scenario 4: "I need content for the next quarter"
```bash
/content-marketing:content-pipeline \
  "Industry Trends" \
  --duration 3months \
  --frequency weekly
```
**Result**: 12-week editorial calendar with topics, keywords, and distribution plan

### Scenario 5: "Which accounts should we focus on?"
```bash
/abm-orchestration:target-accounts \
  --tier 1 \
  --potential high \
  --buying-signals active
```
**Result**: Prioritized account list with engagement strategies

---

## Pro Tips 💡

### 1. Start Simple, Then Expand
Begin with basic commands, then add parameters:
```bash
# Simple
/sales-prospecting:generate-leads

# Advanced
/sales-prospecting:generate-leads \
  --criteria "enterprise fintech" \
  --intent-score 80+ \
  --contacts 5 \
  --enrich comprehensive
```

### 2. Use Natural Language
Just describe what you need:
```
"I need to create a webinar follow-up email sequence for people who attended 
but didn't convert"
```
The right agents and skills will activate automatically!

### 3. Chain Commands for Workflows
```bash
# Generate leads → Create sequences → Schedule sends
/sales-prospecting:generate-leads | \
/sales-prospecting:build-sequence | \
/email-marketing:schedule-campaign
```

### 4. Save Time with Aliases
```bash
# Create shortcuts for common tasks
/alias create weekly-leads \
  "/sales-prospecting:generate-leads --criteria 'my ICP' --count 50"

# Use it anytime
/weekly-leads
```

### 5. Ask for Help Anytime
```bash
# Get command help
/help sales-prospecting

# See examples
/examples generate-leads

# Get suggestions
"What's the best way to improve email open rates?"
```

---

## Common Questions

**Q: Do I need technical knowledge?**
A: No! These plugins are designed for business users. Just describe what you need in plain English.

**Q: How accurate is the data?**
A: We use multiple data sources and verification methods. Accuracy typically exceeds 95% for contact information.

**Q: Can I integrate with my existing tools?**
A: Yes! Plugins support exports to Salesforce, HubSpot, and most major GTM platforms.

**Q: What about data privacy?**
A: All plugins are GDPR/CCPA compliant with enterprise-grade security.

**Q: How much does this cost in tokens?**
A: Plugins use efficient token management. A typical command uses 100-500 tokens.

---

## Get Started Now!

1. **Pick your role**: Sales, Marketing, or Growth
2. **Install plugins**: Use the commands above
3. **Try one command**: Start with something simple
4. **See results**: Get immediate value
5. **Explore more**: Discover advanced features as you go

**Remember**: You don't need to learn everything at once. Start with one plugin and one command. The AI agents will guide you!

---

## Need More Help?

- 📖 [Full Documentation](usage-guide.md)
- ⚙️ [GTM Essentials Setup](docs/gtm-essentials.md)
- 🔧 [All Plugins](../README.md#plugin-categories)
- 💬 [Join Slack Community](https://join.slack.com/t/gtmagents/shared_invite/zt-3iubtzxrn-RpYOb0fPFnTtdoZVcZK3Ww)
- 💬 Ask Claude: "How do I [your task]?"
- 🎯 [Examples](examples/) - Real-world use cases

**Welcome to the future of GTM work! 🚀**
