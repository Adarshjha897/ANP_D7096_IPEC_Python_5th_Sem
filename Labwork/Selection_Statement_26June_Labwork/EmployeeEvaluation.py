"""

4. Employee Performance Evaluation 
Problem Statement 
An employee is evaluated using: 
• Project Score  
• Attendance Percentage  
• Client Feedback Score  
Rules: 
• Excellent → All scores above 90  
• Good → Scores above 75  
• Average → Scores above 60  
• Poor → Otherwise  
Additional Rule: 
• Attendance below 70% cannot receive more than Average rating.  
Sample Input 
Project Score: 95 
Attendance: 65 
Client Feedback: 92 
Sample Output 
Performance Rating: Average 
Reason: Attendance below 70%

"""
print("---------------------------------------------------------")
ProjectScore = int(input("Enter Project Score :"))
if(ProjectScore <0):
    exit("please enter a positive value ")
Attendence = int(input("Enter attendence in % : "))
if(Attendence<0):
    exit("Please enter a positive value")
Client_Feedback = int(input("Enter the client feedback"))
if(Client_Feedback<0):
    exit("Please enter a positive value")
print("-----------------------------------------------------------")

Average_Score = (ProjectScore + Attendence + Client_Feedback)/3
if(Average_Score>90): 
    print("Performance Score : Excellent, keep it up")

elif(Average_Score>75):
    if(Attendence >=70):
        print("Performance Rating : good")
    else:
        print("Performace Rating : Average ")
        print("Reason : Attendence below 70%")
elif(Average_Score>60):
    print("Perfomance Rating : Average")
    if(Attendence<70):
        print("Reason : Attendence below 70%")
else:print("Performace Rating : Poor")
print("-----------------------------------------------------------------")   


#output
"""
-------------------------------------------------------------------------
Project Score: 95 
Attendance: 65 
Client Feedback: 92 
-------------------------------------------------------------------------
Performance Rating: Average 
Reason: Attendance below 70%
-------------------------------------------------------------------------

"""