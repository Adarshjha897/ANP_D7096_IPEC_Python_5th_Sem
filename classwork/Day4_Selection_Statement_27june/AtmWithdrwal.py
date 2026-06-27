"""
#8. ATM Cash Withdrawal
 Problem Statement
#A customer can withdraw money only if the requested amount does not exceed the available balance.
#Accept the account balance and withdrawal amount.
 • If withdrawal amount is less than or equal to balance, display:
 Transaction Successful
#• Otherwise display:
 Insufficient Balance
 Sample Input
 5000
#4500
 Sample Output
Transaction Successful
"""

#------------------------------------

#taking Account balance and the amount to be withdrawl from the user
print("-----------------------------------------------------------------")
account_balance = float(input("Enter the account balance: "))
withdrawal_amount = float(input("Enter the withdrawal amount: "))
print("------------------------------------------------------------------")


#validating account balance and withdrawal amount input
if account_balance < 0 or withdrawal_amount < 0:
    exit("Invalid input. Account balance and withdrawal amount must be non-negative.")


#verifying whether the withdrawal amount is less than or equal to the account balance
if withdrawal_amount <= account_balance:
    print(f"Transaction Successful of amount: {withdrawal_amount}")
else:
    print("Insufficient Balance please try to enter a amount less than account balance")

#------------------------------------
#output:
"""
Enter the account balance: 5000
Enter the withdrawal amount: 4500
Transaction Successful of amount: 4500
"""