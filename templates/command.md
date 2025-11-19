---
name: {{ command_id }}
description: {{ what the command accomplishes }}
usage: /{{ plugin_id }}:{{ command_id }} {{ sample args }}
tool: false
---

# Command: {{ command_id }}

## Inputs
- **param** – description of expected value or format.
- **param** – description.

## Workflow
1. **Step** – describe action and any dependency.
2. **Step** – describe processing, automation, or collaboration.
3. **Step** – describe outputs and validation.

## Outputs
- {{ artifact or report }}
- {{ automation trigger }}

## Agent/Skill Invocations
- `agent-id` – reason invoked.
- `skill-id` – reason invoked.

---
