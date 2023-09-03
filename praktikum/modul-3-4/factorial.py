from os import system


class Dependency:
    textLength = 50
    textFill = "="


class Utility:
    def clear() -> None:
        system("cls")

    def printFormat(text: str = "") -> None:
        print(text.center(Dependency.textLength, Dependency.textFill))


class Program:
    def factorial(number) -> None:
        print(f"{number}! = {number}", end="")

        total = number
        for index in range((number - 1), 0, -1):
            total = total * index

            print(f" x {index}", end="")

        print(f" = {total}")

    def main() -> None:
        programIsRunning = True
        while programIsRunning:
            try:
                Utility.printFormat("Factorial")

                number = int(input("Number: "))

                Utility.printFormat()
                Program.factorial(number)
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
