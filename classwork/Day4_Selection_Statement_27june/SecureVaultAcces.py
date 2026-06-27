"""
1. Secure Vault Access 
Problem Statement 
A digital vault can only be opened if the user enters the correct security code. 
Write a Python program that accepts the entered security code. If the entered code is 7890, display: 
"Access Granted to the Vault." 
Otherwise, do nothing. 
Sample Input 
7890 
Sample Output 
Access Granted to the Vault.

"""
print("---------------------------------")
#taking input
pas = int(input())

#validating the input
if(pas<0 or pas>9999):
    exit()

print("----------------------------------")

#checking for security code
if(pas==7890):
    print("Acces Granted to the Vault")

#output
"""
------------------------------------------
7890 
------------------------------------------
Access Granted to the Vault.
"""