# 9. Mobile Recharge Plan 
# Scenario: 
# A telecom company charges a fixed amount per GB of data. 
# Problem Statement: 
# Write a Python program to calculate the total recharge amount based on the data pack selected. 
# Input: 
# • Cost per GB  
# • Number of GBs  
# Output: 
# • Total Recharge Cost

cost_per_gb = float(input("Enter the cost per GB: "))
number_of_gbs = float(input("Enter the number of GBs: "))
print("Cost per GB: ", cost_per_gb)
print("Number of GBs: ", number_of_gbs)
print("Total Recharge Cost: ", cost_per_gb * number_of_gbs)
 
 # OUTPUT

"""
Enter the cost per GB: 67
Enter the number of GBs: 100
Cost per GB:    67.0
Number of GBs:  100.0
Total Recharge Cost:  6700.0
"""