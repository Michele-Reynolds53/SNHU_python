# *******************************  #
#  Michele Reynolds                #
#  IT-140 - J6840  	               #
#  Password modifier               #
#  June 27, 2023                   #
#  Replace characters and append   #
# *******************************  #

word = input()
s = str("q*s")

# replace characters
password = word.replace("i", "!").replace("a", "@")\
    .replace("m", "M").replace("B", "8").replace("o", ".")

# append output
password += s

# print output
print(password)
