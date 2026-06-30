# accessing the list in forward direction using the negitive index 

#creating a list
num = [1,2,3,4,5,6]

#printing the list
print("printing the list: ")
print(num)

print("-------------------------------")
print("list element using the negitive index :[", end = ' ')
for i in range(-(len(num)),0):
    print(num[i],end =" ")
print("]")
