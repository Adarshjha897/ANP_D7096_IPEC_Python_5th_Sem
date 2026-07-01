#funtions available in list


numbers = [1,2,3,4,5,6,7,8,9,5]#list of 10 numbers
print("-----------------------------------------")

print("The list of numbers is : ", numbers)#printing the list of numbers
print("-----------------------------------------")


#reverse
print("The list of numbers after reversing is : ", numbers.reverse()) # after reversing the list of numbers 

print("-----------------------------------------")
#sort in descending order 
print("The list of numbers after sorting in descending order is : ", numbers.sort(reverse = True))#printing the numbers in descebding order

#sorting in ascending order
print("The list of numbers after sorting in ascending order is :", numbers.sort())#printing the numbers in ascending order

print("-----------------------------------------")


#count method
print("The count of 5 in the list is : ", numbers.count(5))
# when number is not present in the list it will return 0 
print("The count of 100 in the list is : ", numbers.count(100))


