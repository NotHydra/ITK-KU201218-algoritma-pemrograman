# => Program sederhana untuk langsung mencetak total angka dari sekumpulan angka


def cetakTotalAngkaList(sekumpulanAngka):
    total = 0
    for angka in sekumpulanAngka:
        total += angka

    print(f"Total Angka: {total}")


cetakTotalAngkaList([10, 9, 8, 7, 6])
