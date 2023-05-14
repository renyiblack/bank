import json


class Account:
    id: int
    number: int
    balance: int

    def __init__(self, id: int, number: int):
        self.id = id
        self.number = number
        self.balance = 0

    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)

    def __repr__(self):
        return repr(self.to_json())
