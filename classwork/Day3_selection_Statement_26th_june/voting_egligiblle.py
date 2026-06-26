#write a program to check wehter a person is egligible to vote or not if his age is above 18 he is eg
#egligible to vote otherwise he is not eligible to vote
print("--------------------------------------------------------------------------------")
age= int(input("enter youre age:"))
if age< 0:
    print("--------------------------------------------------------------------------------")
    exit("Invalid age. Please provide a positive or a valid age")
#checking ther egligiblity to vote based on the age provided 
if(age>= 18):
    print("youre egligible to vote")
    print("--------------------------------------------------------------------------------")
else:
    print("youre not egligible to vote ")
    print("--------------------------------------------------------------------------------")

#output:

#if age is greater than or equal to 18

"""
-----------------------------------------------------------------------\
enter youre age:28
youre egligible to vote
-----------------------------------------------------------------------

"""
#if age is less than 18
"""
-----------------------------------------------------------------------
enter youre age:16
youre not egligible to vote 
-----------------------------------------------------------------------
"""
