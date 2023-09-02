from os import system
from math import pi, sqrt


class Dependency:
    textLength = 50
    textFill = "="


class Utility:
    def clear() -> None:
        system("cls")

    def printFormat(text: str = "") -> None:
        print(text.center(Dependency.textLength, Dependency.textFill))


class Shape:
    class Cube:
        def volume() -> float:
            return float(input("Length: ")) ** 3

        def surfaceArea() -> float:
            return 6 * (float(input("Length: ")) ** 2)

    class Cuboid:
        def volume() -> float:
            return (
                float(input("Length: "))
                * float(input("Width: "))
                * float(input("Height: "))
            )

        def surfaceArea() -> float:
            length = float(input("Length: "))
            width = float(input("Width: "))
            height = float(input("Height: "))

            return 2 * (length * width + length * height + width * height)

    class Sphere:
        def volume() -> float:
            return (4 / 3) * pi * (float(input("Radius: ")) ** 3)

        def surfaceArea() -> float:
            return 4 * pi * (float(input("Radius: ")) ** 2)

    class Cylinder:
        def volume() -> float:
            return pi * (float(input("Radius: ")) ** 2) * float(input("Height: "))

        def surfaceArea() -> float:
            radius = float(input("Radius: "))
            return 2 * pi * radius * (radius + float(input("Height: ")))

    class Cone:
        def volume() -> float:
            return (
                (1 / 3)
                * pi
                * (float(input("Radius: ")) ** 2)
                * float(input("Height: "))
            )

        def surfaceArea() -> float:
            radius = float(input("Radius: "))
            return (
                pi
                * radius
                * (radius + (sqrt(radius**2 + float(input("Height: ")) ** 2)))
            )


class Program:
    def shape() -> int:
        print("Choose A Shape")
        Utility.printFormat()
        print("1. Cube")
        print("2. Cuboid")
        print("3. Sphere")
        print("4. Cylinder")
        print("5. Cone")
        Utility.printFormat()

        optionShape = int(input("Shape Option: "))
        if optionShape >= 6:
            raise Exception()

        Utility.printFormat()

        return optionShape

    def formula() -> int:
        print("Choose A Formula")
        Utility.printFormat()
        print("1. Volume")
        print("2. Surface Area")
        Utility.printFormat()

        optionFormula = int(input("Formula Option: "))
        if optionFormula >= 3:
            raise Exception()

        Utility.printFormat()

        return optionFormula

    def calculate(shape, formula) -> float:
        if shape == 1:
            if formula == 1:
                result = Shape.Cube.volume()

            elif formula == 2:
                result = Shape.Cube.surfaceArea()

        elif shape == 2:
            if formula == 1:
                result = Shape.Cuboid.volume()

            elif formula == 2:
                result = Shape.Cuboid.surfaceArea()

        elif shape == 3:
            if formula == 1:
                result = Shape.Sphere.volume()

            elif formula == 2:
                result = Shape.Sphere.surfaceArea()

        elif shape == 4:
            if formula == 1:
                result = Shape.Cylinder.volume()

            elif formula == 2:
                result = Shape.Cylinder.surfaceArea()

        elif shape == 5:
            if formula == 1:
                result = Shape.Cone.volume()

            elif formula == 2:
                result = Shape.Cone.surfaceArea()

        else:
            result = 0

        return result

    def main() -> None:
        programIsRunning = True
        while programIsRunning:
            try:
                Utility.printFormat("3D Shapes Calculator")

                result = Program.calculate(Program.shape(), Program.formula())

                Utility.printFormat()
                print(f"Result: {result}")
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
