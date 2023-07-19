# ********************  #
#  Michele Reynolds     #
#  IT-140 - J6840       #
#  Lab 2.12 Name Format #
#  July 3, 2023         #
#  Formatting Names     #
# ********************  #

your_name = input()
broken_name = your_name.split()
if len(broken_name) == 3:
    first_name = broken_name[0]
    middle_name = broken_name[1]
    last_name = broken_name[2]

    first_in = first_name[0]
    middle_in = middle_name[0]
    print(last_name + ', ', first_in + '.' + middle_in + '.')

else:
    if len(broken_name) == 2:
        first_name = broken_name[0]
        last_name = broken_name[1]
        first_in = first_name[0]
        print(last_name + ', ', first_in + '.')
