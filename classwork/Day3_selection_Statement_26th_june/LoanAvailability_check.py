"""Problem 3: Loan Eligibility Check 
Problem Statement 
A bank considers an applicant eligible for a personal loan only if their monthly salary is ₹30,000 or 
more. 
Write a Python program to accept the applicant's monthly salary and display whether they are 
eligible to apply for the loan. 
Sample Input 1 
Enter your monthly salary: 45000 
Sample Output 1 
Congratulations! You are eligible to apply for the loan. 
Sample Input 2 
Enter your monthly salary: 22000 
Sample Output 2 
Sorry! You are not eligible to apply for the loan.
"""

print("--------------------------------------------------------------------------------")
#---------------------------------------------------------------------------------
#taking input from the user and validating the monthly salary
monthly_salary = float(input("Enter your monthly salary: "))
if monthly_salary < 0:
    print("--------------------------------------------------------------------------------")
    exit(print("Invalid salary amount. Please enter a positive value."))
print("--------------------------------------------------------------------------------")
#----------------------------------------------------------------------------------
#checking loan eligibility based on the montly salary
if monthly_salary >= 30000:
    print("Congratulations! You are eligible to apply for the loan.")
    print("--------------------------------------------------------------------------------")
else:
    print("Sorry! You are not eligible to apply for the loan.")
    print("--------------------------------------------------------------------------------")


#output:

# when the monthly salary is less than ₹30,000
"""
------------------------------------------------------------
Enter your monthly salary: 2000
------------------------------------------------------------
Sorry! You are not eligible to apply for the loan.
------------------------------------------------------------
"""
#when the monthly salary is greater than or equal to ₹30,000
"""
------------------------------------------------------------
Enter your monthly salary: 50000
------------------------------------------------------------
Congratulations! You are eligible to apply for the loan.
------------------------------------------------------------

"""
