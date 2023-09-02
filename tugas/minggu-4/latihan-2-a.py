hargaBarang = int(input("Harga Barang: "))
diskon = int(input("Diskon: "))
print()

totalHarga = 0
if hargaBarang <= 50_000:
    totalHarga = hargaBarang

elif 50_000 > hargaBarang >= 100_000:
    totalHarga = hargaBarang - ((diskon / 100) * hargaBarang)

elif hargaBarang > 100_000:
    totalHarga = hargaBarang - ((diskon / 100) * hargaBarang)
    totalHarga = totalHarga - ((10 / 100) * totalHarga)


print(f"Total Harga: {totalHarga}")
