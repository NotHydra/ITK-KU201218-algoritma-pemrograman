from os import system


def clear():
    system("cls")


programIsRunning = True
while programIsRunning:
    try:
        print("======Celsius To Fahrenheit Program======")
        heat = float(input("Insert Heat (C): "))
        fahrenheit = (heat * 9 / 5) + 32
        print(f"Fahrenheit: {fahrenheit}")
        print("=========================================")

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
