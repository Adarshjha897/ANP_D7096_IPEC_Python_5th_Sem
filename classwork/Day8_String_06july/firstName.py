# Wap to take input from user in form of string as name
# and display the first name of user without using library methods

name = input("Enter your full name: ")
first_name = ""

# neglecting the spaces
start = 0
while start < len(name) and name[start] == " ":
    start += 1

# Extract the first word
for i in range(start, len(name)):

    if name[i] == " ":#it will break loop after the first space 
        break
    first_name += name[i]

#printing the first name of the user if he has enternd a valid name
if (first_name.isspace() == False and first_name != ""):
    print("Your first name is:", first_name)
else:
    print("No first name found.")

# output:

"""
Enter your full name: Adarsh kumar jha
Your first name is: Adarsh


.............when only white spaces entered in input...............

Enter your full name:         
Your first name is: No first name found.


"""