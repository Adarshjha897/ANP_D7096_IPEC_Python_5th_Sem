# make a function to calulate simple intrest 

# declaring a function to calculate simple interest
def calculate_simple_interest(principal, rate, time):
   
    # Calculate simple interest
    return(principal * rate * time) / 100

#taking input from the user
print("---------------------------------------------")
p = float(input("Enter the principal amount: "))
r = float(input("Enter the rate of interest: "))
t = float(input("Enter the time in years: "))
print("---------------------------------------------")
# showing output to the user
print("The simple interest is:", calculate_simple_interest(p, r, t))


# output:

"""
-------------------------------------
Enter the principal amount: 100
Enter the rate of interest: 1
Enter the time in years: 1
-------------------------------------
The simple interest is: 1.0

"""