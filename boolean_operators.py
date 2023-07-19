# Detect specific values

special_num = int(input())

if special_num == -99 or special_num == 0 or special_num == 44:
    print('Special number')
else:
    print('Not special number')

# Combining test conditions

user_age = int(input())

if user_age > 17 and user_age != 25:
    print('Eligible')
else:
    print('Ineligible')

# Branching using Boolean variables

young = (input() == 'True')
famous = (input() == 'True')

if young and famous:
    print('You must be rich!')
else:
    print('There is always the lottery...')

# Detect specific values.

special_list = [-99, 0, 44]
special_num = int(input())

if special_num in special_list:
    print('Special number')
else:
    print('Not special number')


