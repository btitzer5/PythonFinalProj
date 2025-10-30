class Deal:

    def __init__(self, name):
        self.name = name

    def to_dict(self):
        return {
            'name': self.name
        }
    
    @classmethod
    def from_dict(cls, data):
        return cls(
            data['name']
        )