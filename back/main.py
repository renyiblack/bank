from flask import Flask, request, json

from entities.account import Account
from entities.bonus_account import BonusAccount
from errors.account_not_found import AccountNotFound
from errors.insufficient_funds import InsufficientFunds
from repositories.account import AccountRepository

app = Flask(__name__)

accRepo: AccountRepository = AccountRepository()

if __name__ == '__main__':
    Flask(__name__)


@app.route("/account", methods=["POST"])
def create_account():
    acc: json = request.get_json()
    print(acc)
    try:
        if acc["account_type"] == "savings" and type(acc["initial_value"]) is None:
            return "failed to create account. Savings Accounts must have initial value", 400

        accRepo.add_account(acc["account_number"], acc["account_type"], acc["initial_value"])
        return "", 201
    except:
        return "failed to create account", 400


@app.route("/balance/<int:account>", methods=["GET"])
def get_balance(account):
    try:
        acc = accRepo.get_account_by_number(account)
        if type(acc) is BonusAccount:
            print(f"Account points: {acc.points}")
        return repr(acc.balance), 200
    except Exception as e:
        print(e)
        return "failed to locate account", 400


@app.route("/debit", methods=["PUT"])
def debit_account():
    acc: json = request.get_json()
    try:
        if acc["transaction"] < 0:
            return "value can't be negative", 400

        account: Account = accRepo.get_account_by_number(acc["account_number"])
        account.update_balance(acc["transaction"] * -1)
        accRepo.update_account(account)
        return "", 204
    except AccountNotFound as e:
        return "failed to update account. Account not found", 400
    except InsufficientFunds as e:
        return "failed to update account. Insufficient funds", 400
    except:
        return "failed to update account.", 400


@app.route("/credit", methods=["PUT"])
def credit_to_account():
    acc: json = request.get_json()
    try:
        if acc["transaction"] < 0:
            return "value can't be negative", 400

        account = accRepo.get_account_by_number(acc["account_number"])
        account.update_balance(acc["transaction"])
        accRepo.update_account(account)
        if type(account) is BonusAccount:
            account.add_points(acc["transaction"], "credit")
        return "", 204
    except AccountNotFound as e:
        return "failed to update account. Account not found", 400
    except InsufficientFunds as e:
        return "failed to update account. Insufficient funds", 400
    except:
        return "failed to update account.", 400


@app.route("/transfer", methods=["POST"])
def transfer():
    acc: json = request.get_json()
    try:
        if acc["value"] < 0:
            return "value can't be negative", 400

        origin_account: Account = accRepo.get_account_by_number(acc["account_number"])
        destination_account = accRepo.get_account_by_number(acc["destination_number"])
        origin_account.update_balance(acc["value"] * -1)
        destination_account.update_balance(acc["value"])
        if type(destination_account) is BonusAccount:
            destination_account.add_points(acc["value"], "transfer")

        try:
            accRepo.update_account(origin_account)
        except:
            return "failed to update origin account", 400

        try:
            accRepo.update_account(destination_account)
        except:
            origin_account.update_balance(acc["value"])
            accRepo.update_account(origin_account)
            return "failed to complete the transfer", 400

        return "", 204
    except:
        return "failed to update account", 400


@app.route("/interest", methods=["PUT"])
def yield_interest():
    acc: json = request.get_json()
    try:
        account = accRepo.get_account_by_number(acc["account_number"])
        account.yield_interest(float(acc["rate"]))
        accRepo.update_account(account)
        return "", 204
    except:
        return "this account type cannot yield interest", 400
