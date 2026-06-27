"""
9. Internet Speed Rating
Problem Statement
An Internet Service Provider categorizes connection quality based on download speed.
• Less than 25 Mbps → Slow
• 25–99 Mbps → Good
• 100 Mbps or above → Excellent
Write a Python program to display the connection quality.
Sample Input
120
Sample Output
Excellent Connection
"""
#taking input from the user
print("----------------------------------------------------------")
internet_speed = float(input("Enter the download speed in Mbps: "))

print("----------------------------------------------------------")
#validating internet speed input
if internet_speed < 0:
    exit("Invalid input. Internet speed must be non-negative.")
print("__________________________________________________________")
#verifying the connection quality based on download speed
if internet_speed < 25:
    print("Slow Connection")
elif internet_speed >= 25 and internet_speed < 100:
    print("Good Connection")
else:
    print("Excellent Connection")
#------------------------------------

# output:
"""
----------------------------------------
 Enter the download speed in Mbps: 120
----------------------------------------
 Excellent Connection
________________________________________
"""