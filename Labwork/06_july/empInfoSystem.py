"""
Lab 3: Employee Information System 
Problem Statement: 
Create a dictionary where: 
• Employee ID is the key.  
• Value is another dictionary containing:  
o Name  
o Department  
o Salary  
Perform the following operations: 
• Display all employee details.  
• Search for an employee using Employee ID.  
• Increase the salary of all employees by 10%.  
• Display employees belonging to a specific department entered by the user.  

"""

# Lab 3: Employee Information System

# Dictionary to store employee details
# Employee ID is the key, and value is another dictionary with Name, Department, and Salary
employees = {}

while True:
    print("\n--- Employee Information System ---")
    print("1. Add Employee")
    print("2. Display All Employees")
    print("3. Search Employee by ID")
    print("4. Increase Salary of All Employees by 10%")
    print("5. Display Employees by Department")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")

    # 1. Add Employee
    
    if choice == "1":
        no = int(input("Enter number of employees to add: "))
        for _ in range(no):
            emp_id = int(input("Enter Employee ID: "))
            name = input("Enter Employee Name: ")
            dept = input("Enter Department: ")
            salary = float(input("Enter Salary: "))
            employees[emp_id] = {"Name": name, "Department": dept, "Salary": salary}
            print("Employee added successfully!")

    # 2. Display All Employees
    elif choice == "2":
        print("\n--- All Employee Details ---")
        if not employees:   # check if dictionary is empty
            print("No employees found.")
        else:
            for emp_id, details in employees.items():
                print(f"ID: {emp_id}, Name: {details['Name']}, Department: {details['Department']}, Salary: {details['Salary']}")

    # 3. Search Employee by ID
    elif choice == "3":
        emp_id = int(input("Enter Employee ID to search: "))
        if emp_id in employees:
            details = employees[emp_id]
            print(f"ID: {emp_id}, Name: {details['Name']}, Department: {details['Department']}, Salary: {details['Salary']}")
        else:
            print("Employee not found.")

    # 4. Increase Salary of All Employees by 10%
    elif choice == "4":
        if not employees:
            print("No employees to update.")
        else:
            for emp_id in employees:
                employees[emp_id]["Salary"] = round(employees[emp_id]["Salary"] * 1.10, 2)
            print("Salaries increased by 10% successfully!")

    # 5. Display Employees by Department
    elif choice == "5":
        dept_name = input("Enter Department name: ")
        found = False
        print(f"\n--- Employees in {dept_name} Department ---")
        for emp_id, details in employees.items():
            if details["Department"].lower() == dept_name.lower():
                print(f"ID: {emp_id}, Name: {details['Name']}, Salary: {details['Salary']}")
                found = True
        if not found:
            print("No employees found in this department.")