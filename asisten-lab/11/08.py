import json
import os


while True:
    print("=========================================")
    print("=========Monitoring Stok Barang==========")
    print("=========================================")
    print("1. Liat Barang")
    print("2. Tambah Barang")
    print("3. Total Stok Barang")
    print("4. Keluar")
    print("=========================================")

    try:
        pilihan = int(input("Pilih menu: "))

        if pilihan < 1 or pilihan > 4:
            raise AssertionError("Pilihan tidak tersedia")

    except AssertionError as error:
        print("=========================================")
        print(error)
        print("=========================================")
        input()

        os.system("cls")

        continue

    except ValueError:
        print("=========================================")
        print("Pilihan harus berupa angka")
        print("=========================================")
        input()

        os.system("cls")

        continue

    print("=========================================")

    if pilihan == 1:
        print("===============Liat Barang===============")
        print("=========================================")

        try:
            with open("asisten-lab/11/data-barang.json", "r") as file:
                database = json.load(file)

                if len(database["barang"]) == 0:
                    print("Data Kosong")

                else:
                    countBarang = 1
                    for barang in database["barang"]:
                        print(
                            f"{countBarang}. Nama: {barang['nama']}, Stok: {barang['stok']}"
                        )

        except FileNotFoundError:
            print("Data Kosong")

            with open("asisten-lab/11/data-barang.json", "w") as file:
                json.dump({"barang": []}, file, indent=4)

        print("=========================================")
        input()

        os.system("cls")

    elif pilihan == 2:
        print("=============Tambah Barang===============")
        print("=========================================")

        namaBarang = input("Nama barang: ")

        try:
            stokBarang = int(input("Stok barang: "))

            if stokBarang < 0:
                raise AssertionError("Stok barang tidak boleh kurang dari 0")

        except AssertionError as error:
            print("=========================================")
            print(error)
            print("=========================================")
            input()

            os.system("cls")

            continue

        except ValueError:
            print("=========================================")
            print("Pilihan harus berupa angka")
            print("=========================================")
            input()

            os.system("cls")

            continue

        try:
            with open("asisten-lab/11/data-barang.json", "r") as file:
                database = json.load(file)

        except FileNotFoundError:
            database = {"barang": []}

        database["barang"].append({"nama": namaBarang, "stok": stokBarang})

        with open("asisten-lab/11/data-barang.json", "w") as file:
            json.dump(database, file, indent=4)

        print("=========================================")
        print("Barang berhasil ditambahkan")
        print("=========================================")
        input()

        os.system("cls")

    elif pilihan == 3:
        print("===========Total Stok Barang=============")
        print("=========================================")

        try:
            with open("asisten-lab/11/data-barang.json", "r") as file:
                database = json.load(file)

                if len(database["barang"]) == 0:
                    print("Data Kosong")

                else:
                    totalStok = 0
                    for barang in database["barang"]:
                        totalStok += barang["stok"]

                    print(f"Total stok barang: {totalStok}")

        except FileNotFoundError:
            print("Data Kosong")

            with open("asisten-lab/11/data-barang.json", "w") as file:
                json.dump({"barang": []}, file, indent=4)

        print("=========================================")
        input()

        os.system("cls")

    elif pilihan == 4:
        print("Keluar")
        print("=========================================")
        break
