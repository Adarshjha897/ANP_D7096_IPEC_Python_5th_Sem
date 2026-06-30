# take the input of person name and salary check wether he fall in Ews cateogry if his salary is less than 5Lpa
#-----------------------------------


# initializing the list
record = []

# Input details of 15 persons
for i in range(15):
    #taking the name 
    name = input("Enter Name: ")
    
    #taking age 
    salary = float(input("Enter Salary (in LPA): "))
    #validating the age
    while salary <= 0:
        print("Salary must be positive. Please enter again.")
        salary = float(input("Enter Salary (in LPA): "))
    #adding the data into the list
    record.append([name, salary])

print()
print("Persons Eligible for EWS Category:")

# Display eligible persons
for person in record:
    # Eligible if salary < 5 LPA
    if person[1] < 5:
        print(person[0])
