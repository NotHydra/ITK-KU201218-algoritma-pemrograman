# => Contoh penggunaan fungsi values pada dictionary
# => Untuk mendapatkan jumlah stok barang

stokBarangATK = {
    "pensil": 10,
    "penghapus": 5,
    "buku": 15,
    "pulpen": 20,
}

jumlah = 0
for stokBarang in stokBarangATK.values():
    jumlah += stokBarang

print(f"Jumlah Stok Barang ATK: {jumlah}")
