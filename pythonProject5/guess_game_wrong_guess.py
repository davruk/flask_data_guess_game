import json
import random
import datetime

secret = random.randint(1, 30)
attempts = 0
wrong_guesses = 0
player_name = input("Please, enter your name: ")

with open("guess_list.txt", "r") as score_file:
    guess_list = json.loads(score_file.read())

while True:
    guess = int(input("Guess the secret number (between 1 and 30): "))
    attempts += 1

    if guess == secret:
        guess_list.append({"player_name": player_name,
                           "attempts": attempts,
                           "secret_number": secret,
                           "wrong_guesses": wrong_guesses,
                           "date": str(datetime.datetime.now())
                           })
        with open("guess_list.txt", "w") as guess_file:
            guess_file.write(json.dumps(guess_list))

            print("You've guessed it - congratulations! It's number" + str(secret))
            print("Attempts needed: " + str(attempts))
            break
    elif guess > secret:
        print("Your guess is not correct... try something smaller")
        wrong_guesses += 1
    elif guess < secret:
        print("Your guess is not correct... try something bigger")
        wrong_guesses += 1
