from os import system


def clear():
    system("cls")


programIsRunning = True
while programIsRunning:
    try:
        print("========Salary Program========")
        salaryPerHour = float(input("Salary Per Hour ($): "))
        salary5Days = salaryPerHour * 8 * 5
        salary7Days = salaryPerHour * 8 * 7
        print(f"Total Salary (5 Days): ${salary5Days}")
        print(f"Total Salary (7 Days): ${salary7Days}")
        print("==============================")

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
