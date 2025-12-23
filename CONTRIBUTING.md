# Contributing to Claude GTM Agents

Thank you for your interest in contributing to Claude GTM Agents! This document provides guidelines and instructions for contributing to this project.

## Table of Contents

- [Code of Conduct](#code-of-conduct)
- [Getting Started](#getting-started)
- [Development Setup](#development-setup)
- [How to Contribute](#how-to-contribute)
- [Creating Plugins, Agents, and Skills](#creating-plugins-agents-and-skills)
- [Quality Standards](#quality-standards)
- [Pull Request Process](#pull-request-process)
- [Community](#community)

## Code of Conduct

This project adheres to a Code of Conduct that all contributors are expected to follow. Please read [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) before contributing.

## Getting Started

### Prerequisites

- Claude Code (latest version recommended)
- Git
- Python 3.8+ (for validation scripts)
- Basic understanding of Claude Code plugin system
- Familiarity with GTM (Go-To-Market) concepts

### Repository Structure

```
gtm-agents/
├── .claude-plugin/
│   └── marketplace.json          # Plugin marketplace definition
├── plugins/
│   └── [plugin-name]/
│       ├── agents/               # Specialized AI agents
│       ├── commands/             # Tools and workflows
│       └── skills/               # Modular knowledge packages
├── docs/                         # Documentation
├── scripts/                      # Validation and scaffolding scripts
└── templates/                    # Templates for new assets
```

## Development Setup

1. **Fork and Clone**
   ```bash
   git clone https://github.com/gtmagents/gtm-agents.git
   cd gtm-agents
   ```

2. **Install Pre-commit Hooks**
   ```bash
   # Install pre-commit
   pip install pre-commit
   pre-commit install
   
   # This will run validation on every commit
   ```

3. **Verify Setup**
   ```bash
   # Run validation scripts
   python scripts/validate_marketplace.py
   python scripts/smoke_test_plugins.py
   ```

## How to Contribute

### Types of Contributions

We welcome various types of contributions:

- **New Plugins**: Add new GTM-focused plugins
- **New Agents**: Create specialized agents for existing plugins
- **New Skills**: Add modular knowledge packages
- **New Commands**: Develop tools and workflows
- **Documentation**: Improve guides, examples, and references
- **Bug Fixes**: Fix issues in existing plugins or scripts
- **Examples**: Add real-world usage examples

### Finding Work

- Check [GitHub Issues](../../issues) for open tasks
- Look for issues labeled `good first issue` or `help wanted`
- Review the [ROADMAP.md](ROADMAP.md) for planned features
- Propose new ideas in [GitHub Discussions](../../discussions)

## Creating Plugins, Agents, and Skills

### Using Scaffolding Scripts

We provide scaffolding scripts to quickly create new assets:

```bash
# Create a new agent
python scripts/scaffold_asset.py agent plugins/your-plugin/agents/example.md

# Create a new command
python scripts/scaffold_asset.py command plugins/your-plugin/commands/run-example.md

# Create a new skill (Agent Skills compliant)
python scripts/scaffold_asset.py skill plugins/your-plugin/skills/example-skill

# Create a skill with optional directories
python scripts/scaffold_asset.py skill plugins/your-plugin/skills/example-skill --with-assets --with-scripts
```

### Plugin Creation Guidelines

1. **Single Purpose**: Each plugin should have a focused, well-defined purpose
2. **Optimal Size**: Follow Anthropic's 2-8 components pattern (average 3.2)
3. **Business-First**: Design for non-technical GTM users
4. **Progressive Disclosure**: Use skills for detailed knowledge that loads on-demand

### Agent Guidelines

- **Clear Expertise**: Each agent should have a specific domain of expertise
- **Activation Criteria**: Define clear criteria for when the agent should activate
- **Model Selection**: Use Haiku for data processing, Sonnet for strategy/creative work
- **Comprehensive Content**: Include relevant knowledge, frameworks, and best practices

### Skill Guidelines (Agent Skills Compliant)

Skills follow the [Agent Skills](https://agentskills.io) open standard for portability across Claude Code, Cursor, VS Code, GitHub Copilot, and other compatible agents.

#### Required Structure

```
skill-name/
├── SKILL.md          # Required: YAML frontmatter + instructions
├── scripts/          # Optional: executable code
├── references/       # Optional: additional documentation
└── assets/           # Optional: templates, resources
```

#### SKILL.md Format

```yaml
---
name: skill-name                    # Required (must match directory name)
description: What it does...        # Required (max 1024 chars)
license: Apache-2.0                 # Recommended
compatibility: Claude Code          # Recommended
metadata:                           # Recommended
  author: gtm-agents
  version: "1.0"
  category: sales|marketing|growth|orchestration
---

# Skill Title

## When to Use
- Trigger condition 1
- Trigger condition 2

## Framework
1. Step one
2. Step two

## Templates
- See `assets/template.md` for...

## Tips
- Best practice
- Pitfall to avoid
```

#### Validation

```bash
# Validate a single skill
python scripts/validate_skills.py plugins/[plugin]/skills/[skill]

# Validate all skills
python scripts/validate_skills.py
```

#### Key Requirements

- **Name Match**: `name` field must match the directory name exactly
- **Description**: Max 1024 characters, describe what it does and when to use
- **Lowercase Hyphenated**: Names use only lowercase letters, numbers, and hyphens
- **No Consecutive Hyphens**: `skill-name` is valid, `skill--name` is not
- **Body Under 500 Lines**: Move detailed content to `references/` directory

### Command Guidelines

- **Clear Purpose**: Each command should solve a specific problem
- **Good Documentation**: Include usage examples and parameter descriptions
- **Error Handling**: Provide helpful error messages
- **Composability**: Design commands to work well with others

### Naming Conventions

- **Files**: Use lowercase with hyphens (e.g., `lead-researcher.md`)
- **Plugins**: Use lowercase with hyphens (e.g., `sales-prospecting`)
- **Commands**: Use verb-noun format (e.g., `generate-leads`)
- **Skills**: Use descriptive names in lowercase with hyphens

## Quality Standards

### Documentation Requirements

All contributions must include:

- **Clear descriptions** of what the component does
- **Usage examples** showing how to use it
- **Activation criteria** (for agents and skills)
- **Dependencies** if any
- **Testing notes** if applicable

### Code Quality

- Follow existing patterns and conventions
- Use clear, descriptive names
- Include comments for complex logic
- Test your changes thoroughly

### Validation

Before submitting, ensure:

```bash
# Validate all skills (Agent Skills compliance)
python scripts/validate_skills.py

# Validate marketplace configuration
python scripts/validate_marketplace.py

# Run smoke tests
python scripts/smoke_test_plugins.py

# Or run all pre-commit hooks manually
pre-commit run --all-files
```

### Testing

- Test your plugin/agent/skill in Claude Code
- Verify activation criteria work as expected
- Test edge cases and error conditions
- Document any manual testing performed

## Pull Request Process

### Before Submitting

1. **Create a feature branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. **Make your changes**
   - Follow the guidelines above
   - Update documentation as needed
   - Add examples if applicable

3. **Test thoroughly**
   - Run validation scripts
   - Test in Claude Code
   - Verify no regressions

4. **Update documentation**
   - Update README if adding new plugins
   - Update relevant docs in `docs/`
   - Update CHANGELOG.md

5. **Commit with clear messages**
   ```bash
   git commit -m "feat: add sales forecasting agent"
   git commit -m "fix: correct activation criteria in lead-researcher"
   git commit -m "docs: improve installation instructions"
   ```

### Submitting the PR

1. **Push your branch**
   ```bash
   git push origin feature/your-feature-name
   ```

2. **Create Pull Request**
   - Use the PR template
   - Provide clear description of changes
   - Reference any related issues
   - Add screenshots/examples if applicable

3. **PR Checklist**
   - [ ] Code follows project conventions
   - [ ] All validation scripts pass
   - [ ] Documentation updated
   - [ ] CHANGELOG.md updated
   - [ ] Examples added/updated if needed
   - [ ] Tested in Claude Code
   - [ ] No breaking changes (or clearly documented)

### Review Process

- Maintainers will review your PR
- Address any feedback or requested changes
- Once approved, a maintainer will merge your PR
- Your contribution will be included in the next release

### Commit Message Format

We follow conventional commits:

- `feat:` New feature
- `fix:` Bug fix
- `docs:` Documentation changes
- `style:` Code style changes (formatting, etc.)
- `refactor:` Code refactoring
- `test:` Adding or updating tests
- `chore:` Maintenance tasks

## Community

### Getting Help

- **GitHub Discussions**: Ask questions and share ideas
- **GitHub Issues**: Report bugs or request features
- **Documentation**: Check the [docs/](docs/) directory

### Communication Channels

- GitHub Issues for bug reports and feature requests
- GitHub Discussions for questions and general discussion
- Pull Requests for code contributions

### Recognition

Contributors will be:
- Listed in the project's contributors
- Mentioned in release notes for significant contributions
- Credited in documentation for major features

## Additional Resources

- [Plugin Reference](docs/plugin-reference.md) - Complete catalog of plugins
- [Agent Reference](docs/agent-reference.md) - All agents organized by function
- [Business Skills](docs/business-skills.md) - Specialized GTM skills
- [Usage Guide](docs/usage-guide.md) - Commands, workflows, and best practices
- [Maintenance Guide](docs/maintenance.md) - Maintenance playbook

## Questions?

If you have questions not covered here:
1. Check existing documentation
2. Search GitHub Issues and Discussions
3. Open a new Discussion
4. Reach out to maintainers

Thank you for contributing to Claude GTM Agents! 🚀
