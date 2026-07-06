"""
Lab 2: Word Frequency Counter 
Problem Statement: 
Accept a sentence from the user and create a dictionary that stores the frequency of each word. 
Example: 
Input: 
python is easy and python is powerful 
 
Output: 
{ 
'python': 2, 
'is': 2, 
'easy': 1, 
'and': 1, 
'powerful': 1 
} 
Additionally: 
• Display the most frequently occurring word.  
• Display all words in alphabetical order.  

"""


# Step 1: Accept input
sentence = input("Enter a sentence: ")

# Step 2: Split into words
words = sentence.split()

# Step 3: Count frequency using dictionary
freq = {}
for word in words:
    freq[word] = freq.get(word, 0) + 1

# Step 4: Display dictionary
print("Word Frequency Dictionary:")
print(freq)

# Step 5: Most frequent word
most_frequent = max(freq, key=freq.get)
print("Most frequent word:", most_frequent)

# Step 6: Words in alphabetical order
print("Words in alphabetical order:")
for word in sorted(freq.keys()):
    print(word)


#output:

"""
Enter a sentence: we are happy as we will be having party today
Word Frequency Dictionary:
{'we': 2, 'are': 1, 'happy': 1, 'as': 1, 'will': 1, 'be': 1, 'having': 1, 'party': 1, 'today': 1}
Most frequent word: we
Words in alphabetical order:
are
as
be
happy
having
party
today
we
will

"""