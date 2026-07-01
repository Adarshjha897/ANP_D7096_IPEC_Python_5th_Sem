"""
write a program to create a list of 20 numbers given by user if ask the user to input any other number 
if the number is present in list remove all the duplicate occurence in
the list 

"""

numbers = []
num = {}
print("Enter any 20 numbers")
print("------------------------------------")

for x in range (20):
#taking input from the user

	num = int(input())

#inserting element into the list

	numbers.append(num)

#taking the input of the number whose duplicate occurence is to be removed
print("The list of numbers is : ", numbers)
print("\n\n------------------------------------")


num = int(input("Enter the number whose duplicate occurence should not be present in the list: "))
index =0
#counting the number of occurences of the given number in the list 
print("-------------------------------------------------------------")

c = numbers.count(num)
print("The number of occurence of the given number in the list is : ", c)
if(c >1):
	# for x in range(20):
	# 	if(numbers[x]==num):
	# 		index = x #storing the first index of the given number in the list
	# 		break
	# for i in range(index+1,20):#removing the duplicate occurence of the given number from the list
	# 	if(numbers[i]==num):
	# 		numbers.remove(num)

	numbers.reverse()
	while True:
		if(c>1):numbers.remove(num)
		c = numbers.count(num)
		if(c == 1):
			numbers.reverse()
			break
elif(c == 1):
	print("The given number has only one occurence in the list")

else:
	print("The given number is not present in the list")

#printing the list after removing the duplicate occurence of the given number
print("The list of numbers after removing the duplicate occurence of the given number is : ", numbers)

#output:

"""
Enter any 20 numbers
------------------------------------
1
2
3
4
12
23
23
445
343
5
4
23
23
44
23
23
445
23
55
2
The list of numbers is : [1, 2, 3, 4, 12, 23, 23, 445, 343, 5, 4, 23, 23, 44, 23, 23, 445, 23, 55, 2]

------------------------------------
Enter the number whose duplicate occurence should not be present in the list: 23
------------------------------------
The number of occurence of the given number in the list is : 7
The list of numbers after removing the duplicate occurence of the given number is :  [1, 2, 3, 4, 12, 23, 445, 343, 5, 4, 44, 445, 55, 2]


"""