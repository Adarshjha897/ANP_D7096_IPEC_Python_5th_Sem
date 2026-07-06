"""
Lab 5: Student Subject Report Card 
Problem Statement: 
Create a nested dictionary to store marks of students in three subjects. 
Example: 
{
 
'Rahul': {'Math': 85, 'Science': 90, 'English': 88}, 
'Priya': {'Math': 78, 'Science': 95, 'English': 82}, 
'Ankit': {'Math': 91, 'Science': 89, 'English': 94} 
} 
Write a program to: 
• Calculate the total marks of each student.  
• Calculate the average marks of each student.  
• Display the topper based on total marks.  
• Display the subject-wise highest marks along with the student's name.  
• Display students whose average is greater than or equal to 85.

"""

# Nested dictionary storing students and their subject marks
students = {
    'Rahul': {'Math': 85, 'Science': 90, 'English': 88},
    'Priya': {'Math': 78, 'Science': 95, 'English': 82},
    'Ankit': {'Math': 91, 'Science': 89, 'English': 94}
}

# Dictionary to store total and average marks of each student
totals = {}
averages = {}

# Step 1: Calculate total and average marks for each student
for name, subjects in students.items():
    total = sum(subjects.values())   # sum of all subject marks
    avg = total / len(subjects)      # average = total / number of subjects
    totals[name] = total
    averages[name] = avg

# Step 2: Display total and average marks of each student
print("... Student Totals and Averages ...")
for name in students:
    print(f"{name} -> Total: {totals[name]}, Average: {averages[name]:.2f}")

# Step 3: Find the topper based on total marks
topper = max(totals, key=totals.get)   # student with highest total
print("\n.. Topper ..")
print(f"{topper} with {totals[topper]} marks")

# Step 4: Subject-wise highest marks with student name
print("\n..Subject-wise Highest Marks..")
for subject in ['Math', 'Science', 'English']:
    highest_student = max(students, key=lambda x: students[x][subject])
    highest_marks = students[highest_student][subject]
    print(f"{subject}: {highest_student} ({highest_marks})")

# Step 5: Students with average >= 85
print("\n=== Students with Average >= 85 ===")
for name, avg in averages.items():
    if avg >= 85:
        print(f"{name} -> Average: {avg:.2f}")

# output:

"""

=== Student Totals and Averages ===
Rahul -> Total: 263, Average: 87.67
Priya -> Total: 255, Average: 85.00
Ankit -> Total: 274, Average: 91.33

=== Topper ===
Ankit with 274 marks

=== Subject-wise Highest Marks ===
Math: Ankit (91)
Science: Priya (95)
English: Ankit (94)

=== Students with Average >= 85 ===
Rahul -> Average: 87.67
Priya -> Average: 85.00
Ankit -> Average: 91.33

"""