"""
5. Parking Entry Validation  
Problem Statement 
Only vehicles having a valid parking pass are allowed to enter a private parking area. 
Accept either 1 (Valid Pass) or 0 (No Pass). 
• If the input is 1, display: 
Entry Allowed 
• Otherwise display: 
Entry Denied 
Sample Input 
0 
Sample Output 
Entry Denied


"""
print("--------------------------")
#taking input from user
pas = int(input("Enter 1 if you have pass 0 if you dont have it: "))
#validating the input

if(pas<0 and pas>1):
    print("___________________________")
    exit("Invalid input enter 0 or 1 only")
print("---------------------------")
#checking for the pass
if(pas==1):
    print("Entry allowed")
else:print("Entery Denied")


# output

"""
-------------------------------------------------
Enter 1 if you have pass 0 if you dont have it: 0 
-------------------------------------------------
Entry Denied

"""