# Food Delivery Business Profit Analysis 
# Scenario: 
# A food delivery startup wants to calculate its daily profit and package distribution details. 
# Problem Statement: 
# Write a Python program that: 
# 1. Calculates total revenue generated.  
# 2. Calculates profit after deducting expenses.  
# 3. Determines how many complete delivery boxes can be prepared.  
# 4. Finds remaining food packets.  
# 5. Predicts revenue after a certain number of days assuming revenue doubles daily.  
# Input: 
# • Number of orders  
# • Price per order  
# • Daily expenses  
# • Total food packets  
# • Packets per box  
# • Number of days  
# Output: 
# • Total Revenue  
# • Profit  
# • Complete Boxes  
# • Remaining Packets  
# • Future Revenue

number_of_orders = int(input("Enter the number of orders: "))
price_per_order = float(input("Enter the price per order: "))
daily_expenses = float(input("Enter the daily expenses: "))
total_food_packets = int(input("Enter the total food packets: "))
packets_per_box = int(input("Enter the number of packets per box: "))
number_of_days = int(input("Enter the number of days for revenue prediction: "))

# Calculations
total_revenue = number_of_orders * price_per_order
profit = total_revenue - daily_expenses
complete_boxes = total_food_packets // packets_per_box
remaining_packets = total_food_packets % packets_per_box
future_revenue = total_revenue * (2 ** number_of_days)

# Output
print("Total Revenue: ", total_revenue)
print("Profit: ", profit)
print("Complete Boxes: ", complete_boxes)
print("Remaining Packets: ", remaining_packets)
print("Future Revenue: ", future_revenue)

#OUTPUT
"""
Enter the number of orders: 100
Enter the price per order: 50
Enter the daily expenses: 2000
Enter the total food packets: 250
Enter the number of packets per box: 10
Enter the number of days for revenue prediction: 3
Total Revenue:  5000.0
Profit:  3000.0 
Complete Boxes:  25
Remaining Packets:  0
Future Revenue:  40000.0

"""