#   WAP TO COUNT THE NUMBER OF SPECIAL CHARRACTERS IN A GIVEN STRING INPUT BY USER
#  USING STRING LIBRARY METHODS

#taking input from the user
sentence = input("Enter your sentence: ")

countSpecial = 0 #initializing the count for speacial charracters

print("------------------------------------------------------------")
for char in sentence:
    if (not char.isalnum()):  # Check if the character is not alphanumeric and not a space
        countSpecial += 1

print(f"Number of special characters: {countSpecial}")#printing the number of special in sentence
print("------------------------------------------------------------")


# output:

"""

Enter your sentence: Adarsh@12u4*3
------------------------------------------------------------
Number of special characters: 2
------------------------------------------------------------


"""