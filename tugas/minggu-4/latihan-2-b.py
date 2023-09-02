hargaBarang = int(input("Harga Barang: "))
diskon = int(input("Diskon: "))
print()

totalHarga = 0
if hargaBarang <= 50_000:
    totalHarga = hargaBarang

else:
    if hargaBarang > 50000 and hargaBarang <= 100000:
        totalHarga = hargaBarang - ((diskon / 100) * hargaBarang)

    else:
        totalHarga = hargaBarang - ((diskon / 100) * hargaBarang)
        totalHarga = totalHarga - ((10 / 100) * totalHarga)


print(f"Total Harga: {totalHarga}")
