from entities.account import Account


class AccountRepository:
    __accounts: []

    def __init__(self):
        self.__accounts = []

    def add_account(self, acc: Account):
        self.__accounts.append(acc)
