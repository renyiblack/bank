from entities.account import Account


class SavingsAccount(Account):

    def __init__(self, acc: Account, initial_value: float):
        super().__init__(acc.number)
        self.balance = initial_value

    def yield_interest(self, rate: float):
        self.balance += self.balance * (rate / 100)
