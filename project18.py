balance =6821.00
amount = int(input("enter the amount to withdraw: "))
if amount <= balance :
    balance -= amount
    print("withdrawal successful")
    print("remaining balance :",balance)
else :
    print("insufficient balance")