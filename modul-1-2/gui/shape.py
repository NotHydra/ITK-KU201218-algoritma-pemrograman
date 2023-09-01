import customtkinter

from math import pi, sqrt


class Shape:
    class Two:
        class Square:
            def area(length: float) -> float:
                return length**2

            def perimeter(length: float) -> float:
                return length * 4

        class Rectangle:
            def area(length: float, width: float) -> float:
                return length * width

            def perimeter(length: float, width: float) -> float:
                return 2 * (length + width)

        class Triangle:
            def area(base: float, height: float) -> float:
                return (1 / 2) * base * height

            def perimeter(
                firstLength: float, secondLength: float, thirdLength: float
            ) -> float:
                return firstLength + secondLength + thirdLength

        class Circle:
            def area(radius: float) -> float:
                return pi * radius**2

            def perimeter(radius: float) -> float:
                return 2 * pi * radius

    class Three:
        class Cube:
            def volume(length: float) -> float:
                return length**3

            def surfaceArea(length: float) -> float:
                return 6 * (length**2)

        class Cuboid:
            def volume(length: float, width: float, height: float) -> float:
                return length * width * height

            def surfaceArea(length: float, width: float, height: float) -> float:
                return 2 * (length * width + length * height + width * height)

        class Cone:
            def volume(radius: float, height: float) -> float:
                return (1 / 3) * pi * (radius**2) * height

            def surfaceArea(radius: float, height: float) -> float:
                return pi * radius * (radius + (sqrt(radius**2 + height**2)))

        class Sphere:
            def volume(radius: float) -> float:
                return (4 / 3) * pi * (radius**3)

            def surfaceArea(radius: float) -> float:
                return 4 * pi * (radius**2)

        class Cylinder:
            def volume(radius: float, height: float) -> float:
                return pi * (radius**2) * height

            def surfaceArea(radius: float, height: float) -> float:
                return 2 * pi * radius * (radius + height)


class Depedency:
    ctkAppearance = "dark"
    ctkColorTheme = "dark-blue"

    resolution = {"width": 400, "height": 600}


customtkinter.set_appearance_mode(Depedency.ctkAppearance)
customtkinter.set_default_color_theme(Depedency.ctkColorTheme)


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.shapeArray = {
            "2D": [
                {
                    "id": 1,
                    "name": "Square",
                    "formula": [
                        {
                            "input": [{"id": 1, "name": "length"}],
                            "output": Shape.Two.Square.area,
                        },
                        {
                            "input": [{"id": 1, "name": "length"}],
                            "output": Shape.Two.Square.perimeter,
                        },
                    ],
                },
                {
                    "id": 2,
                    "name": "Rectangle",
                    "formula": [
                        {
                            "input": [
                                {"id": 1, "name": "length"},
                                {"id": 2, "name": "width"},
                            ],
                            "output": Shape.Two.Rectangle.area,
                        },
                        {
                            "input": [
                                {"id": 1, "name": "length"},
                                {"id": 2, "name": "width"},
                            ],
                            "output": Shape.Two.Rectangle.perimeter,
                        },
                    ],
                },
                {
                    "id": 3,
                    "name": "Triangle",
                    "formula": [
                        {
                            "input": [
                                {"id": 1, "name": "base"},
                                {"id": 1, "name": "height"},
                            ],
                            "output": Shape.Two.Triangle.area,
                        },
                        {
                            "input": [
                                {"id": 1, "name": "firstLength"},
                                {"id": 2, "name": "secondLength"},
                                {"id": 3, "name": "thirdLength"},
                            ],
                            "output": Shape.Two.Triangle.perimeter,
                        },
                    ],
                },
                {
                    "id": 4,
                    "name": "Circle",
                    "formula": [
                        {
                            "input": [{"id": 1, "name": "radius"}],
                            "output": Shape.Two.Circle.area,
                        },
                        {
                            "input": [{"id": 1, "name": "radius"}],
                            "output": Shape.Two.Circle.perimeter,
                        },
                    ],
                },
            ],
            "3D": [
                {
                    "id": 1,
                    "name": "Cube",
                    "formula": [
                        {
                            "input": [{"id": 1, "name": "length"}],
                            "output": Shape.Three.Cube.volume,
                        },
                        {
                            "input": [{"id": 1, "name": "length"}],
                            "output": Shape.Three.Cube.surfaceArea,
                        },
                    ],
                },
                {
                    "id": 2,
                    "name": "Cuboid",
                    "formula": [
                        {
                            "input": [
                                {"id": 1, "name": "length"},
                                {"id": 2, "name": "width"},
                                {"id": 3, "name": "height"},
                            ],
                            "output": Shape.Three.Cuboid.volume,
                        },
                        {
                            "input": [
                                {"id": 1, "name": "length"},
                                {"id": 2, "name": "width"},
                                {"id": 3, "name": "height"},
                            ],
                            "output": Shape.Three.Cuboid.surfaceArea,
                        },
                    ],
                },
                {
                    "id": 3,
                    "name": "Cone",
                    "formula": [
                        {
                            "input": [
                                {"id": 1, "name": "radius"},
                                {"id": 2, "name": "height"},
                            ],
                            "output": Shape.Three.Cone.volume,
                        },
                        {
                            "input": [
                                {"id": 1, "name": "radius"},
                                {"id": 2, "name": "height"},
                            ],
                            "output": Shape.Three.Cone.surfaceArea,
                        },
                    ],
                },
                {
                    "id": 4,
                    "name": "Sphere",
                    "formula": [
                        {
                            "input": [{"id": 1, "name": "radius"}],
                            "output": Shape.Three.Sphere.volume,
                        },
                        {
                            "input": [{"id": 1, "name": "radius"}],
                            "output": Shape.Three.Sphere.surfaceArea,
                        },
                    ],
                },
                {
                    "id": 5,
                    "name": "Cylinder",
                    "formula": [
                        {
                            "input": [
                                {"id": 1, "name": "radius"},
                                {"id": 2, "name": "height"},
                            ],
                            "output": Shape.Three.Cylinder.volume,
                        },
                        {
                            "input": [
                                {"id": 1, "name": "radius"},
                                {"id": 2, "name": "height"},
                            ],
                            "output": Shape.Three.Cylinder.surfaceArea,
                        },
                    ],
                },
            ],
        }
        self.shapeDimension = "2D"
        self.shapeChoiceObject = {
            "2D": self.shapeArray["2D"][0]["name"],
            "3D": self.shapeArray["3D"][0]["name"],
        }
        self.shapeParameterArray = [
            {"id": 1, "name": "length", "display": "Length", "placeholder": "length"},
            {"id": 2, "name": "width", "display": "Width", "placeholder": "width"},
            {"id": 3, "name": "height", "display": "Height", "placeholder": "height"},
            {"id": 4, "name": "base", "display": "Base", "placeholder": "base"},
            {
                "id": 5,
                "name": "firstLength",
                "display": "First Length",
                "placeholder": "first length",
            },
            {
                "id": 6,
                "name": "secondLength",
                "display": "Second Length",
                "placeholder": "second length",
            },
            {
                "id": 7,
                "name": "thirdLength",
                "display": "Third Length",
                "placeholder": "third length",
            },
            {"id": 8, "name": "radius", "display": "Radius", "placeholder": "radius"},
        ]
        self.shapeEntryArray = []

        self.title("Shape Calculator")
        self.geometry(
            f"{Depedency.resolution['width']}x{Depedency.resolution['height']}"
        )
        self.resizable(width=False, height=False)

        self.mainFrame = customtkinter.CTkFrame(self)
        self.mainFrame.pack(pady=20, padx=20, fill="both", expand=True)

        self.dimensionSegmented = customtkinter.CTkSegmentedButton(
            self.mainFrame,
            command=self.refreshDimension,
            values=["2D", "3D"],
            font=customtkinter.CTkFont(size=14, weight="bold"),
        )
        self.dimensionSegmented.set("2D")
        self.dimensionSegmented.pack(pady=10, padx=10, fill="both")

        self.shapeOption = customtkinter.CTkOptionMenu(
            self.mainFrame,
            command=self.refreshShape,
            values=[shape["name"] for shape in self.shapeArray["2D"]],
            font=customtkinter.CTkFont(size=14, weight="bold"),
        )
        self.shapeOption.set(self.shapeArray["2D"][0]["name"])
        self.shapeOption.pack(pady=(10, 5), padx=10, fill="both")

        self.componentParameter()
        self.component2D()
        self.component3D()

        self.refreshShape()

    def componentParameter(self):
        self.shapeParameterComponentObject = {
            shapeParameterObject["name"]: {
                "label": customtkinter.CTkLabel(
                    self.mainFrame,
                    text=f"{shapeParameterObject['display']}:",
                    font=customtkinter.CTkFont(size=14, weight="bold"),
                    anchor="w",
                ),
                "entry": customtkinter.CTkEntry(
                    self.mainFrame,
                    placeholder_text=f"Insert {shapeParameterObject['placeholder']} here",
                    font=customtkinter.CTkFont(size=12, weight="bold"),
                ),
            }
            for shapeParameterObject in self.shapeParameterArray
        }

    def component2D(self):
        self.areaEntryText = customtkinter.StringVar()
        self.areaEntryText.set(0)
        self.areaLabel = customtkinter.CTkLabel(
            self.mainFrame,
            text="Area",
            font=customtkinter.CTkFont(size=16, weight="bold"),
        )
        self.areaEntry = customtkinter.CTkEntry(
            self.mainFrame,
            font=customtkinter.CTkFont(size=14, weight="bold"),
            textvariable=self.areaEntryText,
            state="disabled",
            justify="center",
        )

        self.perimeterEntryText = customtkinter.StringVar()
        self.perimeterEntryText.set(0)
        self.perimeterLabel = customtkinter.CTkLabel(
            self.mainFrame,
            text="Perimeter",
            font=customtkinter.CTkFont(size=16, weight="bold"),
        )
        self.perimeterEntry = customtkinter.CTkEntry(
            self.mainFrame,
            font=customtkinter.CTkFont(size=14, weight="bold"),
            textvariable=self.perimeterEntryText,
            state="disabled",
            justify="center",
        )

    def component3D(self):
        self.volumeEntryText = customtkinter.StringVar()
        self.volumeEntryText.set(0)
        self.volumeLabel = customtkinter.CTkLabel(
            self.mainFrame,
            text="Volume",
            font=customtkinter.CTkFont(size=16, weight="bold"),
        )
        self.volumeEntry = customtkinter.CTkEntry(
            self.mainFrame,
            font=customtkinter.CTkFont(size=14, weight="bold"),
            textvariable=self.volumeEntryText,
            state="disabled",
            justify="center",
        )

        self.surfaceAreaEntryText = customtkinter.StringVar()
        self.surfaceAreaEntryText.set(0)
        self.surfaceAreaLabel = customtkinter.CTkLabel(
            self.mainFrame,
            text="Surface Area",
            font=customtkinter.CTkFont(size=16, weight="bold"),
        )
        self.surfaceAreaEntry = customtkinter.CTkEntry(
            self.mainFrame,
            font=customtkinter.CTkFont(size=14, weight="bold"),
            textvariable=self.surfaceAreaEntryText,
            state="disabled",
            justify="center",
        )

    def hideParameter(self):
        for componentObject in self.shapeParameterComponentObject.values():
            componentObject["label"].pack_forget()
            componentObject["entry"].pack_forget()

    def hide2D(self):
        self.areaLabel.pack_forget()
        self.areaEntry.pack_forget()
        self.perimeterLabel.pack_forget()
        self.perimeterEntry.pack_forget()

    def hide3D(self):
        self.volumeLabel.pack_forget()
        self.volumeEntry.pack_forget()
        self.surfaceAreaLabel.pack_forget()
        self.surfaceAreaEntry.pack_forget()

    def show2D(self):
        self.areaLabel.pack(pady=(20, 0), padx=10, fill="both")
        self.areaEntry.pack(padx=10, fill="both")
        self.perimeterLabel.pack(pady=(10, 0), padx=10, fill="both")
        self.perimeterEntry.pack(padx=10, fill="both")

    def show3D(self):
        self.volumeLabel.pack(pady=(20, 0), padx=10, fill="both")
        self.volumeEntry.pack(padx=10, fill="both")
        self.surfaceAreaLabel.pack(pady=(10, 0), padx=10, fill="both")
        self.surfaceAreaEntry.pack(padx=10, fill="both")

    def refreshDimension(self, value):
        self.shapeDimension = value

        self.shapeOption.configure(
            values=[shape["name"] for shape in self.shapeArray[self.shapeDimension]]
        )
        self.shapeOption.set(self.shapeChoiceObject[self.shapeDimension])

        self.refreshShape(self.shapeChoiceObject[self.shapeDimension])

    def refreshShape(self, value=None):
        self.hide2D()
        self.hide3D()
        self.hideParameter()
        self.shapeEntryArray.clear()

        if value != None:
            self.shapeChoiceObject[self.shapeDimension] = value

        for shape in self.shapeArray[self.shapeDimension]:
            if shape["name"] == self.shapeChoiceObject[self.shapeDimension]:
                for shapeFormulaObject in shape["formula"]:
                    for shapeFormulaInputObject in shapeFormulaObject["input"]:
                        self.shapeParameterComponentObject[
                            shapeFormulaInputObject["name"]
                        ]["label"].pack(pady=(5, 0), padx=10, fill="both")

                        self.shapeParameterComponentObject[
                            shapeFormulaInputObject["name"]
                        ]["entry"].pack(pady=0, padx=10, fill="both")

                        self.shapeEntryArray.append(
                            self.shapeParameterComponentObject[
                                shapeFormulaInputObject["name"]
                            ]["entry"]
                        )

        self.show2D() if self.shapeDimension == "2D" else self.show3D()

        print(self.shapeEntryArray)


if __name__ == "__main__":
    app = App()
    app.mainloop()
