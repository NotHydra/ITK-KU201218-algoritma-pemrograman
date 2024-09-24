# => Contoh penggunaan List untuk menghitung rata-rata sekumpulan angka

angkaAngka = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

jumlah = 0
for angka in angkaAngka:
    jumlah += angka

print(f"Jumlah List: {jumlah}")
print(f"Panjang List: {len(angkaAngka)}")
print(f"Rata-Rata: {jumlah / len(angkaAngka)}")
