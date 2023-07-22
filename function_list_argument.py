# Swap function
def swap(values_list):
    size = len(values_list)

    # Swapping
    temp = values_list[0]
    values_list[0] = values_list[size - 1]
    values_list[size - 1] = temp

    return values_list


# Program receives comma-separated values like 5,4,12,19
values_list = input().split(',')
swap(values_list)

print(values_list)