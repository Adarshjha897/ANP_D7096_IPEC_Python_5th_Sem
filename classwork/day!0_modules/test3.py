from numeric_calculation import calculate_add
print("--------------------------------------------------------------")
a = int(input("Enter the first number: "))
b = int(input("Enter the second nummber: "))
print("---------------------------------------------------------------")

#calling addition function
print("Sum is: ",calculate_add(a,b))


#it will through an error
# calling subtraction function
# print("Difference is: ",calculate_sub(a,b)) 

#output:

"""

--------------------------------------------------------------
Enter the first number: 5
Enter the second nummber: 10
---------------------------------------------------------------
Sum is:  15

Traceback (most recent call last):
  File "d:\ANP_D7096_IPEC_Python_5th_Sem\classwork\day!0_modules\test3.py", line 12, in <module>
    print("Difference is: ",calculate_sub(a,b)) #it will through an error
                            ^^^^^^^^^^^^^
NameError: name 'calculate_sub' is not defined. Did you mean: 'calculate_add'?


"""