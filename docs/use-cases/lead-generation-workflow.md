# Use Case: Generate 100 Qualified Leads

## Overview

**Problem:** You need to build a list of qualified prospects but manual research takes hours per lead.

**Solution:** Use the `sales-prospecting` plugin to automatically research and qualify 100 leads in under 5 minutes.

**Time Saved:** ~18 hours (from 20 hours of manual research to 10 minutes)

**ROI:** At $50/hour, that's $900 saved per 100 leads

---

## Who This Is For

- Sales Development Reps (SDRs)
- Account Executives
- Business Development Managers
- Founders doing their own outreach

---

## What You'll Get

✅ 100 company names with key details  
✅ Contact information for decision-makers  
✅ Personalized talking points for each lead  
✅ LinkedIn profiles and company websites  
✅ Firmographic data (size, industry, funding)  
✅ Export-ready CSV file for your CRM

---

## Prerequisites

- [ ] Claude Code installed
- [ ] GTM Agents marketplace added
- [ ] `sales-prospecting` plugin installed
- [ ] Clear idea of your Ideal Customer Profile (ICP)

**Don't have these yet?** See our [Getting Started Guide](../GETTING_STARTED.md).

---

## Step-by-Step Instructions

### Step 1: Define Your ICP (2 minutes)

Before generating leads, get clear on who you're targeting. Answer these questions:

**Industry:**
- What industry/vertical? (e.g., "B2B SaaS", "Healthcare", "Fintech")

**Company Size:**
- How many employees? (e.g., "50-200", "200-1000", "1000+")

**Funding Stage:**
- What funding stage? (e.g., "Series A", "Series B+", "Bootstrapped")

**Geography:**
- Where are they located? (e.g., "United States", "San Francisco Bay Area", "Global")

**Example ICP:**
```
B2B SaaS companies
50-200 employees
Series A or Series B funded
Located in the United States
Selling to enterprise customers
```

### Step 2: Run the Lead Generation Command (1 minute)

1. Open Claude Code
2. Type or paste:
   ```
   /sales-prospecting:generate-leads
   ```
3. Press Enter

### Step 3: Describe Your ICP (1 minute)

When prompted, describe your ideal customer. You can use natural language:

**Example 1 (Detailed):**
```
Generate 100 leads for B2B SaaS companies with 50-200 employees, 
Series A or B funded, located in the United States, that sell to 
enterprise customers. Focus on companies in sales automation, 
marketing tech, or customer success platforms.
```

**Example 2 (Simple):**
```
100 fintech companies, 100-500 employees, Series B+, in New York
```

**Example 3 (Very Specific):**
```
E-commerce companies using Shopify Plus, $10M+ annual revenue,
based in California, with a marketing team of 5+ people
```

### Step 4: Review the Results (2 minutes)

The plugin will generate your lead list. Review the output:

**What you'll see for each lead:**
- Company name
- Website URL
- Industry/vertical
- Employee count
- Funding information
- Decision-maker names and titles
- Contact information (email, LinkedIn)
- Personalized talking points

**Example output:**
```
Company: Acme SaaS Inc.
Website: acmesaas.com
Industry: B2B SaaS - Sales Automation
Employees: 150
Funding: Series A ($15M, 2023)
Decision Maker: Jane Smith, VP of Sales
Email: jane.smith@acmesaas.com
LinkedIn: linkedin.com/in/janesmith
Talking Points:
- Recently raised Series A to expand sales team
- Using legacy CRM, likely evaluating modern solutions
- Hiring 5 new AEs this quarter
- Pain point: Manual prospecting slowing down team
```

### Step 5: Export to Your CRM (1 minute)

1. Click "Export to CSV" or copy the results
2. Import into your CRM (Salesforce, HubSpot, etc.)
3. Or copy individual leads to your outreach tool

---

## Tips for Better Results

### Be Specific
❌ "SaaS companies"  
✅ "B2B SaaS companies selling to enterprise, 100-500 employees, Series B+"

### Use Multiple Criteria
Include 3-5 qualifying criteria for better targeting:
- Industry
- Company size
- Funding stage
- Geography
- Technology stack

### Iterate and Refine
Start with 25 leads, review quality, then adjust your criteria before generating the full 100.

### Combine with Other Signals
Add criteria like:
- "Recently raised funding"
- "Hiring for sales roles"
- "Using [competitor product]"
- "Mentioned [pain point] on social media"

---

## Common Variations

### By Industry

**SaaS:**
```
B2B SaaS companies, 50-200 employees, Series A+, selling to mid-market
```

**E-commerce:**
```
E-commerce brands, $5M+ revenue, using Shopify Plus, selling consumer goods
```

**Healthcare:**
```
Healthcare providers, 100+ beds, located in major metro areas, using Epic EHR
```

**Financial Services:**
```
Fintech companies, Series B+, focused on payments or lending, US-based
```

### By Company Size

**SMB:**
```
Small businesses, 10-50 employees, $1M-$10M revenue, [your industry]
```

**Mid-Market:**
```
Mid-market companies, 200-1000 employees, $20M-$100M revenue
```

**Enterprise:**
```
Enterprise companies, 1000+ employees, Fortune 2000, [your vertical]
```

### By Geography

**US-Focused:**
```
Companies in San Francisco, New York, or Austin, [other criteria]
```

**Global:**
```
Companies in EMEA, [other criteria], English-speaking markets
```

---

## Next Steps

### Immediate Actions
1. **Enrich the data** - Use `data-enrichment-master` plugin for additional details
2. **Build sequences** - Use `email-marketing` plugin to create outreach campaigns
3. **Track in CRM** - Import leads and set up follow-up tasks

### Follow-Up Workflows
1. **Day 1:** Import to CRM and assign to reps
2. **Day 2:** Send first outreach email (use `email-marketing` plugin)
3. **Day 5:** LinkedIn connection request
4. **Day 8:** Follow-up email
5. **Day 15:** Phone call attempt

### Measure Success
Track these metrics:
- Lead quality score (1-10)
- Response rate to outreach
- Meeting booking rate
- Pipeline generated
- Time saved vs. manual research

---

## Troubleshooting

### "Not enough leads found"
**Solution:** Broaden your criteria. Try:
- Wider employee range (50-500 instead of 50-100)
- Multiple industries
- Larger geography

### "Leads don't match my ICP"
**Solution:** Be more specific in your description. Add:
- Technology stack requirements
- Specific pain points
- Buying signals

### "Missing contact information"
**Solution:** Use the `data-enrichment-master` plugin to fill in gaps:
```
/data-enrichment-master:enrich-leads
```

### "Leads are outdated"
**Solution:** Add recency criteria:
```
"Companies that raised funding in the last 12 months"
"Companies actively hiring for [role]"
```

---

## Real User Example

> "I was spending 3-4 hours every Monday building my weekly prospect list. Now I run this command, get 100 leads in 5 minutes, and spend my time actually selling instead of researching. Game changer."
> 
> — Sarah M., SDR at TechCorp

**Sarah's Results:**
- **Before:** 20 hours/month on lead research
- **After:** 1 hour/month
- **Time saved:** 19 hours/month
- **Value:** $950/month (at $50/hour)
- **Pipeline impact:** +$75K in new opportunities

---

## Advanced Tips

### Combine Multiple Searches
Generate different lists for different segments:
```
1. /sales-prospecting:generate-leads "Series A SaaS, 50-100 employees"
2. /sales-prospecting:generate-leads "Series B SaaS, 100-200 employees"
3. /sales-prospecting:generate-leads "Bootstrapped SaaS, profitable, 50+ employees"
```

### Use Intent Signals
Add buying signals to your criteria:
```
"Companies using [competitor], recently raised funding, hiring sales roles"
```

### Create Territory Lists
Generate leads by territory:
```
"West Coast: CA, OR, WA"
"East Coast: NY, MA, NJ"
"Central: TX, IL, CO"
```

### Build Account Lists for ABM
For account-based marketing:
```
"Top 100 companies in [industry] by revenue, enterprise segment"
```

---

## Related Use Cases

- [Build a Cold Email Sequence](cold-email-sequence.md)
- [Enrich Lead Data](lead-enrichment.md)
- [Score and Prioritize Leads](lead-scoring.md)
- [Research Accounts for ABM](abm-account-research.md)

---

## Resources

- [Sales Prospecting Plugin Documentation](../plugin-reference.md#sales-prospecting)
- [ICP Template](../../templates/icp-template.md)
- [Lead Qualification Framework](../business-skills.md#lead-qualification)
- [CRM Import Guide](../integrations.md#crm-import)

---

**Questions?** [Ask in GitHub Discussions](https://github.com/gtmagents/gtm-agents/discussions)

**Found this helpful?** [Support the project ☕](https://buymeacoffee.com/gtmagents)
