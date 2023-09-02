nilaiSkalaRichter = float(input("Nilai Skala Richter: "))
print()

if nilaiSkalaRichter <= 4.5:
    print("Beberapa Bangunan Rusak Ringan")

else:
    if nilaiSkalaRichter <= 6:
        print("Beberapa Bangunan Rusak Parah")

    else:
        if nilaiSkalaRichter <= 7:
            print("Banyak Bangunan Rusak Parah")

        else:
            print("Semua Bangunan Rata Dengan Tanah")
