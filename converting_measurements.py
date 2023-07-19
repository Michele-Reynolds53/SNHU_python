# define function print_total_inches
def print_total_inches(num_feet, num_inches):
    # print statement is the sum of feet times 12 plus the number of inches
    print('Total inches:',  num_feet * 12 + num_inches)


# input feet and inches
feet = int(input())
inches = int(input())

# print defined function with parameters feet and inches
print_total_inches(feet, inches)
