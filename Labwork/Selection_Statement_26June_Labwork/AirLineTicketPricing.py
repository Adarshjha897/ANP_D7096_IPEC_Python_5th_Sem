"""

3. Airline Ticket Pricing Engine 
Problem Statement 
An airline calculates ticket fare using: 
Base Fare = ₹5000 
Additional Charges: 
• Business Class → +₹3000  
• Window Seat → +₹500  
• Weekend Travel → +₹1000  
Discounts: 
• Age below 12 → 50%  
• Age above 60 → 20%  
Calculate the final ticket fare. 
Sample Input 
Enter Passenger Age: 65 
Business Class (Y/N): Y 
Window Seat (Y/N): Y 
Weekend Travel (Y/N): Y 
Sample Output 
Base Fare: ₹5000 
Additional Charges: ₹4500 
Senior Citizen Discount: 20% 
Final Ticket Fare: ₹7600.0 

"""
print("------------------------------------------------")

Age = int(input("Enter pessenger age : "))
Buisness_class = input("Business Class (Y/N) : ").upper()

if(Buisness_class != "Y" and Buisness_class != "N"):
    exit("Invalid input enter in Y or N")

window_seat = input("Window Seat (Y/N) : ").upper()

if(window_seat != "Y" and window_seat != "N"):
    exit("Invalid input enter in Y or N")

weekend_Travel = input("Weekend Travel (Y/N) : ").upper()

if(weekend_Travel != "Y" and weekend_Travel != "N"):
    exit("Invalid input enter in Y or N")

print("------------------------------------------------")

#checking for user :
Additional_fare = 0
Basefare = 5000;
if(Buisness_class == "Y"):
     Additional_fare += 3000;
if(window_seat == "Y"):
     Additional_fare += 500
if(weekend_Travel == "Y"):
     Additional_fare += 1000

if(Age<12):
     Total_Fare = (Basefare + Additional_fare)*0.50

elif(Age>60):
     Total_Fare = (Basefare + Additional_fare)*(1-0.20)
else: Total_Fare = Basefare + Additional_fare
#printing the bill
print(f"Base fare : ₹{Basefare}")

print(f"Additional charges : ₹{Additional_fare}")
if(Age<12):
     print("Children discound : 50%")
elif(Age>60):
     print("Senior citizen Discount : 20%")
else: print("No Discount")
print("-----------------------------------------------------")
print(f"Final Ticket Fare : {Total_Fare}")
print("------------------------------------------------------")


# output

"""
------------------------------------------------------------
Enter pessenger age : 11
Business Class (Y/N) : y
Window Seat (Y/N) : n
Weekend Travel (Y/N) : y
------------------------------------------------------------
Base fare : ₹5000
Additional charges : ₹4000
Children discount : 50%
Final Ticket Fare : 4500.0

"""