# Create a for loop that compares the two strings. For each match, add one point to user_score.
# Upon a mismatch, end the game.

user_score = 0
simon_pattern = input()
user_pattern = input()

for i in simon_pattern:
    if user_pattern[user_score] == simon_pattern[user_score]:
        user_score += 1

print('User score:', user_score)
