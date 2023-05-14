from entities.account import Account


class AccountRepository:
    __accounts: []

    def __init__(self):
        self.__accounts = []

    def add_account(self, acc: int):
        self.__accounts.append(Account(len(self.__accounts), acc))

    def get_account_by_number(self, number: int) -> Account:
        for acc in self.__accounts:
            account: Account = acc
            if account.number == number:
                return account

        raise Exception("account not found")
