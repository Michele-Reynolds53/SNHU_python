# ***********************************************************  #
#  Michele Reynolds                                            #
#  IT-140 - J6840  	                                           #
#  Mad Lib Loops                                               #
#  July 16, 2023                                              #
#  Create short story with input break if input is quit and 0  #
# ************************************************************ #

 # starting at 0, iterate through input
counter = 0
items = []
numbers = []

# check conditions - add input to sentences and move to next input, quit if conditions are quit and 0

while True:

    line = input()
    input_list = line.split()
    item = input_list[0]
    number = input_list[1]

    if item == "quit":
        break

    items.append(item)
    numbers.append(number)
    counter += 1

# iterate through each entry and print
for i in range(counter):
    print(f"Eating {numbers[i]} {items[i]} a day keeps the doctor away.")
