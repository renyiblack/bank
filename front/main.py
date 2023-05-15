import requests

baseURL = "http://localhost:5000"

def showMenu():
    print("+--------------------+")
    print("|        MENU        |")
    print("+--------------------+")
    print("| 0 - Exit           |")
    print("| 1 - Create Account |")
    print("| 2 - Get Balance    |")
    print("| 3 - Credit         |")
    print("| 4 - Debit          |")
    print("| 5 - Transfer       |")
    print("+--------------------+")

def create_account(number):
    data = {
        "account_number": number
    }
    response = requests.post(baseURL + "/account", json=data)
    if response.status_code == 201:
        print("Account created successfully! Account number:", number)
    else:
        print("Failed to create account. Status:", response.status_code)

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
    response = requests.put(baseURL + "/balance", json=data)

    if response.status_code == 204:
        print("=> Account updated successfully!")
    else:
        print("=> " + response.text)

def debit(account_number, value):
    data = {
        "account_number": account_number,
        "transaction": -value
    }
    response = requests.put(baseURL + "/balance", json=data)

    if response.status_code == 204:
        print("=> Account updated successfully!")
    else:
        print("=> " + response.text)

def transfer(source_account, destination_account, value):
    # Verifica o saldo da conta de origem
    response = requests.get(baseURL + f"/balance/{source_account}")
    if response.status_code != 200:
        print("=> Failed to transfer. Source account not found.")
        return

    source_balance = float(response.text)
    
    # Verifica se há saldo suficiente na conta de origem
    if source_balance < value:
        print("=> Failed to transfer. Insufficient funds in the source account.")
        return

    # Realiza o débito da conta de origem
    debit_data = {
        "account_number": source_account,
        "transaction": -value
    }
    response = requests.put(baseURL + "/balance", json=debit_data)
    if response.status_code != 204:
        print("=> Failed to transfer. Error debiting the source account.")
        return

    # Realiza o crédito na conta de destino
    credit_data = {
        "account_number": destination_account,
        "transaction": value
    }
    response = requests.put(baseURL + "/balance", json=credit_data)
    if response.status_code != 204:
        print("=> Failed to transfer. Error crediting the destination account.")
        return

    print("=> Transfer successful!")

if __name__ == '__main__':
    userInput = 0
    while True:
        showMenu()
        userInput = int(input("=> Choose an option:"))

        match userInput:
            case 0:
                print("=> Exit!")
                break
            case 1:
                account_number = int(input("=> Enter account number:"))
                create_account(account_number)
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
            case _:
                print("=> Invalid Option!")