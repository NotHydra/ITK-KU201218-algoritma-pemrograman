umur = int(input("Masukkan umur Anda: "))

if umur < 0 or umur > 100:
    print("Umur anda ngawur.")

    raise AssertionError("Umur tidak valid. Harus antara 0 dan 100.")

print(f"Umur anda masuk akal, yaitu {umur} tahun.")
