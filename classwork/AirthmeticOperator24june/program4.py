# 4. Bank Account Balance 
# Scenario: 
# A customer withdraws money from their bank account. 
# Problem Statement: 
# Write a Python program to calculate the remaining balance after withdrawal. 
# Input: 
# • Current Balance  
# • Withdrawal Amount  
# Output: 
# • Remaining Balance  

current_balance = float(input("Enter the current balance: "))
withdrawal_amount = float(input("Enter the withdrawal amount: "))
print("The current balance is:", current_balance)
print("The withdrawal amount is:", withdrawal_amount)
print("The remaining balance after withdrawal is:", current_balance - withdrawal_amount)

"""

o/p
Enter the current balance: 567
Enter the withdrawal amount: 56
The current balance is: 567.0
The withdrawal amount is: 56.0
The remaining balance after withdrawal is: 511.0

"""