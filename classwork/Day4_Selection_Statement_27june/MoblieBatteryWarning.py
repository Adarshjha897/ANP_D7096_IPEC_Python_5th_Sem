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
print("--------------------------------")
battery = int(input())

if(battery<0):
    exit()

print("--------------------------------")

if(battery>=15):
    exit()

print("Connect Charger Immediately")

# output

"""
------------------------------------------
10 
------------------------------------------
Connect Charger Immediately

"""