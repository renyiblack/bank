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
        accRepo.add_account(acc["number"])
        return "", 201
    except:
        return "failed to create account", 400
