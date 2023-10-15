from os import system


class Dependency:
    textLength = 50
    textFill = "="


class Utility:
    def clear() -> None:
        system("cls")

    def printFormat(text: str = "", textFill=Dependency.textFill) -> None:
        print(text.center(Dependency.textLength, textFill))


class Program:
    def factorial(number):
        if number > 1:
            return number * Program.factorial(number - 1)

        else:
            return number

    def main() -> None:
        programIsRunning = True
        while programIsRunning:
            try:
                Utility.printFormat()
                Utility.printFormat("Factorial", textFill="-")
                Utility.printFormat()

                number = int(input("Enter A Number: "))

                Utility.printFormat()
                Utility.printFormat("Result", textFill="-")
                Utility.printFormat()

                print(number, end="")
                for i in range(number - 1, 0, -1):
                    print(f" x {i}", end="")

                print(f" = {Program.factorial(number)}")

                Utility.printFormat()

            except:
                Utility.printFormat()
                print("Input Not Valid")
                Utility.printFormat()

            optionIsValid = False
            while not optionIsValid:
                option = input("Try Again? (Y/N): ").upper()
                if option == "Y":
                    optionIsValid = True
                    Utility.clear()

                elif option == "N":
                    Utility.printFormat()
                    Utility.printFormat("Thank You For Using Our Program", textFill="-")
                    Utility.printFormat()

                    programIsRunning = False
                    optionIsValid = True

                else:
                    Utility.printFormat()
                    print("Input Not Valid")
                    Utility.printFormat()

        input()


Program.main()
