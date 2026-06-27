"""
2. Scholarship Eligibility  
Problem Statement 
A university provides a scholarship only to students who score 90 or above. 
Write a Python program to accept a student's percentage and determine whether the student is eligible. 
• If percentage is 90 or above, display: 
Scholarship Approved 
• Otherwise display: 
Scholarship Not Approved 
Sample Input 
92 
Sample Output 
Scholarship Approved 


"""
print("---------------------------------------")
#taking input from the user
mark = int(input("Enter marks in %: "))

# validating the input
if(mark<0 or mark>100):
    exit("Enter a valid number")

print("--------------------------------------")

#checking if he/she is eligible for scholarship
if(mark>=90):
    print("Scholarship Approved")
else:print("Scholarship not approved")


# output
"""
-------------------------------------------------
Enter marks in %: 92 
-------------------------------------------------
Scholarship Approved 

"""