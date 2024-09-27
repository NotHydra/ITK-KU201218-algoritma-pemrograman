# => Terdapat sebuah konsep mengenai List
# => Yaitu list slicing
# => Mirip range gitu, tetapi berdasarkan list yang sudah ada

# => Argumen pertama adalah batas awal
# => Argumen kedua adalah batas akhir
# => Argumen ketiga adalah step

# => Argumen dipisahkan dengan tanda ":"
# => Jika argumen tidak diisi, maka dianggap kosong
# => Bedakan kosong dengan nol (0), kosong != 0

angkaAngkaAcak = [8, 2, 3, 4, 6, 10, 1, 5]

print(angkaAngkaAcak[1:4])
print(angkaAngkaAcak[1:6:2])
print(angkaAngkaAcak[::2])

print(angkaAngkaAcak[::-1])
print(angkaAngkaAcak[::-2])
print(angkaAngkaAcak[-8::1])
