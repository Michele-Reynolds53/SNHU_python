#**********************************************#
#  Michele Reynolds                            #
#  June 27, 2023		               #
#  Myclass			               #
#  Input values, output in short story         #
#  Stores variable, outputs to short story     #
#**********************************************#


# Prompt the user for their name and store the value in first_name
first_name = input("What is your name? ")

# Prompt the user for their location and store the value in generic_location
generic_location = input("Pick a location ")

# Prompt the user for a number and store the value in whole_number
whole_number = input("Please enter a whole number larger than 1: ")

# Prompt the user for a noun (plural) and store the value in plural_noun
plural_noun = input("Enter a plural noun: ")

# Output a short story using the four input values.
print(first_name, 'went to', generic_location, 'to buy', whole_number, 'different types of', plural_noun)