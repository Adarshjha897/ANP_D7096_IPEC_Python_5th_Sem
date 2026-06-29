"""
4. Multiplication Table Generator 
Problem Statement 
Write a Python program that accepts a number from the user and displays its multiplication table up to 
20. 
Sample Output 
Enter Number: 8 
 
8 x 1 = 8 
8 x 2 = 16 
... 
8 x 20 = 160

"""

# taking input
n = int(input("Enter the number whose table you want to print: "))

#printing the table

for i in range(1,21):
    print(n , "*", i ,"=", n*i)
