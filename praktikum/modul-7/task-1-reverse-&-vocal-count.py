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
    def reverse(text: str) -> str:
        return text[::-1]

    def vocalCount(text: str) -> int:
        count = 0
        for char in text:
            if char.upper() in "AIUEO":
                count += 1

        return count

    def main() -> None:
        programIsRunning = True
        while programIsRunning:
            try:
                Utility.printFormat()
                Utility.printFormat("Reverse & Vocal Count", textFill="-")
                Utility.printFormat()

                text = input("Enter A Text: ")

                Utility.printFormat()
                Utility.printFormat("Result", textFill="-")
                Utility.printFormat()

                print(f"Reverse: {Program.reverse(text)}")
                print(f"Vocal Count: {Program.vocalCount(text)}")

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
