import numeric_calculation as nc


print("--------------------------------------------------------------")
a = int(input("Enter the first number: "))
b = int(input("Enter the second nummber: "))
print("---------------------------------------------------------------")

#calling addition function
print("Sum is: ",nc.calculate_add(a,b))
# calling subtraction function
print("Difference is: ",nc.calculate_sub(a,b))
#calling multiplication function
print("Multiplication is: ",nc.calculate_mul(a,b))
#calling division function
print("Division is: ",nc.calculate_div(a,b))
#calling remainder function
print("Remainder is: ",nc.calculate_rem(a,b))


print("------------------------------------------------------------------")

# output:

"""
--------------------------------------------------------------
Enter the first number: 5
Enter the second nummber: 10
---------------------------------------------------------------
Sum is:  15
Difference is:  -5
Multiplication is:  50
Division is:  0.5
Remainder is:  5
------------------------------------------------------------------

"""