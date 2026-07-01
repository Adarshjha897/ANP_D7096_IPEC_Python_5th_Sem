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

c = numbers.count(num)
if(c >1):
	for x in range(20):
		if(numbers[x]==num):
			index = x #storing the first index of the given number in the list
			break
	for i in range(index+1,20):#removing the duplicate occurence of the given number from the list
		if(numbers[i]==num):
			numbers.remove(num)

	
	# while True:
	# 	numbers.remove(num)
	# 	c = numbers.count(num)
	# 	if(c == 1):
	# 		break

else:
	print("The given number is not present in the list or it has only one occurence in the list")

#printing the list after removing the duplicate occurence of the given number
print("The list of numbers after removing the duplicate occurence of the given number is : ", numbers)