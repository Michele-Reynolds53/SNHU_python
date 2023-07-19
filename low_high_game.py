import random

seedVal = int(input("What seed should be used? "))
random.seed(seedVal)

lower = int(input("What is the lower bound? "))
upper = int(input("What is the upper bound? "))
while lower >= upper:
    print("Lower bound must be less than upper bound.")

    lower = int(input("What is the lower bound? "))
    upper = int(input("What is the upper bound? "))

number = random.randint(lower, upper)

guessing = True
while guessing:
    try:
        guess = int(input("What is your guess? "))

        if guess < number:
            print("Nope, too low.")
        elif guess > number:
            print("Nope, too high.")
        elif guess == number:
            guessing = False
            print("You got it!")

    except ValueError:
        print("Invalid input. Please enter a valid integer guess.")
