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
                firstSide: float, secondSide: float, thirdSide: float
            ) -> float:
                return firstSide + secondSide + thirdSide

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

    shapes = {
        "2D": [
            {"id": 1, "name": "Square", "formula": Shape.Two.Square},
            {"id": 2, "name": "Rectangle", "formula": Shape.Two.Rectangle},
            {"id": 3, "name": "Triangle", "formula": Shape.Two.Triangle},
            {"id": 4, "name": "Circle", "formula": Shape.Two.Circle},
        ],
        "3D": [
            {"id": 1, "name": "Cube", "formula": Shape.Three.Cube},
            {"id": 2, "name": "Cuboid", "formula": Shape.Three.Cuboid},
            {"id": 3, "name": "Cone", "formula": Shape.Three.Cone},
            {"id": 4, "name": "Sphere", "formula": Shape.Three.Sphere},
            {"id": 5, "name": "Cylinder", "formula": Shape.Three.Cylinder},
        ],
    }


customtkinter.set_appearance_mode(Depedency.ctkAppearance)
customtkinter.set_default_color_theme(Depedency.ctkColorTheme)


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.shapeChoice = {
            "2D": Depedency.shapes["2D"][0]["name"],
            "3D": Depedency.shapes["3D"][0]["name"],
        }

        self.title("Shape Calculator")
        self.geometry(
            f"{Depedency.resolution['width']}x{Depedency.resolution['height']}"
        )
        self.resizable(width=False, height=False)

        self.mainFrame = customtkinter.CTkFrame(self)
        self.mainFrame.pack(pady=20, padx=20, fill="both", expand=True)

        self.dimensionSegmented = customtkinter.CTkSegmentedButton(
            self.mainFrame,
            command=self.dimensionSegmentedEvent,
            values=["2D", "3D"],
            font=customtkinter.CTkFont(size=14, weight="bold"),
        )
        self.dimensionSegmented.set("2D")
        self.dimensionSegmented.pack(pady=10, padx=10, fill="both")

        self.shapeOption = customtkinter.CTkOptionMenu(
            self.mainFrame,
            command=self.shapeOptionEvent,
            values=[shape["name"] for shape in Depedency.shapes["2D"]],
            font=customtkinter.CTkFont(size=14, weight="bold"),
        )
        self.shapeOption.set(Depedency.shapes["2D"][0]["name"])
        self.shapeOption.pack(pady=10, padx=10, fill="both")

        self.lengthLabel = customtkinter.CTkLabel(
            self.mainFrame,
            text="Length: ",
            font=customtkinter.CTkFont(size=14, weight="bold"),
            anchor="w",
        )
        self.lengthEntry = customtkinter.CTkEntry(
            self.mainFrame,
            placeholder_text="Insert length here",
            font=customtkinter.CTkFont(size=12, weight="bold"),
        )

        self.component2D()
        self.component3D()
        self.defaultShapeDimension()

    def component2D(self):
        self.areaEntryText = customtkinter.StringVar()
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
        )

        self.perimeterEntryText = customtkinter.StringVar()
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
        )

    def component3D(self):
        self.volumeEntryText = customtkinter.StringVar()
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
        )

        self.surfaceAreaEntryText = customtkinter.StringVar()
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
        )

    def show2D(self):
        self.volumeLabel.pack_forget()
        self.volumeEntry.pack_forget()
        self.surfaceAreaLabel.pack_forget()
        self.surfaceAreaEntry.pack_forget()

        self.areaLabel.pack(pady=(40, 0), padx=10, fill="both")
        self.areaEntry.pack(padx=10, fill="both")
        self.perimeterLabel.pack(pady=(10, 0), padx=10, fill="both")
        self.perimeterEntry.pack(padx=10, fill="both")

    def show3D(self):
        self.areaLabel.pack_forget()
        self.areaEntry.pack_forget()
        self.perimeterLabel.pack_forget()
        self.perimeterEntry.pack_forget()

        self.volumeLabel.pack(pady=(40, 0), padx=10, fill="both")
        self.volumeEntry.pack(padx=10, fill="both")
        self.surfaceAreaLabel.pack(pady=(10, 0), padx=10, fill="both")
        self.surfaceAreaEntry.pack(padx=10, fill="both")

    def defaultShapeDimension(self):
        self.shapeDimension = 2
        self.show2D()

    def dimensionSegmentedEvent(self, value):
        if value == "2D":
            self.shapeOption.configure(
                values=[shape["name"] for shape in Depedency.shapes["2D"]]
            )
            self.shapeOption.set(self.shapeChoice["2D"])

            self.show2D()
            self.shapeDimension = 2

        else:
            self.shapeOption.configure(
                values=[shape["name"] for shape in Depedency.shapes["3D"]]
            )
            self.shapeOption.set(self.shapeChoice["3D"])

            self.show3D()
            self.shapeDimension = 3

    def shapeOptionEvent(self, value):
        if self.shapeDimension == 2:
            self.shapeChoice["2D"] = value

        else:
            self.shapeChoice["3D"] = value


if __name__ == "__main__":
    app = App()
    app.mainloop()
