

Since introducing [Skills](https://www.anthropic.com/news/skills), there's been interest in understanding how the various components of Claude's agentic ecosystem work together. 

Whether you're building sophisticated workflows in [Claude Code](https://www.claude.com/product/claude-code), creating enterprise solutions with the API, or maximizing your productivity on [Claude.ai](http://claude.ai/redirect/claudedotcom.v1.28d4c42e-0be5-4102-bb74-8ed5dbfd1c88), knowing which tool to reach for—and when—can transform how you work with Claude.

This guide breaks down each building block, explains when to use what, and shows you how to combine them for powerful agentic workflows.

## **Understanding your agentic building blocks**

### **What are Skills?**

Skills are folders containing instructions, scripts, and resources that Claude discovers and loads dynamically when relevant to a task. Think of them as specialized training manuals that give Claude expertise in specific domains—from working with Excel spreadsheets to following your organization's brand guidelines.

**How Skills work:** When Claude encounters a task, it scans available Skills to find relevant matches. Skills use progressive disclosure: metadata loads first (~100 tokens), providing just enough information for Claude to know when a Skill is relevant. Full instructions load when needed (<5k tokens), and bundled files or scripts load only as required.

**When to use Skills:** Choose Skills when you need Claude to perform specialized tasks consistently and efficiently. They're ideal for:

*   **Organizational workflows**: Brand guidelines, compliance procedures, document templates
*   **Domain expertise:** Excel formulas, PDF manipulation, data analysis
*   **Personal preferences:** Note-taking systems, coding patterns, research methods

**Example:** Create [a brand guidelines Skill](https://github.com/anthropics/skills/tree/main/brand-guidelines) that includes your company's color palette, typography rules, and layout specifications. When Claude creates presentations or documents, it automatically applies these standards without you needing to explain them each time.

[Learn more](https://support.claude.com/en/articles/12512176-what-are-skills) about Skills and check out [our growing Skills library](https://github.com/anthropics/skills).

### **What are prompts?**

[Prompts](https://docs.claude.com/en/prompt-library/library) are the instructions you provide to Claude in natural language during a conversation. They're ephemeral, conversational, and reactive—you provide context and direction in the moment.

**When to use prompts:** Use prompts for:

*   One-off requests: "Summarize this article"
*   Conversational refinement: "Make that tone more professional"
*   Immediate context: "Analyze this data and identify trends"
*   Ad-hoc instructions: "Format this as a bulleted list"

**Example:** 

*Please conduct a comprehensive security review of this code. I'm looking for:*

*1\. Common vulnerabilities including:*

*   *Injection flaws (SQL, command, XSS, etc.)*
*   *Authentication and authorization issues*
*   *Sensitive data exposure*
*   *Security misconfigurations*
*   *Broken access control*
*   *Cryptographic failures*
*   *Input validation problems*
*   *Error handling and logging issues*

*2\. For each issue you find, please provide:*

*   *Severity level (Critical/High/Medium/Low)*
*   *Location in the code (line numbers or function names)*
*   *Explanation of why it's a security risk and how it could be exploited*
*   *Specific fix recommendation with code examples where possible*
*   *Best practice guidance to prevent similar issues*

*3\. Code context: \[Describe what the code does, the language/framework, and the environment it runs in - e.g., "This is a Node.js REST API that handles user authentication and processes payment data"\]*

*4\. Additional considerations:*

*   *Are there any OWASP Top 10 vulnerabilities present?*
*   *Does the code follow security best practices for \[specific framework/language\]?*
*   *Are there any dependencies with known vulnerabilities?*

*Please prioritize findings by severity and potential impact.*

**Pro-tip:** Prompts are your primary way of interacting with Claude, but they don't persist across conversations. For repeated workflows or specialized knowledge, consider capturing prompts as Skills or project instructions.

**When to use a Skill instead:** If you find yourself typing the same prompt repeatedly across multiple conversations, it's time to create a Skill. Transform recurring instructions like "review this code for security vulnerabilities using OWASP standards" or "format this analysis with executive summary, key findings, and recommendations" into Skills. This saves you from re-explaining procedures each time and ensures consistent execution.

Check out our [prompt library](https://docs.claude.com/en/prompt-library/library), [prompting best practices](http://claude.com/blog/prompt-engineering-best-practices), or [our smart prompt maker](https://claude.ai/redirect/claudedotcom.v1.28d4c42e-0be5-4102-bb74-8ed5dbfd1c88/public/artifacts/3796db7e-4ef1-4cab-b70c-d045778f23ec) to get started.

### **What are Projects?**

Available on all paid Claude plans, [Projects](https://support.claude.com/en/articles/9517075-what-are-projects) are self-contained workspaces with their own chat histories and knowledge bases. Each project includes a 200K context window where you can upload documents, provide context, and set custom instructions that apply to all conversations within that project.

**How Projects work:** Everything you upload to a project's knowledge base becomes available across all chats within that project. Claude automatically uses this context to provide more informed, relevant responses. When your project knowledge approaches context limits, Claude seamlessly enables Retrieval Augmented Generation (RAG) mode to expand capacity by up to 10x.

**When to use Projects:** Choose Projects when you need:

*   **Persistent context:** Background knowledge that should inform every conversation
*   **Workspace organization:** Separate contexts for different initiatives
*   **Team collaboration:** Shared knowledge and conversation history (on Team and Enterprise plans)
*   **Custom instructions:** Project-specific tone, perspective, or approach

**Example:** Create a "Q4 Product Launch" project containing market research, competitor analysis, and product specifications. Every chat in this project has access to this knowledge without you needing to re-upload or re-explain the context.

**When to use a Skill instead:** If multiple agents or conversations need the same expertise—like security review procedures or data analysis methods—create a Skill rather than building that knowledge into individual subagents. Skills are portable and reusable, while subagents are purpose-built for specific workflows. Use Skills to teach expertise that any agent can apply; use subagents when you need independent task execution with specific tool permissions and context isolation.

[Learn](https://support.claude.com/en/articles/9517075-what-are-projects) more about Projects.

### **What are subagents?**

[Subagents](https://docs.claude.com/en/docs/claude-code/sub-agents) are specialized AI assistants with their own context windows, custom system prompts, and specific tool permissions. Available in Claude Code and the Claude Agent SDK, subagents handle discrete tasks independently and return results to the main agent.

**How subagents work:** Each subagent operates with its own configuration—you define what it does, how it approaches problems, and which tools it can access. Claude automatically delegates tasks to appropriate subagents based on their descriptions, or you can explicitly request a specific subagent.

**When to use subagents:** Use subagents for:

*   **Task specialization:** Code review, test generation, security audits
*   **Context management:** Keep the main conversation focused while offloading specialized work
*   **Parallel processing:** Multiple subagents can work on different aspects simultaneously
*   **Tool restriction:** Limit specific subagents to safe operations (e.g., read-only access)

**Example:**

```plaintext
Create a code-reviewer subagent with access to Read, Grep, and Glob tools but not Write or Edit. When you modify code, Claude automatically delegates to this subagent for quality and security review without risking unintended code changes.
```

**When to use a Skill instead:** If multiple agents or conversations need the same expertise—like security review procedures or data analysis methods—create a Skill rather than building that knowledge into individual subagents. Skills are portable and reusable, while subagents are purpose-built for specific workflows. Use Skills to teach expertise that any agent can apply; use subagents when you need independent task execution with specific tool permissions and context isolation.

[Learn more](https://code.claude.com/docs/en/sub-agents) about subagents.

### **What is MCP?**

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/69141f0993d68ff4c536f316_619a5262.png)

MCP creates a universal connection layer between AI applications and your existing tools and data sources.

The Model Context Protocol (MCP) is an open standard for connecting AI assistants to external systems where data lives—content repositories, business tools, databases, and development environments.

**How MCP works:** MCP provides a standardized way to connect Claude to your tools and data sources. Instead of building custom integrations for each data source, you build against a single protocol. MCP servers expose data and capabilities; MCP clients (like Claude) connect to these servers.

**When to use MCP:** Choose MCP when you need Claude to:

*   Access external data: Google Drive, Slack, GitHub, databases
*   Use business tools: CRM systems, project management platforms
*   Connect to development environments: Local files, IDEs, version control
*   Integrate with custom systems: Your proprietary tools and data sources

**Example:** Connect Claude to your company's Google Drive via MCP. Now Claude can search documents, read files, and reference internal knowledge without manual uploads—the connection persists and updates automatically.

**When to use a Skill instead:** MCP connects Claude to data; Skills teach Claude what to do with that data. If you're explaining *how* to use a tool or follow procedures—like "when querying our database, always filter by date range first" or "format Excel reports with these specific formulas"—that's a Skill. If you need Claude to *access* the database or Excel files in the first place, that's MCP. Use both together: MCP for connectivity, Skills for procedural knowledge.

[Learn more](https://www.anthropic.com/news/model-context-protocol) about MCP and check out [documentation](https://modelcontextprotocol.io/docs/develop/build-server) on how to build an MCP server.

## **How they work together**

The real power emerges when you combine these building blocks. Each serves a distinct purpose, and together they create sophisticated agentic workflows.

### **Comparison: choosing the right tool**

### **Example agentic workflow: research agent**

Let's build a comprehensive research agent that combines multiple building blocks. This example shows how to assemble and activate an agent for competitive analysis.

**Step 1: Set up your Project**

Create a "Competitive Intelligence" project and upload:

*   Industry reports and market analyses
*   Competitor product documentation
*   Customer feedback from your CRM
*   Previous research summaries

Add project instructions:

*Analyze competitors through the lens of our product strategy. Focus on differentiation opportunities and emerging market trends. Present findings with specific evidence and actionable recommendations.*

**Step 2: Connect data sources via MCP**

Enable MCP servers for:

*   Google Drive (to access shared research documents)
*   GitHub (to review competitor open-source repositories)
*   Web search (for real-time market information)

**Step 3: Create specialized Skills**

Create a "competitive-analysis" skill:

```plaintext
# My Company GDrive Navigation Skill

## Overview
Optimized search and retrieval strategy for Meridian Tech's Google Drive structure. Use this skill to efficiently locate internal documents, research, and strategic materials.

## Drive Organization

**Top-level structure:**
- `/Strategy & Planning/` - OKRs, quarterly plans, board decks
- `/Product/` - PRDs, roadmaps, technical specs
- `/Research/` - Market research, competitive intel, user studies
- `/Sales & Marketing/` - Case studies, pitch decks, campaign materials
- `/Customer Success/` - Implementation guides, success metrics
- `/Company Ops/` - Policies, org charts, team directories

**Naming conventions:**
- Format: `YYYY-MM-DD_DocumentName_vX`
- Final versions marked with `_FINAL`
- Drafts include `_DRAFT` or `_WIP`

## Search Best Practices

1. **Start broad, then filter** - Use folder context + keywords
2. **Target document owners** - Sales materials from Sales/, not root
3. **Check recency** - Prioritize documents from last 6 months for current strategy
4. **Look for "source of truth"** - Files with `_FINAL`, `_APPROVED`, or in `/Archives/Official/`

## Research Agent Workflow

1. Identify topic category (product, market, customer)
2. Search relevant folder with targeted keywords
3. Retrieve 3-5 most recent/relevant documents
4. Cross-reference with `/Strategy & Planning/` for context
5. Cite sources with file names and dates
```

**Step 4: Configure subagents (Claude Code/SDK only)**

Create specialized subagents:

`market-researcher` subagent:

```plaintext
name: market-researcher
description: Research market trends, industry reports, and competitive landscape data. Use proactively for competitive analysis.
tools: Read, Grep, Web-search
---
You are a market research analyst specializing in competitive intelligence.

When researching:
1. Identify authoritative sources (Gartner, Forrester, industry reports)
2. Gather quantitative data (market share, growth rates, funding)
3. Analyze qualitative insights (analyst opinions, customer reviews)
4. Synthesize trends and patterns

Present findings with citations and confidence levels.
```

`technical-analyst` subagent:

```plaintext
name: technical-analyst
description: Analyze technical architecture, implementation approaches, and engineering decisions. Use for technical competitive analysis.
tools: Read, Bash, Grep
---
You are a technical architect analyzing competitor technology choices.

When analyzing:
1. Review public repositories and technical documentation
2. Assess architecture patterns and technology stack
3. Evaluate scalability and performance approaches
4. Identify technical strengths and limitations

Focus on actionable technical insights that inform our product decisions.
```

**Step 5: Activate your research agent**

Now when you ask Claude: "Analyze how our top three competitors are positioning their new AI features and identify gaps we can exploit"

Here's what happens:

1.  **Project context loads**: Claude accesses your uploaded research documents and follows project instructions
2.  **MCP connections activate**: Claude searches your Google Drive for recent competitor briefs and pulls GitHub data
3.  **Skills engage**: The competitive-analysis Skill provides the analytical framework
4.  **Subagents execute** (in Claude Code): The market-researcher gathers industry data while the technical-analyst reviews technical implementations
5.  **Prompts refine**: You provide conversational guidance: "Focus especially on enterprise customers in healthcare"

**The result:** A comprehensive competitive analysis that draws from multiple data sources, follows your analytical framework, leverages specialized expertise, and maintains context throughout your research project.

## **Common questions**

#### **How do Skills work?**

Skills use [progressive disclosure](https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills) to keep Claude efficient. When working on tasks, Claude first scans Skill metadata (descriptions and summaries) to identify relevant matches. If a Skill matches, Claude loads the full instructions. Finally, if the Skill includes executable code or reference files, those load only when needed.

This architecture means you can have many Skills available without overwhelming Claude's context window. Claude accesses exactly what it needs, when it needs it.

#### **Skills vs. subagents: when to use what**

**Use Skills when:** You want capabilities that any Claude instance can load and use. Skills are like training materials—they make Claude better at specific tasks across all conversations.

**Use subagents when:** You need complete, self-contained agents designed for specific purposes that handle workflows independently. Subagents are like specialized employees with their own context and tool permissions.

**Use them together when:** You want subagents with specialized expertise. For example, a code-review subagent can use Skills for language-specific best practices, combining the independence of a subagent with the portable expertise of Skills.

#### **Skills vs. prompts: when to use what**

**Use prompts when:** You're giving one-time instructions, providing immediate context, or having a conversational back-and-forth. Prompts are reactive and ephemeral.

**Use Skills when:** You have procedures or expertise that you'll need repeatedly. Skills are proactive—Claude knows when to apply them—and persistent across conversations.

**Use them together:** Prompts and Skills complement each other naturally. Use Skills to provide foundational expertise, then use prompts to provide specific context and refinement for each task.

#### **Skills vs. Projects: when to use what**

**Use Projects when:** You need background knowledge and context that should inform all conversations about a specific initiative. Projects provide static reference material that's always loaded.

**Use Skills when:** You need procedural knowledge and executable code that activates only when relevant. Skills provide dynamic expertise that loads on-demand, saving your context window.

**Use them together when:** You want both persistent context and specialized capabilities. For example, a "Product Development" project containing product specs and user research, combined with Skills for creating technical documentation and analyzing user feedback data.

**Key difference:** Projects say "here's what you need to know." Skills say "here's how to do things." Projects provide a knowledge base you work within. Skills provide capabilities that work everywhere—any conversation, any project.

#### **Can subagents use Skills?**

Yes. In Claude Code and the Agent SDK, subagents can access and use Skills just like the main agent. This creates powerful combinations where specialized subagents leverage portable expertise.

For example, your python-developer subagent can use the pandas-analysis Skill to perform data transformations following your team's conventions, while your documentation-writer subagent uses the technical-writing skill to format API documentation consistently.

## **Getting started**

Ready to build with Skills? Here's how to start:

[**Claude.ai**](https://Claude.ai) **users:**

*   Enable Skills in Settings → Features
*   Create your first project at claude.ai/projects
*   Try combining project knowledge with Skills for your next analysis task

**API developers:**

*   Explore the Skills endpoint in [documentation](https://docs.anthropic.com)
*   Check out our [skills cookbook](https://github.com/anthropics/claude-cookbooks/tree/main/skills)

**Claude Code users:**

*   Install Skills via [plugin marketplaces](https://code.claude.com/docs/en/plugin-marketplaces)
*   Check out our [skills cookbook](https://github.com/anthropics/claude-cookbooks/tree/main/skills)  
    

No items found.

[Prev](#)Prev

0/5

[Next](#)Next

eBook

## Agent Skills

Start using Skills with Claude to build more powerful applications today.

Get started

[Get started](https://www.claude.com/blog/skills)Get started

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6915038fea2f5466c171c21f_Hand-NodeWeb.svg)![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/691503928e574d7dc8407b4a_Hand-NodeWeb-1.svg)

FAQ

No items found.

[](#)

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

Read more

[Read more](#)Read more

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

[Next](#)Next

Read more

[Read more](#)Read more

Read more

[Read more](#)Read more

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

Read more

[Read more](#)Read more

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

[Next](#)Next

Read more

[Read more](#)Read more

Read more

[Read more](#)Read more

## Related articles

Explore more insights on how Claude supports learning, research, and innovation across education.

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6909386cc7ad3ed2a7ec8eed_Object-ThoughtBubble.svg)

Nov 10, 2025

### Best practices for prompt engineering

Agents

[Best practices for prompt engineering](#)Best practices for prompt engineering

[Best practices for prompt engineering](/blog/best-practices-for-prompt-engineering)Best practices for prompt engineering

![](https://cdn.prod.website-files.com/plugins/Basic/assets/placeholder.60f9b1840c.svg)

Oct 31, 2025

### What is Model Context Protocol? Connect AI to your world

Agents

[What is Model Context Protocol? Connect AI to your world](#)What is Model Context Protocol? Connect AI to your world

[What is Model Context Protocol? Connect AI to your world](/blog/what-is-model-context-protocol)What is Model Context Protocol? Connect AI to your world

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d228c83775fcc75f4e6d_74409af25137110ac04cc39e4d5ea0a2fbcea421-1000x1000.svg)

Oct 30, 2025

### Building AI agents for healthcare and life sciences

Agents

[Building AI agents for healthcare and life sciences](#)Building AI agents for healthcare and life sciences

[Building AI agents for healthcare and life sciences](/blog/building-ai-agents-in-healthcare-and-life-sciences)Building AI agents for healthcare and life sciences

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d2319ef2161fcf9ba649_ddad92700787ec1bf1d80359c0c5e6ca305682b0-1000x1000.svg)

Oct 30, 2025

### Building AI agents for financial services

Agents

[Building AI agents for financial services](#)Building AI agents for financial services

[Building AI agents for financial services](/blog/building-ai-agents-in-financial-services)Building AI agents for financial services

## Transform how your organization operates with Claude

See pricing

[See pricing](https://claude.com/pricing#api)See pricing

Contact sales

[Contact sales](https://claude.com/contact-sales)Contact sales

Get the developer newsletter

Product updates, how-tos, community spotlights, and more. Delivered monthly to your inbox.

[Subscribe](#)Subscribe

Please provide your email address if you'd like to receive our monthly developer newsletter. You can unsubscribe at any time.

Thank you! You’re subscribed.

Sorry, there was a problem with your submission, please try again later.

[Homepage](/?r=0)Homepage

[Next](#)Next

Thank you! Your submission has been received!

Oops! Something went wrong while submitting the form.

Write

[Button Text](#)Button Text

Learn

[Button Text](#)Button Text

Code

[Button Text](#)Button Text

Write

*   Help me develop a unique voice for an audience
    
    [](#)
    
    Hi Claude! Could you help me develop a unique voice for an audience? If you need more information from me, ask me 1-2 key questions right away. If you think I should upload any documents that would help you do a better job, let me know. You can use the tools you have access to— like Google Drive, web search, etc.—if they’ll help you better accomplish this task. Do not use analysis tool. Please keep your responses friendly, brief and conversational.  
      
    Please execute the task as soon as you can—an artifact would be great if it makes sense. If using an artifact, consider what kind of artifact (interactive, visual, checklist, etc.) might be most helpful for this specific task. Thanks for your help!
    
*   Improve my writing style
    
    [](#)
    
    Hi Claude! Could you improve my writing style? If you need more information from me, ask me 1-2 key questions right away. If you think I should upload any documents that would help you do a better job, let me know. You can use the tools you have access to— like Google Drive, web search, etc.—if they’ll help you better accomplish this task. Do not use analysis tool. Please keep your responses friendly, brief and conversational.  
      
    Please execute the task as soon as you can—an artifact would be great if it makes sense. If using an artifact, consider what kind of artifact (interactive, visual, checklist, etc.) might be most helpful for this specific task. Thanks for your help!
    
*   Brainstorm creative ideas
    
    [](#)
    
    Hi Claude! Could you brainstorm creative ideas? If you need more information from me, ask me 1-2 key questions right away. If you think I should upload any documents that would help you do a better job, let me know. You can use the tools you have access to— like Google Drive, web search, etc.—if they’ll help you better accomplish this task. Do not use analysis tool. Please keep your responses friendly, brief and conversational.  
      
    Please execute the task as soon as you can—an artifact would be great if it makes sense. If using an artifact, consider what kind of artifact (interactive, visual, checklist, etc.) might be most helpful for this specific task. Thanks for your help!
    

Learn

*   Explain a complex topic simply
    
    [](#)
    
    Hi Claude! Could you explain a complex topic simply? If you need more information from me, ask me 1-2 key questions right away. If you think I should upload any documents that would help you do a better job, let me know. You can use the tools you have access to— like Google Drive, web search, etc.—if they’ll help you better accomplish this task. Do not use analysis tool. Please keep your responses friendly, brief and conversational.  
      
    Please execute the task as soon as you can—an artifact would be great if it makes sense. If using an artifact, consider what kind of artifact (interactive, visual, checklist, etc.) might be most helpful for this specific task. Thanks for your help!
    
*   Help me make sense of these ideas
    
    [](#)
    
    Hi Claude! Could you help me make sense of these ideas? If you need more information from me, ask me 1-2 key questions right away. If you think I should upload any documents that would help you do a better job, let me know. You can use the tools you have access to— like Google Drive, web search, etc.—if they’ll help you better accomplish this task. Do not use analysis tool. Please keep your responses friendly, brief and conversational.  
      
    Please execute the task as soon as you can—an artifact would be great if it makes sense. If using an artifact, consider what kind of artifact (interactive, visual, checklist, etc.) might be most helpful for this specific task. Thanks for your help!
    
*   Prepare for an exam or interview
    
    [](#)
    
    Hi Claude! Could you prepare for an exam or interview? If you need more information from me, ask me 1-2 key questions right away. If you think I should upload any documents that would help you do a better job, let me know. You can use the tools you have access to— like Google Drive, web search, etc.—if they’ll help you better accomplish this task. Do not use analysis tool. Please keep your responses friendly, brief and conversational.  
      
    Please execute the task as soon as you can—an artifact would be great if it makes sense. If using an artifact, consider what kind of artifact (interactive, visual, checklist, etc.) might be most helpful for this specific task. Thanks for your help!
    

Code

*   Explain a programming concept
    
    [](#)
    
    Hi Claude! Could you explain a programming concept? If you need more information from me, ask me 1-2 key questions right away. If you think I should upload any documents that would help you do a better job, let me know. You can use the tools you have access to— like Google Drive, web search, etc.—if they’ll help you better accomplish this task. Do not use analysis tool. Please keep your responses friendly, brief and conversational.  
      
    Please execute the task as soon as you can—an artifact would be great if it makes sense. If using an artifact, consider what kind of artifact (interactive, visual, checklist, etc.) might be most helpful for this specific task. Thanks for your help!
    
*   Look over my code and give me tips
    
    [](#)
    
    Hi Claude! Could you look over my code and give me tips? If you need more information from me, ask me 1-2 key questions right away. If you think I should upload any documents that would help you do a better job, let me know. You can use the tools you have access to— like Google Drive, web search, etc.—if they’ll help you better accomplish this task. Do not use analysis tool. Please keep your responses friendly, brief and conversational.  
      
    Please execute the task as soon as you can—an artifact would be great if it makes sense. If using an artifact, consider what kind of artifact (interactive, visual, checklist, etc.) might be most helpful for this specific task. Thanks for your help!
    
*   Vibe code with me
    
    [](#)
    
    Hi Claude! Could you vibe code with me? If you need more information from me, ask me 1-2 key questions right away. If you think I should upload any documents that would help you do a better job, let me know. You can use the tools you have access to— like Google Drive, web search, etc.—if they’ll help you better accomplish this task. Do not use analysis tool. Please keep your responses friendly, brief and conversational.  
      
    Please execute the task as soon as you can—an artifact would be great if it makes sense. If using an artifact, consider what kind of artifact (interactive, visual, checklist, etc.) might be most helpful for this specific task. Thanks for your help!
    

More

*   Write case studies
    
    [](#)
    
    This is another test
    
*   Write grant proposals
    
    [](#)
    
    Hi Claude! Could you write grant proposals? If you need more information from me, ask me 1-2 key questions right away. If you think I should upload any documents that would help you do a better job, let me know. You can use the tools you have access to — like Google Drive, web search, etc. — if they’ll help you better accomplish this task. Do not use analysis tool. Please keep your responses friendly, brief and conversational.  
      
    Please execute the task as soon as you can - an artifact would be great if it makes sense. If using an artifact, consider what kind of artifact (interactive, visual, checklist, etc.) might be most helpful for this specific task. Thanks for your help!
    
*   Write video scripts
    
    [](#)
    
    this is a test
    

[Anthropic](https://www.anthropic.com/)Anthropic

© 2025 Anthropic PBC

Products

*   Claude
    
    [Claude](/product/overview)Claude
    
*   Claude Code
    
    [Claude Code](/product/claude-code)Claude Code
    
*   Max plan
    
    [Max plan](/pricing/max)Max plan
    
*   Team plan
    
    [Team plan](/pricing/team)Team plan
    
*   Enterprise plan
    
    [Enterprise plan](/pricing/enterprise)Enterprise plan
    
*   Download app
    
    [Download app](/download)Download app
    
*   Pricing
    
    [Pricing](/pricing)Pricing
    
*   Log in
    
    [Log in](https://claude.ai/redirect/claudedotcom.v1.28d4c42e-0be5-4102-bb74-8ed5dbfd1c88/login)Log in
    

Features

*   Claude and Slack
    
    [Claude and Slack](/claude-and-slack)Claude and Slack
    
*   Claude in Excel
    
    [Claude in Excel](/claude-for-excel)Claude in Excel
    

Models

*   Opus
    
    [Opus](https://www.anthropic.com/claude/opus)Opus
    
*   Sonnet
    
    [Sonnet](https://www.anthropic.com/claude/sonnet)Sonnet
    
*   Haiku
    
    [Haiku](https://www.anthropic.com/claude/haiku)Haiku
    

Solutions

*   AI agents
    
    [AI agents](/solutions/agents)AI agents
    
*   Code modernization
    
    [Code modernization](/solutions/code-modernization)Code modernization
    
*   Coding
    
    [Coding](/solutions/coding)Coding
    
*   Customer support
    
    [Customer support](/solutions/customer-support)Customer support
    
*   Education
    
    [Education](/solutions/education)Education
    
*   Financial services
    
    [Financial services](/solutions/financial-services)Financial services
    
*   Government
    
    [Government](/solutions/government)Government
    
*   Life sciences
    
    [Life sciences](/solutions/life-sciences)Life sciences
    

Claude Developer Platform

*   Overview
    
    [Overview](/platform/api)Overview
    
*   Developer docs
    
    [Developer docs](https://docs.claude.com/)Developer docs
    
*   Pricing
    
    [Pricing](https://claude.com/pricing#api)Pricing
    
*   Amazon Bedrock
    
    [Amazon Bedrock](/partners/amazon-bedrock)Amazon Bedrock
    
*   Google Cloud’s Vertex AI
    
    [Google Cloud’s Vertex AI](/partners/google-cloud-vertex-ai)Google Cloud’s Vertex AI
    
*   Console login
    
    [Console login](https://console.anthropic.com/)Console login
    

Learn

*   Blog
    
    [Blog](/blog)Blog
    
*   Courses
    
    [Courses](https://www.anthropic.com/learn)Courses
    
*   Use cases
    
    [Use cases](/resources/use-cases)Use cases
    
*   Connectors
    
    [Connectors](/connectors)Connectors
    
*   Customer stories
    
    [Customer stories](/customers)Customer stories
    
*   Engineering at Anthropic
    
    [Engineering at Anthropic](https://www.anthropic.com/engineering)Engineering at Anthropic
    
*   Events
    
    [Events](https://www.anthropic.com/events)Events
    
*   Powered by Claude
    
    [Powered by Claude](/partners/powered-by-claude)Powered by Claude
    
*   Service partners
    
    [Service partners](/partners/services)Service partners
    
*   Startups program
    
    [Startups program](/programs/startups)Startups program
    

Company

*   Anthropic
    
    [Anthropic](https://www.anthropic.com/)Anthropic
    
*   Careers
    
    [Careers](https://www.anthropic.com/careers)Careers
    
*   Economic Futures
    
    [Economic Futures](https://www.anthropic.com/economic-futures)Economic Futures
    
*   Research
    
    [Research](https://www.anthropic.com/research)Research
    
*   News
    
    [News](https://www.anthropic.com/news)News
    
*   Responsible Scaling Policy
    
    [Responsible Scaling Policy](https://www.anthropic.com/news/announcing-our-updated-responsible-scaling-policy)Responsible Scaling Policy
    
*   Security and compliance
    
    [Security and compliance](https://trust.anthropic.com/)Security and compliance
    
*   Transparency
    
    [Transparency](https://anthropic.com/transparency)Transparency
    

Help and security

*   Availability
    
    [Availability](https://www.anthropic.com/supported-countries)Availability
    
*   Status
    
    [Status](https://status.anthropic.com/)Status
    
*   Support center
    
    [Support center](https://support.claude.com/en/)Support center
    

Terms and policies

*   Privacy choices
    
*   Privacy policy
    
    [Privacy policy](https://www.anthropic.com/legal/privacy)Privacy policy
    
*   Responsible disclosure policy
    
    [Responsible disclosure policy](https://www.anthropic.com/responsible-disclosure-policy)Responsible disclosure policy
    
*   Terms of service: Commercial
    
    [Terms of service: Commercial](https://www.anthropic.com/legal/commercial-terms)Terms of service: Commercial
    
*   Terms of service: Consumer
    
    [Terms of service: Consumer](https://www.anthropic.com/legal/consumer-terms)Terms of service: Consumer
    
*   Usage policy
    
    [Usage policy](https://www.anthropic.com/legal/aup)Usage policy
    

[x.com](https://x.com/claudeai)x.com

[LinkedIn](https://www.linkedin.com/showcase/claude/)LinkedIn

[YouTube](https://www.youtube.com/@anthropic-ai)YouTube

[Instagram](https://www.instagram.com/claudeai)Instagram

English (US)

×

[Next](#)Next

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

[Next](#)Next

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

[Next](#)Next

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)