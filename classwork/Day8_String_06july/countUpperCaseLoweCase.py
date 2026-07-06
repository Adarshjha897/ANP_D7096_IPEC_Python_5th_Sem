#   wap to count the number of uppercase and lowercase letters in a string without help of library function 

#taking input from the user
sentence = input("Enter your sentence: ")

uppercount = 0
lowecount = 0
print("--------------------------------------------------------------------")
# itterating through the string
for char in sentence:
    if(char>='A' and char<='Z'):
        #increasing the value of uppercount if uppercase letter found
        uppercount+=1
    elif(char>='a' and char<='z'):
        #increasing the value of lowecount if lowercase letter found
        lowecount+=1

print("The number of uppercase letters in the sentence is: ", uppercount)
print("........")
print("The number of lowercase letters in the sentence is: ", lowecount)
print("---------------------------------------------------------------------")

# output:

"""

Enter your sentence: Adarsh Kumar Jha
------------------------------------------------------------
The number of uppercase letters in the sentence is:  3
........
The number of lowercase letters in the sentence is:  11
------------------------------------------------------------


"""