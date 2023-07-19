age = int(input())
weight = float(input())
heart_rate = float(input())
time = int(input())

# Calculate calories burned per minute
calories = ((age * 0.2757) + (weight * 0.03295) + (heart_rate * 1.0781) - 75.4991) * time / 8.368


print('Calories: {:.2f} calories'.format(calories))
