# ****************************************************** #
#  Michele Reynolds                                      #
#  IT-140 - J6840  	                                     #
#  2-3 Assignment: PyCharm Introduction, 2nd submission  #
#  July 14, 2023                                         #
#  Practice Using Pycharm for scripting                  #
# ****************************************************** #

# import date and time type to perform calculation
import datetime

# Prompt the user for their name and store the value in var_name
var_name = input("What is your name? ")

# Prompt the user for their age and store the value in age
age = int(input("How old are you? "))

# Create variable to hold birth year
birth_year = ""

# calculate current year
curr_year = datetime.date.today().year

# Has birthday passed? TRUE or FALSE
birthday_passed = input("Has your birthday already occurred this year? Answer True or False. ")

# Verify whether user's birthday has occurred this year
if birthday_passed == "True":
    birth_year = curr_year - age
else:
    if birthday_passed == "False":
        birth_year = (datetime.date.today().year - 1) - age

# Greet person with their name and year of birth
print("Hello " + var_name + "!" + " You were born in " + str(birth_year) + ".")
