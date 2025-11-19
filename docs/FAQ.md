# Frequently Asked Questions (FAQ)

## Getting Started

### What is Claude GTM Agents?
Claude GTM Agents is a free, open-source collection of 67 specialized plugins for Claude Code that help sales, marketing, and growth teams automate their daily work. Think of it as having 92 AI assistants ready to help with tasks like finding leads, writing emails, creating content, and analyzing data.

### Do I need to know how to code?
**No!** Claude GTM Agents is designed for business users with zero coding experience. You simply type what you want to do in plain English, and the AI agents do the work for you.

### How much does it cost?
**It's completely free!** Claude GTM Agents is open-source (MIT licensed), which means you can use it forever without paying anything. If you find it valuable, you can optionally [support the project](https://buymeacoffee.com/gtmagents).

### What's the difference between Claude Code and Claude GTM Agents?
- **Claude Code** is the platform (like a web browser)
- **Claude GTM Agents** is a plugin marketplace you add to Claude Code (like browser extensions)

Think of it this way: Claude Code is your car, and GTM Agents are the specialized tools in your trunk.

### How long does it take to get started?
Most users are up and running in **10-15 minutes**. Follow our [Getting Started Guide](GETTING_STARTED.md) for step-by-step instructions.

---

## Installation & Setup

### How do I install Claude Code?
1. Visit [code.claude.com](https://code.claude.com)
2. Download for your operating system (Windows, macOS, or Linux)
3. Run the installer
4. Sign in with your Anthropic account

See our [Getting Started Guide](GETTING_STARTED.md) for detailed instructions.

### How do I add the GTM Agents marketplace?
Once Claude Code is installed:
1. Open Claude Code
2. Type: `/plugin marketplace add gtmagents/gtm-agents`
3. Press Enter

That's it! You now have access to all 67 plugins.

### How do I install a plugin?
After adding the marketplace:
1. Type: `/plugin install [plugin-name]`
2. For example: `/plugin install sales-prospecting`

Or browse available plugins by typing: `/plugin`

### Which plugins should I install first?
It depends on your role:

**Sales Reps:**
- `sales-prospecting` - Find and qualify leads
- `sales-calls` - Prepare for and analyze calls
- `email-marketing` - Create outreach sequences

**Marketers:**
- `content-marketing` - Create blog posts and content
- `campaign-orchestration` - Manage campaigns
- `social-media` - Plan social content

**Growth Teams:**
- `growth-experiments` - Design and run experiments
- `customer-analytics` - Analyze customer data
- `revenue-analytics` - Track key metrics

See [Quick Start Guide](QUICK_START.md) for role-specific recommendations.

---

## Using Plugins

### How do I use a plugin after installing it?
Each plugin has commands you can run. For example:
```
/sales-prospecting:generate-leads
```

You can also just describe what you want in plain English:
```
"Generate 50 leads for SaaS companies in fintech"
```

The right agents will activate automatically!

### What's the difference between agents, commands, and skills?
- **Agents** - AI assistants with specific expertise (e.g., "lead-researcher")
- **Commands** - Tools you can run (e.g., "generate-leads")
- **Skills** - Knowledge packages that activate when needed (e.g., "cold-outreach")

As a user, you don't need to worry about these distinctions - just describe what you want!

### Can I use multiple plugins together?
**Yes!** Plugins are designed to work together. For example:
1. Use `sales-prospecting` to find leads
2. Use `email-marketing` to create outreach sequences
3. Use `sales-pipeline` to track progress

### How do I see what a plugin can do?
Type: `/help [plugin-name]`

For example: `/help sales-prospecting`

This shows all available commands and examples.

---

## Common Tasks

### How do I generate leads?
1. Install: `/plugin install sales-prospecting`
2. Run: `/sales-prospecting:generate-leads`
3. Describe your ideal customer (e.g., "B2B SaaS, 50-200 employees")
4. Get your lead list!

### How do I create content?
1. Install: `/plugin install content-marketing`
2. Run: `/content-marketing:generate-blog`
3. Enter your topic
4. Get a complete blog post with SEO optimization!

### How do I build an email sequence?
1. Install: `/plugin install email-marketing`
2. Run: `/email-marketing:design-campaign`
3. Describe your audience and goal
4. Get a multi-touch email sequence!

### How do I analyze my pipeline?
1. Install: `/plugin install sales-pipeline`
2. Run: `/sales-pipeline:audit-pipeline`
3. Connect your CRM data
4. Get health scores and recommendations!

---

## Troubleshooting

### The plugin isn't working. What should I check?
1. **Is Claude Code running?** Make sure it's open
2. **Is the plugin installed?** Type `/plugin` to see installed plugins
3. **Is the command correct?** Check spelling and syntax
4. **Do you have internet?** Plugins need connectivity

### I get an error message. What does it mean?

**"Plugin not found"**
- The plugin isn't installed yet
- Solution: Install it with `/plugin install [name]`

**"Command not recognized"**
- Typo in the command name
- Solution: Type `/help [plugin-name]` to see available commands

**"Marketplace not found"**
- The marketplace isn't added yet
- Solution: Add it with `/plugin marketplace add gtmagents/gtm-agents`

**"Rate limit exceeded"**
- You've made too many requests too quickly
- Solution: Wait a few minutes and try again

### How do I update plugins?
Plugins update automatically when you restart Claude Code. To force an update:
```
/plugin update [plugin-name]
```

### How do I uninstall a plugin?
```
/plugin uninstall [plugin-name]
```

Your data and settings are preserved in case you reinstall later.

---

## Data & Privacy

### What data do the plugins access?
Plugins only access data you explicitly provide. They don't automatically read your files or access your accounts unless you give permission.

### Is my data secure?
Yes! All data processing happens through Claude's secure infrastructure. Your data is:
- Encrypted in transit
- Not stored permanently
- Not used to train models
- Subject to Anthropic's privacy policy

### Can I use this with confidential information?
Yes, but follow your company's data policies. If you're handling sensitive data:
- Review your company's AI usage policy
- Consider using Claude's enterprise tier
- Don't paste passwords or API keys directly

### Where is my data stored?
Data is processed in real-time and not permanently stored by the plugins. Any exports you create are saved locally on your computer.

---

## Performance & Limits

### How fast are the plugins?
Most commands complete in **5-30 seconds**. Complex workflows may take 1-2 minutes.

### Are there usage limits?
Limits depend on your Claude Code subscription:
- **Free tier**: Generous limits for personal use
- **Pro tier**: Higher limits for power users
- **Team/Enterprise**: Custom limits

See [Claude's pricing](https://claude.ai/pricing) for details.

### Can I use this for my whole team?
**Yes!** Each team member can install the plugins. For team-wide deployment, see our [Team Setup Guide](docs/team-setup.md).

### How many leads/posts/emails can I generate?
There's no hard limit, but we recommend:
- **Leads**: 50-100 per request for best quality
- **Content**: 1-5 pieces per request
- **Emails**: 3-7 email sequence

Larger batches may take longer or hit rate limits.

---

## Integration & Export

### Can I export results to my CRM?
Yes! Most plugins support export to:
- CSV files (import to any CRM)
- Salesforce
- HubSpot
- Other tools via API

### Can I integrate with other tools?
Many plugins support integrations. Check the plugin documentation for specific tools.

### How do I save my work?
Results are automatically saved in your Claude Code workspace. You can also:
- Export to CSV
- Copy to clipboard
- Save to files
- Send to other tools

---

## Pricing & Licensing

### Is this really free?
**Yes!** The plugins are 100% free and open-source (MIT License). You can:
- Use for personal or commercial purposes
- Modify and customize
- Share with your team
- No hidden fees or trials

### Do I need a Claude Code subscription?
You need access to Claude Code, which has:
- **Free tier**: Available to everyone
- **Pro tier**: $20/month for higher limits
- **Team tier**: Custom pricing

The GTM Agents plugins work with any tier.

### Can I use this commercially?
**Yes!** The MIT License allows commercial use. Use it to:
- Generate leads for your business
- Create content for clients
- Automate your sales process
- No royalties or fees required

---

## Support & Community

### How do I get help?
Multiple ways to get support:

1. **Documentation**: Check [docs/](docs/) for guides
2. **GitHub Discussions**: Ask questions and share ideas
3. **GitHub Issues**: Report bugs or request features
4. **Community**: Join our [Slack community](https://join.slack.com/t/gtmagents/shared_invite/zt-3iubtzxrn-RpYOb0fPFnTtdoZVcZK3Ww) for real-time help

### How do I report a bug?
1. Go to [GitHub Issues](https://github.com/gtmagents/gtm-agents/issues)
2. Click "New Issue"
3. Describe the problem
4. Include steps to reproduce

We typically respond within 24-48 hours.

### How do I request a feature?
Same process as bug reports, but choose "Feature Request" template. Tell us:
- What you want to do
- Why it would be helpful
- Your use case

### Can I contribute?
**Absolutely!** We welcome contributions:
- New plugins
- Documentation improvements
- Bug fixes
- Feature enhancements

See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

---

## Advanced Usage

### Can I create custom plugins?
Yes! Follow our [Plugin Development Guide](docs/plugin-development.md) to create your own.

### Can I modify existing plugins?
Yes! The code is open-source. Fork the repo and customize as needed.

### Can I run this offline?
No, plugins require internet connectivity to work with Claude's AI models.

### Can I automate workflows?
Yes! Many plugins support automation and can be chained together. See [Workflow Automation Guide](docs/workflows.md).

---

## Comparison Questions

### How is this different from ChatGPT plugins?
- **Specialized for GTM**: Built specifically for sales, marketing, and growth
- **Multi-agent**: Uses multiple specialized AI agents working together
- **Business-focused**: Designed for non-technical business users
- **Open-source**: Free, customizable, and transparent

### How is this different from Zapier/Make?
- **AI-powered**: Uses AI to understand and execute tasks
- **No setup required**: No complex workflows to build
- **Natural language**: Just describe what you want
- **GTM-specific**: Pre-built for common GTM tasks

### Should I use this or hire a VA?
Use both! GTM Agents handle:
- Repetitive tasks (lead research, content drafts)
- Data analysis
- Template creation
- Quick turnaround tasks

VAs are better for:
- Complex judgment calls
- Relationship building
- Custom creative work
- Strategic decisions

---

## Success Tips

### How can I get the most value?
1. **Start small**: Install 2-3 plugins for your top pain points
2. **Use daily**: Make it part of your routine
3. **Experiment**: Try different commands and approaches
4. **Share**: Teach your team what works
5. **Provide feedback**: Help us improve

### What are common mistakes to avoid?
1. **Installing too many plugins at once** - Start with 2-3
2. **Vague requests** - Be specific about what you want
3. **Not reading the output** - Review and refine results
4. **Expecting perfection** - AI is a tool, not magic
5. **Working in isolation** - Share learnings with your team

### How do I measure ROI?
Track:
- **Time saved**: Hours per week automated
- **Output increase**: More leads, content, etc.
- **Quality improvement**: Better results
- **Revenue impact**: Pipeline generated

Use our [ROI Calculator](docs/roi-calculator.md) to quantify value.

---

## Still Have Questions?

- 📖 [Read the full documentation](docs/)
- 💬 [Join the community discussion](https://github.com/gtmagents/gtm-agents/discussions)
- 🐛 [Report an issue](https://github.com/gtmagents/gtm-agents/issues)
- ☕ [Support the project](https://buymeacoffee.com/gtmagents)

**Can't find your answer?** [Open a discussion](https://github.com/gtmagents/gtm-agents/discussions) and we'll help you out!
