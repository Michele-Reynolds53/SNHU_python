user_int = int(input('Enter a number (32 - 126):\n '))
print(user_int)
decimal = float(input('Enter a number with a decimal:\n'))
print(decimal)
character = input('Enter a character:\n ')
print(character)
string = input('Enter a string:\n')
print(string)

print(user_int, decimal, character, string, end='\n')

# Output the four values in reverse
print(string, character, decimal, user_int)

# Convert the integer to a character, and output that character
user_int = chr(user_int)
print("99 converted to a character is " + user_int)


