# ************************************************** #
#  Michele Reynolds                                  #
#  IT-140 - J6840  	                                 #
#  3.11 LAB: Smallest number                         #
#  July 6, 2023                                      #
#  Find the smallest number out of three variables   #
# ************************************************** #

# Create three variables to input integers
x = (int(input()))
y = (int(input()))
z = (int(input()))

# Checking to see if first variable is smaller than the other two variables and print
if x <= y and x <= z:
    print(x)
# Checking to see if second variable is smaller than the other two variables and print
elif y <= x and y <= z:
    print(y)
# Checking to see if third variable is smaller than the other two variables and print
elif z <= x and z <= y:
    print(z)
# if all values are equal, print the first value
else:
    print(x)
