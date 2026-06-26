# 10. Event Management Budget 
# Scenario: 
# An event manager wants to calculate the cost contribution per participant. 
# Problem Statement: 
# Write a Python program to calculate how much each participant should pay. 
# Input: 
# • Total Event Cost  
# • Number of Participants  
# Output: 
# • Amount per Participant 


total_event_cost = float(input("Enter the total event cost: "))
number_of_participants = int(input("Enter the number of participants: "))
print("Total Event Cost: ", total_event_cost)
print("Number of Participants: ", number_of_participants)
print("Amount per Participant: ", total_event_cost / number_of_participants)

"""
Enter the total event cost: 5000
Enter the number of participants: 100
Total Event Cost:  5000.0
Number of Participants:  100
Amount per Participant:  50.0
"""