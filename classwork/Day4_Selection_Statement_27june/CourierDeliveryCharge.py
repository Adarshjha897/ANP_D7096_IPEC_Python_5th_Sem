"""
3. Courier Delivery Charge 
Problem Statement 
A courier company calculates delivery charges based on the package weight. 
• Weight up to 2 kg → ₹50  
• Weight greater than 2 kg and up to 5 kg → ₹100  
• Weight greater than 5 kg → ₹180  
Write a Python program to display the delivery charge. 
Sample Input 
4 
Sample Output 
Delivery Charge = ₹100

"""
#taking input from user 

print("-------------------------")

weight = int(input("Enter the weight of courier in Kg: "))

#validating the input
if(weight<=0):
    print("______________________________________")
    exit("Invalid input Enter a positive value.")

print("--------------------------")

#now calulating price acc to the weight
if(weight<=2):
    print("Delivery Charge = ₹50")
elif(weight>2 and weight<=5):
    print("Delivery Charge = ₹100")

else:
    print("Delivery Charge = ₹180")


#output
"""
----------------------------------
Enter the weight of courier in Kg: 4 
----------------------------------
Delivery Charge = ₹100

"""
