from twodfigures import *
x = """ select one of the following figures with the numbers: 
o select 1 for square
o select 2 for Circle 
o select 3 for Triangle 
o select 4 for Rectangle 

"""
print("-------------------------------------------------------------")
print(x)
print("-------------------------------------------------------------")
shape = int(input("Enter the number of the shape you have selcted"))
print("--------------------------------------------------------------")





if(shape == 1):
    op = """Enter 1 for Area and 2 for perimeter"""
    operation = int(input("Enter operation you want to perform"))
    side = float(input("Enter the side in m"))
    if(side<=0):
        exit("side can not be negitive or zero try again")
    print("-------------------------------------------------------")
    if(operation == 1):
        print("Area is : ", square_area(side),"meter square")
    elif(operation == 2):
        print("perimeter is: ", square_perimeter(side),"meter")


if(shape == 2):
    op = """Enter 1 for Area and 2 for cirumference"""
    operation = int(input("Enter operation you want to perform"))
    radius = float(input("Enter the radius in m"))
    if(radius>0):
        exit("radius can not be negitive try again")
    print("-------------------------------------------------------")
    if(operation == 1):
        print("Area of circle is : ", circle_area(radius),"meter square")
    elif(operation == 2):
        print("circumference of circle is: ", circle_circumference(radius), "meter")


if(shape == 3):
    op = """Enter 1 for Area and 2 for perimeter"""
    operation = int(input("Enter operation you want to perform"))

    b = float(input("Enter the base in m"))
    if(b<=0):exit("Base can not be less than 1")

    h = float(input("Enter the height in m"))
    if(h<=0):exit("height can not be less than 1")
    print("-------------------------------------------------------")
    if(operation == 1):
        print("Area of circle is : ", triagngle_area(b,h),"meter square")
    elif(operation == 2):
        print("circumference of circle is: ", triagngle_perimeter(b,h), "meter")


if(shape == 3):
    op = """Enter 1 for Area and 2 for cirumference"""
    operation = int(input("Enter operation you want to perform"))

    l = float(input("Enter the length in m"))
    if(l<=0):exit("length can not be less than 1")


    b = float(input("Enter the length in m"))
    if(b<=0):exit("length can not be less than 1")

    print("-------------------------------------------------------")

    if(operation == 1):
        print("Area of circle is : ", rectangle_area(l,b),"meter square")
    elif(operation == 2):
        print("circumference of circle is: ", rectangle_perimeter(l,b), "meter")