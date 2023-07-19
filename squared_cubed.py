# **************************************************#
#  Michele Reynolds                            	    #
#  June 27, 2023		              	    #
#  Squared			               	   #
#  Squared and cubed for user_num and user_num2    #
#  Stores variable, outputs to short story         #
# **************************************************#

user_num = int(input('Enter integer:\n'))

# Output the user's input
print("You entered:", user_num)

# Output the input squared and cubed
squared = user_num * user_num
cubed = user_num * user_num * user_num
print(f"{user_num} squared is {squared}")
print(f"And {user_num} cubed is {cubed} !!")

# Get a second user input into user_num2 and output the sum and product
user_num2 = int(input("Enter another integer:\n"))

# Output user_num2's input
total = user_num + user_num2
product = user_num * user_num2
print(user_num, "+", user_num2, "is", total)
print(user_num, "*", user_num2, "is", product)