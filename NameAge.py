# *************************************** #
#  Michele Reynolds                       #
#  IT-140 - J6840  	                      #
#  2-3 Assignment: PyCharm Introduction   #
#  July 1, 2023                           #
#  Practice Using Pycharm for scripting   #
# *************************************** #

# import date and time type to perform calculation
import datetime

# Prompt the user for their name and store the value in var_name
var_name = input("What is your name? ")

# Prompt the user for their age and store the value in age
age = int(input("How old are you?"))

# Get the current date
current_date = datetime.date.today()

# calculate year of birth
curr_year = datetime.date.today().year
birth_year = curr_year - age

# Check if the user's birthday has occurred this year
if current_date.month < 12 or (current_date.month == 12 and current_date.day < 31):
    birth_year -= 1

# Greet person with their name and year of birth
print("Hello " + var_name + "!" + " You were born in " + str(birth_year) + ".")
