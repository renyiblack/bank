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
    response = requests.post(baseURL + "/account", json = data)
    print(response)

def get_balance(number):
    response = requests.get(baseURL + f"/balance/{number}")
    if(response.status_code == 200):
        print("=> Account balance is " + response.text)
    else:
        print("=> " + response.text)

def credit(account_number, value):
    data = {
        "account_number": account_number,
        "transaction": value
    }
    response = requests.put(baseURL + "/balance", json = data)

    if(response.status_code == 204):
        print("=> Account updated succefully!")
    else:
        print("=> " + response.text)


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
                print("=> Debiting from the account.")
            case 5:
                print("=> Transferring money.")
            case _:
                print("=> Invalid Option!")