# => Mencetak "Hello, World!" dengan batas urutan angka tertentu, disini kita menggunakan angka 5

# => Contoh 1, dengan if statement
for i in range(10):
    if i < 5:
        print(f"Hello, World! {i}")

print()  # Mencetak baris kosong

# => Contoh 2, dengan break statement sebelum mencetak
for i in range(10):
    if i == 5:
        break

    print(f"Hello, World! {i}")

print()  # Mencetak baris kosong

# => Contoh 3, dengan continue statement
for i in range(10):
    print(f"Hello, World! {i}")

    if i == 4:
        break
