from os import system


class Dependency:
    textLength = 50
    textFill = "="

    rnaArray = [
        {"id": 1, "codon": ["AUG"], "protein": "Methionine"},
        {"id": 2, "codon": ["UUU", "UUC"], "protein": "Phenylalanine"},
        {"id": 3, "codon": ["UUA", "UUG"], "protein": "Leucine"},
        {"id": 4, "codon": ["UCU", "UCC", "UCA", "UCG"], "protein": "Serine"},
        {"id": 5, "codon": ["UAU", "UAC"], "protein": "Tyrosine"},
        {"id": 6, "codon": ["UGU", "UGC"], "protein": "Cysteine"},
        {"id": 7, "codon": ["UGG"], "protein": "Tryptophan"},
    ]


class Utility:
    def clear() -> None:
        system("cls")

    def printFormat(text: str = "", textFill=Dependency.textFill) -> None:
        print(text.center(Dependency.textLength, textFill))


class Program:
    def convert(rna: str) -> tuple[list[str], list[str]]:
        if len(rna) % 3 == 0:
            codonArray = [rna[i : i + 3] for i in range(0, len(rna), 3)]

            validCodonArray = []
            validProteinArray = []
            for rnaObject in Dependency.rnaArray:
                for rnaCodonObject in rnaObject["codon"]:
                    if rnaCodonObject in codonArray:
                        validCodonArray.append(rnaCodonObject)
                        validProteinArray.append(rnaObject["protein"])

                    elif (
                        "UAA" in codonArray
                        or "UAG" in codonArray
                        or "UGA" in codonArray
                    ):
                        raise Exception()

            return validCodonArray, validProteinArray

        else:
            raise Exception()

    def main() -> None:
        programIsRunning = True
        while programIsRunning:
            try:
                Utility.printFormat()
                Utility.printFormat("Protein To RNA", textFill="-")
                Utility.printFormat()

                codonArray, proteinArray = Program.convert(input("Insert RNA: ").upper())

                Utility.printFormat()
                Utility.printFormat("Codon", textFill="-")
                Utility.printFormat()

                if codonArray:
                    for codonIndex, codonObject in enumerate(codonArray):
                        print(f"{codonIndex + 1}. {codonObject}")

                else:
                    print("Not Found")

                Utility.printFormat()
                Utility.printFormat("Protein", textFill="-")
                Utility.printFormat()

                if proteinArray:
                    for proteinIndex, proteinObject in enumerate(proteinArray):
                        print(f"{proteinIndex + 1}. {proteinObject}")

                else:
                    print("Not Found")

                Utility.printFormat()

            except:
                Utility.printFormat()
                print("Input Not Valid")
                Utility.printFormat()

            optionIsValid = False
            while not optionIsValid:
                option = input("Try Again? (Y/N): ").upper()
                if option == "Y":
                    optionIsValid = True
                    Utility.clear()

                elif option == "N":
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
