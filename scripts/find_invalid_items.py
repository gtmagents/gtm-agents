import json

with open('inventory.json', 'r') as f:
    data = json.load(f)

print("Invalid Skills:")
for skill in data.get('skills', []):
    if not skill.get('status', {}).get('valid', False):
        print(f"- {skill['path']}: {skill['status'].get('error')}")

print("\nInvalid Agents:")
# Agents don't have a 'valid' flag in the current inventory script, 
# but we can check if they are missing expected fields or have empty lists.
for agent in data.get('agents', []):
    # For now, just list them so we can see what we have.
    # The inventory script didn't do deep validation on agents.
    pass
