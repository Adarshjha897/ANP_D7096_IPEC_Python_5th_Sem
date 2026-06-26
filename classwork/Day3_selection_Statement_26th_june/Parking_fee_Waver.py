"""Problem 2: Parking Fee Waiver 
Problem Statement 
A shopping mall waives the parking fee if a customer has made purchases worth ₹2,000 or more. 
Otherwise, the customer must pay a parking fee of ₹100. 
Write a Python program to accept the purchase amount and display whether the parking fee is 
waived or payable. 
Sample Input 1 
Enter the purchase amount: 2500 
Sample Output 1 
Parking Fee Waived! 
Parking Fee: ₹0 
Sample Input 2 
Enter the purchase amount: 1500 
Sample Output 2 
Parking Fee Applicable! 
Parking Fee: ₹100
"""
print("--------------------------------------------------------------------------------")
#--------------------------------------------------------------------------------
#taking input from the user and validating the purchase amount
purchase_amount = float(input("Enter the purchase amount: "))
if purchase_amount < 0:
    exit(print("Invalid purchase amount. Please enter a positive value."))
print("--------------------------------------------------------------------------------")
#--------------------------------------------------------------------------------
#applying parking fee waiver if the purchase amount is ₹2,000 or more
if purchase_amount >= 2000:
    print("Parking Fee Waived!")
    print("--------------------------------------------------------------------------------")
    print(f"Parking Fee: ₹0")
#--------------------------------------------------------------------------------
#displaying the parking fee if the purchase amount is less than ₹2,000
else:
    print("Parking Fee Applicable!")
    print("--------------------------------------------------------------------------------")
    print(f"Parking Fee: ₹100")
print("--------------------------------------------------------------------------------")

#Output:
"""
------------------------------------------------------------
Enter the purchase amount: 2500
------------------------------------------------------------
Parking Fee Waived!
------------------------------------------------------------
Parking Fee : ₹0
------------------------------------------------------------
"""