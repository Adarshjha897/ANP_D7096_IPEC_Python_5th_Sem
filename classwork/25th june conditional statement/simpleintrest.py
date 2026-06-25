# Program to calculate simple interest
#taking principal input from the user
principal = float(input("Enter the principal amount in ruppees: "))
if(principal < 0):
    print("Principal amount cannot be negative. Please enter a valid amount.")
    principal = float(input("Enter the principal amount in ruppees: "))
#taking rate of interest input from the user
rate = float(input("Enter the rate of interest (in %): "))
if(rate < 0):
    print("Rate of interest cannot be negative. Please enter a valid rate.")
    rate = float(input("Enter the rate of interest (in %): "))
#taking time period input from the user
time = int(input("Enter the time period (in years): "))
if(time < 0):
    print("Time period cannot be negative. Please enter a valid time period.")
    time = int(input("Enter the time period (in years): "))

#------------------------------------------------------------------------------
#displaying the inputs provided by the user
print("\nPrincipal Amount: Rs.", principal)
print("Rate of Interest: ", rate, "%")
print("Time Period: ", time, "years")

#------------------------------------------------------------------------------
#displaying the formula for simple interest
print("\nThe formula for calculating simple interest is:")
print("Simple Interest = (Principal * Rate * Time) / 100")