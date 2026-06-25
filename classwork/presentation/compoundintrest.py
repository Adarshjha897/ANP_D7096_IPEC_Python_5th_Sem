#program to calculate compound interest
principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the rate of interest: "))
time = float(input("Enter the time in years: "))

#-------------------------------------------------------
#printing the inputs from user
print("Principal Amount: ", principal)
print("Rate of Interest: ", rate)
print("Time in Years: ", time)

#-------------------------------------------------------
# printing compound intrest answer
print("Compound Interest: ", principal * (1 + rate / 100) ** time)
