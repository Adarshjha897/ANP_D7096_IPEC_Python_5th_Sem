"""

5. Count Prime Numbers in a Range 
Problem Statement 
Accept two integers representing the starting and ending values of a range. 
Display all prime numbers within the range and finally display the total number of prime numbers 
found.


"""
"""
requirements
     
        taking input of starting point and ending point of ranges 
        no can range to negitive to positive 
        if




"""

# Accept starting and ending values from the user
start = int(input("Enter starting number: "))
end = int(input("Enter ending number: "))

print(f"Prime numbers between {start} and {end} are:")

# Variable to keep track of the total count of primes

prime_count = 0

# Loop through each number in the given range
for num in range(start, end + 1):
    # Prime numbers must be greater than 1
    if num > 1:
        is_prime = True
        
        # Check for factors from 2 up to the square root of num (or num-1)
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False  # Found a factor, so it's not prime
                break             # No need to check further, exit inner loop
        
        # If no factors were found, it is prime
        if (is_prime == True):
            print(num, end=" ")
            prime_count += 1

# Print the final count
print(f"Total number of prime numbers found: {prime_count}")