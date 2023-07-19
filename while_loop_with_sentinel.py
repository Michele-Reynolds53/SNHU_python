
entered_age = int(input())

while (entered_age < 16 or entered_age > 35):
    if entered_age < 16:
        print('Too young')
    else:
         print('Already adult')
    entered_age = int(input())

print('Perfect fit', end='')