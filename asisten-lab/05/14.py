# => Mencetak "Hello, World!", tetapi jika urutan angka yang dicetak adalah 5, maka program akan melangkahi angka tersebut

for i in range(0, 10):
    if i == 5:
        continue

    print(f"Hello, World! {i}")
