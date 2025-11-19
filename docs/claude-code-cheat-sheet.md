# Claude Code Cheat Sheet

A comprehensive guide to setting up and using Claude Code efficiently.

---

## 0. First Time Setup: Login

**IMPORTANT**: Before anything else, make sure you're logged in correctly to get the best experience.

### Login Instructions:

1. Open Claude Code in your terminal
2. You'll be prompted to log in
3. **Choose the authentication method attached to your Claude subscription plan** (not API)
   - If you have Claude Pro or Claude Max, use your Anthropic account login
   - This ensures you get the full benefits of your subscription plan
4. Verify you're logged in by running `/cost` - you should see your subscription info

**Why This Matters**: Logging in with your subscription plan (vs API) gives you better rate limits, access to the latest models, and no per-request costs if you have Claude Max.

---

## 1. Claude Code Setup

Configure Claude Code for an optimal development experience. Follow these setup steps in order.

### Step 1: Shift+Enter Support (Essential First Step)

The most important setup - enables submitting messages to Claude with `SHIFT + ENTER`.

**Setup Instructions:**

Run `/terminal-setup` in Claude Code, which will automatically configure your terminal settings.

**Manual Setup Alternative:**
1. Open Cursor/VS Code settings
2. Search for "Terminal > Integrated: Send Keybindings To Shell"
3. **Uncheck** this option

**Fallback**: If Shift+Enter isn't working, use `\ + ENTER` (backslash + enter) to submit messages.

**Why This Matters**: Keeps your hands on the keyboard for faster iterations with Claude.

### Step 2: Settings Customization

Customize Claude Code behavior through `.claude/settings.json` in your project root.

**Common Settings:**

```json
{
  "model": "claude-sonnet-4-5",
  "autoApprovalSettings": {
    "enabled": true,
    "patterns": [
      "Read(//Users/yourname/**)",
      "Bash(npm run lint)",
      "Bash(git log:*)"
    ]
  },
  "statusLine": {
    "enabled": true,
    "template": "{{model}} | {{tokens}}"
  }
}
```

**Key Settings to Know:**
- `model`: Choose which Claude model to use
- `autoApprovalSettings`: Auto-approve specific tool uses to speed up workflow
- `statusLine`: Show model and token usage in status bar
- `hooks`: Configure shell commands that run on events (see Step 4)

### Step 3: MCP Server Configuration

MCP (Model Context Protocol) servers extend Claude Code with specialized capabilities.

**What MCP Servers Provide:**
- **Supabase**: Database operations, migrations, logs
- **Context7**: Up-to-date library documentation
- **Time**: Timezone conversions and current time
- **Custom servers**: Build your own integrations

**Setup via .mcp.json:**

```json
{
  "mcpServers": {
    "supabase": {
      "command": "npx",
      "args": ["-y", "@supabase/mcp-server"]
    },
    "context7": {
      "command": "npx",
      "args": ["-y", "@context7/mcp-server"]
    }
  }
}
```

**When to Use:**
- Working with databases → Supabase MCP
- Need latest library docs → Context7 MCP
- Custom workflows → Build your own MCP server

### Step 4: Hooks Configuration

Hooks run shell commands automatically in response to events.

**Common Hook: Noise When Claude Finishes**

Play a sound when Claude finishes responding (great for audio feedback).

```json
{
  "hooks": {
    "Stop": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "afplay /System/Library/Sounds/Pop.aiff"
          }
        ]
      }
    ]
  }
}
```

**Available Hooks:**
- `UserPromptSubmit`: Runs when you submit a message
- `Stop`: Runs when Claude stops/finishes responding
- `PreToolUse`: Runs before tool execution (with optional matcher)
- `PostToolUse`: Runs after tool execution (with optional matcher)
- `SessionStart` / `SessionEnd`: Runs at session lifecycle events
- `SubagentStop`: Runs when a subagent stops
- `PreCompact`: Runs before conversation compaction
- `Notification`: Runs on notification events

**Example: Validate Bash Commands Before Execution**

```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Bash",
        "hooks": [
          {
            "type": "command",
            "command": "python3 /path/to/validator.py"
          }
        ]
      }
    ]
  }
}
```

**Example: Lint After Edits**

```json
{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Edit",
        "hooks": [
          {
            "type": "command",
            "command": "npm run lint"
          }
        ]
      }
    ]
  }
}
```

**Windows/Linux Alternative for Sounds:**
```json
{
  "hooks": {
    "Stop": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "powershell -c (New-Object Media.SoundPlayer 'C:\\Windows\\Media\\Windows Ding.wav').PlaySync()"
          }
        ]
      }
    ]
  }
}
```

---

## 2. Editor Setup (Cursor/VS Code)

Master these shortcuts to keep your hands on the keyboard and navigate efficiently between editor, terminal, and Claude Code.

### Terminal Management

| Action | macOS | Windows/Linux | Custom Setup Required | Example Use |
|--------|-------|---------------|----------------------|-------------|
| Create Terminal in Editor Area | `CMD + SHIFT + C` | `CTRL + SHIFT + C` | ⚙️ Yes* | Open a new terminal as a tab in the editor (not bottom panel) |
| Rename Terminal | `CMD + SHIFT + R` | `CTRL + SHIFT + R` | ⚙️ Yes* | Label terminals by purpose (e.g., "dev server", "git", "tests") |
| Navigate Terminal Tabs | `CMD + SHIFT + [` / `]` | `CTRL + SHIFT + [` / `]` | ⚙️ Yes* | Switch between multiple terminal instances without using mouse |

**\*Note**: These shortcuts require custom keybinding setup in Cursor/VS Code. See [Custom Keybinding Setup](#custom-keybinding-setup) below.

### Window & Pane Navigation

| Action | macOS | Windows/Linux | Example Use |
|--------|-------|---------------|-------------|
| Toggle Sidebar | `CMD + B` | `CTRL + B` | Hide/show file explorer when you need more screen space |
| Focus File Explorer | `CMD + SHIFT + E` | `CTRL + SHIFT + E` | Open and focus the file explorer sidebar |
| Toggle Terminal | `CTRL + \`` | `CTRL + \`` | Open/close the integrated terminal |
| Toggle Bottom Panel | `CMD + J` | `CTRL + J` | Show/hide bottom panel (terminal, output, problems) |
| Open Source Control | `CMD + SHIFT + G` | `CTRL + SHIFT + G` | View git changes and source control panel |
| Go to Line | `CMD + G` | `CTRL + G` | Jump to a specific line number in current file |
| Split Editor Pane | `CMD + \` | `CTRL + \` | View multiple files side-by-side |
| Focus Specific Pane | `CMD + 1/2/3` | `CTRL + 1/2/3` | Jump to first, second, or third editor pane |
| Close Current Pane | `CMD + W` | `CTRL + W` | Close the currently focused editor pane |
| Quick Open File | `CMD + P` | `CTRL + P` | Open files by name - faster than clicking through folders |
| Command Palette | `CMD + SHIFT + P` | `CTRL + SHIFT + P` | Access all VS Code/Cursor commands |

### File Operations

| Action | How To | Example Use |
|--------|--------|-------------|
| Drag & Drop Images | Hold `SHIFT` while dragging | Add screenshots to Claude Code conversations |

### Keyboard-First Workflow Tips

- **Keep hands centered**: Use keyboard shortcuts instead of reaching for mouse
- **Learn incremental search**: `CMD/CTRL + F` for finding, `CMD/CTRL + H` for find/replace
- **Use breadcrumbs**: `CMD/CTRL + SHIFT + .` to navigate file structure
- **Master pane navigation**: Use `CMD/CTRL + 1/2/3` to jump between split editors instantly

---

### Custom Keybinding Setup

The terminal management shortcuts above require custom configuration in Cursor/VS Code.

**How to Set Up Custom Keybindings:**

1. Open Command Palette: `CMD/CTRL + SHIFT + P`
2. Type "Preferences: Open Keyboard Shortcuts (JSON)"
3. Add your custom keybindings to `keybindings.json`

**Example Keybindings:**

```json
[
  {
    "key": "cmd+shift+c",
    "command": "workbench.action.terminal.newInActiveWorkspace",
    "args": { "location": "editor" }
  },
  {
    "key": "cmd+shift+r",
    "command": "workbench.action.terminal.rename"
  },
  {
    "key": "cmd+shift+[",
    "command": "workbench.action.terminal.focusPrevious"
  },
  {
    "key": "cmd+shift+]",
    "command": "workbench.action.terminal.focusNext"
  }
]
```

**For Windows/Linux**: Replace `"cmd"` with `"ctrl"` in the keybindings above.

**Note**: These are example shortcuts - customize them to match your preferences! The video walkthrough will demonstrate the full setup process.

---

## 3. Claude Code Interface & Commands

Efficient workflows for working with Claude Code during development.

### 3.1 Text Editing Shortcuts

Text editing shortcuts for the Claude Code input field:

| Action | macOS | Windows/Linux | When to Use |
|--------|-------|---------------|-------------|
| New Line | `SHIFT + ENTER` | `SHIFT + ENTER` | Add line breaks in your prompt |
| Go to Beginning of Line | `CTRL + A` | `HOME` or `CTRL + A` | Jump to start without arrow keys |
| Go to End of Line | `CTRL + E` | `END` or `CTRL + E` | Jump to end without arrow keys |
| Delete Entire Line | `CTRL + U` | `CTRL + U` | Clear current line quickly |
| Move Back One Word | `OPTION + ←` | `CTRL + ←` | Navigate backward word by word |
| Delete Previous Word | `OPTION + DELETE` | `CTRL + BACKSPACE` | Remove word at a time |
| Stop Current AI Run | `ESC` | `ESC` | Stop Claude from continuing current execution |
| Revert to Previous Step | `ESC ESC` (double tap) | `ESC ESC` (double tap) | Undo Claude's last action and go back one step |

### 3.2 Claude Code-Specific Panels

| Action | Shortcut | When to Use |
|--------|----------|-------------|
| Show Tasks Panel | `CTRL + T` | View current tasks and todos Claude is tracking |
| View Thinking | `CTRL + O` | Open Claude's reasoning and thought process |
| Toggle Thinking Mode | `TAB` | Show/hide Claude's reasoning and thought process |

### 3.3 Common Claude Code Commands

Essential slash commands to know:

| Command | What It Does | When to Use |
|---------|--------------|-------------|
| `/help` | Show all available commands and general help | Learn what commands are available or get quick reference |
| `/terminal-setup` | Configure terminal for Shift+Enter support | First-time setup to enable Shift+Enter for new lines |
| `/model` | Switch between Claude models (Sonnet, Opus, Haiku) | Use Haiku for speed, Opus for complex reasoning, Sonnet for balance |
| `/context` | Show current context size and token usage | Check how much context you're using before hitting limits |
| `/clear` | Start a new conversation | Switch tasks or when you need fresh context |
| `/compact` | Compress conversation history to save tokens | When approaching context limits but want to keep conversation going |
| `/cost` | Show usage and subscription info | Monitor your usage or verify you're on the right plan |
| `/usage` | Show detailed usage statistics | View token usage across conversations and time periods |
| `/rewind` | Undo the last assistant message and tool executions | When Claude makes a mistake or goes in the wrong direction |
| `/resume` | Resume the last conversation | Continue where you left off after closing Claude Code |

### 3.4 Custom ShipKit Commands

ShipKit templates come with pre-built slash commands to accelerate your development workflow.

**Prep Setup Commands** (Run these in order when starting a new project):

| Command | What It Does |
|---------|--------------|
| `/01_generate_master_idea` | Generate comprehensive master idea document for your app |
| `/02_generate_app_name` | AI-powered app name generation with market research |
| `/03_generate_ui_theme` | Create cohesive, professional color themes |
| `/04_chatgpt_logo_generation` | Generate 10 unique logo prompts for your app |
| `/05_generate_app_pages_and_functionality` | Blueprint your application structure and pages |
| `/06_generate_wireframe` | Create wireframes for your app |
| `/07_generate_initial_data_models` | Design strategic database models |
| `/08_generate_system_design` | Make smart architectural decisions |
| `/09_generate_build_order` | Generate development roadmap and task order |

**Development Workflow Commands:**

| Command | What It Does |
|---------|--------------|
| `/task_template` | Create comprehensive task documents for AI-driven development |
| `/bugfix` | Quick bug triage and fix workflow |
| `/diff` | Analyze and present code changes with before/after comparisons |
| `/cleanup` | Comprehensive codebase cleanup analysis (TypeScript/JavaScript) |
| `/git_workflow_commit` | Analyze changes and create meaningful commit messages |
| `/pr_review` | Systematic code review checklist before merging |

**Database Commands:**

| Command | What It Does |
|---------|--------------|
| `/drizzle_down_migration` | Generate down migrations from up migrations |
| `/drizzle-rollback-workflow` | Guide through complete migration rollback process |

**UI/Design Commands:**

| Command | What It Does |
|---------|--------------|
| `/improve_ui` | Transform generic UI into beautiful, professional design |
| `/generate_landing_page` | Create high-converting landing page from your docs |
| `/generate_diagram` | Create comprehensive Mermaid diagrams with analysis |

**Deployment & Infrastructure:**

| Command | What It Does |
|---------|--------------|
| `/setup_auth` | Guide through OAuth setup (Google & GitHub) |
| `/update_template_workflow` | Safely update project with upstream template improvements |
| `/gcp_debugging_template` | Debug GCP deployment issues |

**Advanced/Specialized Commands:**

| Command | What It Does |
|---------|--------------|
| `/python_task_template` | Task template for Python development projects |
| `/cleanup_python` | Comprehensive cleanup analysis for Python projects |
| `/adk_task_template` | Task template for Google ADK agent systems |
| `/adk_bottleneck_analysis` | Analyze performance bottlenecks in ADK agents |
| `/agent_orchestrator` | Design and build Google ADK workflow projects |

---

## 4. Development Workflows

Practical workflows for common development tasks.

### Quick Review of Changes

Here's a typical workflow for reviewing changes after working with Claude:

1. **Open Source Control** - `CMD/CTRL + SHIFT + G`
   - Review all file changes Claude made
   - See git diff for each file

2. **Open File Explorer** - `CMD/CTRL + SHIFT + E`
   - Navigate to specific files you want to check
   - Browse the project structure

3. **Close Sidebar** - `CMD/CTRL + B`
   - Hide file explorer when done to maximize screen space
   - Return focus to your code

This workflow keeps your hands on the keyboard and lets you efficiently review Claude's changes before committing.