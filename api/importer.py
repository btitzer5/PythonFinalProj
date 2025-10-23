import requests
import json
from models.contact import Contact

def fetch_random_users(n=5):
    url = f'https://randomuser.me/api/?results={n}'
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()['results']
    contacts = []
    for user in data:
        name = f"{user['name']['first']} {user['name']['last']}"
        email = user['email']
        phone = user['phone']
        company = user['location']['city']  # Using city as a placeholder for company
        contacts.append(Contact(name, email, phone, company))
    return contacts

def save_data(contacts, filename='data/contacts.json'):
    with open(filename, 'w') as f:
        json.dump([c.to_dict() for c in contacts], f, indent=2)

if __name__ == '__main__':
    contacts = fetch_random_users()
    save_data(contacts)
    print(f"Saved {len(contacts)} contacts to data/contacts.json")
