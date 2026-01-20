balance=500

print("ATM Menu")
print("\n1.Withdrawl\n 2.Deposit\n 3.Check Balance\n 4.Exit")


while True:
    choice=int(input("Enter choice:"))
    if choice==1:
        withdrawl_amount=int(input("Enter the amount:"))
        if withdrawl_amount<balance:
            balance=balance-withdrawl_amount
            print("Balance left:",balance)
        else:
            print("Doesn't have the sufficient balance.")
        
    elif choice==2:
        amount=int(input("Enter the amount to be deposited:"))
        balance=balance+amount
        print("Deposited Successfully")
        print("Balance=",balance)
        
    elif choice==3:
        print("Balance=",balance)
        
    elif choice==4:
        print("Exit")
        break
    else:
        print("Enter valid option")
        
    
    

    
        
    