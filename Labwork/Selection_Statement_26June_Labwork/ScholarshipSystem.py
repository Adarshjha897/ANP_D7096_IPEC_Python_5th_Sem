"""
6. University Scholarship System 
Problem Statement 
Scholarship is awarded based on percentage: 

Percentage  ->   Scholarship 
95+         ->   100% 
90-94       ->   75% 
85-89       ->   50% 
80-84       ->   25% 
Below 80    ->   No Scholarship 

Conditions: 
• Family income must be below ₹8,00,000.  
• Students with disciplinary actions receive no scholarship.  
Sample Input 
Percentage: 92 
Family Income: 500000 
Disciplinary Action (Y/N): N 
Sample Output 
Scholarship Awarded: 75%

"""
# University Scholarship System

# Step 1: Input values
percentage = float(input("Enter Percentage: "))
if(percentage <= 0):
    exit("percentage is invalid")
income = float(input("Enter Family Income: "))
if(income<0):exit("family income can not be negitive")
disciplinary = input("Disciplinary Action (Y/N): ").upper()
if(disciplinary != "Y" and disciplinary != "N"):
    exit("Enter Y or N Only")

# Step 2: Check conditions
scholarship = 0

if income < 800000 and disciplinary == 'N':
    if percentage >= 95:
        scholarship = 100
    elif 90 <= percentage <= 94:
        scholarship = 75
    elif 85 <= percentage <= 89:
        scholarship = 50
    elif 80 <= percentage <= 84:
        scholarship = 25
    else:
        scholarship = 0
else:
    scholarship = 0

# Step 3: Output
print(f"Scholarship Awarded: {scholarship}%")

"""
--------------------------------------------
Enter Percentage: 92
Enter Family Income: 500000
Disciplinary Action (Y/N): N
Scholarship Awarded: 75%
--------------------------------------------
"""
