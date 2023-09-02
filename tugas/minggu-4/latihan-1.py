# for year in range(1, 2040):
#     print(f"{year} ", end="")

# year = int(input("Input Tahun: "))
year = 2400

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
