num_sales = 7
if num_sales == 0:
    employee_bonus = 0
elif num_sales == 1:
    employee_bonus = 2
elif num_sales == 2:
    employee_bonus = 5
else:
    employee_bonus = 10
print(employee_bonus)


year = int(input())
# If year is 2101 or later, print "Distant future" (without quotes).
if year >= 2101:
    print("Distant Future")
# Otherwise, if year is 2001 or greater, print "21st century".
elif year >= 2001:
    print("21st Century")
# Otherwise, if year is 1901 or greater, print "20th century".
elif year >= 1901:
    print("20th Century")
# Else (1900 or earlier), print "Long ago".
else:
    print("Long ago")

