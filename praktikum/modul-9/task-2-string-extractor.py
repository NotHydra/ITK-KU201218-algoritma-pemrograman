from os import system

from string import ascii_letters, digits, punctuation


class Dependency:
    textLength = 50
    textFill = "="


class Utility:
    def clear() -> None:
        system("cls")

    def printFormat(text: str = "", textFill=Dependency.textFill) -> None:
        print(text.center(Dependency.textLength, textFill))


class Program:
    def extract(text: str) -> list[str]:
        letterArray = []
        digitArray = []
        symbolArray = []
        for char in text:
            if char in ascii_letters:
                letterArray.append(char)

            elif char in digits:
                digitArray.append(char)

            elif char in punctuation:
                symbolArray.append(char)

        return ["".join(letterArray), "".join(digitArray), "".join(symbolArray)]

    def main() -> None:
        programIsRunning = True
        while programIsRunning:
            try:
                Utility.printFormat()
                Utility.printFormat("String Extractor", textFill="-")
                Utility.printFormat()

                text = input("Enter A Text: ")

                Utility.printFormat()
                Utility.printFormat("Result", textFill="-")
                Utility.printFormat()

                for extractedIndex, extractedObject in enumerate(Program.extract(text)):
                    print(f"{extractedIndex  + 1}. {extractedObject}")

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
