"""

Problem Statement 2: List Analysis using Functions 
Write a Python program that defines the following functions: 
• find_max(numbers)  
• find_min(numbers)  
• find_average(numbers)  
The program should: 
• Accept a list of 10 integers from the user.  
• Call all three functions.  
• Display the maximum value, minimum value, and average of the list.

"""
#creating the functions

def find_max(numbers):
    return max(numbers) #returns the maximum value from the list

def find_min(numbers):
    return min(numbers) #return the minimum value from the list

def find_average(numbers):
    return sum(numbers) / len(numbers) #returns the average of the list

print("----------------------------------------------------------")
# Accepting a list of 10 integers from the user
numbers = []
for i in range(10):
    num = int(input(f"Enter integer {i + 1}: "))
    numbers.append(num)

print('-----------------------------------------------------------')
# Displaying the results
print("Maximum value: " ,find_max(numbers))
print("Minimum value: " ,find_min(numbers))
print("Average value: " ,find_average(numbers))

print("------------------------------------------------------------")
# output:
"""
----------------------------------------------------------
Enter integer 1: 4
Enter integer 2: 54
Enter integer 3: 34
Enter integer 4: 334
Enter integer 5: 3
Enter integer 6: 243
Enter integer 7: 5
Enter integer 8: 0
Enter integer 9: 24
Enter integer 10: 34
-----------------------------------------------------------
Maximum value:  334
Minimum value:  0
Average value:  73.5
------------------------------------------------------------

"""