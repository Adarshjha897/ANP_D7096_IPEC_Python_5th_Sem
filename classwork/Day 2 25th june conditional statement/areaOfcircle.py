# calculate the area of a circle  and validate it
# taking radius as input from the user
radius = float(input("Enter the radius of the circle in cm: "))
if(radius < 0):
    exit("Radius cannot be negative. Please enter a valid radius.")

#------------------------------------------------------------------------------
# displaying the input provided by the user
print("\nRadius of the circle: ", radius)
#------------------------------------------------------------------------------
# displaying the formula for area of a circle
print("\nThe formula for calculating the area of a circle is:")
print("Area = π * radius^2")
print("Area = ", 3.14159 * radius * radius, "cm^2")