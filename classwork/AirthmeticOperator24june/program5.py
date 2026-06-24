# 5. Classroom Seating Arrangement 
# Scenario: 
# A school wants to arrange students into equal rows. 
# Problem Statement: 
# Write a Python program to determine how many complete rows can be formed. 
# Input: 
# • Total Students  
# • Students per Row  
# Output: 
# • Number of Complete Rows 

total_students = int(input("Enter the total number of students: "))
students_per_row = int(input("Enter the number of students per row: "))
print("The total number of students is:", total_students)
print("The number of students per row is:", students_per_row)
print("The number of complete rows that can be formed is:", total_students // students_per_row)

"""Enter the total number of students: 56
Enter the number of students per row: 56
The total number of students is: 56
The number of students per row is: 56
The number of complete rows that can be formed is: 1
"""