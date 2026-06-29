# wap to find out factorial of a number

"""
requirements
input of 1 +ve number
cases 
factorial of negitive number is not possible
factorial of 0 and 1 is always 1
factorial of any n num > 0 = 1*2*3*....*n


"""
n = 1
num = int(input("Enter the number: "))

#checking if the number is negitive or not 
if(num<0):
    print("Factorial is not possible")

#if number is equal to 0 or 1 
elif(num == 0 or num ==1):
    print("Factorial of number", num ,"is: 1 ")

# if number > 1
else:
    for i in range(2,num+1):
        n *= i
print("the factorial of number ", num , "is: ", n)

#output

"""
Enter the number: 3
the factorial of the number is:  6
"""