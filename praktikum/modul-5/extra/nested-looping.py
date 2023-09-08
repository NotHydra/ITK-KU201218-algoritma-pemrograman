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
    def nestedLooping(number) -> None:
        Utility.printFormat("A", textFill="-")
        Utility.printFormat()

        print()
        for i in range(number, 0, -1):
            for j in range(i):
                print("x", end="")

            print()

        print()

        Utility.printFormat()
        Utility.printFormat("B", textFill="-")
        Utility.printFormat()

        print()
        for i in range(number, 0, -1):
            if i % 2 == 1:
                for j in range(i):
                    print("x", end="")

            else:
                for j in range(i):
                    print("-", end="")

            print()

        print()

        Utility.printFormat()
        Utility.printFormat("C", textFill="-")
        Utility.printFormat()

        print()
        for i in range(1, number + 1):
            for j in range(1, i + 1):
                print(j, end="")

            print()

        for i in range(number - 1, 0, -1):
            for j in range(1, i + 1):
                print(j, end="")

            print()

        print()

        Utility.printFormat()
        Utility.printFormat("D", textFill="-")
        Utility.printFormat()

        print()
        for i in range(1, number + 1):
            for j in range(i):
                print("x", end="")

            print()

        for i in range(number - 1, 0, -1):
            for j in range(i):
                print("x", end="")

            print()

        print()

        Utility.printFormat()
        Utility.printFormat("E", textFill="-")
        Utility.printFormat()

        print()
        for i in range(number, 0, -1):
            for j in range(i - 1):
                print(". ", end="")

            print(i)

        print()

    def main() -> None:
        programIsRunning = True
        while programIsRunning:
            try:
                Utility.printFormat()
                Utility.printFormat("Nested Looping", textFill="-")
                Utility.printFormat()

                number = int(input("Number: "))

                Utility.printFormat()
                Program.nestedLooping(number)
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
