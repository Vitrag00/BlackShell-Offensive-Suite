import json

def load_config(path="config.json"):
    try:
        with open(path) as f:
            return json.load(f)
    except FileNotFoundError:
        print("[!] config.json not found.")
        return {}
