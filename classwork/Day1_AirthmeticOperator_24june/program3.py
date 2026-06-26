#PROGRAM 3
# 3. Fuel Consumption Tracker 
# Scenario: 
# A person wants to calculate the average fuel consumption of a car. 
# Problem Statement: 
# Write a Python program to find the average mileage of a car. 
# Input: 
# • Total distance traveled (km)  
# • Fuel consumed (liters)  

distance_traveled = float(input("Enter the total distance traveled (in km): "))
fuel_consumed = float(input("Enter the total fuel consumed (in liters): "))

print("The total distance traveled is:", distance_traveled)
print("The total fuel consumed is:", fuel_consumed)
print("The average mileage of the car is:", distance_traveled / fuel_consumed)

"""Enter the total distance traveled (in km): 50
Enter the total fuel consumed (in liters): 5
The total distance traveled is: 50.0
The total fuel consumed is: 5.0
The average mileage of the car is: 10.0
"""