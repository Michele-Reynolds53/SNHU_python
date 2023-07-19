# ******************************************************************** #
#  Michele Reynolds                                                    #
#  IT-140 - J6840  	                                                   #
#  4.14 LAB: Count input length without spaces, periods, or commas     #
#  July 15, 2023                                                       #
#  Output count of characters excluding spaces, periods, or commas     #
# ********************************************************************* #

# variable to hold user input
user_text = input()

# specific characters to be excluded from output
special_characters = [' ', ',', '.']

# store the number of characters in user_text
count_characters = len(user_text)

# initialize index for while loop
i = 0

# iterate through special character list
while i < len(special_characters):
    characters = special_characters[i]

    # subtract the count of special characters from count_characters
    count_characters -= user_text.count(characters)

    # increment i for next iteration
    i += 1

# print count
print(count_characters)
