"""
Lab 1: Student Marks Management 
Problem Statement: 
Create a dictionary to store the marks of 5 students, where the key is the student's name and the 
value is their marks. 
Perform the following operations: 
• Display all student names and marks.  
• Add a new student with marks.  
• Update the marks of an existing student.  
• Delete a student by name.  
• Display the student who scored the highest marks.

"""

# Lab 1: Student Marks Management

# Step 1: Create dictionary with 5 students
student_marks = {
    "Alice": 85,
    "Bob": 92,
    "Charlie": 78,
    "David": 88,
    "Eva": 95
}

# Step 2: Display all student names and marks
print("All Students and Marks:")
for name, marks in student_marks.items():
    print(f"{name}: {marks}")

# Step 3: Add a new student with marks
student_marks["Frank"] = 80
print("\nAfter Adding Frank:")
print(student_marks)

# Step 4: Update marks of an existing student
student_marks["Charlie"] = 90
print("\nAfter Updating Charlie's Marks:")
print(student_marks)

# Step 5: Delete a student by name
del student_marks["Bob"]
print("\nAfter Deleting Bob:")
print(student_marks)

# Step 6: Display student with highest marks
highest_student = max(student_marks, key=student_marks.get)
print(f"\nHighest Scorer: {highest_student} with {student_marks[highest_student]} marks")


# output:
"""    
All Students and Marks:
Alice: 85
Bob: 92
Charlie: 78
David: 88
Eva: 95

After Adding Frank:
{'Alice': 85, 'Bob': 92, 'Charlie': 78, 'David': 88, 'Eva': 95, 'Frank': 80}

After Updating Charlie's Marks:
{'Alice': 85, 'Bob': 92, 'Charlie': 90, 'David': 88, 'Eva': 95, 'Frank': 80}

After Deleting Bob:
{'Alice': 85, 'Charlie': 90, 'David': 88, 'Eva': 95, 'Frank': 80}

Highest Scorer: Eva with 95 marks
    """