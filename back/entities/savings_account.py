from entities.account import Account


class SavingsAccount(Account):
    def yield_interest(self, rate: float):
        self.balance += self.balance * (rate / 100)
