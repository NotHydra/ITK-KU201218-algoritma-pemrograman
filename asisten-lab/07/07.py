# => String juga dapat dilakukan perulangan

barang = "Lampu"

# => Contoh dengan for in
for karakter in barang:
    print(karakter)

print()  # => Jarak

# => Contoh dengan for in range len
for i in range(len(barang)):
    print(barang[i])

print()  # => Jarak


# => Contoh dengan while
i = 0
while i < len(barang):
    print(barang[i])
    i += 1
