"""
4. Mobile Battery Warning 
Problem Statement 
A smartphone displays a low battery warning only when the battery percentage falls below 15%. 
Write a Python program to accept the battery percentage. 
If the battery is below 15, display: 
Connect Charger Immediately 
Otherwise, display nothing. 
Sample Input 
10 
Sample Output 
Connect Charger Immediately

"""
#Taking input from the user
print("--------------------------------")
battery = int(input("Enter battery Percentage of youre Device: "))

#validating the input 
if(battery<0 or battery>100):
    exit("Invalid input enter between 0 to 100")

print("--------------------------------")

#checking wether the warning is required
if(battery>=15):
    exit()

print("Connect Charger Immediately")

# output

"""
------------------------------------------
Enter battery Percentage of youre Device: 10 
------------------------------------------
Connect Charger Immediately

"""