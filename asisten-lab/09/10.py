# => Program sederhana untuk mendapatkan total angka dari sekumpulan


def totalAngkaList(sekumpulanAngka):
    total = 0
    for angka in sekumpulanAngka:
        total += angka

    return total


print(totalAngkaList([10, 9, 8, 7, 6]))

sekumpulanAngka = [3, 4, 2, 1, 10]
totalAngka = totalAngkaList(sekumpulanAngka)

print(totalAngka)
print(f"Total Angka: {totalAngka}")
print(f"Total angkanya adalah {totalAngka}")
