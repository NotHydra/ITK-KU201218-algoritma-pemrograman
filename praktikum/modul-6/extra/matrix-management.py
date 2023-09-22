from os import system
from keyboard import is_pressed
from time import sleep


class Dependency:
    textLength = 50
    textFill = "="

    programIsRunning = True

    menuOption = 1
    menuList = [
        {"id": 1, "title": "List"},
        {"id": 2, "title": "Create"},
        {"id": 3, "title": "Delete"},
        {"id": 4, "title": "Update"},
        {"id": 5, "title": "Exit"},
    ]


class Utility:
    def clear() -> None:
        system("cls")

    def printFormat(text: str = "", textFill=Dependency.textFill) -> None:
        print(text.center(Dependency.textLength, textFill))


class Program:
    matrixList = [
        [[1, 2], [3, 4]],
        [[1, 2], [5, 6]],
        [[5, 6], [1, 2]],
        [[1, 2, 3], [4, 5, 6]],
    ]

    def refresh(customMenuList=None, guide=True):
        Utility.clear()

        Utility.printFormat()
        Utility.printFormat("Matrix Management", textFill="-")
        Utility.printFormat()

        if customMenuList == None:
            for menuDict in Dependency.menuList:
                if menuDict["id"] == Dependency.menuOption:
                    print(f"-> {menuDict['title']}")

                else:
                    print(f"   {menuDict['title']}")

            Utility.printFormat()

        elif customMenuList == []:
            pass

        else:
            for customMenuObject in customMenuList:
                print(f"-> {customMenuObject['title']}")

            Utility.printFormat()

        if guide:
            Utility.printFormat("(↑ = up)---(↓ = down)---(→ = interact)", textFill="-")
            Utility.printFormat()

    def back():
        Utility.printFormat("(→ = back)", textFill="-")
        Utility.printFormat()

    def option():
        sleep(0.10)
        while True:
            if is_pressed("up"):
                if Dependency.menuOption > 1:
                    Dependency.menuOption -= 1

                break

            elif is_pressed("down"):
                if Dependency.menuOption < len(Dependency.menuList):
                    Dependency.menuOption += 1

                break

            elif is_pressed("right"):
                if Dependency.menuOption == 1:
                    Program.refresh(customMenuList=[], guide=False)
                    Utility.printFormat("List", textFill="-")
                    Utility.printFormat()

                    if len(Program.matrixList) == 0:
                        print("Empty")

                    else:
                        for matrixIndex, matrixObject in enumerate(Program.matrixList):
                            print(f"{matrixIndex + 1}. {matrixObject}")

                    Utility.printFormat()
                    Program.back()

                    sleep(0.50)
                    while True:
                        if is_pressed("right"):
                            break

                elif Dependency.menuOption == 2:
                    Program.refresh(customMenuList=[], guide=False)
                    Utility.printFormat("Create", textFill="-")
                    Utility.printFormat()

                    try:
                        rowLength = int(input("Row Length: "))
                        if rowLength <= 0:
                            raise Exception()

                        columnLength = int(input("Column Length: "))
                        if columnLength <= 0:
                            raise Exception()

                        Utility.printFormat()
                        Utility.printFormat("Insert Number", textFill="-")
                        Utility.printFormat()

                        rowArray = []
                        for i in range(rowLength):
                            columnArray = []
                            for j in range(columnLength):
                                columnArray.append(int(input(f"[{i + 1}][{j + 1}]: ")))

                            rowArray.append(columnArray)

                        Utility.printFormat()
                        Utility.printFormat("Created Matrix", textFill="-")
                        Utility.printFormat()
                        print(rowArray)

                        Program.matrixList.append(rowArray)

                    except:
                        Utility.printFormat()
                        Utility.printFormat("Input Not Valid", textFill="-")

                    Utility.printFormat()
                    Program.back()

                    sleep(0.50)
                    while True:
                        if is_pressed("right"):
                            break

                elif Dependency.menuOption == 3:
                    Program.refresh(customMenuList=[], guide=False)
                    Utility.printFormat("Delete", textFill="-")
                    Utility.printFormat()

                    if len(Program.matrixList) == 0:
                        print("Empty")

                    else:
                        try:
                            for matrixIndex, matrixObject in enumerate(
                                Program.matrixList
                            ):
                                print(f"{matrixIndex + 1}. {matrixObject}")

                            Utility.printFormat()
                            Utility.printFormat("Choose", textFill="-")
                            Utility.printFormat()

                            listOption = int(input("List: "))
                            if listOption <= 0 or listOption > len(Program.matrixList):
                                raise Exception()

                            Utility.printFormat()
                            Utility.printFormat("Deleted Matrix", textFill="-")
                            Utility.printFormat()
                            print(Program.matrixList[listOption - 1])

                            Program.matrixList.pop(listOption - 1)

                        except:
                            Utility.printFormat()
                            Utility.printFormat("Input Not Valid", textFill="-")

                    Utility.printFormat()
                    Program.back()

                    sleep(0.50)
                    while True:
                        if is_pressed("right"):
                            break

                elif Dependency.menuOption == 4:
                    Program.refresh(customMenuList=[], guide=False)
                    Utility.printFormat("Update", textFill="-")
                    Utility.printFormat()

                    if len(Program.matrixList) == 0:
                        print("Empty")

                    else:
                        try:
                            for matrixIndex, matrixObject in enumerate(
                                Program.matrixList
                            ):
                                print(f"{matrixIndex + 1}. {matrixObject}")

                            Utility.printFormat()
                            Utility.printFormat("Choose", textFill="-")
                            Utility.printFormat()

                            listOption = int(input("List: "))
                            if listOption <= 0 or listOption > len(Program.matrixList):
                                raise Exception()

                            Utility.printFormat()
                            Utility.printFormat("Selected Matrix", textFill="-")
                            Utility.printFormat()

                            selectedMatrix = Program.matrixList[listOption - 1]
                            print(selectedMatrix)

                            Utility.printFormat()
                            Utility.printFormat("Postition", textFill="-")
                            Utility.printFormat()

                            rowPosition = int(input("Row Position: "))
                            if rowPosition <= 0 or rowPosition > len(selectedMatrix):
                                raise Exception()

                            columnPosition = int(input("Column Position: "))
                            if columnPosition <= 0 or columnPosition > len(
                                selectedMatrix[0]
                            ):
                                raise Exception()

                            Utility.printFormat()
                            Utility.printFormat("Selected Element", textFill="-")
                            Utility.printFormat()

                            selectedElement = selectedMatrix[rowPosition - 1][
                                columnPosition - 1
                            ]

                            print(selectedElement)

                            Utility.printFormat()
                            Utility.printFormat("Change Element", textFill="-")
                            Utility.printFormat()

                            Program.matrixList[listOption - 1][rowPosition - 1][
                                columnPosition - 1
                            ] = int(input("Change: "))

                            Utility.printFormat()
                            Utility.printFormat("Updated Matrix", textFill="-")
                            Utility.printFormat()

                            print(Program.matrixList[listOption - 1])

                        except:
                            Utility.printFormat()
                            Utility.printFormat("Input Not Valid", textFill="-")

                        Utility.printFormat()
                        Program.back()

                        sleep(0.50)
                        while True:
                            if is_pressed("right"):
                                break

                elif Dependency.menuOption == 5:
                    Dependency.programIsRunning = False

                break

    def main() -> None:
        try:
            while Dependency.programIsRunning:
                Program.refresh()
                Program.option()

        except:
            pass


Program.main()
