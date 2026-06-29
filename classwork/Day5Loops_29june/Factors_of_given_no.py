#display factor of a given no
"""
input of one integer no 
factor of +ve number -> +ve numbers 
factor of zero -> infinite factor
factor of -ve number  -> +ve no as well as -ve no


"""
#-------------------------------------------------
print("----------------------------------------------")
num = int(input("Enter the number: "))
print("----------------------------------------------")

#finding factor if the number is 0
if(num==0):
    print("0 have infinite factors !")

#if number is positive
elif(num>0):
    print("Factors are:  ")
    for x in range(1,num+1):

        #checking divisibility
        if(num%x==0):
            print(x , end = " , ")

#if the number is negitive
else :
    no = -num
    print("Factors are:  ")
    for x in range(1,no+1):

        #checking divisibility
        if(no%x==0):
            print(x ," , " ,-x ,end = " , ")
print()

print("_________________________________________________________")

#output
"""
----------------------------------------
Enter the number: -27
----------------------------------------
Factors are:
1 ,  -1 , 3 ,  -3 , 9 ,  -9 , 27 ,  -27 ,
________________________________________
"""