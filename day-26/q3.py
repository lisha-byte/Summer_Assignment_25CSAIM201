# ATM simulation
balance = 10000
pin = 1234

entered_pin = int(input("Enter your PIN: "))

if entered_pin == pin:
    print("1. Check Balance")
    print("2. Withdraw")
    print("3. Deposit")
    choice = int(input("Enter choice: "))
    
    if choice == 1:
        print("Your balance is:", balance)
    
    elif choice == 2:
        amount = int(input("Enter amount to withdraw: "))
        if amount <= balance:
            balance = balance - amount
            print("Withdrawal successful")
            print("Remaining balance:", balance)
        else:
            print("Insufficient balance")
    
    elif choice == 3:
        amount = int(input("Enter amount to deposit: "))
        balance = balance + amount
        print("Deposit successful")
        print("New balance:", balance)
    
    else:
        print("Invalid choice")
else:
    print("Incorrect PIN")