# 6. Pizza Distribution 
# Scenario: 
# A party organizer wants to distribute pizza slices equally among children. 
# Problem Statement: 
# Write a Python program to find how many slices remain after equal distribution. 
# Input: 
# • Total Pizza Slices  
# • Number of Children  
# Output: 
# • Remaining Slices 

total_slices = int(input("Enter the total number of pizza slices: "))
number_of_children = int(input("Enter the number of children: "))
print("The total number of pizza slices is:", total_slices)
print("The number of children is:", number_of_children)
print("The number of remaining slices after equal distribution is:", total_slices % number_of_children)


# O/P
"""
Enter the total number of pizza slices: 6
Enter the number of children: 4
The total number of pizza slices is: 6
The number of children is: 4
The number of remaining slices after equal distribution is: 2

"""