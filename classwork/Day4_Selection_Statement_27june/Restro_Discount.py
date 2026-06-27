"""
6. Restaurant Bill Discount 
Problem Statement 
A restaurant offers discounts based on the total bill amount. 
• Bill below ₹1000 → No Discount  
• ₹1000–₹2999 → 10% Discount  
• ₹3000 or more → 20% Discount  
Write a Python program to determine the applicable discount. 
Sample Input 
3200 
Sample Output 
20% Discount Applied 


"""
print("-----------------------------")
#taking input from the user
bill_amount = int(input("Enter Bill amount: "))

#validating the input
if(bill_amount<0):
    exit("Invalid data")
#------------------------------------
print("-------------------------------")

#checking for the discount

if(bill_amount<1000):
    print("No Discount Applied")


elif(bill_amount>=1000 and bill_amount > 3000):
    print("10% Discount Applied")


else:print("20% Discount is Applied")


#------------------------------------------
print("___________________________________")

#output

"""
------------------------------------------
Enter bill amount: 3200 
------------------------------------------
20% Discount Applied 
__________________________________________

"""