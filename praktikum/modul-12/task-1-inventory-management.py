import json
import os
import customtkinter as ctk
from CTkMessagebox import CTkMessagebox


class Utility:
    def readJSON(path) -> any:
        with open(path, "r") as file:
            return json.load(file)

    def writeJSON(path, data) -> None:
        with open(path, "w") as file:
            file.write(json.dumps(data, indent=4))


class Dependency:
    colorPalette = {
        "blue-darker": "#081d3a",
        "blue-dark": "#0A2647",
        "blue-light": "#144272",
        "white-darker": "#CCCCCC",
        "white": "#FFFFFF",
    }


class Message:
    def errorMessage(message: str) -> None:
        CTkMessagebox(
            corner_radius=8,
            icon="cancel",
            title="Error",
            message=message,
        )

    def successMessage(message: str) -> None:
        CTkMessagebox(
            corner_radius=8,
            icon="check",
            title="Success",
            message=message,
        )

    def confirmationMessage(message: str = "Are You Sure?") -> bool:
        return (
            True
            if CTkMessagebox(
                corner_radius=8,
                icon="question",
                title="Confirmation",
                message=message,
                option_1="Yes",
                option_2="No",
            ).get()
            == "Yes"
            else False
        )


class App(ctk.CTk):
    selectedItemId = None

    def __init__(self) -> None:
        super().__init__()

        self.title("Inventory")

        self.geometry("1280x720")

        self.configure(fg_color=Dependency.colorPalette["blue-dark"])

        if not os.path.isfile("./database.json"):
            Utility.writeJSON("./database.json", {"increment": {"item": 0}, "item": []})

        self.main()

    def main(self) -> None:
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=28)
        self.columnconfigure([1, 2], weight=2)

        self.dataFrame = ctk.CTkFrame(
            master=self, fg_color=Dependency.colorPalette["blue-light"], corner_radius=8
        )
        self.dataFrame.columnconfigure([0, 1, 2, 3, 4], weight=1)
        self.dataFrame.grid(row=0, column=0, padx=24, pady=24, sticky="nsew")

        self.refreshTable()

        actionFrame = ctk.CTkFrame(
            master=self, fg_color=Dependency.colorPalette["blue-light"], corner_radius=8
        )
        actionFrame.columnconfigure(0, weight=1)
        actionFrame.grid(row=0, column=1, padx=(0, 24), pady=24, sticky="nsew")

        titleActionLabel = ctk.CTkLabel(
            master=actionFrame,
            text="Action",
            text_color=Dependency.colorPalette["white"],
            font=ctk.CTkFont(family="Arial", size=16, weight="bold"),
            fg_color=Dependency.colorPalette["blue-dark"],
            corner_radius=8,
        )
        titleActionLabel.grid(row=0, column=0, padx=8, pady=8, sticky="nsew")

        addActionButton = ctk.CTkButton(
            master=actionFrame,
            text="Add",
            text_color=Dependency.colorPalette["white"],
            font=ctk.CTkFont(family="Arial", size=12, weight="bold"),
            fg_color=Dependency.colorPalette["blue-dark"],
            hover_color=Dependency.colorPalette["blue-darker"],
            cursor="hand2",
            corner_radius=8,
            command=self.addEvent,
        )
        addActionButton.grid(row=1, column=0, padx=8, pady=(0, 8), sticky="nsew")

        changeActionButton = ctk.CTkButton(
            master=actionFrame,
            text="Change",
            text_color=Dependency.colorPalette["white"],
            font=ctk.CTkFont(family="Arial", size=12, weight="bold"),
            fg_color=Dependency.colorPalette["blue-dark"],
            hover_color=Dependency.colorPalette["blue-darker"],
            cursor="hand2",
            corner_radius=8,
            command=self.changeEvent,
        )
        changeActionButton.grid(row=2, column=0, padx=8, pady=(0, 8), sticky="nsew")

        removeActionButton = ctk.CTkButton(
            master=actionFrame,
            text="Remove",
            text_color=Dependency.colorPalette["white"],
            font=ctk.CTkFont(family="Arial", size=12, weight="bold"),
            fg_color=Dependency.colorPalette["blue-dark"],
            hover_color=Dependency.colorPalette["blue-darker"],
            cursor="hand2",
            corner_radius=8,
            command=self.removeEvent,
        )
        removeActionButton.grid(row=3, column=0, padx=8, pady=(0, 8), sticky="nsew")

        inputFrame = ctk.CTkFrame(
            master=self, fg_color=Dependency.colorPalette["blue-light"], corner_radius=8
        )
        inputFrame.columnconfigure(0, weight=1)
        inputFrame.grid(row=0, column=2, padx=(0, 24), pady=24, sticky="nsew")

        titleInputLabel = ctk.CTkLabel(
            master=inputFrame,
            text="Item Data",
            text_color=Dependency.colorPalette["white"],
            font=ctk.CTkFont(family="Arial", size=16, weight="bold"),
            fg_color=Dependency.colorPalette["blue-dark"],
            corner_radius=8,
        )
        titleInputLabel.grid(row=0, column=0, padx=8, pady=8, sticky="nsew")

        self.nameInputEntry = ctk.CTkEntry(
            master=inputFrame,
            placeholder_text="name",
            placeholder_text_color=Dependency.colorPalette["white-darker"],
            text_color=Dependency.colorPalette["white"],
            font=ctk.CTkFont(family="Arial", size=16, weight="bold"),
            justify="center",
            fg_color=Dependency.colorPalette["blue-dark"],
            corner_radius=8,
            border_color=Dependency.colorPalette["blue-dark"],
        )
        self.nameInputEntry.grid(row=1, column=0, padx=8, pady=(0, 8), sticky="nsew")

        self.priceInputEntry = ctk.CTkEntry(
            master=inputFrame,
            placeholder_text="price",
            placeholder_text_color=Dependency.colorPalette["white-darker"],
            text_color=Dependency.colorPalette["white"],
            font=ctk.CTkFont(family="Arial", size=16, weight="bold"),
            justify="center",
            fg_color=Dependency.colorPalette["blue-dark"],
            corner_radius=8,
            border_color=Dependency.colorPalette["blue-dark"],
        )
        self.priceInputEntry.grid(row=2, column=0, padx=8, pady=(0, 8), sticky="nsew")

        self.stockInputEntry = ctk.CTkEntry(
            master=inputFrame,
            placeholder_text="Stock",
            placeholder_text_color=Dependency.colorPalette["white-darker"],
            text_color=Dependency.colorPalette["white"],
            font=ctk.CTkFont(family="Arial", size=16, weight="bold"),
            justify="center",
            fg_color=Dependency.colorPalette["blue-dark"],
            corner_radius=8,
            border_color=Dependency.colorPalette["blue-dark"],
        )
        self.stockInputEntry.grid(row=3, column=0, padx=8, pady=(0, 8), sticky="nsew")

    def refreshTable(self) -> None:
        for widget in self.dataFrame.winfo_children():
            if "frame" in str(widget):
                widget.grid_forget()

        titleDataLabel = ctk.CTkLabel(
            master=self.dataFrame,
            text="Item Table",
            text_color=Dependency.colorPalette["white"],
            font=ctk.CTkFont(family="Arial", size=16, weight="bold"),
            fg_color=Dependency.colorPalette["blue-dark"],
            corner_radius=8,
        )
        titleDataLabel.grid(
            row=0, column=0, columnspan=5, padx=8, pady=8, sticky="nsew"
        )

        noDataLabel = ctk.CTkLabel(
            master=self.dataFrame,
            text="No.",
            text_color=Dependency.colorPalette["white"],
            font=ctk.CTkFont(family="Arial", size=12, weight="bold"),
            fg_color=Dependency.colorPalette["blue-dark"],
            corner_radius=8,
        )
        noDataLabel.grid(row=1, column=0, padx=8, pady=(0, 8), sticky="nsew")

        nameDataLabel = ctk.CTkLabel(
            master=self.dataFrame,
            text="Name",
            text_color=Dependency.colorPalette["white"],
            font=ctk.CTkFont(family="Arial", size=12, weight="bold"),
            fg_color=Dependency.colorPalette["blue-dark"],
            corner_radius=8,
        )
        nameDataLabel.grid(row=1, column=1, padx=(0, 8), pady=(0, 8), sticky="nsew")

        priceDataLabel = ctk.CTkLabel(
            master=self.dataFrame,
            text="Price",
            text_color=Dependency.colorPalette["white"],
            font=ctk.CTkFont(family="Arial", size=12, weight="bold"),
            fg_color=Dependency.colorPalette["blue-dark"],
            corner_radius=8,
        )
        priceDataLabel.grid(row=1, column=2, padx=(0, 8), pady=(0, 8), sticky="nsew")

        stockDataLabel = ctk.CTkLabel(
            master=self.dataFrame,
            text="Stock",
            text_color=Dependency.colorPalette["white"],
            font=ctk.CTkFont(family="Arial", size=12, weight="bold"),
            fg_color=Dependency.colorPalette["blue-dark"],
            corner_radius=8,
        )
        stockDataLabel.grid(row=1, column=3, padx=(0, 8), pady=(0, 8), sticky="nsew")

        actionDataLabel = ctk.CTkLabel(
            master=self.dataFrame,
            text="Action",
            text_color=Dependency.colorPalette["white"],
            font=ctk.CTkFont(family="Arial", size=12, weight="bold"),
            fg_color=Dependency.colorPalette["blue-dark"],
            corner_radius=8,
        )
        actionDataLabel.grid(row=1, column=4, padx=(0, 8), pady=(0, 8), sticky="nsew")

        itemTable = Utility.readJSON("./database.json")["item"]
        if len(itemTable) >= 1:
            for itemIndex, itemObject in enumerate(itemTable):
                ctk.CTkLabel(
                    master=self.dataFrame,
                    text=itemIndex + 1,
                    text_color=Dependency.colorPalette["white"],
                    font=ctk.CTkFont(family="Arial", size=12, weight="bold"),
                    fg_color=Dependency.colorPalette["blue-dark"],
                    corner_radius=8,
                ).grid(row=2 + itemIndex, column=0, padx=8, pady=(0, 8), sticky="nsew")

                ctk.CTkLabel(
                    master=self.dataFrame,
                    text=itemObject["name"],
                    text_color=Dependency.colorPalette["white"],
                    font=ctk.CTkFont(family="Arial", size=12, weight="bold"),
                    fg_color=Dependency.colorPalette["blue-dark"],
                    corner_radius=8,
                ).grid(
                    row=2 + itemIndex, column=1, padx=(0, 8), pady=(0, 8), sticky="nsew"
                )

                ctk.CTkLabel(
                    master=self.dataFrame,
                    text=itemObject["price"],
                    text_color=Dependency.colorPalette["white"],
                    font=ctk.CTkFont(family="Arial", size=12, weight="bold"),
                    fg_color=Dependency.colorPalette["blue-dark"],
                    corner_radius=8,
                ).grid(
                    row=2 + itemIndex, column=2, padx=(0, 8), pady=(0, 8), sticky="nsew"
                )

                ctk.CTkLabel(
                    master=self.dataFrame,
                    text=itemObject["stock"],
                    text_color=Dependency.colorPalette["white"],
                    font=ctk.CTkFont(family="Arial", size=12, weight="bold"),
                    fg_color=Dependency.colorPalette["blue-dark"],
                    corner_radius=8,
                ).grid(
                    row=2 + itemIndex, column=3, padx=(0, 8), pady=(0, 8), sticky="nsew"
                )

                ctk.CTkButton(
                    master=self.dataFrame,
                    text="Use",
                    text_color=Dependency.colorPalette["white"],
                    font=ctk.CTkFont(family="Arial", size=12, weight="bold"),
                    fg_color=Dependency.colorPalette["blue-dark"],
                    hover_color=Dependency.colorPalette["blue-darker"],
                    cursor="hand2",
                    corner_radius=8,
                    command=lambda id=itemObject["id"]: self.refreshInput(id),
                ).grid(
                    row=2 + itemIndex, column=4, padx=(0, 8), pady=(0, 8), sticky="nsew"
                )

        else:
            notFoundDataLabel = ctk.CTkLabel(
                master=self.dataFrame,
                text="Data not found",
                text_color=Dependency.colorPalette["white"],
                font=ctk.CTkFont(family="Arial", size=12, weight="bold"),
                fg_color=Dependency.colorPalette["blue-dark"],
                corner_radius=8,
            )
            notFoundDataLabel.grid(
                row=2, column=0, columnspan=5, padx=8, pady=(0, 8), sticky="nsew"
            )

    def refreshInput(self, id):
        database = Utility.readJSON("./database.json")
        itemTable = database["item"]

        for itemObject in itemTable:
            if itemObject["id"] == id:
                self.selectedItemId = itemObject["id"]

                self.nameInputEntry.delete(0, ctk.END)
                self.priceInputEntry.delete(0, ctk.END)
                self.stockInputEntry.delete(0, ctk.END)

                self.nameInputEntry.insert(0, itemObject["name"])
                self.priceInputEntry.insert(0, itemObject["price"])
                self.stockInputEntry.insert(0, itemObject["stock"])

                break

    def addEvent(self) -> None:
        name = self.nameInputEntry.get()
        price = self.priceInputEntry.get()
        stock = self.stockInputEntry.get()

        if "" not in [name, price, stock]:
            if price.isdigit():
                if stock.isdigit():
                    database = Utility.readJSON("./database.json")

                    database["increment"]["item"] += 1
                    database["item"].append(
                        {
                            "id": database["increment"]["item"],
                            "name": name,
                            "price": price,
                            "stock": stock,
                        }
                    )

                    self.selectedItemId = None

                    self.nameInputEntry.delete(0, ctk.END)
                    self.priceInputEntry.delete(0, ctk.END)
                    self.stockInputEntry.delete(0, ctk.END)

                    Utility.writeJSON("./database.json", database)

                    self.refreshTable()

                    Message.successMessage("Item Added")

                else:
                    Message.errorMessage("Stock Must Be A Number")

            else:
                Message.errorMessage("Price Must Be A Number")

        else:
            Message.errorMessage("Please Fill Out The Form")

    def changeEvent(self) -> None:
        if self.selectedItemId != None:
            name = self.nameInputEntry.get()
            price = self.priceInputEntry.get()
            stock = self.stockInputEntry.get()

            if "" not in [name, price, stock]:
                if price.isdigit():
                    if stock.isdigit():
                        database = Utility.readJSON("./database.json")

                        for itemObject in database["item"]:
                            if itemObject["id"] == self.selectedItemId:
                                itemObject["name"] = name
                                itemObject["price"] = price
                                itemObject["stock"] = stock

                                break

                        Utility.writeJSON("./database.json", database)

                        self.refreshTable()

                        Message.successMessage("Item Changed")

                    else:
                        Message.errorMessage("Stock Must Be A Number")

                else:
                    Message.errorMessage("Price Must Be A Number")

            else:
                Message.errorMessage("Please Fill Out The Form")

        else:
            Message.errorMessage("Please Select An Item First")

    def removeEvent(self) -> None:
        if self.selectedItemId != None:
            database = Utility.readJSON("./database.json")

            for itemIndex, itemObject in enumerate(database["item"]):
                if itemObject["id"] == self.selectedItemId:
                    print(itemIndex, self.selectedItemId)

                    database["item"].pop(itemIndex)

                    break

            self.selectedItemId = None

            self.nameInputEntry.delete(0, ctk.END)
            self.priceInputEntry.delete(0, ctk.END)
            self.stockInputEntry.delete(0, ctk.END)

            Utility.writeJSON("./database.json", database)

            self.refreshTable()

            Message.successMessage("Item Removed")

        else:
            Message.errorMessage("Please Select An Item First")


app = App()
app.mainloop()
