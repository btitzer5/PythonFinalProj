import os
import json
from models import contact, company, activity, deal
from . import store
from api import importer

def add_record(model, filename='data/contacts.json'):
    """Add a new record to the database."""
    records = []
    records = list_records(filename)
    records.append(model.to_dict())
    store.save_json(records, filename)

def list_records(filename='data/contacts.json'):
    """List all records in the database."""
    if not os.path.exists(filename):
        return []
    records = store.load_json(filename)
    return records

def search_records(query, filename='data/contacts.json'):
    """Search for records matching the query."""
    records = list_records(filename)
    results = [rec for rec in records if query.lower() in rec.get('name', '').lower()]
    return results

def import_records(users = 5, filename='data/contacts.json'):
    """Import data into the database."""
    data = list_records(filename)
    new_contacts = importer.fetch_random_users(users)
    # If new_contacts are already dicts, don't call .to_dict()
    if hasattr(new_contacts[0], 'to_dict'):
        new_contacts = [c.to_dict() for c in new_contacts if hasattr(c, 'to_dict')]
    store.save_json(data + new_contacts, filename)
    print(f"Imported {len(new_contacts)} records into {filename}")

def clear_records(filename='data/contacts.json'):
    """Clear all records from the database."""
    store.save_json([], filename)
    print(f"Cleared all records from {filename}")

def delete_record(guid, filename='data/contacts.json'):
    """Delete a record by its GUID."""
    records = list_records(filename)
    records = [rec for rec in records if rec.get('guid') != guid]
    store.save_json(records, filename)
    print(f"Deleted record with GUID {guid} from {filename}")