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
    def main() -> None:
        programIsRunning = True
        while programIsRunning:
            try:
                Utility.printFormat("Salary Calculator")

                salaryPerHour = float(input("Salary Per Hour ($): "))
                daysOfWorkPerWeek = int(input("Days Of Work Per Week (1-7): "))
                if not (1 <= daysOfWorkPerWeek <= 7):
                    raise Exception()

                salaryPerWeek = salaryPerHour * 8 * daysOfWorkPerWeek

                Utility.printFormat()
                print(
                    f"Total Weekly Salary ({str(daysOfWorkPerWeek) + ' Day' if daysOfWorkPerWeek == 1 else str(daysOfWorkPerWeek) + ' Days'}): ${salaryPerWeek}"
                )
                print(
                    f"Total Montly Salary ({str(daysOfWorkPerWeek * 4) + ' Days'}): ${salaryPerWeek * 4}"
                )
                Utility.printFormat()

            except:
                Utility.printFormat()
                print("Input Not Valid")
                Utility.printFormat()

            optionIsValid = False
            while not optionIsValid:
                option = input("Calculate Again? (Y/N): ")
                if option == "Y":
                    optionIsValid = True
                    Utility.clear()

                elif option == "N":
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
