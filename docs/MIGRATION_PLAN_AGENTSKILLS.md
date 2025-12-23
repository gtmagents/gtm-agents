# GTM Agents → Agent Skills Standard Migration Plan

## Executive Summary

This document outlines a comprehensive plan to migrate the **gtm-agents** repository to fully comply with the **Agent Skills** open standard (https://agentskills.io) maintained by Anthropic.

**Current State:** gtm-agents has 67 plugins, 203 agents, 243 skills with a custom structure  
**Target State:** Full compliance with Agent Skills specification for interoperability with Claude Code, Cursor, VS Code, GitHub Copilot, OpenAI Codex, and other compatible agents

---

## Gap Analysis

### ✅ Already Compliant

| Requirement | Current Status |
|-------------|----------------|
| Skills use `SKILL.md` files | ✅ All 243 skills have `SKILL.md` |
| YAML frontmatter with `name` and `description` | ✅ Present in all skills |
| Lowercase hyphenated names | ✅ Consistent naming |
| Skills organized in directories | ✅ `plugins/*/skills/*/SKILL.md` |
| Progressive disclosure pattern | ✅ Metadata → Instructions → Resources |
| Assets directory support | ✅ Some skills have `assets/` |

### ⚠️ Partial Compliance (Needs Updates)

| Requirement | Gap | Impact |
|-------------|-----|--------|
| Name must match directory name | Some mismatches possible | Medium |
| Description max 1024 chars | Some may exceed | Low |
| Optional `scripts/` directory | Not standardized | Medium |
| Optional `references/` directory | Not standardized | Medium |
| `license` field | Missing from most skills | Low |
| `compatibility` field | Missing from all skills | Low |
| `metadata` field | Missing from all skills | Low |

### ❌ Not Compliant (New Requirements)

| Requirement | Gap | Impact |
|-------------|-----|--------|
| Agents are NOT part of Agent Skills spec | Agents are custom to gtm-agents | High |
| Commands are NOT part of Agent Skills spec | Commands are custom to gtm-agents | High |
| Plugins structure is custom | Not in Agent Skills spec | High |
| Marketplace JSON is custom | Not in Agent Skills spec | High |
| No validation tooling integrated | Need `skills-ref` CLI | Medium |

---

## Migration Strategy

### Phase 1: Skills Compliance (Priority: HIGH)

**Goal:** Ensure all 243 skills pass `skills-ref validate`

#### 1.1 Frontmatter Standardization

Update all `SKILL.md` files to include:

```yaml
---
name: skill-name                    # Required (must match directory)
description: What it does...        # Required (max 1024 chars)
license: Apache-2.0                 # Optional but recommended
compatibility: Claude Code          # Optional
metadata:                           # Optional
  author: gtm-agents
  version: "1.0"
  category: sales|marketing|growth
---
```

**Tasks:**
- [ ] Create script to validate all skill names match directory names
- [ ] Create script to check description length (max 1024 chars)
- [ ] Add `license: Apache-2.0` to all skills
- [ ] Add `compatibility: Claude Code (or similar products)` to all skills
- [ ] Add `metadata` with author, version, category

#### 1.2 Directory Structure Standardization

Ensure each skill follows:
```
skill-name/
├── SKILL.md          # Required
├── scripts/          # Optional - executable code
├── references/       # Optional - additional docs
└── assets/           # Optional - templates, resources
```

**Tasks:**
- [ ] Audit existing `assets/` directories
- [ ] Rename any non-standard subdirectories
- [ ] Create `scripts/` directories where executable code exists
- [ ] Create `references/` directories for detailed docs

#### 1.3 Content Guidelines

- [ ] Keep `SKILL.md` body under 500 lines
- [ ] Move detailed reference material to `references/REFERENCE.md`
- [ ] Use relative paths for file references
- [ ] Avoid deeply nested reference chains

---

### Phase 2: Validation Tooling (Priority: HIGH)

**Goal:** Integrate `skills-ref` CLI for automated validation

#### 2.1 Add Validation Script

Create `scripts/validate_skills.py`:
```python
#!/usr/bin/env python3
"""Validate all skills against Agent Skills specification."""

import subprocess
import sys
from pathlib import Path

def validate_all_skills():
    skills_dirs = list(Path("plugins").glob("*/skills/*/SKILL.md"))
    errors = []
    
    for skill_md in skills_dirs:
        skill_dir = skill_md.parent
        result = subprocess.run(
            ["skills-ref", "validate", str(skill_dir)],
            capture_output=True, text=True
        )
        if result.returncode != 0:
            errors.append((skill_dir, result.stderr))
    
    return errors

if __name__ == "__main__":
    errors = validate_all_skills()
    if errors:
        for skill, error in errors:
            print(f"❌ {skill}: {error}")
        sys.exit(1)
    print("✅ All skills valid")
```

**Tasks:**
- [ ] Add `skills-ref` to development dependencies
- [ ] Create validation script
- [ ] Add to pre-commit hooks
- [ ] Add to CI/CD pipeline
- [ ] Update `scripts/validate_marketplace.py` to include skills validation

#### 2.2 Generate Prompt XML

Use `skills-ref to-prompt` to generate `<available_skills>` XML for agent integration:

```bash
skills-ref to-prompt plugins/*/skills/*/
```

**Tasks:**
- [ ] Create script to generate skills manifest XML
- [ ] Document how to inject skills into agent prompts
- [ ] Add to build/release process

---

### Phase 3: Repository Restructure (Priority: MEDIUM)

**Goal:** Separate Agent Skills from custom gtm-agents extensions

#### 3.1 New Directory Structure

```
gtm-agents/
├── skills/                         # Agent Skills compliant (NEW)
│   ├── sales/
│   │   ├── cold-outreach/
│   │   │   ├── SKILL.md
│   │   │   ├── scripts/
│   │   │   └── assets/
│   │   ├── lead-qualification/
│   │   └── ...
│   ├── marketing/
│   ├── growth/
│   └── orchestration/
├── plugins/                        # GTM-specific extensions (KEEP)
│   └── [plugin-name]/
│       ├── agents/                 # Custom agent definitions
│       ├── commands/               # Custom command definitions
│       └── skills -> ../../skills/[category]/  # Symlinks
├── .claude-plugin/                 # Claude Code marketplace (KEEP)
│   └── marketplace.json
├── workspace/                      # Agent working directory (KEEP)
└── docs/
```

**Alternative: Keep Current Structure**

If restructuring is too disruptive, keep skills in `plugins/*/skills/` but ensure each skill directory is independently valid per Agent Skills spec.

**Tasks:**
- [ ] Decide on restructure vs. keep current
- [ ] If restructure: create migration script
- [ ] Update all path references
- [ ] Update marketplace.json
- [ ] Update documentation

#### 3.2 Skills Index

Create `skills/index.json` for discovery:

```json
{
  "version": "1.0",
  "skills": [
    {
      "name": "cold-outreach",
      "path": "skills/sales/cold-outreach",
      "category": "sales"
    }
  ]
}
```

**Tasks:**
- [ ] Create index generation script
- [ ] Add to build process
- [ ] Document index format

---

### Phase 4: Documentation Updates (Priority: MEDIUM)

#### 4.1 Update CLAUDE.md

Add Agent Skills compliance section:

```markdown
## Agent Skills Compliance

This repository follows the [Agent Skills](https://agentskills.io) open standard.

### Validating Skills
```bash
skills-ref validate plugins/[plugin]/skills/[skill]
```

### Generating Prompt XML
```bash
skills-ref to-prompt plugins/*/skills/*/
```

### Skill Structure
Each skill follows the Agent Skills specification:
- `SKILL.md` with YAML frontmatter (name, description)
- Optional `scripts/`, `references/`, `assets/` directories
```

**Tasks:**
- [ ] Update CLAUDE.md with compliance section
- [ ] Update README.md
- [ ] Update CONTRIBUTING.md with skill authoring guidelines
- [ ] Create `docs/agent-skills-compliance.md`

#### 4.2 Update Skill Templates

Update `templates/skill.md`:

```markdown
---
name: {{skill-name}}
description: {{description - max 1024 chars}}
license: Apache-2.0
compatibility: Claude Code (or similar products)
metadata:
  author: gtm-agents
  version: "1.0"
  category: {{sales|marketing|growth|orchestration}}
---

# {{Skill Title}}

## When to Use
- Trigger condition 1
- Trigger condition 2

## Framework
1. Step one
2. Step two

## Templates
- See `assets/template.md` for...

## Tips
- Best practice 1
- Best practice 2
```

**Tasks:**
- [ ] Update skill template
- [ ] Update scaffolding script
- [ ] Add validation to scaffolding

---

### Phase 5: Agents & Commands (Priority: LOW)

**Note:** Agents and Commands are **NOT** part of the Agent Skills specification. They are custom extensions specific to gtm-agents.

#### 5.1 Document Custom Extensions

Create clear documentation that:
- Skills follow Agent Skills standard (portable)
- Agents are gtm-agents custom format (not portable)
- Commands are gtm-agents custom format (not portable)

#### 5.2 Consider Future Standards

Monitor for potential future standards:
- Agent definition format
- Command/tool definition format
- Orchestration patterns

**Tasks:**
- [ ] Document custom extensions clearly
- [ ] Add "portability" notes to agent/command docs
- [ ] Track Agent Skills spec evolution

---

## Implementation Checklist

### Immediate Actions (Week 1) ✅ COMPLETED

- [x] Install `skills-ref` CLI: `pip install skills-ref`
- [x] Run validation on all skills: `python scripts/validate_skills.py`
- [x] Document current validation failures - **All 263 skills pass validation**
- [x] Create tracking issue for each failure type - **No failures found**

### Short-term (Weeks 2-4) ✅ COMPLETED

- [x] Fix all validation failures - **All skills already valid**
- [x] Add license field to all skills - **Added `license: Apache-2.0`**
- [x] Add compatibility field to all skills - **Added `compatibility: Claude Code (or similar products)`**
- [x] Add metadata field to all skills - **Added author, version, category**
- [x] Create validation script - **`scripts/validate_skills.py`**
- [x] Add to pre-commit hooks - **`.pre-commit-config.yaml`**

### Medium-term (Months 2-3) - IN PROGRESS

- [ ] Decide on repository restructure - **Recommendation: Keep current structure**
- [x] Update documentation - **CLAUDE.md, CONTRIBUTING.md updated**
- [x] Update templates - **`templates/skill.md` updated**
- [ ] Create skills index - **Optional, can be generated from marketplace.json**
- [ ] Add to CI/CD - **Pre-commit hooks added, GitHub Actions pending**

### Long-term (Ongoing)

- [ ] Monitor Agent Skills spec updates
- [ ] Contribute to Agent Skills community
- [ ] Consider submitting skills to public registries

---

## Validation Commands

```bash
# Install skills-ref
pip install skills-ref

# Validate single skill
skills-ref validate plugins/sales-prospecting/skills/cold-outreach

# Validate all skills (bash)
for skill in plugins/*/skills/*/; do
  skills-ref validate "$skill"
done

# Read skill properties
skills-ref read-properties plugins/sales-prospecting/skills/cold-outreach

# Generate prompt XML
skills-ref to-prompt plugins/*/skills/*/
```

---

## Risk Assessment

| Risk | Likelihood | Impact | Mitigation |
|------|------------|--------|------------|
| Breaking existing workflows | Medium | High | Phased rollout, backward compatibility |
| Validation failures | High | Low | Fix incrementally, track in issues |
| Restructure complexity | Medium | Medium | Consider keeping current structure |
| Spec changes | Low | Medium | Monitor agentskills.io for updates |

---

## Success Criteria

1. **All 243 skills pass `skills-ref validate`**
2. **Pre-commit hooks prevent invalid skills**
3. **CI/CD validates skills on every PR**
4. **Documentation clearly separates portable (skills) from custom (agents/commands)**
5. **Skills can be used in any Agent Skills compatible product**

---

## References

- [Agent Skills Specification](https://agentskills.io/specification)
- [Agent Skills GitHub](https://github.com/agentskills/agentskills)
- [skills-ref CLI](https://github.com/agentskills/agentskills/tree/main/skills-ref)
- [Example Skills](https://github.com/anthropics/skills)
- [Best Practices](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices)

---

## Appendix: Current vs. Target Skill Format

### Current Format (gtm-agents)

```yaml
---
name: account-tiering
description: Use when defining ABM tiers, scoring logic, and coverage rules.
---

# Account Tiering Systems Skill

## When to Use
...
```

### Target Format (Agent Skills Compliant)

```yaml
---
name: account-tiering
description: Define ABM account tiers, scoring logic, and coverage rules. Use when establishing T1/T2/T3 definitions, auditing tier alignment, or planning coverage models.
license: Apache-2.0
compatibility: Claude Code (or similar products)
metadata:
  author: gtm-agents
  version: "1.0"
  category: orchestration
---

# Account Tiering Systems Skill

## When to Use
...
```

**Key Differences:**
1. Added `license` field
2. Added `compatibility` field
3. Added `metadata` with author, version, category
4. Enhanced description with more context (still under 1024 chars)
