# wap to input any 10 numbers from the user and display odd numbers from them


numbers = []
print("Enter any 10 numbers")
print("------------------------------------")

for x in range (10):
#taking input from the user

	num = int(input())

#inserting element into the list

	numbers.append(num)

print("Entered numbers are ", numbers)

print("-------------------------------------")

print("odd nummbers are: [", end = " ")

for i in range (10):
	if((numbers[i])%2==1):
		print(numbers[i],end = " ")



print("]")	
#output

"""
Enter any 10 numbers
----------------------------------------
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
Entered numbers are [1,2,3,4,5,6,7,8,9,10]
------------------------------------------
odd numbers are: [1,3,5,7,9]

"""
