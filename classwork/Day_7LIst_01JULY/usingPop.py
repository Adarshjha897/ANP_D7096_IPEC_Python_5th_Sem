#problem to take input of 10 number in list and then show the use of pop method



numbers = []
print("Enter any 10 numbers")
print("------------------------------------")


for x in range (10):
#taking input from the user

	num = int(input())

#inserting element into the list

	numbers.append(num)

#-------------------------------------------------
print("The list of numbers is : ", numbers)
print("------------------------------------")
numbers.pop()#it will remove the last element from the list
print("The list of numbers after using pop without index is : ", numbers)
print("------------------------------------")
numbers.pop(2)#it will remove the element of the given index from the list
print("The list of numbers after using pop with 2 index is : ", numbers)


#output:
"""

Enter any 10 numbers
------------------------------------
1
2
3
4
5
6
7
8
9
10

The list of numbers is : [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
------------------------------------
The list of numbers after using pop without index is : [1, 2, 3, 4, 5, 6, 7, 8, 9]
------------------------------------
The list of numbers after using pop with 2 index is : [1, 2, 4, 5, 6, 7, 8, 9]




"""
