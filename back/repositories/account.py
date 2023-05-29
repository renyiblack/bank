import typing

from entities.account import Account
from entities.bonus_account import BonusAccount
from entities.savings_account import SavingsAccount
from errors.account_not_found import AccountNotFound


class AccountRepository:
    __accounts: typing.Dict[int, Account]

    def __init__(self):
        self.__accounts = {}

    def add_account(self, acc: int, type: str, balance: int):
        if type == "bonus":
            self.__accounts[acc] = BonusAccount(acc, balance)
        elif type == "savings":
            self.__accounts[acc] = SavingsAccount(acc, balance)
        else:
            self.__accounts[acc] = Account(acc, balance)

    def get_account_by_number(self, number: int) -> Account:
        try:
            return self.__accounts[number]
        except:
            raise Exception("account not found")

    def update_account(self, acc: Account):
        try:
            self.__accounts[acc.number] = acc
        except:
            raise AccountNotFound()
