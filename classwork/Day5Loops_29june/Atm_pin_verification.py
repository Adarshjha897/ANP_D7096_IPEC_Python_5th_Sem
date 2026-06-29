"""

1. ATM PIN Verification 
Problem Statement 
An ATM allows a user to enter the correct PIN. The correct PIN is 4589. The user can keep entering the 
PIN until it matches the correct one. 
Display "Access Granted" when the correct PIN is entered. 
Sample Output 
Enter PIN: 1234 
Incorrect PIN 
 
Enter PIN: 9876 
Incorrect PIN 
 
Enter PIN: 4589 
Access Granted


"""

pin = 4589
access = "f"




# checking for pin

while(access == "f"):
    key = int(input("Enter the pin: "))

    # if key is not a 4 digit number
    if(key<999 or key>10000):
        print("Invalid key key must be a 4 digit positive number")

# if key is correct
    elif(key == pin):
        access = "t"
        break
    # if key is incorrect
    else:print("Incorrect Pin")



print("Access granted")
