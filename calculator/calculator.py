repeat = "y"

with open("calculator.txt", "r") as file:
    count = int(file.read())
print("This calculator has been used to make " + str(count) + " calculations!")


while True:
    if repeat == "n" or repeat == "no":
        with open("calculator.txt", "w") as file:
            file.write(str(count))
        break
    count += 1
    x = raw_input("Please pick the first number: ")
    x = float(x.replace(",","."))
    y = raw_input("Please pick the second number: ")
    y = float(y.replace(",", "."))
    operation = raw_input("Pick the maths operation (+, -, *, /): ")

    if operation == "+":
        print(x+y)
    elif operation == "-":
        print(x-y)
    elif operation == "*":
        print(x*y)
    elif operation == "/":
        print(x/y)
    else:
        print("Error, operation invalid")
    while True:
        repeat = raw_input("Would you like to do another calculation? [y/n]: ")
        repeat = repeat.lower()
        if repeat == "y" or repeat == "yes":
            print("You have chosen to do another calculation.")
            break
        elif repeat == "n" or repeat == "no":
            print("You have chosen not to do another calculation. Shutting down.")
            break
        else:
            print("Invalid input.")
