import json

def load_json(filename):
    """Load JSON data from a file."""
    with open(filename, 'r') as f:
        return json.load(f)
    

def save_json(data, filename):
    """Save JSON data to a file."""
    with open(filename, 'w') as f:
        json.dump(data, f, indent=2)


def validate_json(data, schema):
    """Validate JSON data against a schema."""
    pass
    


