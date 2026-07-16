"""

Problem Statement 3: Password Strength Checker 
Write a function check_password(password) that checks whether a password is strong. 
A password is considered Strong if: 
• It contains at least 8 characters.  
• It contains at least one uppercase letter.  
• It contains at least one lowercase letter.  
• It contains at least one digit.  
The function should return: 
• "Strong Password" or  
• "Weak Password"  
The main program should accept a password from the user and display the result. 


"""

#creating function to check strength of password

def check_password(password):
    if(len(password)>=8):
        if(check_uppercase(password)):
            if(check_Lowercase(password)):
                if(check_digit(password)):
                    return "Strong Password"
    else:
        return "weak password ,Try again!"
                 
      


# checking for a upper case char
def check_uppercase(password):
    for x in password:
        if(x.isupper):
            return True
    return False
        

#checking for a lower case char
def check_Lowercase(password):
    for x in password:
        if(x.islower):
            return True
    return False

def check_digit(password):
    for x in password :
        if(x.isdigit):
            return True
    return False
    
password = input("Enter a strong password: ")
print("You have Entered a",check_password(password))


#output:


"""
Enter a strong password: Adarsh1243
You have Entered a Strong Password

"""