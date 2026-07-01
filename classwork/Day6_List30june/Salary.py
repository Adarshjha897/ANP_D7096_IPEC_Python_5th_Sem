# take the input of 15 person name and salary store it in the list and we have to check wether 
# he fall in Ews cateogry
#  if his salary is less than 5Lpa
#we have to display the name of person in the Ews category
#-----------------------------------


# initializing the list
record = []

# Input details of 15 persons
for i in range(15):
    print("-----------------------------------------------")
    #taking the name 
    name = input("Enter Name: ")
    
    #taking salary input
    salary = float(input("Enter Salary (in LPA): "))
    #validating the salary
    while salary <= 0:
        print("Salary must be positive. Please enter again.")
        salary = float(input("Enter Salary (in LPA): "))

    #adding the data into the list
    record.append([name, salary])

print("______________________________________________________")
print("Persons Eligible for EWS Category:")

# Display eligible persons
for person in record:
    # Eligible if salary < 5 LPA
    if person[1] < 5:
        print(person[0])



#output
"""

------------------------------------------------------------
Enter Name: a
Enter Salary (in LPA): 12
------------------------------------------------------------
Enter Name: b
Enter Salary (in LPA): 23
------------------------------------------------------------
Enter Name: c
Enter Salary (in LPA): 34
------------------------------------------------------------
Enter Name: d
Enter Salary (in LPA): 4
------------------------------------------------------------
Enter Name: e
Enter Salary (in LPA): 96
------------------------------------------------------------
Enter Name: f
Enter Salary (in LPA): 3
------------------------------------------------------------
Enter Name: g
Enter Salary (in LPA): 9
------------------------------------------------------------
Enter Name: h
Enter Salary (in LPA): 34
------------------------------------------------------------
Enter Name: i
Enter Salary (in LPA): 2
------------------------------------------------------------
Enter Name: j
Enter Salary (in LPA): 09
------------------------------------------------------------
Enter Name: k
Enter Salary (in LPA): 34
------------------------------------------------------------
Enter Name: l
Enter Salary (in LPA): 3
------------------------------------------------------------
Enter Name: m
Enter Salary (in LPA): 4.6
------------------------------------------------------------
Enter Name: n
Enter Salary (in LPA): 5.4
------------------------------------------------------------
Enter Name: o
Enter Salary (in LPA): 6.6
------------------------------------------------------------
Persons Eligible for EWS Category:
d
f
i
l
m
n



"""