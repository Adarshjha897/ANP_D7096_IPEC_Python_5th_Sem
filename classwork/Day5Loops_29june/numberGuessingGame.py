"""
3. Number Guessing Game 
Problem Statement 
A secret number is 37. 
Keep asking the user to guess the number until the correct number is entered. 
Display whether the entered number is too high, too low, or correct. 

"""
#initializing the correct no
num = 37
#settting conditon for loop
bol = "f"

while(bol == "f"):
    #Taking input
    no = int(input("Enter the number:"))
    #if number is correct
    if(no == num):
        print("Entered number is correct")
        bol = "t"
        break
    # if entered number is low
    elif(no<num):
        print("Entered number is too low")
    #if entered number is high
    else:print("Entered number is too high")
    