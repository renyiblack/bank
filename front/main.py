import requests

baseURL = "http://localhost:5000"

bonus_points = {
    "deposit": 1,
    "transfer_received": 1
}


def show_menu():
    print("+--------------------+")
    print("|        MENU        |")
    print("+--------------------+")
    print("| 0 - Exit           |")
    print("| 1 - Create Account |")
    print("| 2 - Get Balance    |")
    print("| 3 - Credit         |")
    print("| 4 - Debit          |")
    print("| 5 - Transfer       |")
    print("| 6 - Yield Interest |")
    print("+--------------------+")


def show_create_account_menu():
    print("+--------------------+")
    print("|   CREATE ACCOUNT   |")
    print("+--------------------+")
    print("| 1 - Normal         |")
    print("| 2 - Bonus          |")
    print("| 3 - Savings        |")
    print("+--------------------+")


def create_account(number, acc_type):
    initial_value = 0
    if acc_type == "savings":
        initial_value = int(input("=> Enter initial value:"))

    data = {
        "account_number": number,
        "account_type": acc_type,
        "initial_value": initial_value,
    }
    response = requests.post(baseURL + "/bank/account", json=data)
    if response.status_code == 201:
        print("Account created successfully! Account number:", number)
    else:
        print("Failed to create account. Status:", response.status_code)


def get_balance(number):
    response = requests.get(baseURL + f"/bank/account/{number}/balance")
    if response.status_code == 200:
        print("=> Account balance is " + response.text)
    else:
        print("=> " + response.text)


def credit(account_number, value):
    data = {
        "account_number": account_number,
        "transaction": value
    }
    response = requests.post(baseURL + f"/bank/account/{account_number}/debit", json=data)

    if response.status_code == 204:
        print("=> Account updated successfully!")
    else:
        print("=> " + response.text)


def debit(account_number, value):
    data = {
        "account_number": account_number,
        "transaction": value
    }
    response = requests.put(baseURL + f"/bank/account/{account_number}/debit", json=data)

    if response.status_code == 204:
        print("=> Account updated successfully!")
    else:
        print("=> " + response.text)


def transfer(source_account, destination_account, value):
    transfer_data = {
        "account_number": source_account,
        "destination_number": destination_account,
        "value": value
    }
    response = requests.post(baseURL + "/bank/account/transfer", json=transfer_data)
    if response.status_code != 204:
        print("=> Failed to transfer. " + response.text)
        return

    print("=> Transfer successful!")


def interest(account_number, rate):
    data = {
        "account_number": account_number,
        "rate": rate
    }
    response = requests.put(baseURL + "/bank/account/interest", json=data)

    if response.status_code == 204:
        print("=> Account updated successfully!")
    else:
        print("=> " + response.text)


if __name__ == '__main__':
    userInput = 0
    while True:
        show_menu()
        userInput = int(input("=> Choose an option:"))

        match userInput:
            case 0:
                print("=> Exit!")
                break
            case 1:
                account_number = int(input("=> Enter account number:"))
                show_create_account_menu()
                account_type = int(input("=> Choose an account type:"))
                match account_type:
                    case 1:
                        create_account(account_number, "normal")
                    case 2:
                        create_account(account_number, "bonus")
                    case 3:
                        create_account(account_number, "savings")
                    case _:
                        print("=> Invalid account type!")
            case 2:
                account_number = int(input("=> Enter account number:"))
                get_balance(account_number)
            case 3:
                account_number = int(input("=> Enter account number:"))
                value = int(input("=> Enter the amount to deposit:"))
                credit(account_number, value)
            case 4:
                account_number = int(input("=> Enter account number:"))
                value = int(input("=> Enter the amount to debit:"))
                debit(account_number, value)
            case 5:
                source_account = int(input("=> Enter source account number:"))
                destination_account = int(input("=> Enter destination account number:"))
                value = int(input("=> Enter the amount to transfer:"))
                transfer(source_account, destination_account, value)
            case 6:
                account_number = int(input("=> Enter account number:"))
                rate = float(input("=> Enter the interest rate:"))
                interest(account_number, rate)
            case _:
                print("=> Invalid Option!")
