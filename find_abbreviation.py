user_tweet = input()

if "LOL" in user_tweet:
    user_tweet = user_tweet.replace("LOL", "LOL means laughing out loud")

    print('LOL means laughing out loud.')
else:
    print('No abbreviation.')