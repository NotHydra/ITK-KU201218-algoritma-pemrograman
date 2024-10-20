with open("asisten-lab/11/05.txt", "r") as file:
    for baris in file:
        dataOrang = baris.strip().split(", ")
        print(f"Nama: {dataOrang[0]}")
        print(f"Umur: {dataOrang[1]}")
        print()
