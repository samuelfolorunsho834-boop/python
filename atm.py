banlance = 10000
while True:
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exist")
    
    option = input("choose an option:")
    
    if option == "1":
        print("your balance is ₦",banlance)
    elif option == "2":
        amount = float(input("Enter amount to deposit:"))
        banlance += amount
        print("Deposit succesful. New balance: ₦", banlance)
    elif option == "3":
        amount = float(input("Enter amount to withdraw:"))
    if amount > banlance:
        print("insufficient funds")
    else:
        banlance -= amount
        print("Withradrawal successful. New balance: ₦", banlance)
    print("Thank you for banking with us")
        
    break
else:
    print("inavalid option")
        
            