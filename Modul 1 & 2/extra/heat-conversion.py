from os import system


class Dependency:
    heatArray = [
        {"id": 1, "type": "Celsius"},
        {"id": 2, "type": "Fahrenheit"},
        {"id": 3, "type": "Kelvin"},
        {"id": 4, "type": "Reamur"},
    ]

    textLength = 50
    textFill = "="


class Utility:
    def clear() -> None:
        system("cls")

    def printFormat(text: str = "") -> None:
        print(text.center(Dependency.textLength, Dependency.textFill))


class Heat:
    class Celsius:
        def fahrenheit(heat: float) -> float:
            return (heat * (9 / 5)) + 32

        def kelvin(heat: float) -> float:
            return heat + 273.15

        def reamur(heat: float) -> float:
            return heat * (4 / 5)

    class Fahrenheit:
        def celsius(heat: float) -> float:
            return (heat - 32) * (5 / 9)

        def kelvin(heat: float) -> float:
            return (heat - 32) * (5 / 9) + 273.15

        def reamur(heat: float) -> float:
            return (heat - 32) * (4 / 9)

    class Kelvin:
        def celsius(heat: float) -> float:
            return heat - 273.15

        def fahrenheit(heat: float) -> float:
            return (heat - 273.15) * (9 / 5) + 32

        def reamur(heat: float) -> float:
            return (heat - 273.15) * (4 / 5)

    class Reamur:
        def celsius(heat: float) -> float:
            return heat * (5 / 4)

        def fahrenheit(heat: float) -> float:
            return heat * (9 / 4) + 32

        def kelvin(heat: float) -> float:
            return heat * (5 / 4) + 273.15


class Program:
    heatInputType = ""
    heatOutputType = ""

    def heatInput() -> int:
        print("Choose Heat Input")
        Utility.printFormat()

        for heatIndex, heatObject in enumerate(Dependency.heatArray):
            print(f"{heatIndex + 1}. {heatObject['type']}")

        Utility.printFormat()

        optionHeatInput = int(input("Heat Input Option: "))
        if optionHeatInput > len(Dependency.heatArray):
            raise Exception()

        Program.heatInputType = Dependency.heatArray[optionHeatInput - 1]["type"][0]

        Utility.printFormat()

        return optionHeatInput

    def heatOutput(heatInput: int) -> int:
        print("Choose Heat Output")
        Utility.printFormat()

        heatOuputArray = []
        for heatIndex, heatObject in enumerate(Dependency.heatArray):
            if (heatIndex + 1) != heatInput:
                heatOuputArray.append(heatObject)

        for heatIndex, heatObject in enumerate(heatOuputArray):
            print(f"{heatIndex + 1}. {heatObject['type']}")

        Utility.printFormat()

        optionHeatOutput = int(input("Heat Output Option: "))
        if optionHeatOutput > len(heatOuputArray):
            raise Exception()

        Program.heatOutputType = heatOuputArray[optionHeatOutput - 1]["type"][0]
        Utility.printFormat()

        return optionHeatOutput

    def convert(heatInput: int, heatOutput: int, heat: float):
        if heatInput == 1:
            if heatOutput == 1:
                result = Heat.Celsius.fahrenheit(heat)

            elif heatOutput == 2:
                result = Heat.Celsius.kelvin(heat)

            elif heatOutput == 3:
                result = Heat.Celsius.reamur(heat)

        elif heatInput == 2:
            if heatOutput == 1:
                result = Heat.Fahrenheit.celsius(heat)

            elif heatOutput == 2:
                result = Heat.Fahrenheit.kelvin(heat)

            elif heatOutput == 3:
                result = Heat.Fahrenheit.reamur(heat)

        elif heatInput == 3:
            if heatOutput == 1:
                result = Heat.Kelvin.celsius(heat)

            elif heatOutput == 2:
                result = Heat.Kelvin.fahrenheit(heat)

            elif heatOutput == 3:
                result = Heat.Kelvin.reamur(heat)

        elif heatInput == 4:
            if heatOutput == 1:
                result = Heat.Reamur.celsius(heat)

            elif heatOutput == 2:
                result = Heat.Reamur.fahrenheit(heat)

            elif heatOutput == 3:
                result = Heat.Reamur.kelvin(heat)

        else:
            result = 0

        return result

    def main() -> None:
        programIsRunning = True
        while programIsRunning:
            try:
                Utility.printFormat("Heat Conversion")

                heatInput = Program.heatInput()
                result = Program.convert(
                    heatInput,
                    Program.heatOutput(heatInput),
                    float(input(f"Insert Heat ({Program.heatInputType}): ")),
                )

                Utility.printFormat()
                print(f"Converted Heat ({Program.heatOutputType}): {result}")
                Utility.printFormat()

            except:
                Utility.printFormat()
                print("Input Not Valid")
                Utility.printFormat()

            optionIsValid = False
            while not optionIsValid:
                option = input("Convert Again? (Y/N): ")
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
