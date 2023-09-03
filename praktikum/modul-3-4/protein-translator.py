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
    def translate() -> str:
        codon = input("Codon: ").upper()
        if codon in ["AUG"]:
            proteinName = "Methionine"

        elif codon in ["UUU", "UUC"]:
            proteinName = "Phenylalanine"

        elif codon in ["UUA", "UUG"]:
            proteinName = "Leucine"

        elif codon in ["UCU", "UCC", "UCA", "UCG"]:
            proteinName = "Serine"

        elif codon in ["UAU", "UAC"]:
            proteinName = "Tyrosine"

        elif codon in ["UGU", "UGC"]:
            proteinName = "Cysteine"

        elif codon in ["UGG"]:
            proteinName = "Tryptophan"

        else:
            proteinName = "Not Found"

        return proteinName

    def main() -> None:
        programIsRunning = True
        while programIsRunning:
            Utility.printFormat("Protein Translator")

            proteinName = Program.translate()

            Utility.printFormat()
            print(f"Protein Name: {proteinName}")
            Utility.printFormat()

            optionIsValid = False
            while not optionIsValid:
                option = input("Translate Again? (Y/N): ")
                if option.upper() == "Y":
                    optionIsValid = True
                    Utility.clear()

                elif option.upper() == "N":
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
