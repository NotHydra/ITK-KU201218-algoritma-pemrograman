# => Contoh penggunaan range dan List
# => Untuk menghitung total angka dari 1 sampai 10

totalDenganRange = 0
for angka in range(1, 11):
    totalDenganRange += angka

print(totalDenganRange)

totalDenganList = 0
for angka in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    totalDenganList += angka

print(totalDenganList)
