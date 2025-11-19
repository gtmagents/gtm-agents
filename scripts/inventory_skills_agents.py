import os
import yaml
import json
import re

def validate_skill(skill_path):
    skill_md_path = os.path.join(skill_path, 'SKILL.md')
    if not os.path.exists(skill_md_path):
        return {"valid": False, "error": "Missing SKILL.md"}
    
    try:
        with open(skill_md_path, 'r') as f:
            content = f.read()
        
        # Extract frontmatter
        match = re.match(r'^---\n(.*?)\n---\n', content, re.DOTALL)
        if not match:
            return {"valid": False, "error": "Missing or invalid YAML frontmatter"}
        
        frontmatter = yaml.safe_load(match.group(1))
        
        dirname = os.path.basename(skill_path)
        if frontmatter.get('name') != dirname:
             return {"valid": False, "error": f"Name mismatch: frontmatter '{frontmatter.get('name')}' vs dirname '{dirname}'"}
        
        if not frontmatter.get('description'):
            return {"valid": False, "error": "Missing description"}
            
        return {"valid": True, "name": frontmatter.get('name'), "description": frontmatter.get('description')}
        
    except Exception as e:
        return {"valid": False, "error": str(e)}

def scan_repo(root_dir):
    inventory = {
        "skills": [],
        "agents": []
    }
    
    # Scan examples/skills
    examples_skills_dir = os.path.join(root_dir, 'examples', 'skills')
    if os.path.exists(examples_skills_dir):
        for item in os.listdir(examples_skills_dir):
            path = os.path.join(examples_skills_dir, item)
            if os.path.isdir(path) and not item.startswith('.'):
                # Check if it's a skill
                if os.path.exists(os.path.join(path, 'SKILL.md')):
                    status = validate_skill(path)
                    inventory["skills"].append({
                        "path": path,
                        "location": "examples/skills",
                        "status": status
                    })
                # Also check subdirectories if it's a category folder (like 'document-skills' might contain skills?)
                # Based on previous list_dir, 'document-skills' has 130 children, likely skills.
                # Let's recurse one level if SKILL.md is not found but it has subdirs
                elif not os.path.exists(os.path.join(path, 'SKILL.md')):
                     for subitem in os.listdir(path):
                        subpath = os.path.join(path, subitem)
                        if os.path.isdir(subpath) and os.path.exists(os.path.join(subpath, 'SKILL.md')):
                            status = validate_skill(subpath)
                            inventory["skills"].append({
                                "path": subpath,
                                "location": f"examples/skills/{item}",
                                "status": status
                            })

    # Scan plugins
    plugins_dir = os.path.join(root_dir, 'plugins')
    if os.path.exists(plugins_dir):
        for plugin in os.listdir(plugins_dir):
            plugin_path = os.path.join(plugins_dir, plugin)
            if os.path.isdir(plugin_path) and not plugin.startswith('.'):
                
                # Check for skills in plugin
                skills_dir = os.path.join(plugin_path, 'skills')
                if os.path.exists(skills_dir):
                    for skill in os.listdir(skills_dir):
                        skill_path = os.path.join(skills_dir, skill)
                        if os.path.isdir(skill_path) and os.path.exists(os.path.join(skill_path, 'SKILL.md')):
                            status = validate_skill(skill_path)
                            inventory["skills"].append({
                                "path": skill_path,
                                "location": f"plugins/{plugin}/skills",
                                "status": status
                            })
                
                # Check for agents in plugin
                agents_dir = os.path.join(plugin_path, 'agents')
                if os.path.exists(agents_dir):
                    for agent in os.listdir(agents_dir):
                        agent_path = os.path.join(agents_dir, agent)
                        if os.path.isdir(agent_path):
                            files = os.listdir(agent_path)
                            inventory["agents"].append({
                                "path": agent_path,
                                "location": f"plugins/{plugin}/agents",
                                "type": "directory",
                                "files": files
                            })
                        elif agent.endswith('.md'):
                             inventory["agents"].append({
                                "path": agent_path,
                                "location": f"plugins/{plugin}/agents",
                                "type": "markdown",
                                "name": agent
                            })

    return inventory

if __name__ == "__main__":
    root_dir = "/Users/admac/Developer/github/claude-gtm-agents"
    inventory = scan_repo(root_dir)
    print(json.dumps(inventory, indent=2))
