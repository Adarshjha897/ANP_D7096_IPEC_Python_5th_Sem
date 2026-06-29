"""

2. Password Strength Checker 
Problem Statement 
A website requires users to create a password having at least 8 characters. 
Keep asking the user to enter a password until the entered password satisfies the minimum length 
requirement. 
Sample Output 
Enter Password: hello 
Password too short. 
 
Enter Password: python@123 
Password Accepted. 



"""
"""
Requirements :
    input from user 
    till password is of 8 character
"""

check = "f"

while(check == "f"):
    pas = input("Enter youre Password: ")
    if(len(pas)<8):
        print("Password too short")
        
    else:
        print("password Accepted")
        check = "t"
        break