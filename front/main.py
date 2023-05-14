def showMenu():
    print("+--------------------+")
    print("|        MENU        |")
    print("+--------------------+")
    print("| 0 - Exit           |")
    print("| 1 - Create Account |")
    print("| 2 - Get Balance    |")
    print("| 3 - Deposit        |")
    print("| 4 - Debit          |")
    print("| 5 - Transfer       |")
    print("+--------------------+")

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
                print("=> Creating account.")
            case 2:
                print("=> Getting your balance.")
            case 3:
                print("=> Depositing in the account.")
            case 4:
                print("=> Debiting from the account.")
            case 5:
                print("=> Transferring money.")
            case _:
                print("=> Invalid Option!")