"""Problem 1: Electricity Bill Discount 
Problem Statement 
An electricity provider offers a 10% discount on the total bill amount if the customer's bill is ₹5,000 
or more. Otherwise, no discount is applied. 
Write a Python program to accept the total bill amount from the user and display the final amount to 
be paid. 
Sample Input 1 
Enter the electricity bill amount: 6200 
Sample Output 1 
Discount Applied! 
Final Bill Amount: ₹5580.0 
Sample Input 2 
Enter the electricity bill amount: 4200 
Sample Output 2 
No Discount Applied! 
Final Bill Amount: ₹4200"""
print("--------------------------------------------------------------------------------")
#--------------------------------------------------------------------------------
#taking input from the user and validating the bill amount
bill_amount = float(input("Enter the electricity bill amount: "))
if bill_amount < 0:
    exit(print("Invalid bill amount. Please enter a positive value."))
print("--------------------------------------------------------------------------------")
#--------------------------------------------------------------------------------
#applying discount if the bill amount is ₹5,000 or more
if bill_amount >= 5000:
    print("Discount Applied!")
    print("--------------------------------------------------------------------------------")
    print(f"Final Bill Amount: ₹{bill_amount * 0.9}")
    
#--------------------------------------------------------------------------------
#displaying the final bill amount if the bill amount is less than ₹5,000
else:
   
    print("No Discount Applied!")
    print("--------------------------------------------------------------------------------")
    print(f"Final Bill Amount: ₹{bill_amount}")
print("--------------------------------------------------------------------------------")


#Output:
"""
------------------------------------------------------------
Enter the electricity bill amount: 56788
------------------------------------------------------------
Discount Applied!
------------------------------------------------------------
Final Bill Amount: ₹51109.200000000004
------------------------------------------------------------

"""