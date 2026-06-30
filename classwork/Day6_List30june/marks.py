# Take  name and marks of 15 students in a list and if student have more than 75 percent he is eligible for admission

student = []

# Input details of 15 students
for i in range(15):

    name = input("Enter Student Name: ")

    marks = int(input("Enter Marks: "))

#validating the marks

    if(marks<0 or marks >100 ):
        print("Enter a valid marks b/w 0 - 100")
        marks = int(input("Enter Marks: "))
    student.append([name, marks])

print("-------------------------------------------------")
print("Students Eligible for Admission:")
# Display eligible students
for s in student:
    if s[1] > 75:
        print(s[0])
print("-------------------------------------------------")