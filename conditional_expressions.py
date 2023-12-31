# Print negative or non-negative.

user_val = int(input())

cond_str = "negative" if user_val < 0 else "non-negative"

print(user_val, 'is', cond_str)

# Conditional assignment

num_users = int(input())
update_direction = int(input())

num_users = (num_users+1) if update_direction == 3 else (num_users-1)

print('New value is:', num_users)

# Using a conditional expression, write a statement that increments num_users
# if update_direction is 3, otherwise decrements num_users.
#
# Sample output with inputs: 8 3
# New value is: 9
