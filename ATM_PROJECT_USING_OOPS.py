class User:
    def __init__(self, name, contact, pin, balance):
        self.name = name
        self.contact = contact
        self.pin = pin
        self.balance = balance
        self.transaction_history = []


class ATM:
    def __init__(self, user):
        self.user = user
        self.remaining_attempts = 3

    def verify_pin(self):
        while self.remaining_attempts > 0:
            entered_pin = input("Please enter your ATM PIN: ")

            if len(entered_pin) != 4:
                print("Please enter a valid 4-digit PIN.")
                continue

            if entered_pin == self.user.pin:
                print("\nLogin Successful!")
                return True
            else:
                self.remaining_attempts -= 1
                print("-----* Invalid PIN *-----")

                if self.remaining_attempts > 0:
                    print(f"You have only {self.remaining_attempts} attempts left.")
                else:
                    print("Your card has been BLOCKED.")
        return False

    def check_balance(self):
        print(f"\nYour Current Balance: {self.user.balance}")

    def withdraw_money(self):
        amount = int(input("Enter the amount to withdraw: "))

        if amount > self.user.balance:
            print("----* Insufficient Balance *----")
        elif amount < 100 or amount % 100 != 0:
            print("----* Enter valid amount *----")
        else:
            self.user.balance -= amount
            self.user.transaction_history.append(f"Withdraw: {amount}")
            print("Please collect your cash.")
            print(f"Remaining Balance: {self.user.balance}")

    def deposit_money(self):
        amount = int(input("Enter the amount to deposit: "))

        if amount > 0:
            self.user.balance += amount
            self.user.transaction_history.append(f"Deposited: {amount}")
            print("Money Deposited Successfully.")
            print(f"Updated Balance: {self.user.balance}")
        else:
            print("Enter a valid amount.")

    def mini_statement(self):
        print("\n----- MINI STATEMENT -----")

        if len(self.user.transaction_history) == 0:
            print("No transactions available.")
        else:
            for transaction in self.user.transaction_history:
                print(transaction)

        print(f"Available Balance: {self.user.balance}")

    def change_pin(self):
        old_pin = input("Enter old PIN: ")

        if old_pin == self.user.pin:
            new_pin = input("Enter new 4-digit PIN: ")

            if len(new_pin) == 4:
                confirm_pin = input("Confirm new PIN: ")

                if new_pin == confirm_pin:
                    self.user.pin = new_pin
                    print("PIN changed successfully.")
                else:
                    print("PIN does not match.")
            else:
                print("PIN must contain exactly 4 digits.")
        else:
            print("Wrong old PIN.")

    def menu(self):
        while True:
            print("\n------ ATM MENU ------")
            print("1. Check Balance")
            print("2. Withdraw Money")
            print("3. Deposit Money")
            print("4. Mini Statement")
            print("5. Change PIN")
            print("6. Exit")

            try:
                choice = int(input("Select option: "))
            except ValueError:
                print("Please enter a valid number.")
                continue

            if choice == 1:
                self.check_balance()

            elif choice == 2:
                self.withdraw_money()

            elif choice == 3:
                self.deposit_money()

            elif choice == 4:
                self.mini_statement()

            elif choice == 5:
                self.change_pin()

            elif choice == 6:
                print("Thank you for using ATM.")
                break

            else:
                print("Invalid option.")


# ---------------- MAIN PROGRAM ---------------- #

print("-----* PLEASE INSERT YOUR CARD *-----")

user = User(
    name="Mohith_Ram",
    contact="",
    pin="2435",
    balance=1200000
)

atm = ATM(user)

if atm.verify_pin():
    atm.menu()
