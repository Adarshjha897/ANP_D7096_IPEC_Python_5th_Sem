#calculating the area and perimeter of a rectangle and validating the inputs
#taking length as input from the user
length = float(input("Enter the length of the rectangle in cm: "))
if(length < 0):
    exit("Length cannot be negative. Please enter a valid length.")
#taking breadth as input from the user
breadth = float(input("Enter the breadth of the rectangle in cm: "))
if(breadth < 0):
    exit("Breadth cannot be negative. Please enter a valid breadth.")

#------------------------------------------------------------------------------
#displaying the inputs provided by the user
print("\nLength of the rectangle: ", length, "cm")
print("Breadth of the rectangle: ", breadth, "cm")

#------------------------------------------------------------------------------
# checking what the user want to calculate area or perimeter
choice = input("\nEnter 'A' to calculate area or 'P' to calculate perimeter: ")
#-----------------------------------------------------------------------------
#if the user chooses to calculate area, display the formula for area of a rectangle

if(choice == 'A' or choice == 'a'):
    #displaying the formula for area  of a rectangle
    print("\nThe formula for calculating the area of a rectangle is:")
    print("Area = Length * Breadth")
    print("Area = ", length * breadth, "cm^2")
#-----------------------------------------------------------------------------    
if(choice == 'P' or choice == 'p'):
    #displaying the formula for perimeter of a rectangle
    print("\nThe formula for calculating the perimeter of a rectangle is:")
    print("Perimeter = 2 * (Length + Breadth)")