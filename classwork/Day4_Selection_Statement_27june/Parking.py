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
pas = int(input())
if(pas<0 and pas>1):exit()
print("---------------------------")
if(pas==1):
    print("Entry allowed")
else:print("Entery Denied")


# output

"""
------------------------------
0 
------------------------------
Entry Denied

"""