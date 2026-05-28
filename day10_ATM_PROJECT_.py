'''
print("-----* PLEASE INSERT YOUR CARD *-----")

User_information = {
    "Name": "Mohith_Ram",
    "contact": "",
    "ATM PIN": "2435",
    "Balance": 1200000,
    "Transaction history": []
}

remaining_attempts = 3
while remaining_attempts > 0:
    user_pin = input("Please enter your ATM PIN : ")
    if len(user_pin) == 4:
        if user_pin == User_information["ATM PIN"]:
            while True:
                print("\n------ ATM MENU ------")
                print("1. Check Balance")
                print("2. Withdraw Money")
                print("3. Deposit Money")
                print("4. Mini Statement")
                print("5. Change PIN")
                print("6. Exit")
                Choice = int(input("Select option : "))
                if Choice == 1:
                    print(f"Your Current Balance is : {User_information['Balance']}")
                elif Choice == 2:
                    w_d = int(input("Enter the money to withdraw : "))
                    if w_d <= User_information["Balance"]:
                        if w_d >= 100 and w_d % 100 == 0:
                            User_information["Balance"] -= w_d
                            User_information["Transaction history"].append(
                                f"Withdraw : {w_d}")
                            print("Please collect your cash")
                            print(f"Remaining Balance : {User_information['Balance']}")
                        else:
                            print("----* Enter valid amount *----")
                    else:
                        print("----* Insufficient Balance *----")
                elif Choice == 3:
                    depo = int(input("Enter the money to deposit : "))
                    if depo > 0:
                        User_information["Balance"] += depo
                        User_information["Transaction history"].append(
                           f"Deposited : {depo}")
                        print("Money Deposited Successfully")
                        print(f"Updated Balance : {User_information['Balance']}")
                    else:
                        print("Enter valid amount")
                elif Choice == 4:
                    print("\n----- MINI STATEMENT -----")
                    if len(User_information["Transaction history"]) == 0:
                        print("No transactions available")
                    else:
                        for i in User_information["Transaction history"]:
                            print(i)
                    print(f"Available Balance : {User_information['Balance']}")
                elif Choice == 5:
                    old_pin = input("Enter old PIN : ")
                    if old_pin == User_information["ATM PIN"]:
                        new_pin = input("Enter new 4 digit PIN : ")
                        if len(new_pin) == 4:
                            confirm_pin = input("Confirm new PIN : ")
                            if new_pin == confirm_pin:
                                User_information["ATM PIN"] = new_pin
                                print("PIN changed successfully")
                            else:
                                print("PIN does not match")
                        else:
                            print("PIN must contain 4 digits")
                    else:
                        print("Wrong old PIN")
                elif Choice == 6:

                    print("Thank you for using ATM")
                    break
                else:
                    print("Invalid option")
            break
        else:
            print("-----* Invalid PIN *-----")
            remaining_attempts -= 1
            if remaining_attempts > 0:
                print(f"You have only {remaining_attempts} attempts left")
            else:
                print("Your card has been BLOCKED")
    else:
        print("Please enter 4 digit PIN")
'''
# ---------- FUNCTIONS ----------

def check_balance():
    print(f"\nYour Current Balance is : {User_information['Balance']}")


def withdraw_money():

    w_d = int(input("Enter amount to withdraw : "))

    if w_d <= User_information["Balance"]:

        if w_d >= 100 and w_d % 100 == 0:

            User_information["Balance"] -= w_d

            User_information["Transaction history"].append(
                f"Withdraw : {w_d}"
            )

            print("Please collect your cash")
            print(f"Remaining Balance : {User_information['Balance']}")

        else:
            print("Enter valid amount")

    else:
        print("Insufficient Balance")


def deposit_money():

    depo = int(input("Enter amount to deposit : "))

    if depo > 0:

        User_information["Balance"] += depo

        User_information["Transaction history"].append(
            f"Deposited : {depo}"
        )

        print("Money Deposited Successfully")
        print(f"Updated Balance : {User_information['Balance']}")

    else:
        print("Enter valid amount")


def mini_statement():

    print("\n----- MINI STATEMENT -----")

    if len(User_information["Transaction history"]) == 0:
        print("No transactions available")

    else:
        for i in User_information["Transaction history"]:
            print(i)

    print(f"Available Balance : {User_information['Balance']}")


def change_pin():

    old_pin = input("Enter old PIN : ")

    if old_pin == User_information["ATM PIN"]:

        new_pin = input("Enter new 4 digit PIN : ")

        if len(new_pin) == 4:

            confirm_pin = input("Confirm new PIN : ")

            if new_pin == confirm_pin:

                User_information["ATM PIN"] = new_pin

                print("PIN changed successfully")

            else:
                print("PIN does not match")

        else:
            print("PIN must contain 4 digits")

    else:
        print("Wrong old PIN")


