import json


with open("asisten-lab/11/06.json", "r") as file:
    data = json.load(file)

    for orang in data:
        print(orang)
        print()

        print(f"Nama: {orang['nama']}")
        print(f"Umur: {orang['umur']}")
        print()
        print()
        print()
