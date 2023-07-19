#******************************#
#  Michele Reynolds            #
#  IT-140 - J6840  	           #
#  Lab 2.13.1 Count Characters #
#  July 3, 2023                #
#  Count Character in string   #
#******************************#

# enter string, character index and phrase index
user_string = input()
character=user_string[0]
phrase=user_string[1:]
count=0

# check for a specific character and if exists count the number of occurrences
for i in phrase:
    if i == character:
        count = count+1

# print the count of characters whether it is 0 or above 0
if count != 1:
    print(str(count))
else:
    print(str(count))
