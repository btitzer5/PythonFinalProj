import uuid


class Contact:
    def __init__(self, name, email, phone, company, guid = None):
        self.name = name
        self.email = email
        self.phone = phone
        self.company = company
        self.guid = guid or str(uuid.uuid4())


    def to_dict(self):
        return {
            'guid': self.guid,
            'name': self.name,
            'email': self.email,
            'phone': self.phone,
            'company': self.company
            
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            data['name'],
            data['email'],
            data['phone'],
            data['company'],
            data['guid']
        )
