from os import system
from random import choices
from string import ascii_letters, digits, punctuation


class Dependency:
    textLength = 50
    textFill = "="


class Utility:
    def clear() -> None:
        system("cls")

    def printFormat(text: str = "") -> None:
        print(text.center(Dependency.textLength, Dependency.textFill))


class Program:
    def main() -> None:
        programIsRunning = True
        while programIsRunning:
            try:
                Utility.printFormat("Password Generator")

                number = int(input("Password Length: "))

                Utility.printFormat()
                print(
                    f"Generated Password: {''.join(choices([*ascii_letters, *digits, *punctuation], k=number))}"
                )
                Utility.printFormat()

            except:
                Utility.printFormat()
                print("Input Not Valid")
                Utility.printFormat()

            optionIsValid = False
            while not optionIsValid:
                option = input("Try Again? (Y/N): ")
                if option.upper() == "Y":
                    optionIsValid = True
                    Utility.clear()

                elif option.upper() == "N":
                    Utility.printFormat()
                    print("Thank You For Using Our Program")
                    Utility.printFormat()

                    programIsRunning = False
                    optionIsValid = True

                else:
                    Utility.printFormat()
                    print("Input Not Valid")
                    Utility.printFormat()

        input()


Program.main()
