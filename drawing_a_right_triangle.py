# ****************************** #
#  Michele Reynolds             #
#  IT-140 - J6840  	            #
#  Drawing a Right Triangle     #
#  July 15, 2023                #
#  Output fixed height triangle #
# ****************************** #

# variable to hold character input
triangle_char = input('Enter a character:\n')

# variable to hold height input
triangle_height = int(input('Enter triangle height:\n'))

# print empty space
print('')

# loop that iterates triangle_height
# the number of times entered plus one
for i in range(1, triangle_height + 1):
    # print triangle repeated i times
    print(" ".join(triangle_char * i) + " ")
