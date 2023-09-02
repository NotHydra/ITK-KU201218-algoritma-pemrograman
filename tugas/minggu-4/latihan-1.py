year = int(input("Tahun: "))
print()

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Kabisat")

        else:
            print("N Kabisat")

    else:
        print("Kabisat")

else:
    print("N Kabisat")
