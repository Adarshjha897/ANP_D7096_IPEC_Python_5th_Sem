"""
8. Employee Salary Statistics 
Problem Statement 
A company has N employees. 
Accept the salary of each employee and determine: 
• Highest salary  
• Lowest salary  
• Average salary  
• Number of employees earning more than ₹50,000  
"""

# taking number of emp in company
N = int(input("Enter number of Employee: "))
if N <= 0:
    exit("Number of employee can not be 0 or negative")

count = 0 

# taking salary of 1st employee
salary1 = float(input("Enter the salary of Employee 1: "))
if salary1 < 0:
     exit("Enter a positive value")

# initializing total salary count
total = salary1

# assigning it max and min both for comparison (renamed to avoid overwriting built-in functions)
max_salary = salary1
min_salary = salary1

# checking if salary is more than 50000 (problem states "more than", so > is used)
if salary1 > 50000:
    count += 1

for i in range(2, N + 1):
    # Fixed the string concatenation issue by using an f-string
    salary = float(input(f"Enter the salary of Employee {i}: "))
    
    # Simple correction loop if user enters a negative value once
    if salary < 0:
        salary = float(input(f"Enter a positive salary value for Employee {i}: "))
    
    # adding to total salary
    total += salary
    
    # Corrected logic: check for max salary
    if salary > max_salary:
        max_salary = salary
        
    # Corrected logic: check for min salary
    if salary < min_salary:
        min_salary = salary
        
    # check for salary more than 50000
    if salary > 50000:
        count += 1

# printing the outputs
print("\n--- Statistics ---")
print("Highest salary: ", max_salary) 
print("Lowest salary: ", min_salary) 
print("Average salary: ", total / N)
print("Number of employee earning more than ₹50,000: ", count)
