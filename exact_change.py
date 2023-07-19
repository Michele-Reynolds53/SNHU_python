# *************************************************************************** #
#  Michele Reynolds                                                           #
#  IT-140 - J6840  	                                                          #
#  3.13 LAB: Exact Change                                                     #
#  July 6, 2023                                                               #
#  Store integer and output currency type and count                           #
#  ************************************************************************** #

# create variable to store change
coins = int(input())

# Determines if user input is invalid.
if coins <= 0:
    print('No change')

# Floor division // rounds the result down to the nearest whole number
# convert user input to dollars
dollar = coins // 100
# remaining amount after conversion
coins %= 100

# convert user input to quarters
quarter = coins // 25
# remaining amount after conversion
coins %= 25

# convert user input to dimes
dime = coins // 10
# remaining amount after conversion
coins %= 10

# convert input to nickels
nickel = coins // 5
# remaining input after conversion
coins %= 5

penny = coins

# Count change and assign single or plural name
if dollar > 1:
    print(dollar, 'Dollars')
elif dollar == 1:
    print(dollar, 'Dollar')

if quarter > 1:
    print(quarter, 'Quarters')
elif quarter == 1:
    print(quarter, 'Quarter')

if dime > 1:
    print(dime, 'Dimes')
elif dime == 1:
    print(dime, 'Dime')

if nickel > 1:
    print(nickel, 'Nickels')
elif nickel == 1:
    print(nickel, 'Nickel')

if penny > 1:
    print(penny, 'Pennies')
elif penny == 1:
    print(penny, 'Penny')
