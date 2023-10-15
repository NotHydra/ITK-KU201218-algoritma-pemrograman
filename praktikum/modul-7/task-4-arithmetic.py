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
    programIsRunning = True
    optionIsValid = False

    def arithmetic(textArray: list[str]):
        if textArray[0] == "WHAT" and textArray[1] == "IS" and textArray[-1] == "?":
            if (
                textArray[3] in ["ADDED", "SUBTRACTED", "MULTIPLIED", "DIVIDED"]
                and textArray[4] == "BY"
            ):
                firstNumber = int(textArray[2])
                operator = textArray[3]
                secondNumber = int(textArray[5])

                if operator == "ADDED":
                    return firstNumber + secondNumber

                elif operator == "SUBTRACTED":
                    return firstNumber - secondNumber

                elif operator == "MULTIPLIED":
                    return firstNumber * secondNumber

                elif operator == "DIVIDED":
                    return firstNumber / secondNumber

                else:
                    raise Exception()

            else:
                raise Exception()

        elif textArray[0] == "DONE":
            Program.programIsRunning = False
            Program.optionIsValid = True

        else:
            raise Exception()

    def main() -> None:
        while Program.programIsRunning:
            try:
                Utility.printFormat()
                Utility.printFormat("Arithmetic", textFill="-")
                Utility.printFormat()

                result = Program.arithmetic(
                    input("Enter An Arithmethic Text: ").upper().split(" ")
                )

                if not Program.programIsRunning and Program.optionIsValid:
                    Utility.printFormat()
                    Utility.printFormat("Thank You For Using Our Program", textFill="-")
                    Utility.printFormat()

                    break

                else:
                    Utility.printFormat()
                    Utility.printFormat("Result", textFill="-")
                    Utility.printFormat()
                    print(result)
                    Utility.printFormat()

            except:
                Utility.printFormat()
                print("Input Not Valid")
                Utility.printFormat()

            Program.optionIsValid = False
            while not Program.optionIsValid:
                option = input("Try Again? (Y/N): ").upper()
                if option == "Y":
                    Program.optionIsValid = True
                    Utility.clear()

                elif option == "N":
                    Utility.printFormat()
                    Utility.printFormat("Thank You For Using Our Program", textFill="-")
                    Utility.printFormat()

                    Program.programIsRunning = False
                    Program.optionIsValid = True

                else:
                    Utility.printFormat()
                    print("Input Not Valid")
                    Utility.printFormat()

        input()


Program.main()
