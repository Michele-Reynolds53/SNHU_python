# NOTE: The following statement converts the input into a list container
# Write an expression to print each price in stock_prices.

stock_prices = input().split()

for price in stock_prices:
    print('$', price)