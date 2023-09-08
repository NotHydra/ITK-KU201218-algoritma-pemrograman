tahun = 0
suku_bunga = 0.05
saldo = 10_000

while saldo < 20_000:
    tahun += 1
    bunga = saldo * suku_bunga
    saldo += bunga

    print(tahun, bunga, saldo)

print(tahun)
