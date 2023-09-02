year = int(input("Tahun: "))
print()

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Tahun Kabisat")

        else:
            print("Bbukan Tahun Kabisat")

    else:
        print("Tahun Kabisat")

else:
    print("Bukan Tahun Kabisat")
