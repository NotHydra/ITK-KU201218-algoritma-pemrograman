from os import system
from math import pi


def clear():
    system("cls")


programIsRunning = True
while programIsRunning:
    try:
        print("======Tube Surface Area Program======")
        radius = float(input("Insert Radius: "))
        height = float(input("Insert Height: "))
        surfaceArea = 2 * pi * radius * (radius + height)
        print(f"Surface Area: {surfaceArea}")
        print("=====================================")

    except:
        print("=====================================")
        print("Input Needs To Be A Number")
        print("=====================================")

    optionIsValid = False
    while not optionIsValid:
        option = input("Calculate Again? (Y/N): ")
        if option == "Y":
            optionIsValid = True
            clear()

        elif option == "N":
            print("=====================================")
            print("Thank You For Using Our Program")
            print("=====================================")

            programIsRunning = False
            optionIsValid = True

        else:
            print("=====================================")
            print("Input Not Valid")
            print("=====================================")


input()
