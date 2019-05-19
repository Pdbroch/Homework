import random


secret = random.randint(1,25)
attempts = 0

with open("score.txt", "r") as score_file:
    best_score = int(score_file.read())
    print("Current top score: " + str(best_score) + ". Good luck!")

while True:
    guess = int(input("Guess the secret number (Between 1 and 25): "))
    attempts += 1
    if guess == secret:
        print("Congratulations! " + str(guess) + " was correct!")
        if attempts < best_score:
            with open("score.txt", "w") as score_file:
                score_file.write(str(attempts))
        break
    elif guess > secret:
        print("Sorry, " + str(guess) + " was too high.")
    else:
        print("Sorry, " + str(guess) + " was too low.")
