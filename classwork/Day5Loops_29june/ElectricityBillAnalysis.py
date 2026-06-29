"""
6. Electricity Bill Analysis 
Problem Statement 
An electricity department wants to analyze electricity consumption of N houses. 
Accept the monthly units consumed by each house. 
Calculate and display: 
• Total units consumed  
• Average units consumed  
• Highest consumption  
• Lowest consumption

"""
#taking input of number of houses
N = int(input("Enter number of houses:"))
print("----------------------------------------------------------")
# validating the input
if(N<=0):
    exit("NUmber of house can not be negitive")
max = 0
min = 0

total_units = 0

for i in range (1,N+1):
    bill_units = int(input("Enter bill units consumed in house", i ,": "))
    print("-------------------------------------------------------")
    total_units += bill_units
    if(max<bill_units):
        max=bill_units
        highest = bill_units
    if(min>bill_units):
        min = bill_units
        


print("Total units consumed = ", total_units)
print("Average units consumed = ", total_units/N)
print("Highest units consumed = ", max)
print("lowest units consumed = ", min)