from core import ops, store

def add(model):
    ops.add_record(model)

def list():
    print(ops.list_records())

def search(query):
    print(ops.search_records(query))

def _import(users=5):
    ops.import_records(int(users))

def charts():
    from core.charts import contacts_chart, deals_chart
    contacts_chart()
    deals_chart()
    print("Charts saved to /static")

def __repl__ ():
    while True:
        cmd = input("Enter command (add, list, search <query>, import <n>, exit): ")
        parts = cmd.split()
        if not parts:
            continue
        action = parts[0].lower()
        if action == 'add':
            name = input("Name: ")
            email = input("Email: ")
            phone = input("Phone: ")
            company = input("Company: ")
            from models.contact import Contact
            contact = Contact(name, email, phone, company)
            add(contact)
            print("Contact added.")
        elif action == 'list':
            list()
        elif action == 'search' and len(parts) > 1:
            query = ' '.join(parts[1:])
            search(query)
        elif action == 'charts':
            charts()
        elif action == 'import' and len(parts) > 1:
            print(len(parts))
            print(parts[1])
            try:
                n = int(parts[1])
                _import(n)
            except ValueError as ve:
                print("Please provide a valid number of users to import.", ve)
        elif action == 'exit':
            break
        else:
            print("Unknown command.")

if __name__ == '__main__':
    __repl__()

