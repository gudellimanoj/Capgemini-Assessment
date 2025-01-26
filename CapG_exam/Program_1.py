# 1. ATM Simulation

balance=0.0
def check_balance():
    print(f"Current Balance is: {balance:}")
def deposit():
    global balance
    amount=float(input("enter deposit amount:"))
    if amount > 0:
        balance += amount
        print(f"{amount:} deposited sucessfully")
    else:
        print("Invalid Amount")
def withdraw_money():
    global balance
    amount=float(input("enter withdrawl amount:"))
    if amount >0:
        balance -= amount
        print(f"{amount:} withdrawl sucessfully")
    else:
        print("Invalid amount")
def ATM_menu():
    while True:
        print("MENU")
        print("1. Check Balance:")
        print("2. Deposit Money:")
        print("3. Withdraw Money:")
        print("4.Exit")
        choice=input("Choose Opt:")

        if choice == '1':
            check_balance()
        elif choice == '2':
            deposit()
        elif choice == '3':
            withdraw_money()
        elif choice == '4':
            print("Exit")
            break
        else:
            print("Invalid choice")
ATM_menu()


            

