import os
import json

def get_plugin_contents(root_dir):
    plugins_dir = os.path.join(root_dir, 'plugins')
    empty_plugins = []
    
    if not os.path.exists(plugins_dir):
        return []

    for plugin in os.listdir(plugins_dir):
        plugin_path = os.path.join(plugins_dir, plugin)
        if os.path.isdir(plugin_path) and not plugin.startswith('.'):
            has_skills = False
            has_agents = False
            
            skills_dir = os.path.join(plugin_path, 'skills')
            if os.path.exists(skills_dir) and os.listdir(skills_dir):
                has_skills = True
            
            agents_dir = os.path.join(plugin_path, 'agents')
            if os.path.exists(agents_dir) and os.listdir(agents_dir):
                has_agents = True
            
            if not has_skills and not has_agents:
                empty_plugins.append(plugin)
                
    return empty_plugins

root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
empty = get_plugin_contents(root_dir)

if empty:
    print("Empty Plugins:")
    for p in empty:
        print(f"- {p}")
else:
    print("No empty plugins found.")
