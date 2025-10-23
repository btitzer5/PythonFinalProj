class Contact:
    def __init__(self, name, email, phone, company):
        self.name = name
        self.email = email
        self.phone = phone
        self.company = company

    def to_dict(self):
        return {
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
            data['company']
        )
