hargaBarang = int(input("Harga Barang: "))
diskon = int(input("Diskon: "))
totalHarga = 0

if hargaBarang <= 50_000:
    totalHarga = hargaBarang

elif 50_000 > hargaBarang >= 100_000:
    totalHarga = hargaBarang - ((diskon / 100) * hargaBarang)

elif hargaBarang > 100_000:
    totalHarga = hargaBarang - ((diskon / 100) * hargaBarang)
    print(totalHarga)
    totalHarga = totalHarga - ((10 / 100) * totalHarga)
    print(totalHarga)


print(f"Total Harga: {totalHarga}")
