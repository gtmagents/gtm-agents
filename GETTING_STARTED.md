# 🎯 Getting Started with Claude GTM Agents

**Welcome!** This guide will help you get up and running with Claude GTM Agents, even if you've never used Claude Code before.

## 📋 Table of Contents

- [Is This Guide For You?](#-is-this-guide-for-you)
- [What You'll Need](#what-youll-need)
- [Step 1: Install Claude Code](#step-1-install-claude-code)
- [Step 2: Set Up Your First Workspace](#step-2-set-up-your-first-workspace)
- [Step 3: Add the GTM Agents Marketplace](#step-3-add-the-gtm-agents-marketplace)
- [Step 4: Install Your First Plugins](#step-4-install-your-first-plugins)
- [Step 5: Try Your First Command](#step-5-try-your-first-command)
- [Next Steps](#next-steps)
- [Troubleshooting](#troubleshooting)
- [Quick Reference Card](#-quick-reference-card)
- [Learning Resources](#-learning-resources)
- [Frequently Asked Questions](#-frequently-asked-questions)
- [Need Help?](#-need-help)

---

## 🤔 Is This Guide For You?

This guide is perfect if you:

- ✅ Have **never used Claude Code** before
- ✅ Are **new to AI-powered tools** and want step-by-step instructions
- ✅ Need help with **installation and basic setup**
- ✅ Want to understand **what everything means** before diving in
- ✅ Prefer **detailed explanations** over quick commands

**Already have Claude Code installed?** Skip to the [Quick Start Guide](QUICK_START.md) instead.

**Looking for advanced features?** Check out the [Usage Guide](docs/usage-guide.md).

---

## What You'll Need

Before you begin, make sure you have:

- ✅ **A computer** running Windows, macOS, or Linux
- ✅ **Internet connection** for downloading and using Claude Code
- ✅ **Claude account** (you can sign up at [claude.ai](https://claude.ai))
- ✅ **10-15 minutes** to complete this setup

**No coding experience required!** This system is designed for business users.

---

## Step 1: Install Claude Code

### What is Claude Code?

Claude Code is an AI-powered coding assistant that helps you automate tasks, generate content, and streamline your work. Think of it as having an expert assistant who knows everything about sales, marketing, and growth.

### Installation Steps

### Native / Script Installer (Recommended)
*macOS / Linux / WSL:*
```bash
curl -fsSL https://claude.ai/install.sh | bash
```

*Windows PowerShell:*
```powershell
irm https://claude.ai/install.ps1 | iex
```

*Windows CMD:*
```cmd
curl -fsSL https://claude.ai/install.cmd -o install.cmd && install.cmd && del install.cmd
```

### Homebrew (macOS / Linux)
```bash
brew install --cask claude-code
```

### NPM (Node.js 18+ required)
```bash
npm install -g @anthropic-ai/claude-code
```
**Note:** Avoid using `sudo npm install -g` to prevent permission issues.

---

### Authentication & First Run
1.  Open a terminal and navigate into your project directory:
    ```bash
    cd /path/to/your/project
    ```
2.  Run Claude Code:
    ```bash
    claude
    ```
3.  You’ll be prompted to log in. You can sign in via:
    *   A Claude.ai account (Pro/Max subscription)
    *   Claude Console (API-key based)

4.  After login you’ll see the Claude Code interface. To verify it’s working, try:

    **Verify installation**
    - You should see the Claude Code interface with a chat window
    - Type "Hello" to confirm Claude responds

> **✨ Success!** If Claude responds to your message, you're ready to move on.

---

## Step 2: Set Up Your First Workspace

### What is a Workspace?

A workspace is like a project folder where Claude Code can access and manage files. For GTM Agents, you'll create a workspace to organize your sales, marketing, and growth work.

### Creating Your Workspace

1.  **Create a folder on your computer**
    ```
    📁 Documents/
       └── 📁 GTM-Work/
    ```
    - On **macOS**: Create a folder in your Documents called "GTM-Work"
    - On **Windows**: Create a folder in your Documents called "GTM-Work"

2.  **Open the folder in Claude Code**
    - In Claude Code, click **File → Open Folder** (or similar menu option)
    - Navigate to your newly created `GTM-Work` folder
    - Click **Select Folder** or **Open**

3.  **Confirm workspace is active**
    - You should see your folder name in the Claude Code sidebar or title bar
    - The workspace is now ready for use

> **💡 Tip:** You can create multiple workspaces for different projects (e.g., "Sales-Projects", "Marketing-Campaigns", etc.)

---

## Step 3: Add the GTM Agents Marketplace

### What is a Marketplace?

A marketplace is a collection of plugins (tools and agents) that you can install. The GTM Agents marketplace contains 67 specialized plugins for sales, marketing, and growth teams.

### Adding the Marketplace

1.  **Open the chat in Claude Code**
    - Make sure you're in your GTM-Work workspace

2.  **Type the following command** in the chat:
    ```
    /plugin marketplace add gtmagents/gtm-agents
    ```

3.  **Wait for confirmation**
    - Claude will respond confirming the marketplace has been added
    - This makes all 67 plugins available for installation but **does not load any agents or tools** into your context.

4.  **Browse available plugins** (optional)
    - Type `/plugin` to see all available plugins
    - You'll see a list organized by category

> **✨ Success!** You now have access to all GTM plugins, but they're not loaded yet (which saves memory and keeps things fast).

---

## Step 4: Install Your First Plugins

### Choosing Plugins Based on Your Role

You don't need to install all 67 plugins! Start with the essentials for your role:

#### 🎯 **For Sales Professionals**

Install these three essential plugins:

```
/plugin install sales-prospecting
/plugin install sales-pipeline
/plugin install sales-enablement
```

**What you get:**
- Lead generation and research tools
- Pipeline management and forecasting
- Sales playbooks and battlecards

---

#### 📣 **For Marketing Professionals**

Install these three essential plugins:

```
/plugin install content-marketing
/plugin install email-marketing
/plugin install campaign-orchestration
```

**What you get:**
- Content creation and editorial calendars
- Email campaign automation
- Multi-channel campaign planning

---

#### 📈 **For Growth/Analytics Professionals**

Install these three essential plugins:

```
/plugin install growth-experiments
/plugin install customer-analytics
/plugin install revenue-analytics
```

**What you get:**
- A/B testing and experiment design
- Customer segmentation and behavior analysis
- Revenue forecasting and metrics

---

#### 🎯 **Not sure? Start with the Universal Starter Pack**

If you work across multiple areas, install these versatile plugins:

```
/plugin install sales-prospecting
/plugin install content-marketing
/plugin install customer-analytics
```

---

## Managing Plugins

### List Installed Plugins

```bash
# All installed plugins
/plugin list

# Plugins from specific marketplace
/plugin list gtm-agents
```

---

### Installation Process

1.  **Copy the command** for your role (from above)
2.  **Paste it into Claude Code** chat, one line at a time
3.  **Press Enter** after each command
4.  **Wait for confirmation** that each plugin is installed

> **⏱️ Time:** Installing 3 plugins takes about 30 seconds total.

---

## Step 5: Try Your First Command

Now let's test your setup with a real task!

### Example 1: Generate Sales Leads (Sales)

If you installed sales plugins, try this:

```
/sales-prospecting:generate-leads --criteria "SaaS companies, 50-200 employees, Series A funding"
```

**What happens:**
- Claude will generate a list of qualified leads matching your criteria
- You'll get company names, contact information, and talking points
- Results appear in seconds!

---

### Example 2: Create Content (Marketing)

If you installed marketing plugins, try this:

```
/content-marketing:content-pipeline "AI in sales automation" --duration 1month
```

**What happens:**
- Claude creates a month-long content calendar
- You'll get blog topics, keywords, and publishing schedule
- Ready to use immediately!

---

### Example 3: Analyze Metrics (Growth)

If you installed analytics plugins, try this:

```
/customer-analytics:segment-customers --method behavioral
```

**What happens:**
- Claude analyzes customer behavior patterns
- You'll get segmentation recommendations
- Actionable insights for targeting!

---

### Using Natural Language (Works for Everyone!)

You can also just describe what you need in plain English:

```
"I need to write a cold email to a VP of Sales at a fintech company about our new CRM integration"
```

**What happens:**
- Claude automatically activates the right agents and skills
- You'll get a personalized, professional email draft
- No commands needed!

---

## Next Steps

### 🎓 Learn More

Now that you're set up, explore these resources:

1.  **[Quick Start Guide](QUICK_START.md)** - Top 10 commands and real-world scenarios
2.  **[Usage Guide](docs/usage-guide.md)** - Comprehensive command reference
3.  **[Plugin Reference](docs/plugin-reference.md)** - All 67 plugins explained
4.  **[Business Skills](docs/business-skills.md)** - 52 specialized skills you can use

### 🚀 Expand Your Toolkit

Install more plugins as you need them:

```bash
# See all available plugins
/plugin

# Install additional plugins
/plugin install [plugin-name]

# Get help with any plugin
/help [plugin-name]
```

### 💡 Pro Tips for Beginners

1.  **Start simple** - Use basic commands first, add complexity later
2.  **Use natural language** - Just describe what you need
3.  **Ask for help** - Type `/help` or ask Claude "How do I...?"
4.  **Experiment** - You can't break anything, so try different commands
5.  **Save favorites** - Create aliases for commands you use often

### 📚 Common Next Steps by Role

**Sales:**
- Install `account-management` for customer success workflows
- Install `sales-calls` for call preparation and analysis
- Install `enterprise-sales` for complex deal management

**Marketing:**
- Install `social-media-marketing` for social strategy
- Install `seo` for search optimization
- Install `marketing-analytics` for campaign ROI

**Growth:**
- Install `product-led-growth` for self-serve strategies
- Install `growth-experiments` for A/B testing
- Install `business-intelligence` for executive reporting

---

## Troubleshooting

### Common Issues and Solutions

#### ❌ "Command not found" error

**Problem:** You typed a command but got an error.

**Solution:**
1.  Make sure you installed the required plugin first
2.  Check for typos in the command
3.  Try typing `/plugin` to see installed plugins

---

#### ❌ "Marketplace not found" error

**Problem:** The marketplace couldn't be added.

**Solution:**
1.  Verify you're connected to the internet
2.  Check that you used the correct marketplace name
3.  Make sure you're in a workspace (Step 2)

---

#### ❌ Plugins not showing up

**Problem:** You installed plugins but can't use them.

**Solution:**
1.  Restart Claude Code
2.  Verify the workspace is open
3.  Type `/plugin` to confirm installation

---

#### ❌ Claude isn't responding

**Problem:** Commands aren't working.

**Solution:**
1.  Check your internet connection
2.  Verify you're signed into your Claude account
3.  Try closing and reopening Claude Code

---

#### 🆘 Still stuck?

- **Check the documentation:** [Usage Guide](docs/usage-guide.md)
- **Ask Claude:** Type "I'm having trouble with [describe issue]"
- **Community support:** Check GitHub Issues for similar problems
- **Start fresh:** Create a new workspace and try again

---

## 🎉 You're Ready!

Congratulations! You've successfully:

- ✅ Installed Claude Code
- ✅ Set up your workspace
- ✅ Added the GTM Agents marketplace
- ✅ Installed your first plugins
- ✅ Ran your first command

**You're now ready to automate and accelerate your GTM work with AI!**

---

## 📋 Quick Reference Card

**Save or print this for easy access!**

### Essential Commands

| Command | What It Does |
|---------|-------------|
| `/plugin` | Browse all available plugins |
| `/plugin install [name]` | Install a specific plugin |
| `/help [plugin-name]` | Get help with a plugin |
| `"How do I...?"` | Ask Claude anything in plain English |

### Starter Commands by Role

**Sales:**
```bash
/sales-prospecting:generate-leads --criteria "your ICP"
/sales-pipeline:analyze-pipeline
/sales-enablement:create-battlecard --competitor "Name"
```

**Marketing:**
```bash
/content-marketing:content-pipeline "topic" --duration 1month
/email-marketing:optimize-campaign --metric open-rate
/campaign-orchestration:launch-campaign "Campaign Name"
```

**Growth:**
```bash
/customer-analytics:segment-customers --method behavioral
/growth-experiments:design-experiment --hypothesis "your hypothesis"
/revenue-analytics:calculate-ltv
```

### Tips for Success

1.  **Start simple** → Add complexity as you learn
2.  **Use natural language** → Just describe what you need
3.  **Ask for help** → Claude is always ready to assist
4.  **Experiment freely** → You can't break anything
5.  **Save time** → Create aliases for frequent tasks

### Common Patterns

**Generate → Review → Refine:**
```bash
# 1. Generate first draft
"Create a cold email for [prospect]"

# 2. Review and ask for changes
"Make it more casual and add a PS line"

# 3. Finalize
"Perfect! Save this as a template"
```

**Chain commands for workflows:**
```bash
# Generate leads → Create sequence → Schedule
/sales-prospecting:generate-leads |
/sales-prospecting:build-sequence |
/email-marketing:schedule-campaign
```

---

## 🎓 Learning Resources

### By Experience Level

**Complete Beginner (You are here! ✓)**
- ✅ [Getting Started Guide](GETTING_STARTED.md) ← You just completed this!
- 📖 Next: [Quick Start Guide](QUICK_START.md)

**Getting Comfortable**
- 📖 [Usage Guide](docs/usage-guide.md) - Comprehensive command reference
- 🔍 [Plugin Reference](docs/plugin-reference.md) - Explore all 67 plugins

**Power User**
- 🧠 [Business Skills](docs/business-skills.md) - Master all 52 skills
- ⚙️ [Agent Reference](docs/agent-reference.md) - Understand the 92 agents
- 🏗️ [Architecture](docs/architecture.md) - Deep dive into design

**Contributing Back**
- 🤝 [Contributing Guide](CONTRIBUTING.md) - Build your own plugins

---

## ❓ Frequently Asked Questions

### General Questions

**Q: Do I need to know how to code?**
A: No! These plugins are designed for business users. Just describe what you need in plain English, and Claude will handle the rest.

**Q: How much does this cost?**
A: You'll need a Claude account (check [claude.ai](https://claude.ai) for pricing). The GTM Agents plugins themselves are open-source and free to use.

**Q: Will this work on my computer?**
A: Yes! Claude Code works on Windows, macOS, and Linux.

**Q: How long does setup take?**
A: About 10-15 minutes for first-time setup. After that, installing new plugins takes just seconds.

### Using the Plugins

**Q: Do I need to install all 67 plugins?**
A: No! Start with 2-3 plugins for your role. You can always install more later.

**Q: How do I know which plugins to install?**
A: Follow the recommendations in [Step 4](#step-4-install-your-first-plugins) based on your role (Sales, Marketing, or Growth).

**Q: Can I uninstall plugins I don't use?**
A: Yes! Type `/plugin uninstall [plugin-name]` to remove any plugin.

**Q: What if I make a mistake?**
A: Don't worry! You can't break anything. Just ask Claude to help you fix it or undo changes.

### Data and Privacy

**Q: Is my data safe?**
A: Yes. All plugins follow Claude's security and privacy standards. Your data stays within your Claude workspace.

**Q: Can I use this with my company's data?**
A: Check with your IT department first. Make sure using AI tools complies with your company's policies.

**Q: Where is my work saved?**
A: Everything is saved in your workspace folder on your computer. You have full control over your files.

### Getting Help

**Q: What if a command doesn't work?**
A: Check the [Troubleshooting](#troubleshooting) section, or just ask Claude: "This command isn't working, can you help?"

**Q: Can I see examples before trying a command?**
A: Yes! Type `/examples [command-name]` to see usage examples.

**Q: How do I learn more advanced features?**
A: Once you're comfortable with the basics, check out the [Usage Guide](docs/usage-guide.md) and [Business Skills](docs/business-skills.md) documentation.

**Q: Can I get one-on-one help?**
A: Ask Claude directly! Just describe your problem in the chat, and Claude will guide you through the solution.

### Technical Questions

**Q: Do I need an internet connection?**
A: Yes, Claude Code requires an internet connection to work.

**Q: Can I use this offline?**
A: No, Claude Code needs to connect to Claude's AI to function.

**Q: What if I'm behind a corporate firewall?**
A: You may need to work with your IT department to ensure Claude Code can connect to the internet.

**Q: Can I use this on multiple computers?**
A: Yes! Just install Claude Code on each computer and sign in with the same account.

---

## 📞 Need Help?

- 📖 **Documentation:** [docs/](docs/) folder
- 💬 **Ask Claude:** Just describe your problem
- 🐛 **Report Issues:** [GitHub Issues](../../issues)
- 💡 **Share Ideas:** [GitHub Discussions](../../discussions)

**Welcome to the future of GTM work! 🚀**
