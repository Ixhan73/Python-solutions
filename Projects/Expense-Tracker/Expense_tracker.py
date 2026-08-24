import json


choices = ['\n1.Add new expense', 
           '2.View expenses', 
           '3.Total expenses', 
           '4.Exit']

#========== LOADING THE DATA ====================

def load_data():
    try:
        with open('expenses.json', 'r') as file:
            return json.load(file)
        
    except (FileNotFoundError, json.JSONDecodeError):
        return []


expenses = load_data()

#========= FOR ADDING EXPENSES ==================

def add_expense(expenses):

    while True:
        expense = input("Enter expense: ").title()
        try:
            amount = int(input("Enter amount: "))
            if amount <= 0:
                print("Please enter a valid amount!")
                continue
        except ValueError:
            print("Please enter a number!")
            continue

        expense_amount = {"description":expense,
                        "amount": amount}
        
        expenses.append(expense_amount)

        print("\tInfo stored!")
        break

#========== FOR VIEWING EXPENSES =================

def view_expenses(expenses):

    if not expenses:
        print("You don't have any expenses yet.")
        return

    for i, expense in enumerate(expenses, start=1):
        print(f"{i}. {expense['description']} - ${expense['amount']}")

#=========== FOR CALCULATING TOTAL ===============

def total_expenses(expenses):
    
    
    if not expenses:
        print("You don't have any expenses yet.")
        return
    
    amount = 0

    for expense in expenses:
        amount += expense['amount']

    print(f"Total amount: ${amount}")

#=========== FOR STORING IN A FILE ================

def store_expenses(expenses):
    with open('expenses.json', 'w') as file:
            json.dump(expenses, file, indent=4)


#===================================
#|           MAIN LOOP             |
#===================================

while True:
    for choice in choices:
        print(choice)

    user_choice = input("\nChoose 1-4: ")
    if user_choice == '1':
        add_expense(expenses)
        store_expenses(expenses)
        
    elif user_choice == '2':
        view_expenses(expenses)

    elif user_choice == '3':
        total_expenses(expenses)

    elif user_choice == '4':
        print("Exiting ...")
        break
    else:
        print("Invalid choice")