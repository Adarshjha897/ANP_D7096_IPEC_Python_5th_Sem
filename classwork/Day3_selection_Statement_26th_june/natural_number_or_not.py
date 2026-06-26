# to check whether a number is a natural number or not
print("--------------------------------------------------------------------------------")
number = int(input("Enter a number: "))
if number > 0:
    print(f"{number} is a natural number.")
    print("--------------------------------------------------------------------------------")
else:
    print(f"{number} is not a natural number.")
    print("--------------------------------------------------------------------------------")

# output:
"""
Enter a number: 5
5 is a natural number.
--------------------------------------------------------------------------------    

"""
"""
enter a number: -3
-3 is not a natural number.
--------------------------------------------------------------------------------
"""