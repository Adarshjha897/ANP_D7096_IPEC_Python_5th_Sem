#count the number of vovels in a string


#initializing the count
count = 0

#taking input from the user
sentence = input("Enter youre sentence: ")
print("-----------------------------------------------")
# itterating through the string
for char in sentence:
    if(char=="a" or char=="e" or char=="i" or char=="o" or char=="u" or char=="A" or char=="E" or char=="I" or char=="O" or char=="U"):
        #increasing the value of count if vovel found
        count+=1
#printing the number of vovel in a string
print("The number of vovels in the sentence is: ", count)
print("------------------------------------------------")

# output:

"""
Enter youre sentence: Adarsh kumar Jha
----------------------------------------------
The number of vovels in the sentence is:  5
----------------------------------------------

"""