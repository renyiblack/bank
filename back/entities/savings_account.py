from account import Account

class SavingsAccount(Account):

    def yield_interest(rate: float):
        super.balance += super.balance * (1 + rate/100)