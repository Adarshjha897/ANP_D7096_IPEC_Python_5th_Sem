"""
10. Electricity Consumption Category (if...elif...else Statement)
 Problem Statement
 An electricity department categorizes households based on monthly electricity consumption.
 • Up to 100 units → Low Consumption
 • 101–300 units → Moderate Consumption
 • Above 300 units → High Consumption
 Write a Python program to display the consumption category.
Sample Input
245
Sample Output
Moderate Consumption


"""

#taking input from the user
print("---------------------------------------------------------")
electricity_units = float(input("Enter the monthly electricity consumption in units: "))
print("---------------------------------------------------------")

#validating electricity consumption input
if electricity_units < 0:
    exit("Invalid input. Electricity consumption must be non-negative.")
#verifying the consumption category based on monthly electricity consumption
if electricity_units <= 100:
    print("Low Consumption")
elif electricity_units >= 101 and electricity_units <= 300:
    print("Moderate Consumption")
else:
    print("High Consumption")
print("__________________________________________________________")

#------------------------------------


#output
"""
---------------------------------------------------------
Enter the monthly electricity consumption in units: 245
---------------------------------------------------------
Moderate Consumption
_________________________________________________________

"""