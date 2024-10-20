import json


with open("asisten-lab/11/07.json", "r") as file:
    database = json.load(file)

    print(database)
    print()

    print(json.dumps(database, indent=4))
    print()

    print("List Mahasiswa:")

    countMahasiswa = 1
    for mahasiswa in database["mahasiswa"]:
        print(f"Mahasiswa {countMahasiswa}")
        print(f"Nama: {mahasiswa['nama']}")
        print(f"Program Studi: {mahasiswa['programStudi']}")
        print()

        countMahasiswa += 1

    print()
    print()

    print("List Mata Kuliah:")

    countMataKuliah = 1
    for mataKuliah in database["mataKuliah"]:
        print(f"Mata Kuliah {countMataKuliah}")
        print(f"Nama: {mataKuliah['nama']}")
        print(f"SKS: {mataKuliah['sks']}")
        print()

        countMataKuliah += 1
