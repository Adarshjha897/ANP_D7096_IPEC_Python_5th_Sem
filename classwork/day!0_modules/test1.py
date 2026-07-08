import numeric_calculation

print("--------------------------------------------------------------")
a = int(input("Enter the first number: "))
b = int(input("Enter the second nummber: "))
print("---------------------------------------------------------------")

#calling addition function
print("Sum is: ",numeric_calculation.calculate_add(a,b))
# calling subtraction function
print("Difference is: ",numeric_calculation.calculate_sub(a,b))
#calling multiplication function
print("Multiplication is: ",numeric_calculation.calculate_mul(a,b))
#calling division function
print("Division is: ",numeric_calculation.calculate_div(a,b))
#calling remainder function
print("Remainder is: ",numeric_calculation.calculate_rem(a,b))


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