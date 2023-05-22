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
    print("+---------------------------+")
    print("|    CREATE ACCOUNT MENU    |")
    print("+---------------------------+")
    print("| 1 - Normal                |")
    print("| 2 - Bonus                 |")
    print("| 3 - Poupança              |")
    print("+---------------------------+")


def create_account(number):
    data = {
        "account_number": number
    }
    response = requests.post(baseURL + "/account", json=data)
    if response.status_code == 201:
        print("Account created successfully! Account number:", number)
    else:
        print("Failed to create account. Status:", response.status_code)


def create_bonus_account(number):
    data = {
        "account_number": number,
        "account_type": "Bonus",
        "points": 10
    }
    response = requests.post(baseURL + "/account", json=data)
    if response.status_code == 201:
        print("Bonus account created successfully! Account number:", number)
        print("Initial points:", data["points"])
    else:
        print("Failed to create bonus account. Status:", response.status_code)


def get_balance(number):
    response = requests.get(baseURL + f"/balance/{number}")
    if response.status_code == 200:
        print("=> Account balance is " + response.text)
    else:
        print("=> " + response.text)


def credit(account_number, value):
    data = {
        "account_number": account_number,
        "transaction": value
    }
    response = requests.put(baseURL + "/credit", json=data)

    if response.status_code == 204:
        print("=> Account updated successfully!")
        if value > 0:
            account_type = get_account_type(account_number)
            if account_type == "Bonus":
                update_points(account_number, calculate_bonus_points(value))
    else:
        print("=> " + response.text)


def debit(account_number, value):
    data = {
        "account_number": account_number,
        "transaction": value
    }
    response = requests.put(baseURL + "/debit", json=data)

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
    response = requests.post(baseURL + "/transfer", json=transfer_data)
    if response.status_code != 204:
        print("=> Failed to transfer. " + response.text)
        return

    print("=> Transfer successful!")
    account_type = get_account_type(destination_account)
    if account_type == "Bonus":
        update_points(destination_account, calculate_bonus_points(value))


def get_account_type(number):
    response = requests.get(baseURL + f"/account/{number}")
    if response.status_code == 200:
        account = response.json()
        return account.get("account_type")
    else:
        print("=> Failed to get account type. " + response.text)
        return None


def update_points(account_number, points):
    data = {
        "account_number": account_number,
        "points": points
    }
    response = requests.put(baseURL + "/points", json=data)

    if response.status_code == 204:
        print("=> Points updated successfully!")
    else:
        print("=> " + response.text)


def calculate_bonus_points(amount):
    return amount // 100 if amount > 0 else 0

def interest(account_number, rate):
    data = {
        "account_number": account_number,
        "rate": rate
    }
    response = requests.put(baseURL + "/interest", json=data)

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
                show_create_account_menu()
                account_type = int(input("=> Choose an account type:"))
                if account_type in [1, 2, 3]:
                    account_number = int(input("=> Enter account number:"))
                    if account_type == 2:
                        create_bonus_account(account_number)
                    else:
                        create_account(account_number)
                else:
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