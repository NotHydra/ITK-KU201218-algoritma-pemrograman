import customtkinter as ctk


class Dependency:
    colorPalette = {
        "blue-darker": "#081d3a",
        "blue-dark": "#0A2647",
        "blue-light": "#144272",
        "white-darker": "#CCCCCC",
        "white": "#FFFFFF",
    }


class App(ctk.CTk):
    def __init__(self) -> None:
        super().__init__()

        self.title("Calculator")

        self.geometry("400x600")

        self.configure(fg_color=Dependency.colorPalette["blue-darker"])

        self.main()

    def main(self) -> None:
        self.rowconfigure(0, weight=2)
        self.rowconfigure([1, 2, 3, 4, 5], weight=1)
        self.columnconfigure([0, 1, 2, 3], weight=1)

        self.resultValue = ctk.StringVar()
        self.resultValue.set("")
        resultEntry = ctk.CTkEntry(
            master=self,
            textvariable=self.resultValue,
            text_color=Dependency.colorPalette["white"],
            font=ctk.CTkFont(family="Arial", size=24, weight="bold"),
            fg_color=Dependency.colorPalette["blue-light"],
            corner_radius=8,
            border_width=0,
            state="readonly",
        )
        resultEntry.grid(row=0, column=0, columnspan=4, padx=8, pady=8, sticky="nsew")

        # First Row
        modButton = ctk.CTkButton(
            master=self,
            text="mod",
            text_color=Dependency.colorPalette["white"],
            font=ctk.CTkFont(family="Arial", size=12, weight="bold"),
            fg_color=Dependency.colorPalette["blue-light"],
            hover_color=Dependency.colorPalette["blue-dark"],
            cursor="hand2",
            corner_radius=8,
            # command=self.removeEvent,
        )
        modButton.grid(row=1, column=0, padx=8, pady=(0, 8), sticky="nsew")

        powerButton = ctk.CTkButton(
            master=self,
            text="^",
            text_color=Dependency.colorPalette["white"],
            font=ctk.CTkFont(family="Arial", size=12, weight="bold"),
            fg_color=Dependency.colorPalette["blue-light"],
            hover_color=Dependency.colorPalette["blue-dark"],
            cursor="hand2",
            corner_radius=8,
            # command=self.removeEvent,
        )
        powerButton.grid(row=1, column=1, padx=(0, 8), pady=(0, 8), sticky="nsew")

        clearButton = ctk.CTkButton(
            master=self,
            text="C",
            text_color=Dependency.colorPalette["white"],
            font=ctk.CTkFont(family="Arial", size=12, weight="bold"),
            fg_color=Dependency.colorPalette["blue-light"],
            hover_color=Dependency.colorPalette["blue-dark"],
            cursor="hand2",
            corner_radius=8,
            command=self.clearEvent,
        )
        clearButton.grid(row=1, column=2, padx=(0, 8), pady=(0, 8), sticky="nsew")

        deleteButton = ctk.CTkButton(
            master=self,
            text="<",
            text_color=Dependency.colorPalette["white"],
            font=ctk.CTkFont(family="Arial", size=12, weight="bold"),
            fg_color=Dependency.colorPalette["blue-light"],
            hover_color=Dependency.colorPalette["blue-dark"],
            cursor="hand2",
            corner_radius=8,
            command=self.deleteEvent,
        )
        deleteButton.grid(row=1, column=3, padx=(0, 8), pady=(0, 8), sticky="nsew")

        # Second Row
        sevenButton = ctk.CTkButton(
            master=self,
            text="7",
            text_color=Dependency.colorPalette["white"],
            font=ctk.CTkFont(family="Arial", size=12, weight="bold"),
            fg_color=Dependency.colorPalette["blue-light"],
            hover_color=Dependency.colorPalette["blue-dark"],
            cursor="hand2",
            corner_radius=8,
            command=lambda: self.numberEvent(7),
        )
        sevenButton.grid(row=2, column=0, padx=8, pady=(0, 8), sticky="nsew")

        eightButton = ctk.CTkButton(
            master=self,
            text="8",
            text_color=Dependency.colorPalette["white"],
            font=ctk.CTkFont(family="Arial", size=12, weight="bold"),
            fg_color=Dependency.colorPalette["blue-light"],
            hover_color=Dependency.colorPalette["blue-dark"],
            cursor="hand2",
            corner_radius=8,
            command=lambda: self.numberEvent(8),
        )
        eightButton.grid(row=2, column=1, padx=(0, 8), pady=(0, 8), sticky="nsew")

        nineButton = ctk.CTkButton(
            master=self,
            text="9",
            text_color=Dependency.colorPalette["white"],
            font=ctk.CTkFont(family="Arial", size=12, weight="bold"),
            fg_color=Dependency.colorPalette["blue-light"],
            hover_color=Dependency.colorPalette["blue-dark"],
            cursor="hand2",
            corner_radius=8,
            command=lambda: self.numberEvent(9),
        )
        nineButton.grid(row=2, column=2, padx=(0, 8), pady=(0, 8), sticky="nsew")

        divideButton = ctk.CTkButton(
            master=self,
            text=":",
            text_color=Dependency.colorPalette["white"],
            font=ctk.CTkFont(family="Arial", size=12, weight="bold"),
            fg_color=Dependency.colorPalette["blue-light"],
            hover_color=Dependency.colorPalette["blue-dark"],
            cursor="hand2",
            corner_radius=8,
            command=lambda: self.operatorEvent(":"),
        )
        divideButton.grid(row=2, column=3, padx=(0, 8), pady=(0, 8), sticky="nsew")

        # Third Row
        fourButton = ctk.CTkButton(
            master=self,
            text="4",
            text_color=Dependency.colorPalette["white"],
            font=ctk.CTkFont(family="Arial", size=12, weight="bold"),
            fg_color=Dependency.colorPalette["blue-light"],
            hover_color=Dependency.colorPalette["blue-dark"],
            cursor="hand2",
            corner_radius=8,
            command=lambda: self.numberEvent(4),
        )
        fourButton.grid(row=3, column=0, padx=8, pady=(0, 8), sticky="nsew")

        fiveButton = ctk.CTkButton(
            master=self,
            text="5",
            text_color=Dependency.colorPalette["white"],
            font=ctk.CTkFont(family="Arial", size=12, weight="bold"),
            fg_color=Dependency.colorPalette["blue-light"],
            hover_color=Dependency.colorPalette["blue-dark"],
            cursor="hand2",
            corner_radius=8,
            command=lambda: self.numberEvent(5),
        )
        fiveButton.grid(row=3, column=1, padx=(0, 8), pady=(0, 8), sticky="nsew")

        sixButton = ctk.CTkButton(
            master=self,
            text="6",
            text_color=Dependency.colorPalette["white"],
            font=ctk.CTkFont(family="Arial", size=12, weight="bold"),
            fg_color=Dependency.colorPalette["blue-light"],
            hover_color=Dependency.colorPalette["blue-dark"],
            cursor="hand2",
            corner_radius=8,
            command=lambda: self.numberEvent(6),
        )
        sixButton.grid(row=3, column=2, padx=(0, 8), pady=(0, 8), sticky="nsew")

        multiplyButton = ctk.CTkButton(
            master=self,
            text="x",
            text_color=Dependency.colorPalette["white"],
            font=ctk.CTkFont(family="Arial", size=12, weight="bold"),
            fg_color=Dependency.colorPalette["blue-light"],
            hover_color=Dependency.colorPalette["blue-dark"],
            cursor="hand2",
            corner_radius=8,
            command=lambda: self.operatorEvent("x"),
        )
        multiplyButton.grid(row=3, column=3, padx=(0, 8), pady=(0, 8), sticky="nsew")

        # Fourth Row
        oneButton = ctk.CTkButton(
            master=self,
            text="1",
            text_color=Dependency.colorPalette["white"],
            font=ctk.CTkFont(family="Arial", size=12, weight="bold"),
            fg_color=Dependency.colorPalette["blue-light"],
            hover_color=Dependency.colorPalette["blue-dark"],
            cursor="hand2",
            corner_radius=8,
            command=lambda: self.numberEvent(1),
        )
        oneButton.grid(row=4, column=0, padx=8, pady=(0, 8), sticky="nsew")

        twoButton = ctk.CTkButton(
            master=self,
            text="2",
            text_color=Dependency.colorPalette["white"],
            font=ctk.CTkFont(family="Arial", size=12, weight="bold"),
            fg_color=Dependency.colorPalette["blue-light"],
            hover_color=Dependency.colorPalette["blue-dark"],
            cursor="hand2",
            corner_radius=8,
            command=lambda: self.numberEvent(2),
        )
        twoButton.grid(row=4, column=1, padx=(0, 8), pady=(0, 8), sticky="nsew")

        threeButton = ctk.CTkButton(
            master=self,
            text="3",
            text_color=Dependency.colorPalette["white"],
            font=ctk.CTkFont(family="Arial", size=12, weight="bold"),
            fg_color=Dependency.colorPalette["blue-light"],
            hover_color=Dependency.colorPalette["blue-dark"],
            cursor="hand2",
            corner_radius=8,
            command=lambda: self.numberEvent(3),
        )
        threeButton.grid(row=4, column=2, padx=(0, 8), pady=(0, 8), sticky="nsew")

        subtractButton = ctk.CTkButton(
            master=self,
            text="-",
            text_color=Dependency.colorPalette["white"],
            font=ctk.CTkFont(family="Arial", size=12, weight="bold"),
            fg_color=Dependency.colorPalette["blue-light"],
            hover_color=Dependency.colorPalette["blue-dark"],
            cursor="hand2",
            corner_radius=8,
            command=lambda: self.operatorEvent("-"),
        )
        subtractButton.grid(row=4, column=3, padx=(0, 8), pady=(0, 8), sticky="nsew")

        # Fifth Row
        zeroButton = ctk.CTkButton(
            master=self,
            text="0",
            text_color=Dependency.colorPalette["white"],
            font=ctk.CTkFont(family="Arial", size=12, weight="bold"),
            fg_color=Dependency.colorPalette["blue-light"],
            hover_color=Dependency.colorPalette["blue-dark"],
            cursor="hand2",
            corner_radius=8,
            command=lambda: self.numberEvent(0),
        )
        zeroButton.grid(row=5, column=0, padx=8, pady=(0, 8), sticky="nsew")

        equalButton = ctk.CTkButton(
            master=self,
            text="=",
            text_color=Dependency.colorPalette["white"],
            font=ctk.CTkFont(family="Arial", size=12, weight="bold"),
            fg_color=Dependency.colorPalette["blue-light"],
            hover_color=Dependency.colorPalette["blue-dark"],
            cursor="hand2",
            corner_radius=8,
            command=self.equalEvent,
        )
        equalButton.grid(
            row=5, column=1, columnspan=2, padx=(0, 8), pady=(0, 8), sticky="nsew"
        )

        addButton = ctk.CTkButton(
            master=self,
            text="+",
            text_color=Dependency.colorPalette["white"],
            font=ctk.CTkFont(family="Arial", size=12, weight="bold"),
            fg_color=Dependency.colorPalette["blue-light"],
            hover_color=Dependency.colorPalette["blue-dark"],
            cursor="hand2",
            corner_radius=8,
            command=lambda: self.operatorEvent("+"),
        )
        addButton.grid(row=5, column=3, padx=(0, 8), pady=(0, 8), sticky="nsew")

    def numberEvent(self, number) -> None:
        self.resultValue.set(f"{self.resultValue.get()}{number}")

    def operatorEvent(self, operator) -> None:
        currentResultValue = self.resultValue.get()

        if currentResultValue != "":
            if currentResultValue[-1] not in ["+", "-", "x", ":"]:
                self.resultValue.set(f"{currentResultValue}{operator}")

            elif currentResultValue[-1] in ["+", "-", "x", ":"]:
                self.resultValue.set(f"{currentResultValue[0:-1]}{operator}")

    def equalEvent(self) -> None:
        try:
            currentResultValue = self.resultValue.get()
            currentResultValue = currentResultValue.replace("x", "*")
            currentResultValue = currentResultValue.replace(":", "/")

            self.resultValue.set(str(eval(currentResultValue)))

        except:
            pass

    def deleteEvent(self) -> None:
        self.resultValue.set(self.resultValue.get()[0:-1])

    def clearEvent(self) -> None:
        self.resultValue.set("")


app = App()
app.mainloop()
