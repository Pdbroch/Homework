import json

mood_dict = {}
with open("mood_count.txt", "r") as file:
    for line in file:
        mood_dict = eval(open("mood_count.txt").read())

repeat = "y"
while True:
    if repeat == "n" or repeat == "no":
        break
    mood = raw_input("What is your mood today? ")
    if mood == "happy":
        mood_dict["happy"] +=1
        print("Great to see you happy! You have been happy " + str(mood_dict["happy"]) + " times!")
    elif mood == "nervous":
        mood_dict["nervous"] += 1
        print("Take three deep breathes! You have been nervous " + str(mood_dict["nervous"]) + " times!")
    elif mood == "sad":
        mood_dict["sad"] += 1
        print("Cheer up, it will be a great day! You have been sad " + str(mood_dict["sad"]) + " times!")
    elif mood == "excited":
        mood_dict["excited"] += 1
        print("I'm getting excited just watching you! You have been excited " + str(mood_dict["excited"]) + " times!")
    elif mood == "relaxed":
        mood_dict["relaxed"] += 1
        print("What a chill start to the day. You have been relaxed " + str(mood_dict["relaxed"]) + " times!")
    else:
        print("I don't recognize this mood.")
    while True:
        repeat = raw_input("Would you like to do another mood check?[y/n]: ")
        repeat = str(repeat.lower())
        if repeat == "n" or repeat == "no":
            print("You have chosen to not do another mood check. Have a wonderful day!")
            with open("mood_count.txt", "w") as file:
                file.write(json.dumps(mood_dict))
            break
        elif repeat == "y" or repeat == "yes":
            print("You have chosen to do another mood check.")
            break
        else:
            print("Invalid input")