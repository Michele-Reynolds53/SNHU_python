# Write multiple if statements
car_year = int(input())

# If car_year is 1969 or earlier, print "Few safety features."
if car_year <= 1969:
    print("Few safety features.")
# If 1970 or later, print "Probably has seat belts."
if car_year >= 1970:
    print("Probably has seat belts.")
# If 1990 or later, print "Probably has anti-lock brakes."
if car_year >= 1990:
    print("Probably has anti-lock brakes.")
# If 2000 or later, print "Probably has airbags."
if car_year >= 2000:
    print("Probably has airbags.")
