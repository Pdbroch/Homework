import random

secret = random.randint(1, 25)
repeat = "y"
attempts = 0

with open("score.txt", "r") as score_file:
    best_score = int(score_file.read())
    print("Current top score: " + str(best_score) + ". Good luck!")

while True:
    if repeat == "n" or repeat == "no":
        break
    guess = int(input("Guess the secret number (Between 1 and 25): "))
    attempts += 1
    if guess == secret:
        print("Congratulations! " + str(guess) + " was correct!")
        if attempts < best_score:
            with open("score.txt", "w") as score_file:
                score_file.write(str(attempts))
        while True:
            repeat = raw_input("Would you like to play again? [y/n]: ")
            repeat = repeat.lower()
            if repeat == "y" or repeat == "yes":
                print("You have chosen to play again.")
                secret = random.randint(1, 25)
                break
            elif repeat == "n" or repeat == "no":
                print("You have chosen not to play again. Shutting down.")
                break
            else:
                print("Invalid input.")
    elif guess > secret:
        print("Sorry, " + str(guess) + " was too high.")
    else:
        print("Sorry, " + str(guess) + " was too low.")
