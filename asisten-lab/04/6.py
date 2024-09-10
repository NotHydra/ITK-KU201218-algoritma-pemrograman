# => "Hello, World!" akan dicetak secara terbalik dari 10 sampai 1 hanya jika nomor urutnya ganjil

i = 10
while i >= 1:
    if i % 2 == 1:
        print(f"Hello, World! {i}")

    i -= 1
