'''
5. E-Commerce Premium Membership Eligibility 
Problem Statement 
A customer becomes Premium Member if: 
• Total Purchases > ₹50,000  
• Orders Completed ≥ 20  
• Customer Rating ≥ 4.5  
Special Case: 
• Purchases above ₹1,00,000 automatically qualify.  
Sample Input 
Total Purchases: 120000 
Orders Completed: 10 
Customer Rating: 4.0 
Sample Output 
Premium Membership Status: Eligible 
Reason: Purchase amount exceeded ₹100000.

'''
purchase = float(input("Total purchase: "))
if(purchase<0):
    exit("Enter a valid purchase amount")
order = int(input("Order completed: "))
if(order<0):
    exit("Enter a valid number of orders completed")

Rating = float(input("Customer Rating: "))
if(Rating<0):
    exit("Rating can not be negtive")

print("---------------------------------------------------")
if(purchase > 100000):
    print("Premium Membership Status : Eligible")
    print("Reason: Purchase amount exceeded ₹100000.")
elif(purchase>50000 and order >= 20 and Rating >= 4.5):
    print("Premium Membership Status : Eligible")

print("---------------------------------------------------")

# output

"""

Total Purchases: 120000 
Orders Completed: 10 
Customer Rating: 4.0 
-----------------------------------------------------------
Premium Membership Status: Eligible 
Reason: Purchase amount exceeded ₹100000.
-----------------------------------------------------------




"""