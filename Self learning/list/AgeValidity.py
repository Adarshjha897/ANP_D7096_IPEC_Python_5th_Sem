# Wap to input the age of 15 person for people and displaye the persons as adult whose age is greater = to 18

ages = []
print("Enter age of 15 persons")
print("------------------------------------")

for x in range (15):
#taking input from the user
     age = int(input())
    if(age<=0):
	    print("Invalid age try again")
	    i = i-1
        
    else:
        ages.append(age)
        
#inserting element into the list

print("Entered ages are", ages)
count = 0
print("-------------------------------------")

for i in range(15):
    if(ages[i]>=18):
        print(f"the person at {i} index is an adult")
        print("-------------------------------------")
		
		