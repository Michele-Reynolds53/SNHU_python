# Given num_rows and num_cols, print a list of all seats in a theater.
# Rows are numbered, columns lettered, as in 1A or 3E.
# Print a space after each seat.

num_rows = int(input())
num_cols = int(input())

# Note 1: You will need to declare more variables
# Note 2: Place end=' ' at the end of your print statement to separate seats by spaces

seats = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')

for i in range(num_rows):
    for j in range(num_cols):
        print('{}{}' .format(i+1, seats[j]), end=' ')
    print()

