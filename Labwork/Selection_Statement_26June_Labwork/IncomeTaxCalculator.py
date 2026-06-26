
#. Smart Income Tax Calculator 
# . Smart Income Tax Calculator 
# Problem Statement 
# A government tax portal calculates tax based on the following conditions: 
# • Income up to ₹5,00,000 → No tax  
# • ₹5,00,001 to ₹10,00,000 → 10%  
# • ₹10,00,001 to ₹20,00,000 → 20%  
# • Above ₹20,00,000 → 30%  
# Additional Benefits: 
# • Senior citizens (Age ≥ 60) receive a 5% rebate on tax.  
# • Women taxpayers receive an additional 2% rebate on tax.  
# Write a Python program to calculate the final tax amount payable. 
# Sample Input 
# Enter Annual Income: 1200000 
# Enter Age: 65 
# Enter Gender (M/F): F 
# Sample Output 
# Tax before rebate: ₹240000.0 
# Senior Citizen Rebate: ₹12000.0 
# Women Rebate: ₹4800.0 
# Final Tax Payable: ₹223200.0 
#---------------------------------------------------
# Smart Income Tax Calculator

print("Welcome to the Smart Income Tax Calculator")
print("---------------------------------------------------")
# Input values
income = float(input("Enter Annual Income: "))
age = int(input("Enter Age: "))
gender = input("Enter Gender (M/F): ").upper()
print("---------------------------------------------------")
# Step 1: Calculate tax before rebate (flat rate based on range)
if income <= 500000:
    TAX = 0
elif income <= 1000000:
    TAX = income * 0.10
elif income <= 2000000:
    TAX = income * 0.20
else:
    TAX = income * 0.30
print(f"Tax before rebate: ₹{TAX:.2f}")
print("---------------------------------------------------")

# Step 2: Calculate rebates
senior_rebate = TAX * 0.05 if age >= 60 else 0
women_rebate = TAX * 0.02 if (gender == 'F' or gender == 'f') else 0

print(f"Senior Citizen Rebate: ₹{senior_rebate:.2f}")
print(f"Women Rebate: ₹{women_rebate:.2f}")
print("---------------------------------------------------")
# Step 3: Final tax payable
final_tax = TAX - senior_rebate - women_rebate
print(f"Final Tax Payable: ₹{final_tax:.2f}")

#oytput
"""
Welcome to the Smart Income Tax Calculator
------------------------------------------------------------
Enter Annual Income: 5699898
Enter Age: 34
Enter Gender (M/F): f
------------------------------------------------------------
Tax before rebate: ₹1709969.40
Senior Citizen Rebate: ₹0.00
Women Rebate: ₹34199.39
Final Tax Payable: ₹1675769.99

"""