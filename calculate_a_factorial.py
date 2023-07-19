N = int(input())  # Read user-entered number
total = N
# Initialize the loop variable
i = N -1

while i >= 1:
    # Set total to total * (i)
    total = total * i
    # Decrement i
    i -= 1

print(total)