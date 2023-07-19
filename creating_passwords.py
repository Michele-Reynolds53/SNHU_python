# Output all the values on a single line
favorite_color = input()
flower_name = input()
number_value = int(input())
print("You entered: " + favorite_color + " " + flower_name + " " + str(number_value))
print()
# first password option
password1 = favorite_color + "_" + flower_name
print("First password: " "" + password1)
# second password option
password2 = str(number_value) + favorite_color + str(number_value)
print("Second password: " "" + password2)
print()
password1_length = len(password1)
password2_length = len(password2)
print("Number of characters in " + password1 + ":" + " " + str(password1_length))
print("Number of characters in " + password2 + ":" + " " + str(password2_length))