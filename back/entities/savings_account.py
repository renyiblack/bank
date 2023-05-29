from entities.account import Account

from errors.insufficient_funds import InsufficientFunds

class SavingsAccount(Account):

    def update_balance(self, balance: float):
        temp_balance: float = self.balance + balance

        if temp_balance < 0:
            raise InsufficientFunds()

        self.balance = temp_balance

    def yield_interest(self, rate: float):
        self.update_balance(self.balance * (rate / 100))
