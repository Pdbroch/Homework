import json


print("Hello and welcome! This program converts kilometers into miles.")
repeat = "y"

variables_strings = {}
with open("converter.txt", "r") as file:
    for line in file:
        variables_strings = eval(open("converter.txt").read())
    print("This program has made " + str(variables_strings["conversions"]) + " previous conversions. The longest distance was " + str(variables_strings["largest"]) + "km, while the shortest was " + str(variables_strings["smallest"]) + "km.")


while True:
    if repeat == "n" or repeat == "no":
        with open("converter.txt", "w") as file:
            file.write(json.dumps(variables_strings))
        break
    km = raw_input("Please enter the distance in kilometers you'd like converted (Numbers only): ")
    km = float(km.replace(",","."))
    miles = km * 0.62137199
    print("The distance of " + str(km) + "km is " + str(miles) + " miles")
    variables_strings["conversions"] += 1
    if km > variables_strings["largest"]:
        variables_strings["largest"] = km
    if km < variables_strings["smallest"]:
        variables_strings["smallest"] = km
    while True:
        repeat = raw_input("Would you like to do another conversion? [y/n]: ")
        repeat = str(repeat.lower())
        if repeat == "n" or repeat == "no":
            print("You have chosen to not do another conversion. The program will now end. Have a nice day!")
            break
        elif repeat == "y" or repeat == "yes":
            print("You have chosen to do another conversion.")
            break
        else:
            print("Invalid input")