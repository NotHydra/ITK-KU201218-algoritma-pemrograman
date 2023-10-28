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
    def checkPrime(number: int) -> bool:
        if number == 1:
            return False

        else:
            for i in range(2, number):
                if number % i == 0:
                    return False

            else:
                return True

    def main() -> None:
        programIsRunning = True
        while programIsRunning:
            try:
                Utility.printFormat()
                Utility.printFormat("Prime Checker", textFill="-")
                Utility.printFormat()

                number = int(input("Enter A Number: "))

                Utility.printFormat()
                Utility.printFormat("Result", textFill="-")
                Utility.printFormat()

                print(
                    f"{number} Is A Prime Number"
                    if Program.checkPrime(number)
                    else f"{number} Is Not A Prime Number"
                )

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