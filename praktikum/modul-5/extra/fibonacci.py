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
    def fibonacci(number) -> None:
        print("1", end="")

        firstValue = 1
        secondValue = 1
        tempValue = 1
        for _ in range(number - 1):
            tempValue = secondValue
            secondValue = firstValue + secondValue
            firstValue = tempValue

            print(f", {firstValue}", end="")

        print()

    def main() -> None:
        programIsRunning = True
        while programIsRunning:
            try:
                Utility.printFormat("Fibonacci")

                number = int(input("Number: "))

                Utility.printFormat()
                Program.fibonacci(number)
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
