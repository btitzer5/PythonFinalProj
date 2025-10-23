class Company:
    def __init__(self, name, industry, size):
        self.name = name
        self.industry = industry
        self.size = size

    def to_dict(self):
        return {
            'name': self.name,
            'industry': self.industry,
            'size': self.size
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            data['name'],
            data['industry'],
            data['size']
        )
