from flask import Flask, request, json

from entities.account import Account
from repositories.account import AccountRepository

app = Flask(__name__)

accRepo: AccountRepository = AccountRepository()

if __name__ == '__main__':
    Flask(__name__)


@app.route("/account", methods=["POST"])
def create_account():
    acc: json = request.get_json()
    try:
        accRepo.add_account(acc["account_number"])
        return "", 201
    except:
        return "failed to create account", 400


@app.route("/balance/<int:account>", methods=["GET"])
def get_balance(account):
    try:
        acc: Account = accRepo.get_account_by_number(account)
        return repr(acc.balance), 200
    except Exception as e:
        print(e)
        return "failed to locate account", 400


@app.route("/balance", methods=["PUT"])
def update_account_balance():
    acc: json = request.get_json()
    try:
        account: Account = accRepo.get_account_by_number(acc["account_number"])
        account.balance += acc["transaction"]
        accRepo.update_account(account)
        return "", 204
    except:
        return "failed to update account", 400


@app.route("/transfer", methods=["POST"])
def transfer():
    acc: json = request.get_json()
    try:
        origin_account: Account = accRepo.get_account_by_number(acc["account_number"])
        destination_account: Account = accRepo.get_account_by_number(acc["destination_number"])
        origin_account.balance -= acc["value"]
        destination_account.balance += acc["value"]

        try:
            accRepo.update_account(origin_account)
        except:
            return "failed to update origin account", 400

        try:
            accRepo.update_account(destination_account)
        except:
            origin_account.balance += acc["value"]
            accRepo.update_account(origin_account)
            return "failed to complete the transfer", 400

        return "", 204
    except:
        return "failed to update account", 400
