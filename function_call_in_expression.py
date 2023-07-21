# Assign max_sum with the greater of num_a and num_b, PLUS the greater of num_y and num_z.
# Use just one statement. Hint: Call find_max() twice in an expression.

def find_max(num_1, num_2):
    max_val = 0.0

    if num_1 > num_2:  # if num1 is greater than num2,
        max_val = num_1   # then num1 is the maxVal.
    else:                # Otherwise,
        max_val = num_2   # num2 is the maxVal

    return max_val


num_a = float(input())
num_b = float(input())
num_y = float(input())
num_z = float(input())

max_1 = find_max(num_a, num_b)
max_2 = find_max(num_y, num_z)

max_sum = max_1 + max_2
print("Max sum is:", max_sum)
