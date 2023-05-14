class Account:
    id: int
    number: int
    balance: int

    def __init__(self, id: int, number: int):
        self.id = id
        self.number = number
        self.balance = 0
