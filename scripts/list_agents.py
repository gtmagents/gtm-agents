import json

with open('inventory.json', 'r') as f:
    data = json.load(f)

print(f"Total Agents: {len(data.get('agents', []))}")
for agent in data.get('agents', []):
    print(f"- {agent['location']}: {agent.get('name') or agent.get('files')}")
