# Program to input the age of 15 persons
# and display the persons as adults (age >= 18)

ages = []
print("Enter age of 15 persons")
print("------------------------------------")

for x in range(15):
    while True:  # keep asking until valid age is entered
        age = int(input(f"Enter age of person {x+1}: "))
        if age <= 0:
            print("Invalid age, try again")
        else:
            ages.append(age)
            break

print("Entered ages are:", ages)
print("-------------------------------------")
#printing the person who is 18 or above 
for i in range(15):
    if ages[i] >= 18:
        print(f"The person at index {i} is an adult (age {ages[i]})")
