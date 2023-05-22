from entities.account import Account


class SavingsAccount(Account):

    def __init__(self, acc: Account):
        super().__init__(acc.number)
        self.balance = acc.balance

    def yield_interest(self, rate: float):
        self.balance += self.balance * (rate / 100)
