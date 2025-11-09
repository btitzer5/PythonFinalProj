import requests
import json
from models.contact import Contact
import random

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
        company = assign_company()
        contact = Contact(name, email, phone, company)
        contacts.append(contact)
    return contacts

def assign_company():
    commpanies = {
        1 : 'Google',
        2 : 'Microsoft',
        3 : 'Apple',
        4 : 'Amazon',
        5 : 'Facebook',
        6 : 'Tesla',
        7 : 'Netflix',
        8 : 'IBM',
        9 : 'Intel',
        10 : 'Cisco'
    }
    x = random.randint(1, 10)
    return commpanies[x]




# def save_data(contacts, filename='data/contacts.json'):
#     with open(filename, 'w') as f:
#        json.dump([c.to_dict() for c in contacts], f, indent=2)

# if __name__ == '__main__':
#     contacts = fetch_random_users()
#     save_data(contacts)
#     print(f"Saved {len(contacts)} contacts to data/contacts.json")
