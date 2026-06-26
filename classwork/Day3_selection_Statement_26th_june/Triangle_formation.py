#check wether the three angles can form a triangle or not and validate the angles
#--------------------------------------------------------------------------------
print("--------------------------------------------------------------------------------")

#taking input from the user and validating the angles

angle1 = float(input("Enter the first angle (in degrees): "))
if (angle1 <= 0 or angle1 >= 180):
    exit(print("Invalid angle. Please enter an angle between 0 and 180 degrees."))
   
angle2 = float(input("Enter the second angle (in degrees): "))
if (angle2 <= 0 or angle2 >= 180):
    exit(print("Invalid angle. Please enter an angle between 0 and 180 degrees."))

angle3 = float(input("Enter the third angle (in degrees): "))
if (angle3 <= 0 or angle3 >= 180):
    exit(print("Invalid angle. Please enter an angle between 0 and 180 degrees."))
#--------------------------------------------------------------------------------
#if the sum of the three angles is equal to 180 degrees, then they can form a triangle
print("--------------------------------------------------------------------------------")
if angle1 + angle2 + angle3 == 180:
    print("The angles can form a triangle.")
#--------------------------------------------------------------------------------
#it is not possible to form a triangle if the sum of the three angles is not equal to 180 degrees
else:
    print("The angles cannot form a triangle.")
print("--------------------------------------------------------------------------------")

"""
-----------------------------------------------------------------------------------------
Enter the first angle (in degrees): 20
Enter the second angle (in degrees): 60
Enter the third angle (in degrees): 100
-----------------------------------------------------------------------------------------
The angles can form a triangle.
-----------------------------------------------------------------------------------------
"""