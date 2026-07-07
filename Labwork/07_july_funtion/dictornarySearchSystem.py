"""
Problem Statement 4: Dictionary Search System 
Write a Python program that defines a function search_student(student_dict, roll_no). 
The function should: 
• Accept a dictionary where:  
o Key = Roll Number  
o Value = Student Name  
• Search for the given roll number.  
• Return the student name if found; otherwise return "Student Not Found".  
The main program should: 
• Create a dictionary of at least 5 students.  
• Accept a roll number from the user.  
• Display the search result.  


"""
# Function to search student by roll number
def search_student(students, roll_no):
    # Check if roll number exists in dictionary
    if roll_no in students:
        return students[roll_no]
    else:
        return "Student Not Found"

# Dictionary of students (Roll No -> Name)
students = {
    101: "Aarav",
    102: "Priya",
    103: "Rohan",
    104: "Meera",
    105: "Aditya"
    
}
# Accept roll number from user
roll_no = int(input("Enter Roll Number to search: "))

# Display search result

print("Search Result:", search_student(students , roll_no))

 
#output:

"""
Enter Roll Number to search: 23
Search Name: Student Not Found


Enter Roll Number to search: 101
Search Name: Aarav
"""

