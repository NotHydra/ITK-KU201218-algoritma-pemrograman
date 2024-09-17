# => "Hello, World!" akan dicetak hanya jika nomor urutnya genap

i = 1
while i <= 10:
    if i % 2 == 0:
        print(f"Hello, World! {i}")

    i += 1
