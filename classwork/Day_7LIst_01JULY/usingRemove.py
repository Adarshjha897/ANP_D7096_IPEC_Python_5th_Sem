#  from the 10 numbers present in the list we are shwoing the use of remove method

numbers = [1,5,6,7,8,5,4,3,2,5]#list of 10 numbers
print("-----------------------------------------")

print("The list of numbers is : ", numbers)#printing the list of numbers
print("-----------------------------------------")

numbers.remove(5)#it will remove the first occurrence of the given element from the list
print("the list of numbers after using remove method is : ", numbers)
print("-----------------------------------------")

numbers.remove(1)# it will remove as it has only one occurence in the given list
print("the list of numbers after using remove method is : ", numbers)
print("-----------------------------------------")

numbers.remove(45)# it will give an error as the given element is not present in the list
print("the list of numbers after using remove method is : ", numbers)
print("-----------------------------------------")

#output:

"""

---------------------------------
The list of numbers is : [1, 5, 6, 7, 8, 5, 4, 3, 2, 5]
---------------------------------
the list of numbers after using remove method is : [1, 6, 7, 8, 5, 4, 3, 2, 5]
---------------------------------
the list of numbers after using remove method is : [6, 7, 8, 5, 4, 3, 2, 5]
---------------------------------
Traceback (most recent call last):
  File "d:\ANP_D7096_IPEC_Python_5th_Sem\classwork\Day_7List_01JULY\usingRemove.py", line 18, in <module>
    numbers.remove(45) # it will give an error as the given element is not present in the list
    ^^^^^^^^^^^^^^^^^^
ValueError: list.remove(x): x not in list


"""