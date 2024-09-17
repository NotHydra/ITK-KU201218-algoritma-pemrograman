# => Mencetak "Hello, World!" dengan urutan genap, menggunakan continue statement

for i in range(0, 10):
    if i % 2 == 1:
        continue

    print(f"Hello, World! {i}")
