def split_check(amount=50, num_people=4, tax_percentage=0.095, tip_percentage=0.18):
    tax_amount = amount * tax_percentage
    tip_amount = amount * tip_percentage
    total_amount = amount + tax_amount + tip_amount
    per_person_amount = total_amount / num_people
    return per_person_amount


# Correct way to call the function and print the result
result = split_check(amount=50, num_people=4)
print(result)
