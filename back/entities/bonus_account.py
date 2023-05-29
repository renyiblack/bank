from entities.account import Account


class BonusAccount(Account):
    points: int

    def __init__(self, number: int, balance: int):
        super().__init__(number, balance)
        self.points = 10

    def add_points(self, value: int, op: str):
        if op == "credit":
            points_to_add = int(value/100)
            self.points += points_to_add
        elif op == "transfer":
            points_to_add = int(value/150)
            self.points += points_to_add
        