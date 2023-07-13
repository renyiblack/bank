import json

from errors.insufficient_funds import InsufficientFunds


class Account:
    number: int
    balance: float

    def __init__(self, number: int):
        self.number = number
        self.balance = 0

    def update_balance(self, balance: float):
        temp_balance: float = self.balance + balance

        if temp_balance < -1000:
            raise InsufficientFunds()

        self.balance = temp_balance

    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)

    def __repr__(self):
        return repr(self.to_json())
