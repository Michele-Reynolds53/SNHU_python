#  Given positive integer num_insects, write a while loop that prints, then doubles, num_insects each iteration.
#  Print values ≤ 100.
#  Follow each number with a space.

num_insects = int(input())

while num_insects <= 100:
    print(num_insects, end=' ')
    num_insects *= 2
