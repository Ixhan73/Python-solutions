#============================= CREATE BANK ACCOUNT CLASS ===================

class BankAccount():
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    # DEPOSIT FUNCTION
    def deposit(self, deposit):
        if deposit > 0:
            self.balance += deposit
            return True
        else:
            print("Invalid amount!\n")
            return False

    # WTIHDRAW FUNCTION
    def withdraw(self, withdraw):
        if withdraw <= 0:
            print("Invalid withdrawal amount!")
            return False

        elif self.balance >= withdraw:
            self.balance -= withdraw
            return True
        else:
            print("There isn't enough money in your account")
            return False

    # VIEW BALANCE FUNCTION
    def show_balance(self):
        print("Current Balance: ", self.balance, '\n')

#=============================================================================

options = ['1.Deposit', '2.Withdraw', '3.Check Balance', '4.Exit']      
owner = input("\nPlease enter your name: ")
amount = int(input("Please enter your initial deposit: "))

#=============================================================================

#=============================================================================
                            # MAIN CODE LOOP
#=============================================================================
account = BankAccount(owner, amount)

while True:
    for option in options:
        print(option)

    choice = input("\nYour entry: ")
    if choice == '1':
        deposit_amount = int(input('\nHow much do you want to deposit: '))
        if account.deposit(deposit_amount):
            print(deposit_amount,"$ have been deposited!\n")
        

    elif choice == '2':
        withdraw_amount = int(input('\nEnter the amount you want to withdraw: '))
        if account.withdraw(withdraw_amount):
            print(withdraw_amount,"$ have been withdrawn!")


    elif choice == '3':
        account.show_balance()


    elif choice == '4':
        print('\n\tExiting')
        break

    else:
        print("Invalid choice! Please enter from 1-4\n")