# 7. Compound Growth of Savings 
# Scenario: 
# A person invests money and wants to see how the amount grows over years. 
# Problem Statement: 
# Write a Python program to calculate the value of money after a certain number of years assuming it 
# doubles every year. 
# Input: 
# • Initial Amount  
# • Number of Years  
# Output: 
# • Final Amount 

initial_amount = float(input("Enter the initial amount: "))
number_of_years = int(input("Enter the number of years: "))
print("The initial amount is:", initial_amount)
print("The number of years is:", number_of_years)
print("The final amount after", number_of_years, "years is:", initial_amount * (2 ** number_of_years))

"""
Enter the initial amount: 67
Enter the number of years: 5
The initial amount is: 67.0
The number of years is: 5
The final amount after 5 years is: 2144.0
"""