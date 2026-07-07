"""
Problem Statement 1: Student Grade Calculator 
Write a Python program that defines a function calculate_grade(marks). 
The function should: 
• Accept marks (0–100) as a parameter.  
• Return the grade according to the following criteria:  
o 90 and above → A+  
o 75–89 → A  
o 60–74 → B  
o 40–59 → C  
o Below 40 → Fail  
The main program should: 
• Accept marks of 5 students.  
• Call the function for each student.  
• Display the marks and corresponding grade.  


"""
print("--------------------------------------------------")
#defining a funtion that calulates the grade
def calulate_grades(marks):
    if marks >= 90:                  # for marks>=90  => A+
        return "A+"
    elif marks >= 75:                #for marks >= 75 => A
        return "A"
    elif marks >= 60:               # for marks >= 60 => B
        return "B"
    elif marks >= 40:               # for marks >= 40 => c
        return "C"
    else:                           # fial
        return "Fail"

marks = []  #List of marks
for i in range(5):  # loop to accept marks of 5 students
    mark = int(input(f"Enter marks for student {i + 1}: "))  # accepting marks from user
    marks.append(mark)  # appending marks to the list

print("---------------------------------------------------")
for i in range(5):  # loop to display marks and corresponding grade
    grade = calulate_grades(marks[i])  # calling the function to calculate grade
    print(f"Student {i + 1}: Marks = {marks[i]}, Grade = {grade}")  # displaying marks and grade
print("---------------------------------------------------")

# output:

"""
--------------------------------------
Enter marks for student 1: 34
Enter marks for student 2: 93
Enter marks for student 3: 3
Enter marks for student 4: 56
Enter marks for student 5: 78
--------------------------------------
Student 1: Marks = 34, Grade = Fail
Student 2: Marks = 93, Grade = A+
Student 3: Marks = 3, Grade = Fail
Student 4: Marks = 56, Grade = C
Student 5: Marks = 78, Grade = A
--------------------------------------

"""