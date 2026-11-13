from practice_tools import deposit,withdraw

balance=5000

print("Current balance:",balance)
print("1. Deposit")
print("2. Withdraw")

choice=int(input("Enter your choice :"))
if choice==1:
    amount=int(input("Enter deposit amount :")) 
    if amount <=0:
        print("Invalid amount")
    else:
        balance=deposit.add_money(balance,amount)    
        print("updated balance :",balance)
if choice==2:
    amount=int(input("enter the withdrawal amount :")) 
    result=withdraw.withdraw_money(balance,amount)  
    if isinstance(result, str):
        print(result)
    else:
        balance = result
        print("Updated balance:", balance)

else:
    print("Invalid choice")         