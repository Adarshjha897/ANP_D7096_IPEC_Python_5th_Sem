"""

7. Bank Transaction Summary 
Problem Statement 
A customer keeps entering transaction amounts. 
Positive numbers indicate deposits, while negative numbers indicate withdrawals. 
The customer enters 0 to finish. 
Display: 
• Total Deposit  
• Total Withdrawal  
• Final Balance 


"""
# initializing the data
i = "f";
deposite = 0
withdrawl = 0
balance = 0
while(i=="f"):
    inp = int(input("Enter the amount +ve for Deposite and negitive for withdrawl o for exit: "))
    if(inp==0):
        i="t"
    elif(inp>0):
        deposite += inp
        balance += inp
    else: 
        withdrawl += -inp
        balance = balance +(inp)
# printing the reuslts
print("Total Deposite = ", deposite)
print("Total withdrawl = ", withdrawl)
print("Total balance = ", balance)

