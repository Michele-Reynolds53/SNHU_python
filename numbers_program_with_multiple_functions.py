size = 5


def get_numbers(num):
    numbers = []
    user_input = input('Enter {} integers:\n'.format(num))

    i = 0
    for token in user_input.split():
        number = int(token)     # Convert string input into integer
        numbers.append(number)  # Add to numbers list

        print(i, number)
        i += 1

    return numbers


def print_all_numbers(numbers):
    print('Numbers:', *numbers)


def print_odd_numbers(numbers):
    odd_numbers = [num for num in numbers if num % 2 != 0]
    print('Odd numbers: ', *odd_numbers)


def print_negative_numbers(numbers):
    negative_numbers = [num for num in numbers if num < 0]
    print('Negative numbers:', *negative_numbers)


nums = get_numbers(size)
print_all_numbers(nums)
print_odd_numbers(nums)
print_negative_numbers(nums)
