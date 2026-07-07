"""
Problem Statement 5: Vowel Counter using Function 
Write a Python program that defines a function count_vowels(text). 
The function should: 
• Accept a string.  
• Count the total number of vowels (a, e, i, o, u) irrespective of case.  
• Return the total vowel count.  
The main program should: 
• Accept a sentence from the user.  
• Call the function.  
• Display the total number of vowels.  
Sample Output 
Enter a sentence: 
Python Programming is Fun 
 
Total Vowels: 6

"""
def vowel_counter(text):
    
    count = 0      #initializing the count to 0

    #looping to count all the vowel
    for char in text:
        if char in "aeiouAEIOU":
            count += 1 #increasing the count when vowel found 
    return count

#taking the input text
sentence = input("Enter a sentence: ")

#checking for the count of vowel and printing it
print("Number of vowels:", vowel_counter(sentence))


# output:

"""
Enter a sentence: Adarshuweuherubw
Number of vowels: 7

"""
