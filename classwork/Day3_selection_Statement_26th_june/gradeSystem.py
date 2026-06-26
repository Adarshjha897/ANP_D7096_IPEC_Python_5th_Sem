"""
Problem Statement 3 : Student Grade Calculator
A school assigns grades based on the marks obtained by students according to the following criteria:
• Marks 90 and above → Grade A
• Marks 75 to 89 → Grade B
• Marks 50 to 74 → Grade C
• Below 50 → Grade F
Write a Python program to accept marks from the user and display the corresponding grade.
Sample Input
Enter Marks: 92
Sample Output
Grade A
Sample Input
Enter Marks: 80
Sample Output
Grade B
Sample Input
Enter Marks: 65
Sample Output
Grade C
Sample Input
Enter Marks: 35
Sample Output
Grade F"""
print("--------------------------------------------------------------------------------")
#taking the marks from user
marks = int(input("Enter Marks: "))
print("--------------------------------------------------------------------------------")
#determining the grade based on marks
if marks >= 90:
    grade = "A"
elif marks >= 75:
    grade = "B"
elif marks >= 50:
    grade = "C"
else:
    grade = "F"

print(f"Grade {grade}")
print("--------------------------------------------------------------------------------")

#output:
"""
-------------------------------------------------------------------------------
Enter Marks: 92
--------------------------------------------------------------------------------
Grade A
--------------------------------------------------------------------------------


-------------------------------------------------------------------------------
Enter Marks: 80
--------------------------------------------------------------------------------
Grade B
--------------------------------------------------------------------------------    


--------------------------------------------------------------------------------
Enter Marks: 65 
--------------------------------------------------------------------------------
Grade C
--------------------------------------------------------------------------------


--------------------------------------------------------------------------------
Enter Marks: 35
--------------------------------------------------------------------------------
Grade F
---------------------------------------------------------------------------------
"""