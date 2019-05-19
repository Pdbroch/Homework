import time
repeat = "y"

print("Hello, and welcome. Let's play a little game shall we?")
with open("playthrough.txt", "r") as play_file:
    plays = int(play_file.read())


while True:
    if repeat == "n" or repeat == "no":
        break
    plays += 1
    with open("playthrough.txt", "w") as play_file:
        play_file.write(str(plays))
        print("You have played this game " + str(plays) + " times!")
    number = int(input("Pick a number between 1 and 100: "))


    while True:
        if number > 100:
            number = int(input("The number you picked is too high, please pick one between 1 and 100: "))
        elif number < 1:
            number = int(input("The number you picked is too low, please pick one between 1 and 100: "))
        else:
            break

    for x in range(1,number+1):
        time.sleep(0.25)
        if x % 3 == 0 and x % 5 == 0:
            print("fizzbuzz")
        elif x % 3 == 0:
            print("fizz")
        elif x % 5 == 0:
            print("buzz")
        else:
            print(x)

    while True:
        if repeat == "n" or repeat == "no":
            break
        repeat = raw_input("Wanna play again? [y/n]: ")
        repeat =  repeat.lower()
        if repeat == "y" or repeat == "yes":
            print("YAY!")
            break
        elif repeat == "n" or repeat == "no":
            print("Aww... okay")
            break
        else:
            print("Invalid input.")