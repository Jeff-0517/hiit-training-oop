balance = 1000000 
while True:
    print("/n==== BANK MENU ====")
    print("1. Check Balance")
    print("2. Recharge")
    print("3. Transfer")

    option = int(input("Select an option: "))

    if option == 1:
        print(f"Your balance is ₦{balance}")
    elif option == 2:
        amount = float(input("Enter the amount to recharge: ₦"))
        if amount <= balance:
            balance -= amount
            print(f" Recharge successful!")
            print(f" Remaining balance: ₦{balance}")
        else:
            print("Insufficient balance!")
    elif option == 3:
        amount = float(input("Enter transfer amount: ₦"))
        
        if amount <= balance:
            balance -= amount
            print("Transfer successful!")
            print(f"Remaining balance: ₦{balance}")
        else:
            print(" Insufficient balance!")
    else:
        print("invalid option!")
    choice = input("do you want to perform anthor transaction? (Yes/No): ")
    if choice.lower() != "yes":
        print("Thank you for banking with us.")
        break

 
            