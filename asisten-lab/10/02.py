while True:
    try:
        umur = int(input("Masukkan umur Anda: "))

        if umur < 0:
            raise AssertionError("Umur tidak valid. Harus lebih dari sama dengan 0.")

        if umur > 100:
            raise AssertionError("Umur tidak valid. Harus kurang dari sama dengan 100.")

        print(f"Umur anda masuk akal, yaitu {umur} tahun.")
        break

    except ValueError:
        print("Masukkan angka, bukan huruf.")

    except AssertionError as error:
        print(error)
