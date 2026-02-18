# ATM MINI PROJECT
balance = 200000
correct_pin = 9660
transection = []

print("--------------- Welcome to ATM ---------------")

pin = int(input("Enter your PIN: "))

if pin != correct_pin:
    print("Invalid PIN. Please enter correct PIN.")
else:
    while True:  # NEW 
        print("\n1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Transaction History")
        print("5. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            print("Current Balance =", balance)

        elif choice == 2:
            amount = int(input("Enter deposit amount: "))
            if amount > 0:
                balance += amount   ## NEW
                transection.append(f"Deposited: {amount}")
                print("Amount deposited successfully")  # NEW
                print("Available Balance =", balance)
            else:
                print("Invalid amount")

        elif choice == 3:
            amount = int(input("Enter withdraw amount: "))
            if amount > 0 and amount <= balance:  # NEW
                balance -= amount
                transection.append(f"Withdrawn: {amount}")
                print("Collect your cash")
                print("Available Balance =", balance)
            else:
                print("Insufficient balance or invalid amount") # NEW

        elif choice == 4:
            if not transection:  # NEW
                print("No transaction history")
            else:
                print("Transaction History:")
                for t in transection:
                    print("-", t)

        elif choice == 5:
            print("Thanks for visiting ATM")
            break

        else:
            print("Invalid choice")




