import json

def settings():
    with open('settings.json', 'r+', errors="ignore") as f:
        return json.loads(f.read())