import json
from models.contact import Contact
from models.company import Company
import os

def save_contacts(contacts, filename='data/contacts.json'):
    with open(filename, 'w') as f:
        json.dump([c.to_dict() for c in contacts], f, indent=2)

def load_contacts(filename='data/contacts.json'):
    if not os.path.exists(filename):
        return []
    with open(filename, 'r') as f:
        data = json.load(f)
        return [Contact.from_dict(item) for item in data]

if __name__ == '__main__':
    # Run the API importer
    from api.importer import fetch_random_users, save_data
    contacts = fetch_random_users()
    save_data(contacts)
    loaded = load_contacts()
    print(f"Loaded {len(loaded)} contacts from data/contacts.json:")
    for c in loaded:
        print(c.to_dict())
