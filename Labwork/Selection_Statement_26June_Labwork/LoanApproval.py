"""
2. Loan Approval System 
Problem Statement 
A bank evaluates loan applications using: 
• Credit Score ≥ 750  
• Annual Income ≥ ₹8,00,000  
• Existing Loan Amount ≤ ₹2,00,000  
Conditions: 
• All conditions satisfied → Approved  
• Only one condition fails → Manual Review  
• More than one condition fails → Rejected  
Sample Input 
Enter Credit Score: 780 
Enter Annual Income: 750000 
Enter Existing Loan Amount: 100000 
Sample Output 
Loan Status: Manual Review 
Reason: Income criteria not satisfied


"""


credit_score = int(input("Enter Credit Score: "))
if credit_score < 300 or credit_score > 850:
    exit("Invalid Credit Score. Please enter a value between 300 and 850.")
    
annual_income = float(input("Enter Annual Income: "))
if annual_income < 0:
    exit("Invalid Annual Income. Please enter a non-negative value.")
existing_loan_amount = float(input("Enter Existing Loan Amount: "))
if existing_loan_amount < 0:
    exit("Invalid Existing Loan Amount. Please enter a non-negative value.")
#-----------------------------------------------------------------------------------

#checking the profile provided by user 
        
