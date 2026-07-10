"""
7. Cybersecurity Login Validation 
Problem Statement 
A login system validates: 
• Username  
• Password  
• OTP  
Conditions: 
• All correct → Login Successful  
• Incorrect OTP → Re-enter OTP  
• Incorrect Password after 3 attempts → Account Locked  
• Incorrect Username → User Not Found  
Sample Input 
Username: admin 
Password: admin123 
OTP: 4567 
Sample Output 
Login Successful 
Welcome Admin 

"""

uid = input("Username: ")
pas = input("password: ")
print("--------------------------------------")
otp = int("OTP: ")
if(uid=="admin"):
    if(pas == "admin123"):
        print("hello")
    
    
