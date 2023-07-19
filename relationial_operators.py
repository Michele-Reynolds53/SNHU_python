# num_cents is read from input.
# Complete the following to output
# 'Dollar or more' if the value of num_cents is at least a dollar (100 cents is a dollar).

num_cents = int(input())

if num_cents >= 100:
    print('Dollar or more')
else:
    print('Not a dollar')